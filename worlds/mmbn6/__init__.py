import os
import settings
import typing

from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification, Region, \
    LocationProgressType

from worlds.AutoWorld import WebWorld, World

from .Rom import MMBN6DeltaPatch, LocalRom, get_base_rom_path
from .Items import MMBN6Item, ItemData, item_table, all_items, item_frequencies, items_by_id, ItemType, item_groups
from .Locations import MMBN6Location, all_locations, location_table, location_data_table, \
    requests, location_groups, graveyard_locations, ex_boss_locations, sp_boss_locations
from .Options import MMBN6Options
from .Regions import regions, RegionName
from .Names.ItemName import ItemName
from .Names.LocationName import LocationName
from .Client import MMBN6Client
from worlds.generic.Rules import add_rule


class MMBN6Settings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the MMBN6 Cybeast Gregar US rom"""
        copy_to = "Mega Man Battle Network 6 - Cybeast Gregar.gba"
        description = "MMBN6 ROM File"
        md5s = [MMBN6DeltaPatch.hash]

    class RomStart(str):
        """
        Set this to false to never autostart a rom (such as after patching),
                    true  for operating system default program
        Alternatively, a path to a program to open the .gba file with
        """

    rom_file: RomFile = RomFile(RomFile.copy_to)
    rom_start: RomStart | bool = True


class MMBN6Web(WebWorld):
    theme = "ice"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the MegaMan Battle Network 6 Randomizer connected to an Archipelago Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Risch"]
    )
    tutorials = [setup_en]


class MMBN6World(World):
    """
    Play as Lan and MegaMan to stop the evil organization WWW led by the nefarious
    Dr. Wily in their plans to take over the Net! Collect BattleChips, Customize your Navi,
    and utilize powerful Cross transformations to grow strong enough to take on the greatest
    threat the Internet has ever faced (once again)!
    """
    game = "MegaMan Battle Network 6"
    options_dataclass = MMBN6Options
    options: MMBN6Options
    settings: typing.ClassVar[MMBN6Settings]
    topology_present = False

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {loc_data.name: loc_data.id for loc_data in all_locations}

    excluded_locations: typing.Set[str]
    item_frequencies: typing.Dict[str, int]

    location_name_groups = location_groups
    item_name_groups = item_groups

    web = MMBN6Web()

    def generate_early(self) -> None:
        """
        called per player before any items or locations are created. You can set properties on your world here.
        Already has access to player options and RNG.
        """
        self.item_frequencies = item_frequencies.copy()

        self.excluded_locations = set()
        if not self.options.include_jobs:
            self.excluded_locations |= {request.name for request in requests}
        if not self.options.include_graveyard:
            self.excluded_locations |= graveyard_locations
        if not self.options.include_ex_bosses:
            self.excluded_locations |= ex_boss_locations
        if not self.options.include_sp_bosses:
            self.excluded_locations |= sp_boss_locations

    def create_regions(self) -> None:
        """
        called to place player's regions into the MultiWorld's regions list. If it's hard to separate, this can be done
        during generate_early or basic as well.
        """
        name_to_region = {}
        for region_info in regions:
            region = Region(region_info.name, self.player, self.multiworld)
            name_to_region[region_info.name] = region
            for location in region_info.locations:
                loc = MMBN6Location(self.player, location, self.location_name_to_id.get(location, None), region)
                if location in self.excluded_locations:
                    loc.progress_type = LocationProgressType.EXCLUDED
                region.locations.append(loc)
            self.multiworld.regions.append(region)

        # Regions which contribute to explore score when accessible.
        explore_score_region_names = (
            RegionName.Seaside_Overworld,
            RegionName.Seaside_Cyberworld,
            RegionName.Green_Overworld,
            RegionName.Green_Cyberworld,
            RegionName.Sky_Overworld,
            RegionName.Sky_Cyberworld,
            RegionName.ACDC_Overworld,
            RegionName.ACDC_Cyberworld,
            RegionName.Undernet,
            RegionName.Graveyard,
            RegionName.Expo
        )
        explore_score_regions = [self.get_region(region_name) for region_name in explore_score_region_names]

        # Entrances which use explore score in their logic need to register all the explore score regions as indirect
        # conditions.
        def register_explore_score_indirect_conditions(entrance):
            for explore_score_region in explore_score_regions:
                self.multiworld.register_indirect_condition(explore_score_region, entrance)

        for region_info in regions:
            region = name_to_region[region_info.name]
            for connection in region_info.connections:
                entrance = region.connect(name_to_region[connection])

                # Overworld Regions
                if connection == RegionName.Seaside_Overworld:
                    entrance.access_rule = lambda state: state.has(ItemName.Fish, self.player)
                if connection == RegionName.Green_Overworld:
                    entrance.access_rule = lambda state: state.has(ItemName.AuthData, self.player)
                if connection == RegionName.Sky_Overworld:
                    entrance.access_rule = lambda state: state.has(ItemName.Umbrella, self.player)
                if connection == RegionName.ACDC_Overworld:
                    entrance.access_rule = lambda state: state.has(ItemName.ACDCKyDt, self.player)

                # Cyberworld Regions
                # Central 3 can be reached from Central 1 with KeyData, or any cyberworld with the proper key item
                if connection == RegionName.Central3_and_Underground:
                    entrance.access_rule = lambda state: \
                        state.has(ItemName.KeyData, self.player) or \
                        (state.can_reach_region(RegionName.Seaside_Cyberworld, self.player) and \
                         state.has(ItemName.ToolPrgm, self.player)) or \
                        (state.can_reach_region(RegionName.Green_Cyberworld, self.player) and \
                         state.has(ItemName.CybBrdAx, self.player)) or \
                        (state.can_reach_region(RegionName.Sky_Cyberworld, self.player) and \
                         state.has(ItemName.VacData, self.player)) or \
                        (state.can_reach_region(RegionName.ACDC_Cyberworld, self.player) and \
                         state.has(ItemName.AreaPass, self.player)) or \
                        self.multiworld.register_indirect_condition(self.get_region(RegionName.Seaside_Cyberworld),
                                                                    entrance)
                    self.multiworld.register_indirect_condition(self.get_region(RegionName.Green_Cyberworld), entrance)
                    self.multiworld.register_indirect_condition(self.get_region(RegionName.Sky_Cyberworld), entrance)
                    self.multiworld.register_indirect_condition(self.get_region(RegionName.ACDC_Cyberworld), entrance)
                if connection == RegionName.Seaside_Cyberworld:
                    entrance.access_rule = lambda state: \
                        state.has(ItemName.ToolPrgm, self.player) or \
                        state.can_reach_region(RegionName.Seaside_Overworld, self.player)
                    self.multiworld.register_indirect_condition(self.get_region(RegionName.Seaside_Overworld), entrance)
                if connection == RegionName.Green_Cyberworld:
                    entrance.access_rule = lambda state: \
                        state.has(ItemName.CybBrdAx, self.player) or \
                        state.can_reach_region(RegionName.Green_Overworld, self.player)
                    self.multiworld.register_indirect_condition(self.get_region(RegionName.Green_Overworld), entrance)
                if connection == RegionName.Sky_Cyberworld:
                    entrance.access_rule = lambda state: \
                        state.has(ItemName.VacData, self.player) or \
                        state.can_reach_region(RegionName.Sky_Overworld, self.player)
                    self.multiworld.register_indirect_condition(self.get_region(RegionName.Sky_Overworld), entrance)
                if connection == RegionName.ACDC_Cyberworld:
                    entrance.access_rule = lambda state: \
                        state.has(ItemName.AreaPass, self.player) or \
                        state.can_reach_region(RegionName.ACDC_Overworld, self.player)
                    self.multiworld.register_indirect_condition(self.get_region(RegionName.ACDC_Overworld), entrance)
                if connection == RegionName.Undernet:
                    entrance.access_rule = lambda state: self.explore_score(state) > 6 and \
                                                         state.can_reach_region(RegionName.Sky_Cyberworld, self.player)
                    self.multiworld.register_indirect_condition(self.get_region(RegionName.Sky_Cyberworld), entrance)
                if connection == RegionName.Graveyard:
                    entrance.access_rule = lambda state: self.explore_score(state) > 9 and \
                                                         state.can_reach_region(RegionName.Undernet, self.player) and \
                                                         state.has(ItemName.BatKey, self.player)
                    self.multiworld.register_indirect_condition(self.get_region(RegionName.Undernet), entrance)
                if connection == RegionName.Expo:
                    entrance.access_rule = lambda state: \
                        state.has(ItemName.StampCrd, self.player)

    def create_items(self) -> None:
        # First add in all progression and useful items
        required_items = []
        for item in all_items:
            if item.progression != ItemClassification.filler:
                freq = self.item_frequencies.get(item.itemName, 1)
                required_items += [item.itemName for _ in range(freq)]

        for itemName in required_items:
            self.multiworld.itempool.append(self.create_item(itemName))

        # Then, get a random amount of fillers until we have as many items as we have locations
        filler_items = []
        for item in all_items:
            if item.progression == ItemClassification.filler:
                freq = self.item_frequencies.get(item.itemName, 1)
                filler_items += [item.itemName for _ in range(freq)]

        remaining = len(all_locations) - len(required_items)
        for i in range(remaining):
            filler_item_name = self.random.choice(filler_items)
            item = self.create_item(filler_item_name)
            self.multiworld.itempool.append(item)
            filler_items.remove(filler_item_name)

    def set_rules(self) -> None:
        """
        called to set access and item rules on locations and entrances.
        """

        # Set WWW ID requirements
        def has_www_id(state):
            return state.has(ItemName.WWWID, self.player)

        add_rule(self.multiworld.get_location(LocationName.Central_Area_1_BMD_2, self.player), has_www_id)
        add_rule(self.multiworld.get_location(LocationName.Seaside_Area_1_BMD_2, self.player), has_www_id)
        add_rule(self.multiworld.get_location(LocationName.Green_Area_2_BMD_3, self.player), has_www_id)
        add_rule(self.multiworld.get_location(LocationName.ACDC_Area_BMD_2, self.player), has_www_id)

        # Set Rush Food requirements. For now, this just requires Sky Town access
        def has_rush_food(state):
            return state.has(ItemName.Umbrella, self.player)

        add_rule(self.multiworld.get_location(LocationName.Green_Area_2_BMD_2, self.player), has_rush_food)
        add_rule(self.multiworld.get_location(LocationName.Sky_Area_1_BMD_2, self.player), has_rush_food)
        add_rule(self.multiworld.get_location(LocationName.ACDC_Area_BMD_1, self.player), has_rush_food)
        add_rule(self.multiworld.get_location(LocationName.Undernet_0_Heel_Navi, self.player), has_rush_food)

        # Rush Food requirement, but also blocked by a Tree
        self.multiworld.get_location(LocationName.Undernet_Zero_BMD_1, self.player).access_rule = \
            lambda state: \
                state.has(ItemName.Umbrella, self.player) and \
                (state.has(ItemName.HeatCross, self.player) or \
                 state.has_all({ItemName.SlashCross, ItemName.AuthData}, self.player))

        # Set Link Navi requirements
        # Fires
        self.multiworld.get_location(LocationName.Sky_Area_2_BMD_3, self.player).access_rule = \
            lambda state: \
                (state.has(ItemName.HeatCross, self.player) or \
                 state.has_all({ItemName.ChargeCross, ItemName.Fish}, self.player))
        self.multiworld.get_location(LocationName.Underground_2_BMD_2, self.player).access_rule = \
            lambda state: \
                (state.has(ItemName.HeatCross, self.player) or \
                 state.has_all({ItemName.ChargeCross, ItemName.Fish}, self.player))
        self.multiworld.get_location(LocationName.Graveyard_BMD_2, self.player).access_rule = \
            lambda state: \
                (state.has(ItemName.HeatCross, self.player) or \
                 state.has_all({ItemName.ChargeCross, ItemName.Fish}, self.player))

        # Geysers
        self.multiworld.get_location(LocationName.Seaside_Area_1_BMD_3, self.player).access_rule = \
            lambda state: \
                (state.has(ItemName.EraseCross, self.player) or \
                 state.has_all({ItemName.ElecCross, ItemName.Umbrella}, self.player))
        self.multiworld.get_location(LocationName.Undernet_Zero_BMD_2, self.player).access_rule = \
            lambda state: \
                (state.has(ItemName.EraseCross, self.player) or \
                 state.has_all({ItemName.ElecCross, ItemName.Umbrella}, self.player))
        self.multiworld.get_location(LocationName.Graveyard_PMD_1, self.player).access_rule = \
            lambda state: \
                (state.has(ItemName.EraseCross, self.player) or \
                 state.has_all({ItemName.ElecCross, ItemName.Umbrella}, self.player))

        # Trees
        self.multiworld.get_location(LocationName.Green_Area_1_BMD_2, self.player).access_rule = \
            lambda state: \
                (state.has(ItemName.HeatCross, self.player) or \
                 state.has_all({ItemName.SlashCross, ItemName.AuthData}, self.player))
        self.multiworld.get_location(LocationName.Sky_1_Brown_Navi, self.player).access_rule = \
            lambda state: \
                (state.has(ItemName.HeatCross, self.player) or \
                 state.has_all({ItemName.SlashCross, ItemName.AuthData}, self.player))
        self.multiworld.get_location(LocationName.Graveyard_BMD_3, self.player).access_rule = \
            lambda state: \
                (state.has(ItemName.HeatCross, self.player) or \
                 state.has_all({ItemName.SlashCross, ItemName.AuthData}, self.player))

        # Cloud
        self.multiworld.get_location(LocationName.Sky_Area_1_PMD, self.player).access_rule = \
            lambda state: \
                (state.has(ItemName.EraseCross, self.player) or \
                 state.has_all({ItemName.ElecCross, ItemName.Umbrella}, self.player))

        # Tornado
        self.multiworld.get_location(LocationName.Seaside_Area_2_BMD_3, self.player).access_rule = \
            lambda state: \
                (state.has_all({ItemName.SlashCross, ItemName.AuthData}, self.player) or \
                 state.has_all({ItemName.ChargeCross, ItemName.Fish}, self.player))
        self.multiworld.get_location(LocationName.Graveyard_BMD_4, self.player).access_rule = \
            lambda state: \
                (state.has_all({ItemName.SlashCross, ItemName.AuthData}, self.player) or \
                 state.has_all({ItemName.ChargeCross, ItemName.Fish}, self.player))

        # Lab Comp 2 requires EraseCross, or access to Undernet
        self.multiworld.get_location(LocationName.Graveyard_BMD_4, self.player).access_rule = \
            lambda state: \
                state.has(ItemName.EraseCross, self.player) or \
                state.can_reach_region(RegionName.Undernet, self.player)

        # For now, set PMDs to be behind an explore score of 6. Otherwise, PMDs are in logic from the get-go, which
        # can be frustrating with a lot of zenny requirements.
        self.multiworld.get_location(LocationName.ACDC_HP_PMD, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6
        self.multiworld.get_location(LocationName.Aquarium_HP_PMD, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6
        self.multiworld.get_location(LocationName.Green_HP_PMD, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6
        self.multiworld.get_location(LocationName.Sky_HP_PMD, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6
        self.multiworld.get_location(LocationName.Class_6_2_Comp_PMD, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6
        self.multiworld.get_location(LocationName.Labs_Comp_2_PMD, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6
        self.multiworld.get_location(LocationName.Punish_Chair_Comp_PMD, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6
        self.multiworld.get_location(LocationName.Oxygen_Tank_Comp_PMD, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6
        self.multiworld.get_location(LocationName.Central_Area_3_PMD, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6
        self.multiworld.get_location(LocationName.Seaside_Area_3_PMD, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6
        self.multiworld.get_location(LocationName.Green_Area_1_PMD, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6
        self.multiworld.get_location(LocationName.Underground_1_PMD_1, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6
        self.multiworld.get_location(LocationName.Underground_1_PMD_2, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6
        self.multiworld.get_location(LocationName.Sky_Area_1_PMD, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6
        self.multiworld.get_location(LocationName.ACDC_Area_PMD, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6
        self.multiworld.get_location(LocationName.Undernet_1_PMD, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6
        self.multiworld.get_location(LocationName.Undernet_2_PMD, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6

        # Set EX Bosses to be blocked by explore score to prevent forcing players to fight them right away.
        self.multiworld.get_location(LocationName.BlastMan_EX, self.player).access_rule = \
            lambda state: self.explore_score(state) > 4
        self.multiworld.get_location(LocationName.DiveMan_EX, self.player).access_rule = \
            lambda state: self.explore_score(state) > 4
        self.multiworld.get_location(LocationName.CircusMan_EX, self.player).access_rule = \
            lambda state: self.explore_score(state) > 4
        self.multiworld.get_location(LocationName.JudgeMan_EX, self.player).access_rule = \
            lambda state: self.explore_score(state) > 4
        self.multiworld.get_location(LocationName.CircusMan_EX, self.player).access_rule = \
            lambda state: self.explore_score(state) > 4
        self.multiworld.get_location(LocationName.Colonel_EX, self.player).access_rule = \
            lambda state: self.explore_score(state) > 4

        # Set SP Bosses to be blocked by explore score to prevent forcing players to fight them right away.
        self.multiworld.get_location(LocationName.BlastMan_SP, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6
        self.multiworld.get_location(LocationName.DiveMan_SP, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6
        self.multiworld.get_location(LocationName.CircusMan_SP, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6
        self.multiworld.get_location(LocationName.JudgeMan_SP, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6
        self.multiworld.get_location(LocationName.CircusMan_SP, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6
        self.multiworld.get_location(LocationName.Colonel_SP, self.player).access_rule = \
            lambda state: self.explore_score(state) > 6

        # Get the player's current possible request points based on accessible locations. This determines if a certain rank
        # is achievable to unlock higher star requests.
        def request_points_possible(state):
            # 1 star jobs
            # Virus Deletion and Find Keepsake always reachable
            request_points = 2

            # If Got a Problem. beatable
            if state.can_reach_region(RegionName.Seaside_Overworld, self.player):
                request_points += 1

            # If Errand Request and Get The Chip! beatable
            if state.can_reach_region(RegionName.Seaside_Cyberworld, self.player):
                # Get The Chip! requires DolThdr1 A
                if state.has(ItemName.DolThdr1_A, self.player):
                    request_points += 1
                # Loan Collection starts in Green HP
                if state.can_reach_region(RegionName.Green_Cyberworld, self.player):
                    request_points += 1

                request_points += 1

            # For Somebody Help!, we force the 10,000z option. To prevent heavy grinding, require Millions or
            # a 100,000z drop
            if state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player):
                request_points += 1

            # If Daughter Worry, Stop Him!, and Diet Goods Money beatable
            if state.can_reach_region(RegionName.Green_Overworld, self.player):
                # Daughter Worry and Diet Goods Money require Seaside Cyberworld access
                if state.can_reach_region(RegionName.Seaside_Cyberworld, self.player):
                    request_points += 2

                request_points += 1

            # If Songwriter beatable
            if state.can_reach_region(RegionName.Sky_Cyberworld, self.player):
                request_points += 1

            # If not Rank B, then can't do more requests
            if request_points < 10:
                return request_points

            # 2 star jobs
            # Juvenile Division always beatable. We also cannot get this far without Green Overworld and Seaside Cyberworld
            # access, so Stand In Recruit and Lumber Merchant are always beatable too
            request_points += 6

            # If For Victory! beatable
            if state.has(ItemName.GunDelS1_C, self.player):
                request_points += 2

            # If Stock Up!, Penguins Ran Away, Update Help, and Do Something! beatable
            # Note: Do Something! requires fire damage, but for simplicity, we just assume you can get those in Robo Control
            if state.can_reach_region(RegionName.Seaside_Overworld, self.player):
                request_points += 8

            # If Buy Which Stock? and Want to Meet Daughter beatable
            if state.can_reach_region(RegionName.Sky_Cyberworld, self.player):
                request_points += 4

            # If Not Enough Member beatable
            if state.has_all({ItemName.Fanfare_Z, ItemName.Discord_S, ItemName.Timpani_T}, self.player):
                request_points += 2

            # If Self Research beatable. Assumed you get PoisSeed P, and have OrderSys to buy second one.
            if state.has_all({ItemName.PoisSeed_P, ItemName.OrderSys, ItemName.Anubis_P}, self.player):
                request_points += 2

            # If not Rank B, then can't do more requests
            if request_points < 25:
                return request_points

            # 3 star jobs
            # We cannot get this far without Green Overworld and Seaside Cyberworld access, so Time Capsule and
            # Road to Soul Battler always beatable
            request_points += 6

            # If Find the Virus!, Can't Open Safe, Track the Criminal, and An Experiment! are beatable
            if state.can_reach_region(RegionName.Seaside_Overworld, self.player):
                request_points += 12

            # If Get the Bad Guy is beatable
            if state.has(ItemName.KeyData, self.player):
                request_points += 3

            # If Official Request beatable
            if state.can_reach_region(RegionName.Sky_Overworld, self.player):
                request_points += 3

            # At this point, if we have over 35 request points, all requests are available
            return request_points

        # Set Job additional area access
        self.multiworld.get_location(LocationName.Errand_Request, self.player).access_rule = \
            lambda state: \
                state.can_reach_region(RegionName.Seaside_Cyberworld, self.player)
        self.multiworld.get_location(LocationName.For_Victory, self.player).access_rule = \
            lambda state: \
                state.has(ItemName.GunDelS1_C, self.player) and \
                request_points_possible(state) >= 10
        self.multiworld.get_location(LocationName.JuvenileDiv, self.player).access_rule = \
            lambda state: \
                request_points_possible(state) >= 10
        # For Somebody Help!, we force the 10,000z option. To prevent heavy grinding, require Millions
        self.multiworld.get_location(LocationName.Somebody_Help, self.player).access_rule = \
            lambda state: \
                state.has(ItemName.Millions, self.player)
        self.multiworld.get_location(LocationName.Get_The_Chip, self.player).access_rule = \
            lambda state: \
                state.has(ItemName.DolThdr1_A, self.player)
        self.multiworld.get_location(LocationName.Stock_Up, self.player).access_rule = \
            lambda state: \
                request_points_possible(state) >= 10
        self.multiworld.get_location(LocationName.StandIn_Recruit, self.player).access_rule = \
            lambda state: \
                request_points_possible(state) >= 10
        self.multiworld.get_location(LocationName.PenguinsRanAway, self.player).access_rule = \
            lambda state: \
                request_points_possible(state) >= 10
        self.multiworld.get_location(LocationName.Daughter_Worry, self.player).access_rule = \
            lambda state: \
                state.can_reach_region(RegionName.Seaside_Cyberworld, self.player)
        self.multiworld.get_location(LocationName.Loan_Collection, self.player).access_rule = \
            lambda state: \
                state.can_reach_region(RegionName.Seaside_Cyberworld, self.player)
        self.multiworld.get_location(LocationName.Lumber_Merchant, self.player).access_rule = \
            lambda state: \
                state.can_reach_region(RegionName.Seaside_Cyberworld, self.player) and \
                request_points_possible(state) >= 10
        self.multiworld.get_location(LocationName.TimeCpsl, self.player).access_rule = \
            lambda state: \
                request_points_possible(state) >= 25
        self.multiworld.get_location(LocationName.DietGood_Money, self.player).access_rule = \
            lambda state: \
                state.can_reach_region(RegionName.Seaside_Cyberworld, self.player) and \
                state.can_reach_region(RegionName.Green_Overworld, self.player)
        self.multiworld.get_location(LocationName.Find_The_Virus, self.player).access_rule = \
            lambda state: \
                state.can_reach_region(RegionName.Seaside_Overworld, self.player) and \
                request_points_possible(state) >= 25
        self.multiworld.get_location(LocationName.Buy_Whch_Stock, self.player).access_rule = \
            lambda state: \
                request_points_possible(state) >= 10
        self.multiworld.get_location(LocationName.Cant_Open_Safe, self.player).access_rule = \
            lambda state: \
                request_points_possible(state) >= 25
        self.multiworld.get_location(LocationName.Get_The_Bad_Guy, self.player).access_rule = \
            lambda state: \
                state.has(ItemName.KeyData, self.player) and \
                request_points_possible(state) >= 25
        self.multiworld.get_location(LocationName.Update_Help, self.player).access_rule = \
            lambda state: \
                request_points_possible(state) >= 10
        # Note: This request requires fire damage, but we assume you can get fire chips from Robo Control in a worst case
        self.multiworld.get_location(LocationName.Do_Something, self.player).access_rule = \
            lambda state: \
                request_points_possible(state) >= 10
        self.multiworld.get_location(LocationName.Want_Meet_Dghtr, self.player).access_rule = \
            lambda state: \
                state.can_reach_region(RegionName.Green_Cyberworld, self.player) and \
                request_points_possible(state) >= 10
        self.multiworld.get_location(LocationName.Not_Engh_Member, self.player).access_rule = \
            lambda state: \
                state.has_all({ItemName.Fanfare_Z, ItemName.Timpani_T}, self.player) and \
                state.has(ItemName.Discord_S, self.player, 2) and \
                request_points_possible(state) >= 10
        self.multiworld.get_location(LocationName.Track_The_Crmnl_1, self.player).access_rule = \
            lambda state: \
                request_points_possible(state) >= 25
        self.multiworld.get_location(LocationName.Track_The_Crmnl_2, self.player).access_rule = \
            lambda state: \
                request_points_possible(state) >= 25
        self.multiworld.get_location(LocationName.Track_The_Crmnl_3, self.player).access_rule = \
            lambda state: \
                request_points_possible(state) >= 25
        # Pipe Comp requires access to Track the Criminal to open up
        self.multiworld.get_location(LocationName.Pipe_Comp_BMD, self.player).access_rule = \
            lambda state: \
                request_points_possible(state) >= 25
        # To do the PA, we assume you get PoisSeed P, and have OrderSys to buy a second one.
        self.multiworld.get_location(LocationName.Self_Research, self.player).access_rule = \
            lambda state: \
                state.has_all({ItemName.PoisSeed_P, ItemName.OrderSys, ItemName.Anubis_P}, self.player) and \
                request_points_possible(state) >= 10
        self.multiworld.get_location(LocationName.OfficialRequest_1, self.player).access_rule = \
            lambda state: \
                request_points_possible(state) >= 25
        self.multiworld.get_location(LocationName.OfficialRequest_2, self.player).access_rule = \
            lambda state: \
                request_points_possible(state) >= 25
        self.multiworld.get_location(LocationName.OfficialRequest_3, self.player).access_rule = \
            lambda state: \
                request_points_possible(state) >= 25
        self.multiworld.get_location(LocationName.Wheres_My_Navi, self.player).access_rule = \
            lambda state: \
                state.can_reach_region(RegionName.Undernet, self.player) and \
                request_points_possible(state) >= 35
        self.multiworld.get_location(LocationName.One_More_Time, self.player).access_rule = \
            lambda state: \
                state.can_reach_region(RegionName.Green_Overworld, self.player) and \
                state.can_reach_region(RegionName.ACDC_Overworld, self.player) and \
                request_points_possible(state) >= 35
        self.multiworld.get_location(LocationName.SupportChip_Pls, self.player).access_rule = \
            lambda state: \
                state.has_all({ItemName.Atk_30_star, ItemName.BblWrap_Q, ItemName.Geddon_A, ItemName.Recov80_H},
                              self.player) and \
                state.has(ItemName.Discord_S, self.player, 2) and \
                request_points_possible(state) >= 35
        self.multiworld.get_location(LocationName.Negotiate, self.player).access_rule = \
            lambda state: \
                state.can_reach_region(RegionName.Undernet, self.player) and \
                state.can_reach_region(RegionName.Green_Overworld, self.player) and \
                request_points_possible(state) >= 35
        self.multiworld.get_location(LocationName.An_Experiment_1, self.player).access_rule = \
            lambda state: \
                request_points_possible(state) >= 25
        self.multiworld.get_location(LocationName.An_Experiment_2, self.player).access_rule = \
            lambda state: \
                request_points_possible(state) >= 25
        self.multiworld.get_location(LocationName.An_Experiment_3, self.player).access_rule = \
            lambda state: \
                request_points_possible(state) >= 25
        self.multiworld.get_location(LocationName.RoadToSoulBtlr, self.player).access_rule = \
            lambda state: \
                state.can_reach_region(RegionName.Green_Overworld, self.player) and \
                request_points_possible(state) >= 25

        # Set Trade quests
        self.multiworld.get_location(LocationName.Central_Barr100_H_Trade, self.player).access_rule = \
            lambda state: state.has(ItemName.Barr100_H, self.player)
        self.multiworld.get_location(LocationName.Aquarium_PnlRetrn_star_Trade, self.player).access_rule = \
            lambda state: state.has(ItemName.PnlRetrn_star, self.player)
        self.multiworld.get_location(LocationName.Green_HolyPnl_S_Trade, self.player).access_rule = \
            lambda state: state.has(ItemName.HolyPanl_S, self.player)
        self.multiworld.get_location(LocationName.AirCon_AuraHed1_B_Trade, self.player).access_rule = \
            lambda state: state.has(ItemName.AuraHed1_B, self.player)
        self.multiworld.get_location(LocationName.Class_1_2_EnergBom_K_Trade, self.player).access_rule = \
            lambda state: state.has(ItemName.EnergBom_K, self.player)
        self.multiworld.get_location(LocationName.Aquarium_DublShot_C_Trade, self.player).access_rule = \
            lambda state: state.has(ItemName.DublShot_C, self.player)
        self.multiworld.get_location(LocationName.WatrMchn_HiBoomer_V_Trade, self.player).access_rule = \
            lambda state: state.has(ItemName.HiBoomer_V, self.player)
        self.multiworld.get_location(LocationName.Sky_GrabRvng_I_Trade, self.player).access_rule = \
            lambda state: state.has(ItemName.GrabRvng_I, self.player)
        self.multiworld.get_location(LocationName.ACDC_BigBomb_O_Trade, self.player).access_rule = \
            lambda state: state.has(ItemName.BigBomb_O, self.player)

        # For now, Green Quiz isn't enabled until after Aquarium Quiz. Add a rule so that this logic doesn't cause issues
        self.multiworld.get_location(LocationName.Green_Quiz_King, self.player).access_rule = \
            lambda state: state.has(ItemName.Fish, self.player)

        # Set Number Traders

        # The first 5 are considered cheap enough to grind for in Central. Robo Control 2 GMDs can drop 450-1200z.
        self.multiworld.get_location(LocationName.Lotto_Code_06, self.player).access_rule = \
            lambda state: self.explore_score(state) > 2
        self.multiworld.get_location(LocationName.Lotto_Code_07, self.player).access_rule = \
            lambda state: self.explore_score(state) > 2
        self.multiworld.get_location(LocationName.Lotto_Code_08, self.player).access_rule = \
            lambda state: self.explore_score(state) > 2
        self.multiworld.get_location(LocationName.Lotto_Code_09, self.player).access_rule = \
            lambda state: self.explore_score(state) > 2
        self.multiworld.get_location(LocationName.Lotto_Code_10, self.player).access_rule = \
            lambda state: self.explore_score(state) > 2
        self.multiworld.get_location(LocationName.Lotto_Code_11, self.player).access_rule = \
            lambda state: self.explore_score(state) > 4
        self.multiworld.get_location(LocationName.Lotto_Code_12, self.player).access_rule = \
            lambda state: self.explore_score(state) > 4
        self.multiworld.get_location(LocationName.Lotto_Code_13, self.player).access_rule = \
            lambda state: self.explore_score(state) > 4
        self.multiworld.get_location(LocationName.Lotto_Code_14, self.player).access_rule = \
            lambda state: self.explore_score(state) > 4
        self.multiworld.get_location(LocationName.Lotto_Code_15, self.player).access_rule = \
            lambda state: self.explore_score(state) > 4

        # After the first 15, require Millions logically.
        self.multiworld.get_location(LocationName.Lotto_Code_16, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_17, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_18, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_19, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_20, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_21, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_22, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_23, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_24, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_25, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)

        self.multiworld.get_location(LocationName.Lotto_Code_26, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_27, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_28, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_29, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_30, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_31, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_32, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_33, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_34, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_35, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)

        self.multiworld.get_location(LocationName.Lotto_Code_36, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_37, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_38, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_39, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_40, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_41, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_42, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_43, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_44, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_45, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)

        self.multiworld.get_location(LocationName.Lotto_Code_46, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_47, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_48, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_49, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_50, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_51, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_52, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_53, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_54, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_55, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)

        self.multiworld.get_location(LocationName.Lotto_Code_56, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_57, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)
        self.multiworld.get_location(LocationName.Lotto_Code_58, self.player).access_rule = \
            lambda state: state.has(ItemName.Millions, self.player) or state.has(ItemName.zenny_100000z, self.player)

        # Gregar requires all 4 Win Cards to be defeatable:
        self.multiworld.get_location(LocationName.Gregar_Defeated, self.player).access_rule = \
            lambda state: \
                state.has_all({ItemName.WinCardA, ItemName.WinCardB, ItemName.WinCardC, ItemName.WinCardD}, self.player)

        # place "Victory" at "Final Boss" and set collection as win condition
        self.multiworld.get_location(LocationName.Gregar_Defeated, self.player) \
            .place_locked_item(self.create_event(ItemName.Victory))
        self.multiworld.completion_condition[self.player] = \
            lambda state: state.has(ItemName.Victory, self.player)

    def generate_output(self, output_directory: str) -> None:
        rompath: str = ""

        try:
            world = self.multiworld
            player = self.player

            rom = LocalRom(get_base_rom_path())

            for location_name in location_table.keys():
                location = world.get_location(location_name, player)
                ap_item = location.item
                item_id = ap_item.code
                if item_id is not None:
                    if ap_item.player != player or item_id not in items_by_id:
                        item = ItemData(item_id, ap_item.name, ap_item.classification, ItemType.External)
                        item = item._replace(recipient=self.multiworld.player_name[ap_item.player])
                    else:
                        item = items_by_id[item_id]

                    location_data = location_data_table[location_name]
                    # print("Placing item "+item.itemName+" at location "+location_data.name)
                    rom.replace_item(location_data, item)
                    if location_data.inject_name:
                        item_name_text = "Item"
                        long_item_text = ""

                        # No item hinting
                        if self.options.trade_quest_hinting == 0:
                            item_name_text = "Check"
                        # Partial item hinting
                        elif self.options.trade_quest_hinting == 1:
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

                        rom.insert_hint_text(location_data, item_name_text, long_item_text)

            rom.inject_name(world.player_name[player])

            rompath = os.path.join(output_directory, f"{self.multiworld.get_out_file_name_base(self.player)}.gba")

            rom.write_changed_rom()
            rom.write_to_file(rompath)

            patch = MMBN6DeltaPatch(os.path.splitext(rompath)[0] + MMBN6DeltaPatch.patch_file_ending, player=player,
                                    player_name=world.player_name[player], patched_path=rompath)
            patch.write()
        except:
            raise
        finally:
            if os.path.exists(rompath):
                os.unlink(rompath)

    @classmethod
    def stage_assert_generate(cls, multiworld: "MultiWorld") -> None:
        rom_file = get_base_rom_path()
        if not os.path.exists(rom_file):
            raise FileNotFoundError(rom_file)

    def create_item(self, name: str) -> "Item":
        item = item_table[name]
        return MMBN6Item(item.itemName, item.progression, item.code, self.player)

    def create_event(self, event: str):
        # while we are at it, we can also add a helper to create events
        return MMBN6Item(event, ItemClassification.progression, None, self.player)

    def fill_slot_data(self):
        return self.options.as_dict("include_jobs", "trade_quest_hinting")

    def explore_score(self, state):
        """
        Determine roughly how much of the game you can explore to make certain checks not restrict much movement
        """
        score = 0
        if state.can_reach_region(RegionName.Seaside_Overworld, self.player):
            score += 2
        if state.can_reach_region(RegionName.Seaside_Cyberworld, self.player):
            score += 1
        if state.can_reach_region(RegionName.Green_Overworld, self.player):
            score += 1
        if state.can_reach_region(RegionName.Green_Cyberworld, self.player):
            score += 1
        if state.can_reach_region(RegionName.Sky_Overworld, self.player):
            score += 2
        if state.can_reach_region(RegionName.Sky_Cyberworld, self.player):
            score += 1
        if state.can_reach_region(RegionName.ACDC_Overworld, self.player):
            score += 1
        if state.can_reach_region(RegionName.ACDC_Cyberworld, self.player):
            score += 1
        if state.can_reach_region(RegionName.Undernet, self.player):
            score += 1
        if state.can_reach_region(RegionName.Graveyard, self.player):
            score += 1
        if state.can_reach_region(RegionName.Expo, self.player):
            score += 1
        return score
