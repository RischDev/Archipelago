import typing

from enum import IntEnum, Enum
from BaseClasses import Item, ItemClassification
from .Names.ItemName import ItemName


class ItemType(str, Enum):
    Chip = "chip"
    KeyItem = "key"
    SubChip = "subchip"
    Zenny = "zenny"
    Program = "program"
    BugFrag = "bugfrag"
    External = "External"

    __str__ = str.__str__


class ProgramColor(IntEnum):
    White = 1
    Yellow = 2
    Pink = 3
    Red = 4
    Blue = 5
    Green = 6


def chip_code(c):
    if c == '*':
        return 26
    return ord(c) - ord('A')


class ItemData(typing.NamedTuple):
    code: int
    itemName: str
    progression: ItemClassification
    type: ItemType
    itemID: int = 0x00
    subItemID: int = 0x00
    count: int = 1
    recipient: str = "Myself"


class MMBN6Item(Item):
    game: str = "MegaMan Battle Network 6 Gregar"


keyItemList: typing.List[ItemData] = [
    # ItemData(0x, ItemName.PET,		                ItemClassification.filler,	    ItemType.KeyItem, 	0),   #Given at the beginning of the game
    # ItemData(0x, ItemName.StudntID,		        ItemClassification.filler,	    ItemType.KeyItem, 	1),   #Unlocks right part of school
    # ItemData(0x, ItemName.Bucket,		            ItemClassification.filler,	    ItemType.KeyItem, 	2),   #Needed for story progression, unneeded here
    # ItemData(0x, ItemName.TeachrID,		        ItemClassification.filler,	    ItemType.KeyItem, 	3),   #Unlocks Teacher's Room
    # ItemData(0x, ItemName.Graffiti,		        ItemClassification.filler,	    ItemType.KeyItem, 	4),   #Unlocks KeyData check in Central 2
    # ItemData(0x, ItemName.WatrData,		        ItemClassification.filler,	    ItemType.KeyItem, 	5),   #Given for Robo Control Comps, unneeded here.
    ItemData(0xB61000, ItemName.KeyData, ItemClassification.progression, ItemType.KeyItem, 6),  # Unlocks Central 3 door
    ItemData(0xB61001, ItemName.Fish, ItemClassification.progression, ItemType.KeyItem, 7),
    # Needed for story progression, used to unlock SeaSide LevBus
    ItemData(0xB61002, ItemName.ToolPrgm, ItemClassification.progression, ItemType.KeyItem, 8),
    # Unlocks Seaside Internet Area
    # ItemData(0x, ItemName.Toy,		                ItemClassification.filler,	    ItemType.KeyItem, 	9),   #???

    ItemData(0xB61003, ItemName.BeastOut, ItemClassification.useful, ItemType.KeyItem, 10),
    # Re-named from HealWatr, since it's thematic
    ItemData(0xB61004, ItemName.TagChip, ItemClassification.useful, ItemType.KeyItem, 11),
    # Given by email, unlocks Tag System
    # ItemData(0x, ItemName.Report,		            ItemClassification.filler,	    ItemType.KeyItem, 	12),  #???
    # ItemData(0x, ItemName.ImgData,		            ItemClassification.filler,	    ItemType.KeyItem, 	13),  #???
    ItemData(0xB61005, ItemName.AuthData, ItemClassification.progression, ItemType.KeyItem, 14),
    # Needed for story progression, used to unlock Green LevBus
    ItemData(0xB61006, ItemName.Umbrella, ItemClassification.progression, ItemType.KeyItem, 15),
    # Used to unlock Sky LevBus
    ItemData(0xB61007, ItemName.WinCardA, ItemClassification.progression, ItemType.KeyItem, 16),
    # Used as win condition
    ItemData(0xB61008, ItemName.WinCardB, ItemClassification.progression, ItemType.KeyItem, 17),
    # Used as win condition
    ItemData(0xB61009, ItemName.WinCardC, ItemClassification.progression, ItemType.KeyItem, 18),
    # Used as win condition
    ItemData(0xB6100A, ItemName.WinCardD, ItemClassification.progression, ItemType.KeyItem, 19),
    # Used as win condition

    # ItemData(0x, ItemName.CybrBat1,		        ItemClassification.filler,	    ItemType.KeyItem, 	20),  #???
    # ItemData(0x, ItemName.CybrBat2,		        ItemClassification.filler,	    ItemType.KeyItem, 	21),  #???
    # ItemData(0x, ItemName.CybrBat3,		        ItemClassification.filler,	    ItemType.KeyItem, 	22),  #???
    # ItemData(0x, ItemName.CybrBat4,		        ItemClassification.filler,	    ItemType.KeyItem, 	23),  #???
    # ItemData(0x, ItemName.CybrBat5,		        ItemClassification.filler,	    ItemType.KeyItem, 	24),  #???
    # ItemData(0x, ItemName.MoonSton,		        ItemClassification.filler,	    ItemType.KeyItem, 	25),  #Used for story progression
    ItemData(0xB6100B, ItemName.ACDCKyDt, ItemClassification.progression, ItemType.KeyItem, 26),
    # Unlocks door in ACDC Area, used to unlock ACDC LevBus
    ItemData(0xB6100C, ItemName.AreaPass, ItemClassification.progression, ItemType.KeyItem, 27),
    # Used to go from Central 3 to ACDC Area
    ItemData(0xB6100D, ItemName.VacData, ItemClassification.progression, ItemType.KeyItem, 28),
    # Used to go from Central 3 to Sky Area
    # ItemData(0x, ItemName.PcktWtch,		        ItemClassification.filler,	    ItemType.KeyItem, 	29),  #Needed in Find Keepsake request

    # ItemData(0x, ItemName.TunaData,		        ItemClassification.filler,	    ItemType.KeyItem, 	30),  #Needed in Stock Up request
    # ItemData(0x, ItemName.SalmData,		        ItemClassification.filler,	    ItemType.KeyItem, 	31),  #Needed in Stock Up request
    # ItemData(0x, ItemName.EelData,		            ItemClassification.filler,	    ItemType.KeyItem, 	32),  #Needed in Stock Up request
    # ItemData(0x, ItemName.ShrimpDt,		        ItemClassification.filler,	    ItemType.KeyItem, 	33),  #Needed in Stock Up request
    # ItemData(0x, ItemName.HrringDt,		        ItemClassification.filler,	    ItemType.KeyItem, 	34),  #Needed in Stock Up request
    # ItemData(0x, ItemName.YTailDat,		        ItemClassification.filler,	    ItemType.KeyItem, 	35),  #Needed in Stock Up request
    # ItemData(0x, ItemName.UrchnDat,		        ItemClassification.filler,	    ItemType.KeyItem, 	36),  #Needed in Stock Up request
    # ItemData(0x, ItemName.SnpprDat,		        ItemClassification.filler,	    ItemType.KeyItem, 	37),  #Needed in Stock Up request
    # ItemData(0x, ItemName.TimeCpsl,		        ItemClassification.filler,	    ItemType.KeyItem, 	38),  #Needed in TimeCpsl request
    # ItemData(0x, ItemName.CashData,		        ItemClassification.filler,	    ItemType.KeyItem, 	39),  #Job related?

    # ItemData(0x, ItemName.TextData,		        ItemClassification.filler,	    ItemType.KeyItem, 	40),  #Job related?
    # ItemData(0x, ItemName.Pendant,		            ItemClassification.filler,	    ItemType.KeyItem, 	41),  #Job related?
    # ItemData(0x, ItemName.RplyLttr,		        ItemClassification.filler,	    ItemType.KeyItem, 	42),  #Job related?
    ItemData(0xB6100E, ItemName.StampCrd, ItemClassification.progression, ItemType.KeyItem, 43),
    # Used in Pavilion, used to unlock Expo Site
    # ItemData(0x, ItemName.RushFood,		        ItemClassification.filler,	    ItemType.KeyItem, 	44),  #Used for shortcuts
    # ItemData(0x, ItemName.CyberAxe,		        ItemClassification.filler,	    ItemType.KeyItem, 	45),  #Needed in Lumber Merchant request
    # ItemData(0x, ItemName.Tulip,		            ItemClassification.filler,	    ItemType.KeyItem, 	46),  #Needed in One More Time. request
    # ItemData(0x, ItemName.UpdtData,		        ItemClassification.filler,	    ItemType.KeyItem, 	47),  #Needed in Update Help request
    # ItemData(0x, ItemName.Coffee,		            ItemClassification.filler,	    ItemType.KeyItem, 	48),  #Needed in Track the Criminal request
    # ItemData(0x, ItemName.ScrtData,		        ItemClassification.filler,	    ItemType.KeyItem, 	49),  #Job related?

    # ItemData(0x, ItemName.CrosBatc,		        ItemClassification.filler,	    ItemType.KeyItem, 	50),  #Job related?
    ItemData(0xB6100F, ItemName.BatKey, ItemClassification.progression, ItemType.KeyItem, 51),
    # Used to unlock Graveyard Area
    # ItemData(0x, ItemName.ScrtMemo,		        ItemClassification.filler,	    ItemType.KeyItem, 	52),  #Job related?
    ItemData(0xB61010, ItemName.HeatCross, ItemClassification.progression, ItemType.KeyItem, 53),
    # Renamed from QuizData
    # ItemData(0x, ItemName.ScrblDat,		        ItemClassification.filler,	    ItemType.KeyItem, 	54),  #Job related?
    ItemData(0xB61011, ItemName.SlashCross, ItemClassification.progression, ItemType.KeyItem, 55),
    # Renamed from PngnThnk
    ItemData(0xB61012, ItemName.ElecCross, ItemClassification.progression, ItemType.KeyItem, 56),
    # Renamed from RefrncBk
    ItemData(0xB61013, ItemName.OrderSys, ItemClassification.progression, ItemType.KeyItem, 57),
    # Renamed QuizBook to be OrderSys
    ItemData(0xB61014, ItemName.EraseCross, ItemClassification.progression, ItemType.KeyItem, 58),
    # Renamed from InvteCrd
    # ItemData(0x, ItemName.ThnkULtr,		        ItemClassification.filler,	    ItemType.KeyItem, 	59),  #Job related?

    ItemData(0xB61015, ItemName.ChargeCross, ItemClassification.progression, ItemType.KeyItem, 60),
    # Renamed from SrialDat
    # ItemData(0x, ItemName.SciManul,		        ItemClassification.filler,	    ItemType.KeyItem, 	61),  #Reward for Self Research request, lotto code. Renamed to AP Item
    # ItemData(0x, ItemName.SoulEmbl,		        ItemClassification.filler,	    ItemType.KeyItem, 	62),  #Reward for RodToSoulBtlr! request, lotto code
    # ItemData(0x, ItemName.NaviRuin,		        ItemClassification.filler,	    ItemType.KeyItem, 	63),  #Needed in Where's My Navi request
    # ItemData(0x, ItemName.BtlrCard,		        ItemClassification.filler,	    ItemType.KeyItem, 	64),  #Unlocks Virus Battler and rare viruses
    # ItemData(0x, ItemName.F.Fries,		            ItemClassification.filler,	    ItemType.KeyItem, 	65),  #Needed in Got a Problem. request
    ItemData(0xB61016, ItemName.CybBrdAx, ItemClassification.progression, ItemType.KeyItem, 66),
    # Used to go from Central 3 to Green Area
    # ItemData(0x, ItemName.ResrvTck,		        ItemClassification.filler,	    ItemType.KeyItem, 	67),  #Needed in Errand Request request
    ItemData(0xB61017, ItemName.WWWID, ItemClassification.progression, ItemType.KeyItem, 68),
    # Unlocks certain location checks
    # ItemData(0x, ItemName.SeaSdKey,		        ItemClassification.filler,	    ItemType.KeyItem, 	70),  #Unlocks door in Seaside 3

    ItemData(0xB61018, ItemName.SpinWhit, ItemClassification.useful, ItemType.KeyItem, 80),  # Useful NaviCust upgrade
    ItemData(0xB61019, ItemName.SpinYllw, ItemClassification.useful, ItemType.KeyItem, 81),  # Useful NaviCust upgrade
    ItemData(0xB6101A, ItemName.SpinPink, ItemClassification.useful, ItemType.KeyItem, 82),  # Useful NaviCust upgrade
    ItemData(0xB6101B, ItemName.SpinRed, ItemClassification.useful, ItemType.KeyItem, 83),  # Useful NaviCust upgrade
    ItemData(0xB6101C, ItemName.SpinBlue, ItemClassification.useful, ItemType.KeyItem, 84),  # Useful NaviCust upgrade
    ItemData(0xB6101D, ItemName.SpinGrn, ItemClassification.useful, ItemType.KeyItem, 85),  # Useful NaviCust upgrade
    # ItemData(0x, ItemName.SchPCode,		        ItemClassification.filler,	    ItemType.KeyItem, 	96),  #Unlocks Lab 1 Comp
    # ItemData(0xB6101E, ItemName.WtrBannr,		    ItemClassification.progression,	ItemType.KeyItem, 	104), #SeaSide HP Shortcut
    # ItemData(0xB6101F, ItemName.GrnBannr,		    ItemClassification.progression,	ItemType.KeyItem, 	105), #Green HP Shortcut
    # ItemData(0xB61020, ItemName.SkyBannr,		    ItemClassification.progression,	ItemType.KeyItem, 	106), #Sky HP Shortcut

    # ItemData(0xB61021, ItemName.ACDCBanr,		    ItemClassification.progression,	ItemType.KeyItem, 	107), #ACDC HP Shortcut
    ItemData(0xB61022, ItemName.HPMemry, ItemClassification.useful, ItemType.KeyItem, 112),
    ItemData(0xB61023, ItemName.ExpMemry, ItemClassification.useful, ItemType.KeyItem, 113),
    ItemData(0xB61024, ItemName.RegUP1, ItemClassification.filler, ItemType.KeyItem, 114),
    ItemData(0xB61025, ItemName.RegUP2, ItemClassification.filler, ItemType.KeyItem, 115),
    ItemData(0xB61026, ItemName.RegUP3, ItemClassification.useful, ItemType.KeyItem, 116),
    ItemData(0xB61027, ItemName.SubMemry, ItemClassification.filler, ItemType.KeyItem, 117)
]

