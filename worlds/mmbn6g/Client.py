import asyncio
import logging
from typing import TYPE_CHECKING

from NetUtils import ClientStatus
from .._bizhawk import guarded_write, guarded_read, RequestFailedError, read, write, display_message
from .._bizhawk.client import BizHawkClient
from .Locations import all_locations, LocationData, LocationType
from .Items import all_items, ItemType, ItemData, programs_to_item_id, chips_amount_index
from .BN6RomUtils import int32_to_byte_list_le

if TYPE_CHECKING:
    from .._bizhawk.context import BizHawkClientContext

logger = logging.getLogger("Client")

ROM_ADDRS = {"game_identifier": (0xA0, 10, "ROM")}

RAM_ADDRS = {
    # 0x00: World Initialization
    # 0x04: World
    # 0x08: Battle Init
    # 0x0C: Battle
    # 0x10: Map Change
    # 0x14: Character Change
    # 0x18: Menu
    # 0x1C: BBS
    # 0x20: Shop
    # 0x24: Chip Trader
    # 0x30: Request BBS
    # 0x34: Mailbox
    # 0x38: ChargeMan Minigame
    "game_state": (0x1B80, 1, "EWRAM"),
    #
    "main_area": (0x1B84, 1, "IWRAM"),
    #
    "sub_area": (0x1B85, 1, "IWRAM"),
    "zenny_amount": (0x1BDC, 4, "EWRAM"),
    # Base value is set on new game. Does "Zenny Amount XOR Anticheat Base" to get anticheat value
    "zenny_anticheat_base": (0x0060, 4, "EWRAM"),
    "bugfrag_amount": (0x1BE0, 4, "EWRAM"),
    # Base value is set on new game. Does "BugFrag Amount XOR Anticheat Base" to get anticheat value
    "bugfrag_anticheat_base": (0x18B8, 4, "EWRAM"),
    # An arbitrary address that isn't used strictly by the game
    # We'll use it to store the index of the last processed remote item
    # (May actually be used somewhere, but I guess we'll find out)
    "received_index": (0x1B60, 2, "EWRAM"),
    # A set of flags set by early game cutscenes. Since this should be 0x00, we use this to know if RAM can be trusted
    "canary_byte": (0x1D09, 1, "EWRAM"),
    # Contains the victory flag at bit 0x80
    "gregar_icon_flag": (0x1E48, 1, "EWRAM")
}


