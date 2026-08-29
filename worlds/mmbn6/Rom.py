import struct
from typing import TYPE_CHECKING, List, Tuple, Dict

from BaseClasses import ItemClassification
from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes, APPatchExtension

import bsdiff4

from .Data import data
from .Options import GameVersion, TradeQuestHinting
from .GregarLocations import gregar_update_addresses
from .FalzarLocations import falzar_update_addresses
from .lz10 import gba_decompress, gba_compress

from settings import get_settings

from .BN6RomUtils import (read_u16_le, int16_to_byte_list_le, int24_to_byte_list_le, generate_text_bytes,
                          generate_external_item_message, generate_item_message)

from .Items import ItemType, items_by_id, ItemData
from .Locations import LocationType, location_table, falzar_only_locs, gregar_only_locs, location_data_table, \
    LocationData

if TYPE_CHECKING:
    from . import MMBN6World

CHECKSUM_GREG = "5acc75848bb1ffd3d6d8705554ee333d"
CHECKSUM_FALZ = "1e8c774ba210d1c55113531c7360c737"


def list_contains_subsequence(lst, sublist) -> bool:
    sub_index = 0
    for index, item in enumerate(lst):
        if item == sublist[sub_index]:
            sub_index += 1
            if sub_index >= len(sublist):
                return True
        else:
            sub_index = 0
    return False


class ArchiveScript:
    def __init__(self, index, message_bytes):
        self.index = index
        self.messageBoxes = []

        self.set_bytes(message_bytes)

    def get_bytes(self):
        data = []
        for message in self.messageBoxes:
            data.extend(message)
        return data

    def set_bytes(self, message_bytes):
        self.messageBoxes = []

        message_box = []

        byte_index = 0
        for byte in message_bytes:
            byte_index += 1
            if byte == 0xF2 or byte == 0xE6:
                if len(message_box) >= 2 and (message_box[-2] == 0xFA or message_box[-2] == 0xF4):
                    # If there was a print item/chip or give item/chip command before this, then just add the byte and move on.
                    message_box.append(byte)
                    continue

                if byte == 0xF2:  # More textboxes to come, don't end it yet
                    message_box.append(byte)
                    self.messageBoxes.append(message_box)
                else:  # It's the end of the script, add another message to end it after this one
                    self.messageBoxes.append(message_box)
                    self.messageBoxes.append([0xE6])

                message_box = []

            else:
                message_box.append(byte)

        # If there's still bytes left over, add them even if we didn't hit an end
        if len(message_box) > 0:
            self.messageBoxes.append(message_box)

    def __str__(self):
        s = str(self.index)+' - \n'
        for messageBox in self.messageBoxes:
            s += '  '+str(["{:02x}".format(x) for x in messageBox])+'\n'