subChipList: typing.List[ItemData] = [
    ItemData(0xB61028, ItemName.Unlocker, ItemClassification.progression, ItemType.SubChip, 133),
    ItemData(0xB61029, ItemName.Untrap, ItemClassification.filler, ItemType.SubChip, 131),
    ItemData(0xB6102A, ItemName.LocEnemy, ItemClassification.filler, ItemType.SubChip, 132),
    ItemData(0xB6102B, ItemName.MiniEnrg, ItemClassification.filler, ItemType.SubChip, 128),
    ItemData(0xB6102C, ItemName.FullEnrg, ItemClassification.filler, ItemType.SubChip, 129),
    ItemData(0xB6102D, ItemName.SneakRun, ItemClassification.filler, ItemType.SubChip, 130)
]

chipList: typing.List[ItemData] = [
    ItemData(0xB6102E, ItemName.AirHocky_M, ItemClassification.useful, ItemType.Chip, 50, chip_code('M')),  # Trade
    ItemData(0xB6102F, ItemName.AirSpin2_L, ItemClassification.filler, ItemType.Chip, 127, chip_code('L')),  # Trade
    ItemData(0xB61030, ItemName.AirSpin3_O, ItemClassification.useful, ItemType.Chip, 128, chip_code('O')),
    # Lotto Code
    ItemData(0xB61031, ItemName.AntiNavi_star, ItemClassification.filler, ItemType.Chip, 186, chip_code('*')),
    # Request
    ItemData(0xB61032, ItemName.AntiRecv_star, ItemClassification.filler, ItemType.Chip, 189, chip_code('*')),
    # Request
    ItemData(0xB61033, ItemName.AntiSwrd_star, ItemClassification.filler, ItemType.Chip, 188, chip_code('*')),
    # NetCafe
    ItemData(0xB61034, ItemName.Anubis_P, ItemClassification.progression, ItemType.Chip, 152, chip_code('P')),
    # PMD, Request Required
    ItemData(0xB61035, ItemName.AreaGrab_star, ItemClassification.filler, ItemType.Chip, 163, chip_code('*')),
    # Request
    ItemData(0xB61036, ItemName.Atk_30_star, ItemClassification.progression, ItemType.Chip, 195, chip_code('*')),  # PMD
    ItemData(0xB61037, ItemName.AuraHed1_B, ItemClassification.progression, ItemType.Chip, 95, chip_code('B')),
    # Virus Drop, Trade Required

    ItemData(0xB61038, ItemName.Barr100_H, ItemClassification.progression, ItemType.Chip, 179, chip_code('H')),
    # BMD, Trade Required
    ItemData(0xB61039, ItemName.BigBomb_O, ItemClassification.progression, ItemType.Chip, 202, chip_code('O')),
    # Trade, Trade Required
    ItemData(0xB6103A, ItemName.BigBomb_P, ItemClassification.filler, ItemType.Chip, 202, chip_code('P')),  # Request
    ItemData(0xB6103B, ItemName.BlastMan_star, ItemClassification.useful, ItemType.Chip, 257, chip_code('*')),
    # Lotto Code
    ItemData(0xB6103C, ItemName.BlkBomb_F, ItemClassification.useful, ItemType.Chip, 60, chip_code('F')),  # PMD
    ItemData(0xB6103D, ItemName.BlzrdBal_H, ItemClassification.filler, ItemType.Chip, 199, chip_code('H')),
    # Lotto Code
    ItemData(0xB6103E, ItemName.BblWrap_Q, ItemClassification.progression, ItemType.Chip, 181, chip_code('Q')),
    # BugFrag Trader, Request Required
    ItemData(0xB6103F, ItemName.BugFix_P, ItemClassification.filler, ItemType.Chip, 176, chip_code('P')),  # PMD
    ItemData(0xB61040, ItemName.BugFix_star, ItemClassification.filler, ItemType.Chip, 176, chip_code('*')),
    # Virus Battler
    ItemData(0xB61041, ItemName.ChrgeMan_star, ItemClassification.useful, ItemType.Chip, 239, chip_code('*')),
    # Lotto Code

    ItemData(0xB61042, ItemName.CircGun_V, ItemClassification.filler, ItemType.Chip, 142, chip_code('V')),  # Lotto Code
    ItemData(0xB61043, ItemName.CircGun_P, ItemClassification.filler, ItemType.Chip, 142, chip_code('P')),  # PMD
    ItemData(0xB61044, ItemName.ColArmy_star, ItemClassification.filler, ItemType.Chip, 198, chip_code('*')),
    # Lotto Code
    ItemData(0xB61045, ItemName.ColArmy_B, ItemClassification.filler, ItemType.Chip, 198, chip_code('B')),  # BMD
    ItemData(0xB61046, ItemName.Colonel_star, ItemClassification.useful, ItemType.Chip, 272, chip_code('*')),  # Request
    ItemData(0xB61047, ItemName.ColorPt_star, ItemClassification.filler, ItemType.Chip, 194, chip_code('*')),  # BMD
    ItemData(0xB61048, ItemName.ComingRd_star, ItemClassification.filler, ItemType.Chip, 170, chip_code('*')),  # BMD
    ItemData(0xB61049, ItemName.CopyDmg_star, ItemClassification.filler, ItemType.Chip, 190, chip_code('*')),  # BMD
    ItemData(0xB6104A, ItemName.CrcusMan_star, ItemClassification.useful, ItemType.Chip, 263, chip_code('*')),
    # Request
    ItemData(0xB6104B, ItemName.DblPoint_star, ItemClassification.useful, ItemType.Chip, 196, chip_code('*')),  # BMD

    ItemData(0xB6104C, ItemName.Discord_S, ItemClassification.progression, ItemType.Chip, 147, chip_code('S')),
    # Virus Drop, Request Required
    ItemData(0xB6104D, ItemName.Diveman_star, ItemClassification.useful, ItemType.Chip, 260, chip_code('*')),
    # Lotto Code
    ItemData(0xB6104E, ItemName.DolThdr1_A, ItemClassification.progression, ItemType.Chip, 31, chip_code('A')),
    # Virus drop, Request Required
    ItemData(0xB6104F, ItemName.DrilArm_M, ItemClassification.filler, ItemType.Chip, 51, chip_code('M')),  # Lotto Code
    ItemData(0xB61050, ItemName.DublShot_C, ItemClassification.progression, ItemType.Chip, 90, chip_code('C')),
    # Trade, Trade Required
    ItemData(0xB61051, ItemName.DublShot_star, ItemClassification.filler, ItemType.Chip, 90, chip_code('*')),  # BMD
    ItemData(0xB61052, ItemName.ElecMan_star, ItemClassification.useful, ItemType.Chip, 230, chip_code('*')),
    # Lotto Code
    ItemData(0xB61053, ItemName.ElecSwrd_E, ItemClassification.filler, ItemType.Chip, 78, chip_code('E')),  # PMD
    ItemData(0xB61054, ItemName.ElemTrap_star, ItemClassification.filler, ItemType.Chip, 197, chip_code('*')),
    # Lotto Code
    ItemData(0xB61055, ItemName.ElmntMan_star, ItemClassification.useful, ItemType.Chip, 269, chip_code('*')),
    # Request

    ItemData(0xB61056, ItemName.EnergBom_K, ItemClassification.progression, ItemType.Chip, 55, chip_code('K')),
    # BMD, Trade Required
    ItemData(0xB61057, ItemName.EraseMan_star, ItemClassification.useful, ItemType.Chip, 236, chip_code('*')),
    # Lotto Code
    ItemData(0xB61058, ItemName.Fan_star, ItemClassification.filler, ItemType.Chip, 130, chip_code('*')),  # BMD
    ItemData(0xB61059, ItemName.Fanfare_Z, ItemClassification.progression, ItemType.Chip, 146, chip_code('Z')),
    # Virus Drop, Request Required
    ItemData(0xB6105A, ItemName.FireHit1_F, ItemClassification.filler, ItemType.Chip, 107, chip_code('F')),  # BMD
    ItemData(0xB6105B, ItemName.FstGauge_star, ItemClassification.useful, ItemType.Chip, 173, chip_code('*')),
    # Request
    ItemData(0xB6105C, ItemName.Geddon_A, ItemClassification.progression, ItemType.Chip, 167, chip_code('A')),
    # Trade, Request Required
    ItemData(0xB6105D, ItemName.Geddon_star, ItemClassification.filler, ItemType.Chip, 167, chip_code('*')),
    # Lotto Code
    ItemData(0xB6105E, ItemName.GrabRvng_I, ItemClassification.progression, ItemType.Chip, 165, chip_code('I')),
    # Trade, Trade Required
    ItemData(0xB6105F, ItemName.GoingRd_star, ItemClassification.filler, ItemType.Chip, 171, chip_code('*')),  # BMD

    ItemData(0xB61060, ItemName.Guardian_O, ItemClassification.useful, ItemType.Chip, 151, chip_code('O')),  # PMD
    ItemData(0xB61061, ItemName.GunDelS1_C, ItemClassification.progression, ItemType.Chip, 15, chip_code('C')),
    # Tab's Shop, Request Required
    ItemData(0xB61062, ItemName.GunDelS2_E, ItemClassification.filler, ItemType.Chip, 16, chip_code('E')),  # BMD
    ItemData(0xB61063, ItemName.GunDelS3_W, ItemClassification.filler, ItemType.Chip, 17, chip_code('W')),  # Lotto Code
    ItemData(0xB61064, ItemName.HeatMan_star, ItemClassification.useful, ItemType.Chip, 227, chip_code('*')),
    # Lotto Code
    ItemData(0xB61065, ItemName.HiBoomer_V, ItemClassification.progression, ItemType.Chip, 117, chip_code('V')),
    # Trade, Trade Required
    ItemData(0xB61066, ItemName.HiCannon_M, ItemClassification.filler, ItemType.Chip, 2, chip_code('M')),  # BMD
    ItemData(0xB61067, ItemName.HiCannon_L, ItemClassification.filler, ItemType.Chip, 2, chip_code('L')),  # BMD
    ItemData(0xB61068, ItemName.HolyPanl_A, ItemClassification.filler, ItemType.Chip, 168, chip_code('A')),  # BMD
    ItemData(0xB61069, ItemName.HolyPanl_S, ItemClassification.progression, ItemType.Chip, 168, chip_code('S')),
    # GMD, Trade Required

    ItemData(0xB6106A, ItemName.IceSeed_A, ItemClassification.filler, ItemType.Chip, 69, chip_code('A')),  # BMD
    ItemData(0xB6106B, ItemName.IceSeed_star, ItemClassification.filler, ItemType.Chip, 69, chip_code('*')),  # BMD
    ItemData(0xB6106C, ItemName.JudgeMan_star, ItemClassification.useful, ItemType.Chip, 266, chip_code('*')),
    # Request
    ItemData(0xB6106D, ItemName.JustcOne_J, ItemClassification.useful, ItemType.Chip, 140, chip_code('J')),  # Trade
    ItemData(0xB6106E, ItemName.Lance_star, ItemClassification.useful, ItemType.Chip, 119, chip_code('*')),
    # Lotto Code
    ItemData(0xB6106F, ItemName.Lance_W, ItemClassification.filler, ItemType.Chip, 119, chip_code('W')),  # PMD
    ItemData(0xB61070, ItemName.LifeSync_star, ItemClassification.filler, ItemType.Chip, 191, chip_code('*')),  # BMD
    ItemData(0xB61071, ItemName.LongBlde_B, ItemClassification.filler, ItemType.Chip, 75, chip_code('B')),  # BMD
    ItemData(0xB61072, ItemName.M_Boomer_M, ItemClassification.filler, ItemType.Chip, 118, chip_code('M')),
    # Lotto Code
    ItemData(0xB61073, ItemName.M_Cannon_star, ItemClassification.filler, ItemType.Chip, 3, chip_code('*')),  # BMD

    ItemData(0xB61074, ItemName.M_Cannon_S, ItemClassification.filler, ItemType.Chip, 3, chip_code('S')),  # BMD
    ItemData(0xB61075, ItemName.MuraMasa_M, ItemClassification.filler, ItemType.Chip, 85, chip_code('M')),  # PMD
    ItemData(0xB61076, ItemName.PnlRetrn_star, ItemClassification.progression, ItemType.Chip, 166, chip_code('*')),
    # BMD, Trade Required
    ItemData(0xB61077, ItemName.PoisSeed_P, ItemClassification.progression, ItemType.Chip, 70, chip_code('P')),
    # BugFrag Trader/Chip Order, Request Required
    ItemData(0xB61078, ItemName.ProtoMan_star, ItemClassification.useful, ItemType.Chip, 224, chip_code('*')),
    # Request
    ItemData(0xB61079, ItemName.Recov80_H, ItemClassification.progression, ItemType.Chip, 157, chip_code('H')),
    # OrderSys, Request Required
    ItemData(0xB6107A, ItemName.Recov120_F, ItemClassification.filler, ItemType.Chip, 158, chip_code('F')),  # BMD
    ItemData(0xB6107B, ItemName.Recov150_M, ItemClassification.filler, ItemType.Chip, 159, chip_code('M')),  # BMD
    ItemData(0xB6107C, ItemName.Recov200_Z, ItemClassification.filler, ItemType.Chip, 160, chip_code('Z')),  # BMD
    ItemData(0xB6107D, ItemName.Recov300_Y, ItemClassification.filler, ItemType.Chip, 161, chip_code('Y')),
    # Lotto Code

    ItemData(0xB6107E, ItemName.Recov30_star, ItemClassification.filler, ItemType.Chip, 155, chip_code('*')),  # BMD
    ItemData(0xB6107F, ItemName.Roll_star, ItemClassification.useful, ItemType.Chip, 221, chip_code('*')),  # Request
    ItemData(0xB61080, ItemName.SlashMan_star, ItemClassification.useful, ItemType.Chip, 233, chip_code('*')),
    # Lotto Code
    ItemData(0xB61081, ItemName.Snake_H, ItemClassification.filler, ItemType.Chip, 134, chip_code('H')),  # PMD
    ItemData(0xB61082, ItemName.Spreadr1_M, ItemClassification.filler, ItemType.Chip, 9, chip_code('M')),  # BMD
    ItemData(0xB61083, ItemName.Spreadr2_C, ItemClassification.filler, ItemType.Chip, 10, chip_code('C')),  # BMD
    ItemData(0xB61084, ItemName.Spreadr3_S, ItemClassification.filler, ItemType.Chip, 11, chip_code('S')),  # BMD
    ItemData(0xB61085, ItemName.Spreadr3_star, ItemClassification.filler, ItemType.Chip, 11, chip_code('*')),  # BMD
    ItemData(0xB61086, ItemName.Spreadr3_R, ItemClassification.filler, ItemType.Chip, 11, chip_code('R')),  # Request
    ItemData(0xB61087, ItemName.StepSwrd_L, ItemClassification.filler, ItemType.Chip, 81, chip_code('L')),  # BMD

    ItemData(0xB61088, ItemName.StepSwrd_B, ItemClassification.filler, ItemType.Chip, 81, chip_code('B')),  # PMD
    ItemData(0xB61089, ItemName.SuprVulc_V, ItemClassification.filler, ItemType.Chip, 8, chip_code('V')),
    # Virus Battler
    ItemData(0xB6108A, ItemName.Thunder_star, ItemClassification.filler, ItemType.Chip, 30, chip_code('*')),  # BMD
    ItemData(0xB6108B, ItemName.TimeBom3_M, ItemClassification.filler, ItemType.Chip, 201, chip_code('M')),
    # Lotto Code
    ItemData(0xB6108C, ItemName.TimeBom3_N, ItemClassification.filler, ItemType.Chip, 201, chip_code('N')),  # Trade
    ItemData(0xB6108D, ItemName.Timpani_T, ItemClassification.progression, ItemType.Chip, 148, chip_code('T')),
    # Virus Drop/OrderSys, Request Required
    ItemData(0xB6108E, ItemName.Tornado_L, ItemClassification.filler, ItemType.Chip, 52, chip_code('L')),  # PMD
    ItemData(0xB6108F, ItemName.TrplShot_star, ItemClassification.filler, ItemType.Chip, 91, chip_code('*')),  # BMD
    ItemData(0xB61090, ItemName.Uninstll_G, ItemClassification.filler, ItemType.Chip, 185, chip_code('G')),
    # Lotto Code
    ItemData(0xB61091, ItemName.VarSwrd_W, ItemClassification.filler, ItemType.Chip, 82, chip_code('W')),  # PMD

    ItemData(0xB61092, ItemName.Vdoll_F, ItemClassification.filler, ItemType.Chip, 150, chip_code('F')),  # BMD
    ItemData(0xB61093, ItemName.Vulcan2_D, ItemClassification.filler, ItemType.Chip, 6, chip_code('D')),  # BMD
    ItemData(0xB61094, ItemName.Vulcan3_A, ItemClassification.filler, ItemType.Chip, 7, chip_code('A')),  # BMD
    ItemData(0xB61095, ItemName.WhiCapsl_star, ItemClassification.filler, ItemType.Chip, 184, chip_code('*')),  # BMD
    ItemData(0xB61096, ItemName.WideBlde_B, ItemClassification.filler, ItemType.Chip, 74, chip_code('B')),  # PMD
    ItemData(0xB61097, ItemName.WindRack_star, ItemClassification.filler, ItemType.Chip, 80, chip_code('*')),
    # Virus Battler
    ItemData(0xB61098, ItemName.YoYo_N, ItemClassification.filler, ItemType.Chip, 19, chip_code('N')),  # BMD
    ItemData(0xB61099, ItemName.YoYo_star, ItemClassification.filler, ItemType.Chip, 19, chip_code('*'))  # BMD
]