class MMBN6Client(BizHawkClient):
    game = "MegaMan Battle Network 6"
    system = "GBA"
    patch_suffix = ".apbn6"
    location_by_id: dict[int, LocationData]
    item_by_id: dict[int, ItemData]
    main_area: int
    sub_area: int
    player_name: str | None
    seed_verify = False

    def __init__(self) -> None:
        super().__init__()
        self.location_by_id = {loc_data.id: loc_data for loc_data in all_locations}
        self.item_by_id = {item_data.code: item_data for item_data in all_items}
        self.main_area = 0x00
        self.sub_area = 0x00

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        try:
            # Check ROM name/patch version
            rom_name_bytes = (await read(ctx.bizhawk_ctx, [ROM_ADDRS["game_identifier"]]))[0]
            rom_name = bytes([byte for byte in rom_name_bytes if byte != 0]).decode("ascii")
            if rom_name != "MEGAMAN6_G":
                return False

        except UnicodeDecodeError:
            return False
        except RequestFailedError:
            return False

        ctx.game = self.game
        # We send items, and can have starting inventory set. In some specific circumstances, we need to "send" items
        # found locally (boss checks)
        ctx.items_handling = 0b111
        ctx.want_slot_data = True
        ctx.watcher_timeout = 0.5
        name_bytes = (await read(ctx.bizhawk_ctx, [(0x7FFFC0, 63, "ROM")]))[0]
        name = bytes([byte for byte in name_bytes if byte != 0]).decode("UTF-8")
        self.player_name = name

        return True

    async def set_auth(self, ctx: "BizHawkClientContext") -> None:
        ctx.auth = self.player_name

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        if ctx.server is None or ctx.server.socket.closed or ctx.slot_data is None:
            return

        try:
            # Handle giving the player items
            read_result = await read(ctx.bizhawk_ctx, [
                RAM_ADDRS["game_state"],  # Current state of game (is the player actually in-game?)
                RAM_ADDRS["main_area"],
                RAM_ADDRS["sub_area"],
                RAM_ADDRS["received_index"],
                RAM_ADDRS["canary_byte"],
                RAM_ADDRS["gregar_icon_flag"]
            ])
            if read_result is None:
                return

            game_state = read_result[0][0]
            main_area_id = read_result[1][0]
            sub_area_id = read_result[2][0]
            received_index = (read_result[3][0] << 8) + read_result[3][1]
            canary_byte = read_result[4][0]
            gregar_icon_flag = read_result[5][0]

            # Do nothing if canary byte is not 0x00
            if canary_byte == 0x00:
                # Check for goal, Cybeast flag is located at 0x80
                if not ctx.finished_game and (gregar_icon_flag | 0x80) == gregar_icon_flag:
                    await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])

                # Only process items/locations if the player is in "normal" gameplay
                if game_state == 0x04:
                    await self.handle_item_receiving(ctx, received_index)
                    await self.handle_location_sending(ctx)
                    await self.handle_special_items(ctx)

                # Player moved to a new room that isn't the pause menu. Pause menu `room_area_id` == 0x0000
                if game_state == 0x04 and (self.main_area != main_area_id or self.sub_area != sub_area_id):
                    await self.handle_room_change(ctx, main_area_id, sub_area_id)

        except RequestFailedError:
            # The connector didn't respond. Exit handler and return to main loop to reconnect
            pass

    @staticmethod
    async def give_chip(ctx: "BizHawkClientContext", chip) -> bool:
        # First, get the amount of that item we have. Chips surprisingly don't have an anticheat system that I've found.
        # First four bytes are amount, then four 2-byte values indicating pack location. We don't need to bother setting
        # pack location, so just change amount and move on.
        index = chips_amount_index[chip]
        amount = await read(ctx.bizhawk_ctx, [(0x223C + index, 1, "EWRAM")])

        write_result = False
        total = 0
        while not write_result:
            # Write to the address if it hasn't changed.
            # Anticheat mechanism just XORs the base value with 0x55
            write_result = await guarded_write(ctx.bizhawk_ctx,
                                               [(0x223C + index, [amount[0][0] + 1], "EWRAM")],
                                               [(0x223C + index, [amount[0][0]], "EWRAM")])

            await asyncio.sleep(0.05)
            total += 0.05
            if write_result:
                total = 1
            if total > 1:
                return False

        return True

    @staticmethod
    async def give_item(ctx: "BizHawkClientContext", item) -> bool:
        # First, get the amount of that item we have
        amount = await read(ctx.bizhawk_ctx, [(0x3134 + item, 1, "EWRAM")])
        # Get the base anticheat value
        anticheat_base = await read(ctx.bizhawk_ctx, [(0x04E0 + item, 1, "EWRAM")])

        write_result = False
        total = 0
        while not write_result:
            # Write to the address if it hasn't changed.
            # Anticheat mechanism just XORs the base value with 0x55
            write_result = await guarded_write(ctx.bizhawk_ctx,
                                               [(0x3134 + item, [amount[0][0] + 1], "EWRAM"),
                                                (0x4A8C + item, [anticheat_base[0][0] ^ 0x55], "EWRAM")],
                                               [(0x3134 + item, [amount[0][0]], "EWRAM")])

            await asyncio.sleep(0.05)
            total += 0.05
            if write_result:
                total = 1
            if total > 1:
                return False

        return True

    @staticmethod
    async def change_zenny(ctx: "BizHawkClientContext", amount) -> bool:
        # First, get the values of the Zenny and the anticheat addresses
        read_result = await read(ctx.bizhawk_ctx, [
            RAM_ADDRS["zenny_amount"],  # Current state of game (is the player actually in-game?)
            RAM_ADDRS["zenny_anticheat_base"]
        ])

        curr_zenny = int.from_bytes(read_result[0], "little")
        anticheat_base = int.from_bytes(read_result[1], "little")
        anticheat_value = (curr_zenny + amount) ^ anticheat_base

        write_result = False
        total = 0
        while not write_result:
            # Write to the address if it hasn't changed
            write_result = await guarded_write(ctx.bizhawk_ctx,
                                               [(0x1BDC, int32_to_byte_list_le(curr_zenny + amount), "EWRAM"),
                                                (0x5028, int32_to_byte_list_le(anticheat_value), "EWRAM")],
                                               [(0x1BDC, int32_to_byte_list_le(curr_zenny), "EWRAM"),
                                                (0x5028, int32_to_byte_list_le(curr_zenny ^ anticheat_base), "EWRAM")])

            await asyncio.sleep(0.05)
            total += 0.05
            if write_result:
                total = 1
            if total > 1:
                return False

        return True

    @staticmethod
    async def change_bugfrags(ctx: "BizHawkClientContext", amount) -> bool:
        # First, get the values of the Bugfrags and the anticheat addresses
        read_result = await read(ctx.bizhawk_ctx, [
            RAM_ADDRS["bugfrag_amount"],
            RAM_ADDRS["bugfrag_anticheat_base"]
        ])

        curr_bugfrag = int.from_bytes(read_result[0], "little")
        anticheat_base = int.from_bytes(read_result[1], "little")
        anticheat_value = (curr_bugfrag + amount) ^ anticheat_base

        write_result = False
        total = 0
        while not write_result:
            # Write to the address if it hasn't changed
            write_result = await guarded_write(ctx.bizhawk_ctx,
                                               [(0x1BE0, int32_to_byte_list_le(curr_bugfrag + amount), "EWRAM"),
                                                (0x5030, int32_to_byte_list_le(anticheat_value), "EWRAM")],
                                               [(0x1BE0, int32_to_byte_list_le(curr_bugfrag), "EWRAM"),
                                                (0x5030, int32_to_byte_list_le(curr_bugfrag ^ anticheat_base), "EWRAM")])

            await asyncio.sleep(0.05)
            total += 0.05
            if write_result:
                total = 1
            if total > 1:
                return False

        return True

    async def handle_item_receiving(self, ctx: "BizHawkClientContext", received_index: int) -> None:
        # Read all pending receive items and dump into game ram
        print(received_index, len(ctx.items_received))
        for i in range(len(ctx.items_received) - received_index):
            result = False
            location_id = ctx.items_received[received_index + i].location
            location = self.location_by_id[location_id]
            if location is not None and location.type != LocationType.Boss:
                # Skip over local non-Boss locations
                print("Skipping over local non-Boss received item")
                await write(ctx.bizhawk_ctx, [(
                    RAM_ADDRS["received_index"][0],
                    [(received_index + i + 1) // 0x100, (received_index + i + 1) % 0x100],
                    "EWRAM",
                )])
                break

            item_id = ctx.items_received[received_index + i].item
            item = self.item_by_id[item_id]
            if item.type == ItemType.Chip:
                result = await self.give_chip(ctx, item.itemName)
            elif item.type == ItemType.KeyItem or item.type == ItemType.SubChip:
                result = await self.give_item(ctx, item.itemID)
                print(result)
            elif item.type == ItemType.Program:
                # Programs use the same area of memory as key items, but start at itemID 148
                result = await self.give_item(ctx, programs_to_item_id[item.itemName])
            elif item.type == ItemType.Zenny:
                result = await self.change_zenny(ctx, item.count)
            elif item.type == ItemType.BugFrag:
                result = await self.change_bugfrags(ctx, item.count)

            if not result:
                break
            await write(ctx.bizhawk_ctx, [(
                RAM_ADDRS["received_index"][0],
                [(received_index + i + 1) // 0x100, (received_index + i + 1) % 0x100],
                "EWRAM",
            )])

    async def handle_location_sending(self, ctx: "BizHawkClientContext") -> None:
        # Read all location flags in area and add to pending location checks if updates
        locations_to_read = [self.location_by_id[loc_id] for loc_id in ctx.missing_locations
                             if self.location_by_id[loc_id].flag_byte is not None]
        location_reads = [(loc.flag_byte, 1, "EWRAM") for loc in locations_to_read]
        # Only do location checks if the game state is still 0x04
        loc_bytes = await guarded_read(ctx.bizhawk_ctx, location_reads, [(0x1B80, [0x04], "EWRAM")])

        if loc_bytes is not None:
            locs_to_send = [locations_to_read[i].id for i, loc_ram in enumerate(loc_bytes)
                            if loc_ram[0] | locations_to_read[i].flag_mask == loc_ram[0]]

            # Send location checks
            if len(locs_to_send) > 0:
                await ctx.send_msgs([{"cmd": "LocationChecks", "locations": locs_to_send}])

    async def handle_special_items(self, ctx: "BizHawkClientContext") -> None:
        # If we have any of the Cross or BeastOut key items, set the proper flags
        beastout = await read(ctx.bizhawk_ctx, [(0x3134 + 10, 1, "EWRAM")])
        heat_cross = await read(ctx.bizhawk_ctx, [(0x3134 + 53, 1, "EWRAM")])
        slash_cross = await read(ctx.bizhawk_ctx, [(0x3134 + 55, 1, "EWRAM")])
        elec_cross = await read(ctx.bizhawk_ctx, [(0x3134 + 56, 1, "EWRAM")])
        erase_cross = await read(ctx.bizhawk_ctx, [(0x3134 + 58, 1, "EWRAM")])
        charge_cross = await read(ctx.bizhawk_ctx, [(0x3134 + 60, 1, "EWRAM")])

        flag_val = await read(ctx.bizhawk_ctx, [(0x1CA4, 1, "EWRAM")])
        new_val = flag_val[0][0]

        if beastout[0][0] > 0:
            new_val = new_val | 0x80
            await display_message(ctx.bizhawk_ctx, "Enabling BeastOut")
        if heat_cross[0][0] > 0:
            new_val = new_val | 0x20
        if slash_cross[0][0] > 0:
            new_val = new_val | 0x08
        if elec_cross[0][0] > 0:
            new_val = new_val | 0x10
        if erase_cross[0][0] > 0:
            new_val = new_val | 0x04
        if charge_cross[0][0] > 0:
            new_val = new_val | 0x02
            
        if not(flag_val[0][0] == new_val):
            await guarded_write(ctx.bizhawk_ctx,[(0x1CA4, [new_val], "EWRAM")],[(0x1CA4, flag_val[0], "EWRAM")])

    async def handle_room_change(self, ctx: "BizHawkClientContext", main_area_id, sub_area_id) -> None:
        self.main_area = main_area_id
        self.sub_area = sub_area_id
        # Room sync for poptracker tab tracking
        await ctx.send_msgs([{
            "cmd": "Set",
            "key": f"mmbn6_room_{ctx.team}_{ctx.slot}",
            "default": 0,
            "want_reply": False,
            "operations": [{"operation": "replace", "value": f"{main_area_id:02x} {sub_area_id:02x}"}]
        }])