class TextArchive:
    def __init__(self, data, offset, size, references, compressed=True):
        self.startOffset = offset
        self.compressed = compressed
        self.scripts = {}
        self.scriptCount = 0xFF
        self.references = references
        self.unused_indices = []  # A list of places it's okay to inject new scripts

        self.text_changed = False

        if compressed:
            self.compressedSize = size
            self.compressedData = data
            self.uncompressedData = gba_decompress(self.compressedData)
            self.uncompressedSize = len(self.uncompressedData)
        else:
            self.uncompressedSize = size
            self.uncompressedData = data
            self.compressedData = gba_compress(self.uncompressedData)
            self.compressedSize = len(self.compressedData)
        self.scriptCount = (read_u16_le(self.uncompressedData, 0)) >> 1

        for i in range(0, self.scriptCount):
            start_offset = read_u16_le(self.uncompressedData, i * 2)
            next_offset = read_u16_le(self.uncompressedData, (i + 1) * 2)

            # The last script is assumed to go until the end of the specified region of the ROM
            if i == self.scriptCount - 1:
                next_offset = len(self.uncompressedData)

            if start_offset != next_offset:
                message_bytes = list(self.uncompressedData[start_offset:next_offset])
                message = ArchiveScript(i, message_bytes)
                self.scripts[i] = message
            else:
                self.unused_indices.append(i)

    def generate_data(self, compressed=True):
        header = []
        scripts = []
        byte_offset = self.scriptCount * 2
        for i in range(0, self.scriptCount):
            header.extend(int16_to_byte_list_le(byte_offset))
            if i in self.scripts:
                script = self.scripts[i]
                scriptbytes = script.get_bytes()
                scripts.extend(scriptbytes)
                byte_offset += len(scriptbytes)

        data = []
        data.extend(header)
        data.extend(scripts)
        byte_data = bytes(data)
        if compressed:
            byte_data = gba_compress(byte_data)

        return bytearray(byte_data)

    def inject_item_message(self, script_index, message_indices, new_bytes):
        # First step, if the old message had any flag sets or flag clears, we need to keep them.
        # Mystery data has a flag set to actually remove the mystery data, and jobs often have a completion flag
        for message_index in message_indices:
            # print(hex(self.startOffset) + ": " + str(script_index) + " " + str(message_indices))
            oldbytes = self.scripts[script_index].messageBoxes[message_index]
            for i in range(len(oldbytes)-3):
                # EA 00 is the code for "flagSet", with the two bytes after it being the flag to set.
                # EA 01 is the code for "flagClear", which also needs to come along for the ride
                # Add those to the message box after the other text.
                if oldbytes[i] == 0xEA and (oldbytes[i+1] == 0x00 or oldbytes[i+1] == 0x01):
                    flag = oldbytes[i:i+4]
                    new_bytes.extend(flag)

        first_message_index = message_indices[0]
        # Then, overwrite the existing script with the new one
        self.scripts[script_index].messageBoxes[first_message_index] = new_bytes
        for index in message_indices[1:]:
            self.scripts[script_index].messageBoxes[index] = []

    def write_tokens(self, world: "MMBN6World", rom_length):
        patch = world.patch_data
        working_data = self.generate_data(self.compressed)

        # It needs to start on a byte divisible by 4. If the rom data is not, add an FF
        while rom_length % 4 != 0:
            patch.write_token(rom_length, 0, struct.pack("<B", 0xFF))
            rom_length += 1

        # Only try to inject the 3 bytes after 0x08 or 0x88 for references
        new_start_offset = rom_length
        for byte in working_data:
            patch.write_token(rom_length, 0, struct.pack("<B", byte))
            rom_length += 1
        for address in self.references:
            patch.write_token(address, 0, struct.pack("<L", new_start_offset)[:3])
        return rom_length

    def inject_item_text(self, item_text, next_message=""):
        item_text_bytes = generate_text_bytes(item_text)
        next_message_bytes = generate_text_bytes(next_message)
        for script_index in self.scripts:
            script = self.scripts[script_index]
            # Loop through the bytes
            for message_index in range(0, len(script.messageBoxes)):
                oldbytes = self.scripts[script_index].messageBoxes[message_index]
                for i in range(0, len(oldbytes)-1):
                    if oldbytes[i] == 0x69 and oldbytes[i+1] == 0x69:
                        oldbytes[i:i+2] = item_text_bytes
                        self.text_changed = True

                        # If there's another text box to display, add it to the message bytes before setting them back
                        if len(next_message) > 0:
                            oldbytes.extend(next_message_bytes)
                            # TODO append end message nextline etc.
                            # I think this is "wait for button press" then "clearmessage"
                            oldbytes.extend([0xE7, 0x00, 0xF2])
                        self.scripts[script_index].messageBoxes[message_index] = oldbytes

class MMBN6PatchExtension(APPatchExtension):
    game = "MegaMan Battle Network 6"

    @staticmethod
    def apply_bsdiff(caller: APProcedurePatch, rom: bytes, patch: str) -> bytes:
        rom_data = bytearray(rom)
        if rom_data[0xBC] == 1:
            return bsdiff4.patch(rom, caller.get_file("base_patch.bsdiff4"))
        return bsdiff4.patch(rom, caller.get_file(patch))

    @staticmethod
    def apply_tokens(caller: APProcedurePatch, rom: bytes, token_file: str) -> bytes:
        rom_data = bytearray(rom)

        token_data = caller.get_file(token_file)

        token_count = int.from_bytes(token_data[0:4], "little")
        bpr = 4
        for _ in range(token_count):
            token_type = token_data[bpr:bpr + 1][0]
            offset = int.from_bytes(token_data[bpr + 1:bpr + 5], "little")
            size = int.from_bytes(token_data[bpr + 5:bpr + 9], "little")
            data = token_data[bpr + 9:bpr + 9 + size]
            if token_type in [APTokenTypes.AND_8, APTokenTypes.OR_8, APTokenTypes.XOR_8]:
                arg = data[0]
                if token_type == APTokenTypes.AND_8:
                    rom_data[offset] = rom_data[offset] & arg
                elif token_type == APTokenTypes.OR_8:
                    rom_data[offset] = rom_data[offset] | arg
                else:
                    rom_data[offset] = rom_data[offset] ^ arg
            elif token_type in [APTokenTypes.COPY, APTokenTypes.RLE]:
                length = int.from_bytes(data[:4], "little")
                value = int.from_bytes(data[4:], "little")
                if token_type == APTokenTypes.COPY:
                    rom_data[offset: offset + length] = rom_data[value: value + length]
                else:
                    rom_data[offset: offset + length] = bytes([value] * length)
            else:
                rom_data[offset:offset + len(data)] = data
            bpr += 9 + size
        return bytes(rom_data)