secretChipList: typing.List[ItemData] = [
    ItemData(0xB6109A, ItemName.DustMan_star, ItemClassification.useful, ItemType.Chip, 254, chip_code('*')),
    ItemData(0xB6109B, ItemName.DustMan_D, ItemClassification.filler, ItemType.Chip, 254, chip_code('D')),
    ItemData(0xB6109C, ItemName.DustManEX_D, ItemClassification.filler, ItemType.Chip, 255, chip_code('D')),
    ItemData(0xB6109D, ItemName.DustManSP_D, ItemClassification.useful, ItemType.Chip, 256, chip_code('D')),
    ItemData(0xB6109E, ItemName.GrndMan_star, ItemClassification.useful, ItemType.Chip, 251, chip_code('*')),
    ItemData(0xB6109F, ItemName.GrndMan_G, ItemClassification.filler, ItemType.Chip, 251, chip_code('G')),
    ItemData(0xB610A0, ItemName.GrndManEX_G, ItemClassification.filler, ItemType.Chip, 252, chip_code('G')),
    ItemData(0xB610A1, ItemName.GrndManSP_G, ItemClassification.useful, ItemType.Chip, 253, chip_code('G')),
    ItemData(0xB610A2, ItemName.SpoutMan_star, ItemClassification.useful, ItemType.Chip, 242, chip_code('*')),
    ItemData(0xB610A3, ItemName.SpoutMan_A, ItemClassification.filler, ItemType.Chip, 242, chip_code('A')),

    ItemData(0xB610A4, ItemName.SpoutMnEX_A, ItemClassification.filler, ItemType.Chip, 243, chip_code('A')),
    ItemData(0xB610A5, ItemName.SpoutMnSP_A, ItemClassification.useful, ItemType.Chip, 244, chip_code('A')),
    ItemData(0xB610A6, ItemName.TenguMan_star, ItemClassification.useful, ItemType.Chip, 248, chip_code('*')),
    ItemData(0xB610A7, ItemName.TenguMan_T, ItemClassification.filler, ItemType.Chip, 248, chip_code('T')),
    ItemData(0xB610A8, ItemName.TenguMnEX_T, ItemClassification.filler, ItemType.Chip, 249, chip_code('T')),
    ItemData(0xB610A9, ItemName.TenguMnSP_T, ItemClassification.useful, ItemType.Chip, 250, chip_code('T')),
    ItemData(0xB610AA, ItemName.TmhkMan_star, ItemClassification.useful, ItemType.Chip, 245, chip_code('*')),
    ItemData(0xB610AB, ItemName.TmhkMan_T, ItemClassification.filler, ItemType.Chip, 245, chip_code('T')),
    ItemData(0xB610AC, ItemName.TmhkManEX_T, ItemClassification.filler, ItemType.Chip, 246, chip_code('T')),
    ItemData(0xB610AD, ItemName.TmhkManSP_T, ItemClassification.useful, ItemType.Chip, 247, chip_code('T'))
]

programList: typing.List[ItemData] = [
    ItemData(0xB610AE, ItemName.AirShoes, ItemClassification.filler, ItemType.Program, 12, ProgramColor.White),
    ItemData(0xB610AF, ItemName.AntiDmg, ItemClassification.filler, ItemType.Program, 10, ProgramColor.Green),
    ItemData(0xB610B0, ItemName.Attack_Plus_Blue, ItemClassification.filler, ItemType.Program, 35, ProgramColor.Blue),
    ItemData(0xB610B1, ItemName.Attack_Plus_Pink, ItemClassification.filler, ItemType.Program, 35, ProgramColor.Pink),
    ItemData(0xB610B2, ItemName.Attack_Plus_Red, ItemClassification.filler, ItemType.Program, 35, ProgramColor.Red),
    ItemData(0xB610B3, ItemName.AttckMAX, ItemClassification.useful, ItemType.Program, 38, ProgramColor.Red),
    ItemData(0xB610B4, ItemName.AutoHeal, ItemClassification.filler, ItemType.Program, 26, ProgramColor.Pink),
    ItemData(0xB610B5, ItemName.Battery, ItemClassification.filler, ItemType.Program, 19, ProgramColor.Yellow),
    # ItemData(0x,      ItemName.Beat,               ItemClassification.filler, ItemType.Program, 33, ProgramColor.Blue),   #Multiplayer only
    ItemData(0xB610B6, ItemName.BodyPack, ItemClassification.useful, ItemType.Program, 28, ProgramColor.Pink),

    ItemData(0xB610B7, ItemName.BugStop, ItemClassification.useful, ItemType.Program, 31, ProgramColor.Yellow),
    ItemData(0xB610B8, ItemName.BustPack, ItemClassification.useful, ItemType.Program, 27, ProgramColor.Red),
    ItemData(0xB610B9, ItemName.Charge_Plus_Green, ItemClassification.filler, ItemType.Program, 37, ProgramColor.Green),
    ItemData(0xB610BA, ItemName.Charge_Plus_Pink, ItemClassification.filler, ItemType.Program, 37, ProgramColor.Pink),
    ItemData(0xB610BB, ItemName.Charge_Plus_White, ItemClassification.filler, ItemType.Program, 37, ProgramColor.White),
    ItemData(0xB610BC, ItemName.ChargMAX, ItemClassification.useful, ItemType.Program, 40, ProgramColor.Blue),
    # ItemData(0x,      ItemName.ChpShufl,           ItemClassification.filler, ItemType.Program, 14, ProgramColor.Green),  #Shop only
    # ItemData(0x,      ItemName.Collect,            ItemClassification.filler, ItemType.Program, 21, ProgramColor.Pink),   #Shop only
    # ItemData(0x,      ItemName.Custom1,            ItemClassification.useful, ItemType.Program, 2,  ProgramColor.Blue),   #Shop only
    ItemData(0xB610BD, ItemName.Custom2, ItemClassification.useful, ItemType.Program, 3, ProgramColor.White),

    ItemData(0xB610BE, ItemName.Fish_Prog, ItemClassification.filler, ItemType.Program, 18, ProgramColor.Blue),
    ItemData(0xB610BF, ItemName.FldrPak1, ItemClassification.filler, ItemType.Program, 29, ProgramColor.Yellow),
    ItemData(0xB610C0, ItemName.FldrPak2, ItemClassification.filler, ItemType.Program, 30, ProgramColor.Pink),
    # ItemData(0x,      ItemName.FlotShoe,           ItemClassification.filler, ItemType.Program, 11, ProgramColor.Pink),   #Shop only
    ItemData(0xB610C1, ItemName.FstBarr, ItemClassification.useful, ItemType.Program, 7, ProgramColor.Blue),
    # ItemData(0x,      ItemName.GigFldr1,           ItemClassification.filler, ItemType.Program, 6,  ProgramColor.Red),    #Shop only
    ItemData(0xB610C2, ItemName.HP_100_Blue, ItemClassification.filler, ItemType.Program, 42, ProgramColor.Blue),
    ItemData(0xB610C3, ItemName.HP_100_Pink, ItemClassification.filler, ItemType.Program, 42, ProgramColor.Pink),
    ItemData(0xB610C4, ItemName.HP_100_White, ItemClassification.filler, ItemType.Program, 42, ProgramColor.White),
    ItemData(0xB610C5, ItemName.HP_200_Blue, ItemClassification.filler, ItemType.Program, 43, ProgramColor.Blue),

    ItemData(0xB610C6, ItemName.HP_200_White, ItemClassification.filler, ItemType.Program, 43, ProgramColor.White),
    # ItemData(0x,      ItemName.HP_200_Yellow,      ItemClassification.filler, ItemType.Program, 43, ProgramColor.Yellow), #Shop only
    ItemData(0xB610C7, ItemName.HP_300_Green, ItemClassification.filler, ItemType.Program, 44, ProgramColor.Green),
    ItemData(0xB610C8, ItemName.HP_300_Pink, ItemClassification.filler, ItemType.Program, 44, ProgramColor.Pink),
    ItemData(0xB610C9, ItemName.HP_300_White, ItemClassification.filler, ItemType.Program, 44, ProgramColor.White),
    ItemData(0xB610CA, ItemName.HP_400_Green, ItemClassification.useful, ItemType.Program, 45, ProgramColor.Green),
    ItemData(0xB610CB, ItemName.HP_400_White, ItemClassification.useful, ItemType.Program, 45, ProgramColor.White),
    # ItemData(0x,      ItemName.HP_400_Yellow,      ItemClassification.filler, ItemType.Program, 45, ProgramColor.Yellow), #Shop only
    ItemData(0xB610CC, ItemName.HP_50_Blue, ItemClassification.filler, ItemType.Program, 41, ProgramColor.Blue),
    ItemData(0xB610CD, ItemName.HP_50_Pink, ItemClassification.filler, ItemType.Program, 41, ProgramColor.Pink),

    ItemData(0xB610CE, ItemName.HP_50_white, ItemClassification.filler, ItemType.Program, 41, ProgramColor.White),
    ItemData(0xB610CF, ItemName.HP_500_Green, ItemClassification.useful, ItemType.Program, 46, ProgramColor.Green),
    ItemData(0xB610D0, ItemName.HP_500_Pink, ItemClassification.useful, ItemType.Program, 46, ProgramColor.Pink),
    ItemData(0xB610D1, ItemName.HP_500_White, ItemClassification.useful, ItemType.Program, 46, ProgramColor.White),
    ItemData(0xB610D2, ItemName.Humor, ItemClassification.filler, ItemType.Program, 23, ProgramColor.Pink),
    ItemData(0xB610D3, ItemName.Jungle, ItemClassification.filler, ItemType.Program, 20, ProgramColor.Green),
    # ItemData(0x,      ItemName.MegFldr1,           ItemClassification.filler, ItemType.Program, 4, ProgramColor.Green), #Shop only
    ItemData(0xB610D4, ItemName.MegFldr2, ItemClassification.filler, ItemType.Program, 5, ProgramColor.White),
    ItemData(0xB610D5, ItemName.Millions, ItemClassification.progression, ItemType.Program, 22, ProgramColor.Red),
    ItemData(0xB610D6, ItemName.NumbrOpn, ItemClassification.filler, ItemType.Program, 15, ProgramColor.Pink),

    ItemData(0xB610D7, ItemName.OilBody, ItemClassification.filler, ItemType.Program, 17, ProgramColor.Red),
    ItemData(0xB610D8, ItemName.Poem, ItemClassification.filler, ItemType.Program, 24, ProgramColor.Yellow),
    # ItemData(0x,      ItemName.Reflect,            ItemClassification.filler, ItemType.Program, 9,  ProgramColor.Green),  #Shop only
    # ItemData(0x,      ItemName.Rush,               ItemClassification.filler, ItemType.Program, 32, ProgramColor.Yellow), #Multiplayer only
    ItemData(0xB610D9, ItemName.Shield, ItemClassification.filler, ItemType.Program, 8, ProgramColor.Blue),
    ItemData(0xB610DA, ItemName.SlipRunr, ItemClassification.useful, ItemType.Program, 25, ProgramColor.Yellow),
    # ItemData(0x,      ItemName.SneakRun,           ItemClassification.filler, ItemType.Program, 16,ProgramColor.White),   #Shop only
    ItemData(0xB610DB, ItemName.Speed_Plus_Blue, ItemClassification.filler, ItemType.Program, 36, ProgramColor.Blue),
    ItemData(0xB610DC, ItemName.Speed_Plus_Pink, ItemClassification.filler, ItemType.Program, 36, ProgramColor.Pink),
    ItemData(0xB610DD, ItemName.Speed_Plus_White, ItemClassification.filler, ItemType.Program, 36, ProgramColor.White),

    ItemData(0xB610DE, ItemName.SpeedMAX, ItemClassification.filler, ItemType.Program, 39, ProgramColor.Green),
    # ItemData(0x,      ItemName.SuprArmr,           ItemClassification.useful, ItemType.Program, 1,  ProgramColor.Red),    #Shop only
    # ItemData(0x,      ItemName.Tango,              ItemClassification.filler, ItemType.Program, 34, ProgramColor.Green),  #Multiplayer only
    ItemData(0xB610DF, ItemName.UnderSht, ItemClassification.useful, ItemType.Program, 13, ProgramColor.White)

]