class MMBN6GregarProcedurePatch(APProcedurePatch, APTokenMixin):
    hash = CHECKSUM_GREG
    game = "MegaMan Battle Network 6"
    patch_file_ending = ".apbn6g"
    result_file_ending = ".gba"

    procedure = [
        ("apply_bsdiff4", ["base_patch.bsdiff"]),
        ("apply_tokens", ["token_data.bin"])
    ]

    @classmethod
    def get_source_data(cls) -> bytes:
        with open(get_settings().mmbn6_settings.gregar_rom_file, "rb") as infile:
            base_rom_bytes = bytes(infile.read())
        return base_rom_bytes

class MMBN6FalzarProcedurePatch(APProcedurePatch, APTokenMixin):
    hash = CHECKSUM_FALZ
    game = "MegaMan Battle Network 6"
    patch_file_ending = ".apbn6f"
    result_file_ending = ".gba"

    procedure = [
        ("apply_bsdiff4", ["base_patch.bsdiff"]),
        ("apply_tokens", ["token_data.bin"])
    ]

    @classmethod
    def get_source_data(cls) -> bytes:
        with open(get_settings().mmbn6_settings.falzar_rom_file, "rb") as infile:
            base_rom_bytes = bytes(infile.read())
        return base_rom_bytes

class MMBN6PatchData:
    tokens: APTokenMixin
    game_version: str
    changed_archives: Dict[int, TextArchive]

    def __init__(self) -> None:
        self.tokens = APTokenMixin()
        self.game_version = ""
        self.item_hinting = -1
        self.token_data = []
        self.changed_archives = {}

    def set_game_version(self, game_version: str) -> None:
        self.game_version = game_version

    def set_item_hinting(self, item_hinting: TradeQuestHinting) -> None:
        self.item_hinting = item_hinting

    def write_token(self,
                    address: int | List[int],
                    offset: int,
                    data: bytes | Tuple[int, int] | int) -> None:
        if type(address) is int:
            self.tokens.write_token(APTokenTypes.WRITE, address + offset, data)
        elif type(address) is list:
            for addr in address:
                self.tokens.write_token(APTokenTypes.WRITE, addr + offset, data)

    def get_token_bytes(self) -> bytes:
        return self.tokens.get_token_binary()

def write_tokens(world: "MMBN6World", player: "int") -> None:
    patch = world.patch_data

    # Write player name
    authname = world.multiworld.player_name[player]
    authname = bytes(authname + ('\x00' * (63 - len(authname))), 'utf-8')
    for j, b in enumerate(authname):
        patch.write_token(0x7FFFC0, j, struct.pack("<B", b))

    for location_name in location_table.keys():
        # Skip locations from the opposite version
        if patch.game_version == "gregar" and location_name in falzar_only_locs:
            continue
        elif patch.game_version == "falzar" and location_name in gregar_only_locs:
            continue

        location_data = location_data_table[location_name]

        # Skip Boss locations, as there is nothing to update
        if location_data.type == LocationType.Boss:
            continue

        location = world.get_location(location_name)
        ap_item = location.item
        item_id = ap_item.code

        if item_id is not None:
            if ap_item.player != player or item_id not in items_by_id:
                item = ItemData(item_id, ap_item.name, ap_item.classification, ItemType.External)
                item = item._replace(recipient=world.multiworld.player_name[ap_item.player])
            else:
                item = items_by_id[item_id]

            if patch.game_version == "gregar":
                address = gregar_update_addresses[location_name]
            else:
                address = falzar_update_addresses[location_name]

            if location_data.type == LocationType.BlueMysteryData or location_data.type == LocationType.PurpleMysteryData:
                set_mystery_data(world, address, item)
            elif location_data.type in (LocationType.OverWorld, LocationType.Request, LocationType.LottoCode):
                set_text_archive(world, location_data, address, item)

            if location_data.inject_name:
                set_hint_text(world, location_data, address, item)

    write_text_archives(world)