zennyList: typing.List[ItemData] = [
    ItemData(0xB610E0, ItemName.zenny_600z, ItemClassification.filler, ItemType.Zenny, count=600),
    ItemData(0xB610E1, ItemName.zenny_700z, ItemClassification.filler, ItemType.Zenny, count=700),
    ItemData(0xB610E2, ItemName.zenny_1000z, ItemClassification.filler, ItemType.Zenny, count=1000),
    ItemData(0xB610E3, ItemName.zenny_1200z, ItemClassification.filler, ItemType.Zenny, count=1200),
    ItemData(0xB610E4, ItemName.zenny_1600z, ItemClassification.filler, ItemType.Zenny, count=1600),
    ItemData(0xB610E5, ItemName.zenny_2400z, ItemClassification.filler, ItemType.Zenny, count=2400),
    ItemData(0xB610E6, ItemName.zenny_3000z, ItemClassification.filler, ItemType.Zenny, count=3000),
    ItemData(0xB610E7, ItemName.zenny_5000z, ItemClassification.filler, ItemType.Zenny, count=5000),
    ItemData(0xB610E8, ItemName.zenny_6000z, ItemClassification.filler, ItemType.Zenny, count=6000),
    ItemData(0xB610E9, ItemName.zenny_8000z, ItemClassification.filler, ItemType.Zenny, count=8000),
    ItemData(0xB610EA, ItemName.zenny_100000z, ItemClassification.progression, ItemType.Zenny, count=100000)
]

bugFragList: typing.List[ItemData] = [
    ItemData(0xB610EB, ItemName.bugfrag_10, ItemClassification.filler, ItemType.BugFrag, count=10),
    ItemData(0xB610EC, ItemName.bugfrag_05, ItemClassification.filler, ItemType.BugFrag, count=5),
    ItemData(0xB610ED, ItemName.bugfrag_03, ItemClassification.filler, ItemType.BugFrag, count=3),
    ItemData(0xB610EE, ItemName.bugfrag_01, ItemClassification.filler, ItemType.BugFrag, count=1)
]

item_frequencies: typing.Dict[str, int] = {
    ItemName.ExpMemry: 2,
    ItemName.Unlocker: 7,
    ItemName.HPMemry: 27,
    ItemName.RegUP1: 11,
    ItemName.RegUP2: 13,
    ItemName.RegUP3: 3,
    ItemName.Untrap: 3,
    ItemName.SubMemry: 4,
    ItemName.MiniEnrg: 3,
    ItemName.FullEnrg: 5,
    ItemName.SneakRun: 3,
    ItemName.LocEnemy: 4,
    ItemName.Discord_S: 2,
    ItemName.Charge_Plus_White: 2,
    ItemName.Speed_Plus_White: 2,
    ItemName.WhiCapsl_star: 2,
    ItemName.zenny_3000z: 2,
    ItemName.zenny_5000z: 3,
    ItemName.zenny_100000z: 2,
    ItemName.bugfrag_10: 2
}