def set_mystery_data(world: "MMBN6World", address: "int", item: "ItemData") -> None:
    # Reference to the Mystery Data structure: https://forums.therockmanexezone.com/bn4-6-sf1-mystery-data-wave-structure-t5398.html
    # The update address for Mystery Data is the Contents Entry. All we need to update is the type (0x00), the item sub-value (0x03), and the item value (0x04)
    patch = world.patch_data
    item_type = 0
    sub_value = 0xFF
    value = 0

    # Define the mystery data item type, sub-value, and value
    if item.type == ItemType.KeyItem:
        # Item = HPMemory
        if item.itemID == 112:
            item_type = 0x08
        # Item = RegUp1, RegUp2, RegUp3
        elif item.itemID == 114 or item.itemID == 115 or item.itemID == 116:
            item_type = 0x0A
        if item.itemID == 117:
            # Item = SubMemry
            item_type = 0x0B
        if item.itemID == 113:
            # Item = ExpMemry
            item_type = 0x0C
        else:
            # Item = Key Item
            item_type = 0x04
        # Sub-value is 0xFF, value is itemID
        sub_value = 0xFF
        value = item.itemID
    elif item.type == ItemType.Chip:
        item_type = 0x01
        sub_value = item.subItemID
        value = item.itemID
    elif item.type == ItemType.SubChip:
        item_type = 0x02
        sub_value = 0xFF
        value = item.itemID
    elif item.type == ItemType.Zenny:
        item_type = 0x03
        sub_value = 0xFF
        value = item.count
    elif item.type == ItemType.BugFrag:
        item_type = 0x05
        sub_value = 0xFF
        value = item.count
    elif item.type == ItemType.Program:
        # For programs, multiply the programID by 4 and add 144 to get the value
        item_type = 0x09
        sub_value = item.subItemID
        value = 144 + (item.itemID * 4)
    elif item.type == ItemType.External:
        # External items use itemID 61, or 0x3D
        item_type = 0x04
        sub_value = 0xFF
        value = 0x3D

    patch.write_token(address, 0, struct.pack("<B", item_type))
    patch.write_token(address, 3, struct.pack("<B", sub_value))
    patch.write_token(address, 4, struct.pack("<I", value))

def set_text_archive(world: "MMBN6World", location: "LocationData", address: "int", item: "ItemData") -> None:
    patch = world.patch_data

    if address in patch.changed_archives:
        archive = patch.changed_archives[address]
    else:
        address_key = hex(address).upper().replace("X", "x")
        archive_data = {}
        if patch.game_version == "gregar":
            archive_data = data.gregar_archive_data[address_key]
        elif patch.game_version == "falzar":
            archive_data = data.falzar_archive_data[address_key]

        is_compressed = archive_data["compressed"]
        size = archive_data["size"]
        references = archive_data["references"]
        byte_data = bytearray(archive_data["bytes"])

        archive = TextArchive(byte_data, address, size, references, is_compressed)
        patch.changed_archives[address] = archive

    if item.type == ItemType.External:
        item_bytes = generate_external_item_message(item.itemName, item.recipient)
    else:
        item_bytes = generate_item_message(item)

    archive.inject_item_message(location.text_script_index, location.text_box_indices,
                                item_bytes)

def set_hint_text(world: "MMBN6World", location: "LocationData", address: "int", item: "ItemData") -> None:
    patch = world.patch_data

    item_name_text = "Item"
    long_item_text = ""

    # No item hinting
    if patch.item_hinting == 0:
        item_name_text = "Check"
    # Partial item hinting
    elif patch.item_hinting == 1:
        if item.progression == ItemClassification.progression \
                or item.progression == ItemClassification.progression_skip_balancing:
            item_name_text = "Progress"
        elif item.progression == ItemClassification.useful \
                or item.progression == ItemClassification.trap:
            item_name_text = "Item"
        else:
            item_name_text = "Garbage"

        if item.recipient == 'Myself':
            item_name_text = "Your " + item_name_text
        else:
            item_name_text = item.recipient + "'s " + item_name_text
    # Full item hinting
    else:
        owners_name = "Your" if item.recipient == 'Myself' else item.recipient + "'s"
        if item.recipient == "Myself":
            long_item_text = f"It's {owners_name} \n\"{item.itemName}\"!!"
        else:
            # To keep things consistent, only specify "AP Item" in game
            long_item_text = f"It's {owners_name} \n\"AP Item\"!!"

    # If the archive is already loaded, use that
    if address in patch.changed_archives:
        archive = patch.changed_archives[address]
    else:
        # It should be theoretically impossible to call insert_hint_text before actually injecting the item.
        raise AssertionError(
            f"Inserting a hint at a location that doesn't have an item! Location: {location.name}")
    # If a string is too long, remove "Program: " to prevent garbled text.
    if len(long_item_text) > 20:
        long_text = long_item_text.replace("Program: ", "")
    archive.inject_item_text(item_name_text, long_item_text)

def write_text_archives(world: "MMBN6World") -> None:
    patch = world.patch_data
    rom_length = data.rom_data_end

    for archive in patch.changed_archives.values():
        rom_length = archive.write_tokens(world, rom_length)