item_groups: typing.Dict[str, typing.Set[str]] = {
    "Key Items": {loc.itemName for loc in keyItemList},
    "Subchips": {loc.itemName for loc in subChipList},
    "Programs": {loc.itemName for loc in programList},
    "BattleChips": {loc.itemName for loc in chipList},
    "Secret Chips": {loc.itemName for loc in secretChipList},
    "Zenny": {loc.itemName for loc in zennyList},
    "BugFrags": {loc.itemName for loc in bugFragList}
}

all_items: typing.List[
    ItemData] = keyItemList + subChipList + chipList + secretChipList + programList + zennyList + bugFragList
item_table: typing.Dict[str, ItemData] = {item.itemName: item for item in all_items}
items_by_id: typing.Dict[int, ItemData] = {item.code: item for item in all_items}

# Used to get the index in the chip amounts array
chips_amount_index: typing.Dict[str, int] = {
    ItemName.AirHocky_M: 589,
    ItemName.AirSpin2_L: 1513,
    ItemName.AirSpin3_O: 1525,
    ItemName.AntiNavi_star: 2223,
    ItemName.AntiRecv_star: 2259,
    ItemName.AntiSwrd_star: 2247,
    ItemName.Anubis_P: 1812,
    ItemName.AreaGrab_star: 1947,
    ItemName.Atk_30_star: 2328,
    ItemName.AuraHed1_B: 1128,
    ItemName.Barr100_H: 2136,
    ItemName.BigBomb_O: 2412,
    ItemName.BigBomb_P: 2413,
    ItemName.BlastMan_star: 3073,
    ItemName.BlkBomb_F: 709,
    ItemName.BlzrdBal_H: 2376,
    ItemName.BblWrap_Q: 2161,
    ItemName.BugFix_P: 2101,
    ItemName.BugFix_star: 2103,
    ItemName.ChrgeMan_star: 2857,
    ItemName.CircGun_V: 1694,
    ItemName.CircGun_P: 1692,
    ItemName.ColArmy_star: 2367,
    ItemName.ColArmy_B: 2364,
    ItemName.Colonel_star: 3253,
    ItemName.ColorPt_star: 2316,
    ItemName.ComingRd_star: 2028,
    ItemName.CopyDmg_star: 2268,
    ItemName.CrcusMan_star: 3145,
    ItemName.DblPoint_star: 2340,
    ItemName.Discord_S: 1754,
    ItemName.Diveman_star: 3109,
    ItemName.DolThdr1_A: 360,
    ItemName.DrilArm_M: 601,
    ItemName.DublShot_C: 1068,
    ItemName.DublShot_star: 1071,
    ItemName.ElecMan_star: 2749,
    ItemName.ElecSwrd_E: 924,
    ItemName.ElemTrap_star: 2355,
    ItemName.ElmntMan_star: 3217,
    ItemName.EnergBom_K: 649,
    ItemName.EraseMan_star: 2821,
    ItemName.Fan_star: 1548,
    ItemName.Fanfare_Z: 1742,
    ItemName.FireHit1_F: 1274,
    ItemName.FstGauge_star: 2067,
    ItemName.Geddon_A: 1992,
    ItemName.Geddon_star: 1995,
    ItemName.GrabRvng_I: 1968,
    ItemName.GoingRd_star: 2040,
    ItemName.Guardian_O: 1800,
    ItemName.GunDelS1_C: 168,
    ItemName.GunDelS2_E: 181,
    ItemName.GunDelS3_W: 194,
    ItemName.HeatMan_star: 2713,
    ItemName.HiBoomer_V: 1394,
    ItemName.HiCannon_M: 13,
    ItemName.HiCannon_L: 12,
    ItemName.HolyPanl_A: 2004,
    ItemName.HolyPanl_S: 2006,
    ItemName.IceSeed_A: 816,
    ItemName.IceSeed_star: 819,
    ItemName.JudgeMan_star: 3181,
    ItemName.JustcOne_J: 1668,
    ItemName.Lance_star: 1419,
    ItemName.Lance_W: 1418,
    ItemName.LifeSync_star: 2280,
    ItemName.LongBlde_B: 888,
    ItemName.M_Boomer_M: 1405,
    ItemName.M_Cannon_star: 27,
    ItemName.M_Cannon_S: 25,
    ItemName.MuraMasa_M: 1008,
    ItemName.PnlRetrn_star: 1980,
    ItemName.PoisSeed_P: 830,
    ItemName.ProtoMan_star: 2677,
    ItemName.Recov80_H: 1872,
    ItemName.Recov120_F: 1884,
    ItemName.Recov150_M: 1897,
    ItemName.Recov200_Z: 1910,
    ItemName.Recov300_Y: 1922,
    ItemName.Recov30_star: 1851,
    ItemName.Roll_star: 2641,
    ItemName.SlashMan_star: 2785,
    ItemName.Snake_H: 1596,
    ItemName.Spreadr1_M: 97,
    ItemName.Spreadr2_C: 110,
    ItemName.Spreadr3_S: 122,
    ItemName.Spreadr3_star: 123,
    ItemName.Spreadr3_R: 121,
    ItemName.StepSwrd_L: 961,
    ItemName.StepSwrd_B: 960,
    ItemName.SuprVulc_V: 84,
    ItemName.Thunder_star: 351,
    ItemName.TimeBom3_M: 2401,
    ItemName.TimeBom3_N: 2402,
    ItemName.Timpani_T: 1766,
    ItemName.Tornado_L: 612,
    ItemName.TrplShot_star: 1083,
    ItemName.Uninstll_G: 2208,
    ItemName.VarSwrd_W: 974,
    ItemName.Vdoll_F: 1788,
    ItemName.Vulcan2_D: 60,
    ItemName.Vulcan3_A: 72,
    ItemName.WhiCapsl_star: 2196,
    ItemName.WideBlde_B: 876,
    ItemName.WindRack_star: 951,
    ItemName.YoYo_N: 218,
    ItemName.YoYo_star: 219,
    ItemName.DustMan_star: 3037,
    ItemName.DustMan_D: 3036,
    ItemName.DustManEX_D: 3048,
    ItemName.DustManSP_D: 3060,
    ItemName.GrndMan_star: 3001,
    ItemName.GrndMan_G: 3000,
    ItemName.GrndManEX_G: 3012,
    ItemName.GrndManSP_G: 3024,
    ItemName.SpoutMan_star: 2893,
    ItemName.SpoutMan_A: 2892,
    ItemName.SpoutMnEX_A: 2904,
    ItemName.SpoutMnSP_A: 2916,
    ItemName.TenguMan_star: 2965,
    ItemName.TenguMan_T: 2964,
    ItemName.TenguMnEX_T: 2976,
    ItemName.TenguMnSP_T: 2988,
    ItemName.TmhkMan_star: 2929,
    ItemName.TmhkMan_T: 2928,
    ItemName.TmhkManEX_T: 2940,
    ItemName.TmhkManSP_T: 2952
}

# Used to get the itemID when giving a program via the client.
# How to get: (programID * 4) + 144, +1 for each possible color (in color order)
programs_to_item_id: typing.Dict[str, int] = {
    ItemName.AirShoes: 192,
    ItemName.AntiDmg: 184,
    ItemName.Attack_Plus_Blue: 286,
    ItemName.Attack_Plus_Pink: 284,
    ItemName.Attack_Plus_Red: 285,
    ItemName.AttckMAX: 296,
    ItemName.AutoHeal: 248,
    ItemName.Battery: 220,
    ItemName.BodyPack: 256,
    ItemName.BugStop: 268,
    ItemName.BustPack: 252,
    ItemName.Charge_Plus_Green: 294,
    ItemName.Charge_Plus_Pink: 293,
    ItemName.Charge_Plus_White: 292,
    ItemName.ChargMAX: 304,
    ItemName.Custom2: 156,
    ItemName.Fish_Prog: 216,
    ItemName.FldrPak1: 260,
    ItemName.FldrPak2: 264,
    ItemName.FstBarr: 172,
    ItemName.HP_100_Blue: 314,
    ItemName.HP_100_Pink: 313,
    ItemName.HP_100_White: 312,
    ItemName.HP_200_Blue: 317,
    ItemName.HP_200_White: 316,
    ItemName.HP_300_Green: 322,
    ItemName.HP_300_Pink: 321,
    ItemName.HP_300_White: 320,
    ItemName.HP_400_Green: 326,
    ItemName.HP_400_White: 324,
    ItemName.HP_50_Blue: 310,
    ItemName.HP_50_Pink: 309,
    ItemName.HP_50_white: 308,
    ItemName.HP_500_Green: 330,
    ItemName.HP_500_Pink: 329,
    ItemName.HP_500_White: 328,
    ItemName.Humor: 236,
    ItemName.Jungle: 224,
    ItemName.MegFldr2: 164,
    ItemName.Millions: 232,
    ItemName.NumbrOpn: 204,
    ItemName.OilBody: 212,
    ItemName.Poem: 240,
    ItemName.Shield: 176,
    ItemName.SlipRunr: 244,
    ItemName.Speed_Plus_Blue: 290,
    ItemName.Speed_Plus_Pink: 289,
    ItemName.Speed_Plus_White: 288,
    ItemName.SpeedMAX: 300,
    ItemName.UnderSht: 196
}