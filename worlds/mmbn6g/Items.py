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


class MMBN6gItem(Item):
    game: str = "MegaMan Battle Network 6 Gregar"
    

keyItemList: typing.List[ItemData] = [
    #ItemData(0x, ItemName.PET,		    ItemClassification.,	ItemType.KeyItem, 	0)  #Given at the beginning of the game
    #ItemData(0x, ItemName.StudntID,		ItemClassification.,	ItemType.KeyItem, 	1)  #Unlocks right part of school
    #ItemData(0x, ItemName.Bucket,		ItemClassification.,	ItemType.KeyItem, 	2)  #Needed for story progression, unneeded here
    #ItemData(0x, ItemName.TeachrID,		ItemClassification.,	ItemType.KeyItem, 	3)  #Unlocks Teacher's Room
    #ItemData(0x, ItemName.Graffiti,		ItemClassification.,	ItemType.KeyItem, 	4)  #Unlocks KeyData check in Central 2
    #ItemData(0x, ItemName.WatrData,		ItemClassification.,	ItemType.KeyItem, 	5)  #Given for Robo Control Comps, unneeded here.
    ItemData(0x, ItemName.KeyData,		ItemClassification.,	ItemType.KeyItem, 	6)  #Unlocks Central 3 door
    ItemData(0x, ItemName.Fish,		    ItemClassification.,	ItemType.KeyItem, 	7)  #Needed for story progression, used to unlock SeaSide LevBus
    ItemData(0x, ItemName.ToolPrgm,		ItemClassification.,	ItemType.KeyItem, 	8)  #Unlocks Seaside Internet Area
    #ItemData(0x, ItemName.Toy,		    ItemClassification.,	ItemType.KeyItem, 	9)  #???
    #ItemData(0x, ItemName.HealWatr,		ItemClassification.,	ItemType.KeyItem, 	10) #Technically used for BeastOut, unneeded here
    ItemData(0x, ItemName.TagChip,		ItemClassification.,	ItemType.KeyItem, 	11) #Given by email, unlocks Tag System
    #ItemData(0x, ItemName.Report,		ItemClassification.,	ItemType.KeyItem, 	12) #???
    #ItemData(0x, ItemName.ImgData,		ItemClassification.,	ItemType.KeyItem, 	13)
    ItemData(0x, ItemName.AuthData,		ItemClassification.,	ItemType.KeyItem, 	14) #Needed for story progression, used to unlock Green LevBus
    ItemData(0x, ItemName.Umbrella,		ItemClassification.,	ItemType.KeyItem, 	15) #Used to unlock Sky LevBus
    ItemData(0x, ItemName.WinCardA,		ItemClassification.,	ItemType.KeyItem, 	16) #Used as win condition
    ItemData(0x, ItemName.WinCardB,		ItemClassification.,	ItemType.KeyItem, 	17) #Used as win condition
    ItemData(0x, ItemName.WinCardC,		ItemClassification.,	ItemType.KeyItem, 	18) #Used as win condition
    ItemData(0x, ItemName.WinCardD,		ItemClassification.,	ItemType.KeyItem, 	19) #Used as win condition
    #ItemData(0x, ItemName.CybrBat1,		ItemClassification.,	ItemType.KeyItem, 	20)
    #ItemData(0x, ItemName.CybrBat2,		ItemClassification.,	ItemType.KeyItem, 	21)
    #ItemData(0x, ItemName.CybrBat3,		ItemClassification.,	ItemType.KeyItem, 	22)
    #ItemData(0x, ItemName.CybrBat4,		ItemClassification.,	ItemType.KeyItem, 	23)
    #ItemData(0x, ItemName.CybrBat5,		ItemClassification.,	ItemType.KeyItem, 	24)
    #ItemData(0x, ItemName.MoonSton,		ItemClassification.,	ItemType.KeyItem, 	25) #Unneeded
    ItemData(0x, ItemName.ACDCKyDt,		ItemClassification.,	ItemType.KeyItem, 	26) #Unlocks door in ACDC Area, used to unlock ACDC LevBus
    ItemData(0x, ItemName.AreaPass,		ItemClassification.,	ItemType.KeyItem, 	27) #Used to go from Central 3 to ACDC Area
    ItemData(0x, ItemName.VacData,		ItemClassification.,	ItemType.KeyItem, 	28) #Used to go from Central 3 to Sky Area
    #ItemData(0x, ItemName.PcktWtch,		ItemClassification.,	ItemType.KeyItem, 	29) #Job related?
    #ItemData(0x, ItemName.TunaData,		ItemClassification.,	ItemType.KeyItem, 	30) #Used for Stock Up request, maybe leave vanilla
    #ItemData(0x, ItemName.SalmData,		ItemClassification.,	ItemType.KeyItem, 	31) #Used for Stock Up request, maybe leave vanilla
    #ItemData(0x, ItemName.EelData,		ItemClassification.,	ItemType.KeyItem, 	32) #Used for Stock Up request, maybe leave vanilla
    #ItemData(0x, ItemName.ShrimpDt,		ItemClassification.,	ItemType.KeyItem, 	33) #Used for Stock Up request, maybe leave vanilla
    #ItemData(0x, ItemName.HrringDt,		ItemClassification.,	ItemType.KeyItem, 	34) #Used for Stock Up request, maybe leave vanilla
    #ItemData(0x, ItemName.YTailDat,		ItemClassification.,	ItemType.KeyItem, 	35) #Used for Stock Up request, maybe leave vanilla
    #ItemData(0x, ItemName.UrchnDat,		ItemClassification.,	ItemType.KeyItem, 	36) #Used for Stock Up request, maybe leave vanilla
    #ItemData(0x, ItemName.SnpprDat,		ItemClassification.,	ItemType.KeyItem, 	37) #Used for Stock Up request, maybe leave vanilla
    #ItemData(0x, ItemName.TimeCpsl,		ItemClassification.,	ItemType.KeyItem, 	38) #Job related?
    #ItemData(0x, ItemName.CashData,		ItemClassification.,	ItemType.KeyItem, 	39) #Job related?
    #ItemData(0x, ItemName.TextData,		ItemClassification.,	ItemType.KeyItem, 	40) #Job related?
    #ItemData(0x, ItemName.Pendant,		ItemClassification.,	ItemType.KeyItem, 	41) #Job related?
    #ItemData(0x, ItemName.RplyLttr,		ItemClassification.,	ItemType.KeyItem, 	42) #Job related?
    ItemData(0x, ItemName.StampCrd,		ItemClassification.,	ItemType.KeyItem, 	43) #Used in Pavilion, used to unlock Expo Site
    ItemData(0x, ItemName.RushFood,		ItemClassification.,	ItemType.KeyItem, 	44) #Used for shortcuts
    #ItemData(0x, ItemName.CyberAxe,		ItemClassification.,	ItemType.KeyItem, 	45)
    #ItemData(0x, ItemName.Tulip,		ItemClassification.,	ItemType.KeyItem, 	46)
    #ItemData(0x, ItemName.UpdtData,		ItemClassification.,	ItemType.KeyItem, 	47)
    #ItemData(0x, ItemName.Coffee,		ItemClassification.,	ItemType.KeyItem, 	48)
    #ItemData(0x, ItemName.ScrtData,		ItemClassification.,	ItemType.KeyItem, 	49)
    #ItemData(0x, ItemName.CrosBatc,		ItemClassification.,	ItemType.KeyItem, 	50)
    ItemData(0x, ItemName.BatKey,		ItemClassification.,	ItemType.KeyItem, 	51) #Used to unlock Graveyard Area
    #ItemData(0x, ItemName.ScrtMemo,		ItemClassification.,	ItemType.KeyItem, 	52)
    ItemData(0x, ItemName.QuizData,		ItemClassification.,	ItemType.KeyItem, 	53)
    #ItemData(0x, ItemName.ScrblDat,		ItemClassification.,	ItemType.KeyItem, 	54)
    #ItemData(0x, ItemName.PngnThnk,		ItemClassification.,	ItemType.KeyItem, 	55)
    #ItemData(0x, ItemName.RefrncBk,		ItemClassification.,	ItemType.KeyItem, 	56)
    ItemData(0x, ItemName.OrderSys,		ItemClassification.,	ItemType.KeyItem, 	57) #Renamed QuizBook to be OrderSys
    #ItemData(0x, ItemName.InvteCrd,		ItemClassification.,	ItemType.KeyItem, 	58)
    #ItemData(0x, ItemName.ThnkULtr,		ItemClassification.,	ItemType.KeyItem, 	59)
    #ItemData(0x, ItemName.SrialDat,		ItemClassification.,	ItemType.KeyItem, 	60)
    #ItemData(0x, ItemName.SciManul,		ItemClassification.,	ItemType.KeyItem, 	61)
    #ItemData(0x, ItemName.SoulEmbl,		ItemClassification.,	ItemType.KeyItem, 	62)
    #ItemData(0x, ItemName.NaviRuin,		ItemClassification.,	ItemType.KeyItem, 	63)
    ItemData(0x, ItemName.BtlrCard,		ItemClassification.,	ItemType.KeyItem, 	64)
    #ItemData(0x, ItemName.F.Fries,		ItemClassification.,	ItemType.KeyItem, 	65) #Job related?
    ItemData(0x, ItemName.CybBrdAx,		ItemClassification.,	ItemType.KeyItem, 	66) #Used to go from Central 3 to Green Area
    #ItemData(0x, ItemName.ResrvTck,		ItemClassification.,	ItemType.KeyItem, 	67)
    ItemData(0x, ItemName.WWWID,		ItemClassification.,	ItemType.KeyItem, 	68) #Unlocks certain location checks
    ItemData(0x, ItemName.SeaSdKey,		ItemClassification.,	ItemType.KeyItem, 	70) #Unlocks door in Seaside 3
    ItemData(0x, ItemName.SpinWhit,		ItemClassification.,	ItemType.KeyItem, 	80) #Useful NaviCust upgrade
    ItemData(0x, ItemName.SpinYllw,		ItemClassification.,	ItemType.KeyItem, 	81) #Useful NaviCust upgrade
    ItemData(0x, ItemName.SpinPink,		ItemClassification.,	ItemType.KeyItem, 	82) #Useful NaviCust upgrade
    ItemData(0x, ItemName.SpinRed,		ItemClassification.,	ItemType.KeyItem, 	83) #Useful NaviCust upgrade
    ItemData(0x, ItemName.SpinBlue,		ItemClassification.,	ItemType.KeyItem, 	84) #Useful NaviCust upgrade
    ItemData(0x, ItemName.SpinGrn,		ItemClassification.,	ItemType.KeyItem, 	85) #Useful NaviCust upgrade
    ItemData(0x, ItemName.SchPCode,		ItemClassification.,	ItemType.KeyItem, 	96) #Unlocks Lab 1 Comp
    ItemData(0x, ItemName.WtrBannr,		ItemClassification.,	ItemType.KeyItem, 	104) #SeaSide HP Shortcut
    ItemData(0x, ItemName.GrnBannr,		ItemClassification.,	ItemType.KeyItem, 	105) #Green HP Shortcut
    ItemData(0x, ItemName.SkyBannr,		ItemClassification.,	ItemType.KeyItem, 	106) #Sky HP Shortcut
    ItemData(0x, ItemName.ACDCBanr,		ItemClassification.,	ItemType.KeyItem, 	107) #ACDC HP Shortcut
    ItemData(0x, ItemName.HPMemry,		ItemClassification.,	ItemType.KeyItem, 	112)
    ItemData(0x, ItemName.ExpMemry,		ItemClassification.,	ItemType.KeyItem, 	113)
    ItemData(0x, ItemName.RegUP1,		ItemClassification.,	ItemType.KeyItem, 	114)
    ItemData(0x, ItemName.RegUP2,		ItemClassification.,	ItemType.KeyItem, 	115)
    ItemData(0x, ItemName.RegUP3,		ItemClassification.,	ItemType.KeyItem, 	116)
    ItemData(0x, ItemName.SubMemry,		ItemClassification.,	ItemType.KeyItem, 	117)
]

subChipList: typing.List[ItemData] = [
    ItemData(0x, ItemName.Unlocker, ItemClassification.progression, ItemType.SubChip,  133),
    ItemData(0x, ItemName.Untrap,   ItemClassification.filler, ItemType.SubChip,  131),
    ItemData(0x, ItemName.LocEnemy, ItemClassification.filler, ItemType.SubChip,  132),
    ItemData(0x, ItemName.MiniEnrg, ItemClassification.filler, ItemType.SubChip,  128),
    ItemData(0x, ItemName.FullEnrg, ItemClassification.filler, ItemType.SubChip,  129),
    ItemData(0x, ItemName.SneakRun, ItemClassification.filler, ItemType.SubChip,  130)
]

chipList: typing.List[ItemData] = [
    ItemData(0x, ItemName.AirSpin3_O, ItemClassification.filler, ItemType.Chip, 128, chip_code('O')),
    ItemData(0x, ItemName.AntiNavi_*, ItemClassification.filler, ItemType.Chip, 186, chip_code('*')),
    ItemData(0x, ItemName.AntiRecv_*, ItemClassification.filler, ItemType.Chip, 189, chip_code('*')),
    ItemData(0x, ItemName.Anubis_P, ItemClassification.filler, ItemType.Chip, 152, chip_code('P')),
    ItemData(0x, ItemName.AreaGrab_*, ItemClassification.filler, ItemType.Chip, 163, chip_code('*')),
    ItemData(0x, ItemName.Atk_30_*, ItemClassification.filler, ItemType.Chip, 195, chip_code('*')),
    ItemData(0x, ItemName.Barr100_H, ItemClassification.filler, ItemType.Chip, 179, chip_code('H')),
    ItemData(0x, ItemName.BigBomb_P, ItemClassification.filler, ItemType.Chip, 202, chip_code('P')),
    ItemData(0x, ItemName.BlastMan_*, ItemClassification.filler, ItemType.Chip, 257, chip_code('*')),
    ItemData(0x, ItemName.BlkBomb_F, ItemClassification.filler, ItemType.Chip, 60, chip_code('F')),

    ItemData(0x, ItemName.BlzrdBal_H, ItemClassification.filler, ItemType.Chip, 199, chip_code('H')),
    ItemData(0x, ItemName.BugFix_P, ItemClassification.filler, ItemType.Chip, 176, chip_code('P')),
    ItemData(0x, ItemName.BugFix_*, ItemClassification.filler, ItemType.Chip, 176, chip_code('*')),
    ItemData(0x, ItemName.ChargeMan_*, ItemClassification.filler, ItemType.Chip, 239, chip_code('*')),
    ItemData(0x, ItemName.CircGun_V, ItemClassification.filler, ItemType.Chip, 142, chip_code('V')),
    ItemData(0x, ItemName.CircGun_P, ItemClassification.filler, ItemType.Chip, 142, chip_code('P')),
    ItemData(0x, ItemName.ColArmy_*, ItemClassification.filler, ItemType.Chip, 198, chip_code('*')),
    ItemData(0x, ItemName.ColArmy_B, ItemClassification.filler, ItemType.Chip, 198, chip_code('B')),
    ItemData(0x, ItemName.Colonel_*, ItemClassification.filler, ItemType.Chip, 272, chip_code('*')),
    ItemData(0x, ItemName.ColorPt_*, ItemClassification.filler, ItemType.Chip, 194, chip_code('*')),

    ItemData(0x, ItemName.ComingRd_*, ItemClassification.filler, ItemType.Chip, 170, chip_code('*')),
    ItemData(0x, ItemName.CopyDmg_*, ItemClassification.filler, ItemType.Chip, 190, chip_code('*')),
    ItemData(0x, ItemName.CrcusMan_*, ItemClassification.filler, ItemType.Chip, 263, chip_code('*')),
    ItemData(0x, ItemName.DblPoint_*, ItemClassification.filler, ItemType.Chip, 196, chip_code('*')),
    ItemData(0x, ItemName.Diveman_*, ItemClassification.filler, ItemType.Chip, 260, chip_code('*')),
    ItemData(0x, ItemName.DrilArm_M, ItemClassification.filler, ItemType.Chip, 51, chip_code('M')),
    ItemData(0x, ItemName.DublShot_*, ItemClassification.filler, ItemType.Chip, 90, chip_code('*')),
    ItemData(0x, ItemName.ElecMan_*, ItemClassification.filler, ItemType.Chip, 230, chip_code('*')),
    ItemData(0x, ItemName.ElecSwrd_E, ItemClassification.filler, ItemType.Chip, 78, chip_code('E')),
    ItemData(0x, ItemName.ElemTrap_*, ItemClassification.filler, ItemType.Chip, 197, chip_code('*')),


    ItemData(0x, ItemName.ElmntMan_*, ItemClassification.filler, ItemType.Chip, 269, chip_code('*')),
    ItemData(0x, ItemName.EnergBom_K, ItemClassification.filler, ItemType.Chip, 55, chip_code('K')),
    ItemData(0x, ItemName.EraseMan_*, ItemClassification.filler, ItemType.Chip, 236, chip_code('*')),
    ItemData(0x, ItemName.Fan_*, ItemClassification.filler, ItemType.Chip, 130, chip_code('*')),
    ItemData(0x, ItemName.FireHit1_F, ItemClassification.filler, ItemType.Chip, 107, chip_code('F')),
    ItemData(0x, ItemName.FstGauge_*, ItemClassification.filler, ItemType.Chip, 173, chip_code('*')),
    ItemData(0x, ItemName.Geddon_*, ItemClassification.filler, ItemType.Chip, 167, chip_code('*')),
    ItemData(0x, ItemName.GoingRd_*, ItemClassification.filler, ItemType.Chip, 171, chip_code('*')),
    ItemData(0x, ItemName.Guardian_O, ItemClassification.filler, ItemType.Chip, 151, chip_code('O')),
    ItemData(0x, ItemName.GunDelS2_E, ItemClassification.filler, ItemType.Chip, 16, chip_code('E')),

    ItemData(0x, ItemName.GunDelS3_W, ItemClassification.filler, ItemType.Chip, 17, chip_code('W')),
    ItemData(0x, ItemName.HeatMan_*, ItemClassification.filler, ItemType.Chip, 227, chip_code('*')),
    ItemData(0x, ItemName.HiCannon_M, ItemClassification.filler, ItemType.Chip, 2, chip_code('M')),
    ItemData(0x, ItemName.HiCannon_L, ItemClassification.filler, ItemType.Chip, 2, chip_code('L')),
    ItemData(0x, ItemName.HolyPanl_A, ItemClassification.filler, ItemType.Chip, 168, chip_code('A')),
    ItemData(0x, ItemName.IceSeed_A, ItemClassification.filler, ItemType.Chip, 69, chip_code('A')),
    ItemData(0x, ItemName.JudgeMan_*, ItemClassification.filler, ItemType.Chip, 266, chip_code('*')),
    ItemData(0x, ItemName.Lance_*, ItemClassification.filler, ItemType.Chip, 119, chip_code('*')),
    ItemData(0x, ItemName.Lance_W, ItemClassification.filler, ItemType.Chip, 119, chip_code('W')),
    ItemData(0x, ItemName.LifeSync_*, ItemClassification.filler, ItemType.Chip, 191, chip_code('*')),

    ItemData(0x, ItemName.LongBlde_B, ItemClassification.filler, ItemType.Chip, 75, chip_code('B')),
    ItemData(0x, ItemName.M-Boomer_M, ItemClassification.filler, ItemType.Chip, 118, chip_code('M')),
    ItemData(0x, ItemName.M-Cannon_*, ItemClassification.filler, ItemType.Chip, 3, chip_code('*')),
    ItemData(0x, ItemName.M-Cannon_S, ItemClassification.filler, ItemType.Chip, 3, chip_code('S')),
    ItemData(0x, ItemName.MuraMasa_M, ItemClassification.filler, ItemType.Chip, 85, chip_code('M')),
    ItemData(0x, ItemName.PnlRetrn_*, ItemClassification.filler, ItemType.Chip, 166, chip_code('*')),
    ItemData(0x, ItemName.ProtoMan_*, ItemClassification.filler, ItemType.Chip, 224, chip_code('*')),
    ItemData(0x, ItemName.Recov120_F, ItemClassification.filler, ItemType.Chip, 158, chip_code('F')),
    ItemData(0x, ItemName.Recov150_M, ItemClassification.filler, ItemType.Chip, 159, chip_code('M')),
    ItemData(0x, ItemName.Recov200_Z, ItemClassification.filler, ItemType.Chip, 160, chip_code('Z')),

    ItemData(0x, ItemName.Recov300_Y, ItemClassification.filler, ItemType.Chip, 161, chip_code('Y')),
    ItemData(0x, ItemName.Recov300_*, ItemClassification.filler, ItemType.Chip, 161, chip_code('*')),
    ItemData(0x, ItemName.Roll_*, ItemClassification.filler, ItemType.Chip, 221, chip_code('*')),
    ItemData(0x, ItemName.SlashMan_*, ItemClassification.filler, ItemType.Chip, 233, chip_code('*')),
    ItemData(0x, ItemName.Snake_H, ItemClassification.filler, ItemType.Chip, 134, chip_code('H')),
    ItemData(0x, ItemName.Spreadr1_M, ItemClassification.filler, ItemType.Chip, 9, chip_code('M')),
    ItemData(0x, ItemName.Spreadr2_C, ItemClassification.filler, ItemType.Chip, 10, chip_code('C')),
    ItemData(0x, ItemName.Spreadr3_S, ItemClassification.filler, ItemType.Chip, 11, chip_code('S')),
    ItemData(0x, ItemName.Spreadr3_*, ItemClassification.filler, ItemType.Chip, 11, chip_code('*')),
    ItemData(0x, ItemName.Spreadr3_R, ItemClassification.filler, ItemType.Chip, 11, chip_code('R')),

    ItemData(0x, ItemName.StepSwrd_L, ItemClassification.filler, ItemType.Chip, 81, chip_code('L')),
    ItemData(0x, ItemName.StepSwrd_B, ItemClassification.filler, ItemType.Chip, 81, chip_code('B')),
    ItemData(0x, ItemName.SuprVulc_V, ItemClassification.filler, ItemType.Chip, 8, chip_code('V')),
    ItemData(0x, ItemName.Thunder_*, ItemClassification.filler, ItemType.Chip, 30, chip_code('*')),
    ItemData(0x, ItemName.TimeBom3_M, ItemClassification.filler, ItemType.Chip, 201, chip_code('M')),
    ItemData(0x, ItemName.Tornado_L, ItemClassification.filler, ItemType.Chip, 52, chip_code('L')),
    ItemData(0x, ItemName.TrplShot_*, ItemClassification.filler, ItemType.Chip, 91, chip_code('*')),
    ItemData(0x, ItemName.Uninstll_G, ItemClassification.filler, ItemType.Chip, 185, chip_code('G')),
    ItemData(0x, ItemName.Vdoll_F, ItemClassification.filler, ItemType.Chip, 150, chip_code('F')),
    ItemData(0x, ItemName.Vulcan2_D, ItemClassification.filler, ItemType.Chip, 6, chip_code('D')),

    ItemData(0x, ItemName.Vulcan3_A, ItemClassification.filler, ItemType.Chip, 7, chip_code('A')),
    ItemData(0x, ItemName.WhiCapsl_*, ItemClassification.filler, ItemType.Chip, 184, chip_code('*')),
    ItemData(0x, ItemName.WideBlde_B, ItemClassification.filler, ItemType.Chip, 74, chip_code('B')),
    ItemData(0x, ItemName.WindRack_*, ItemClassification.filler, ItemType.Chip, 80, chip_code('*')),
    ItemData(0x, ItemName.YoYo_N, ItemClassification.filler, ItemType.Chip, 19, chip_code('N')),
    ItemData(0x, ItemName.YoYo_*, ItemClassification.filler, ItemType.Chip, 19, chip_code('*'))
]

secretChipList: typing.List[ItemData] = [
    ItemData(0x, ItemName.DustMan_*, ItemClassification.filler, ItemType.Chip, 254, chip_code('*')),
    ItemData(0x, ItemName.DustMan_D, ItemClassification.filler, ItemType.Chip, 254, chip_code('D')),
    ItemData(0x, ItemName.DustManEX_D, ItemClassification.filler, ItemType.Chip, 255, chip_code('D')),
    ItemData(0x, ItemName.DustManSP_D, ItemClassification.filler, ItemType.Chip, 256, chip_code('D')),
    ItemData(0x, ItemName.GrndMan_*, ItemClassification.filler, ItemType.Chip, 251, chip_code('*')),
    ItemData(0x, ItemName.GrndMan_G, ItemClassification.filler, ItemType.Chip, 251, chip_code('G')),
    ItemData(0x, ItemName.GrndManEX_G, ItemClassification.filler, ItemType.Chip, 252, chip_code('G')),
    ItemData(0x, ItemName.GrndManSP_G, ItemClassification.filler, ItemType.Chip, 253, chip_code('G')),
    ItemData(0x, ItemName.SpoutMan_*, ItemClassification.filler, ItemType.Chip, 242, chip_code('*')),
    ItemData(0x, ItemName.SpoutMan_A, ItemClassification.filler, ItemType.Chip, 242, chip_code('A')),

    ItemData(0x, ItemName.SpoutManEX_A, ItemClassification.filler, ItemType.Chip, 243, chip_code('A')),
    ItemData(0x, ItemName.SpoutManSP_A, ItemClassification.filler, ItemType.Chip, 244, chip_code('A')),
    ItemData(0x, ItemName.TenguMan_*, ItemClassification.filler, ItemType.Chip, 248, chip_code('*')),
    ItemData(0x, ItemName.TenguMan_T, ItemClassification.filler, ItemType.Chip, 248, chip_code('T')),
    ItemData(0x, ItemName.TenguManEX_T, ItemClassification.filler, ItemType.Chip, 249, chip_code('T')),
    ItemData(0x, ItemName.TenguManSP_T, ItemClassification.filler, ItemType.Chip, 250, chip_code('T')),
    ItemData(0x, ItemName.TmhkMan_*, ItemClassification.filler, ItemType.Chip, 245, chip_code('*')),
    ItemData(0x, ItemName.TmhkMan_T, ItemClassification.filler, ItemType.Chip, 245, chip_code('T')),
    ItemData(0x, ItemName.TmhkManEX_T, ItemClassification.filler, ItemType.Chip, 246, chip_code('T')),
    ItemData(0x, ItemName.TmhkManSP_T, ItemClassification.filler, ItemType.Chip, 247, chip_code('T'))
]

programList: typing.List[ItemData] = [
    ItemData(0x, ItemName.AirShoes,          ItemClassification.filler, ItemType.Program, 12, ProgramColor.White),
    ItemData(0x, ItemName.AntiDmg,          ItemClassification.filler, ItemType.Program, 10, ProgramColor.Green),
    ItemData(0x, ItemName.Attack_Plus_Blue,          ItemClassification.filler, ItemType.Program, 35, ProgramColor.Blue),
    ItemData(0x, ItemName.Attack_Plus_Pink,          ItemClassification.filler, ItemType.Program, 35, ProgramColor.Pink),
    ItemData(0x, ItemName.Attack_Plus_Red,          ItemClassification.filler, ItemType.Program, 35, ProgramColor.Red),
    ItemData(0x, ItemName.AttckMAX,          ItemClassification.useful, ItemType.Program, 38, ProgramColor.Red),
    ItemData(0x, ItemName.AutoHeal,          ItemClassification.filler, ItemType.Program, 26, ProgramColor.Pink),
    ItemData(0x, ItemName.Battery,          ItemClassification.filler, ItemType.Program, 19, ProgramColor.Yellow),
    #ItemData(0x, ItemName.Beat,          ItemClassification.filler, ItemType.Program, 33, ProgramColor.Blue),
    ItemData(0x, ItemName.BodyPack,          ItemClassification.useful, ItemType.Program, 28, ProgramColor.Pink),

    ItemData(0x, ItemName.BugStop,          ItemClassification.useful, ItemType.Program, 31, ProgramColor.Yellow),
    ItemData(0x, ItemName.BustPack,          ItemClassification.useful, ItemType.Program, 27, ProgramColor.Red),
    ItemData(0x, ItemName.Charge_Plus_Green,          ItemClassification.filler, ItemType.Program, 37, ProgramColor.Green),
    ItemData(0x, ItemName.Charge_Plus_Pink,          ItemClassification.filler, ItemType.Program, 37, ProgramColor.Pink),
    ItemData(0x, ItemName.Charge_Plus_White,          ItemClassification.filler, ItemType.Program, 37, ProgramColor.White),
    ItemData(0x, ItemName.ChargMAX,          ItemClassification.useful, ItemType.Program, 40, ProgramColor.Blue),
    ItemData(0x, ItemName.ChpShufl,          ItemClassification.filler, ItemType.Program, 14, ProgramColor.Green),
    ItemData(0x, ItemName.Collect,          ItemClassification.filler, ItemType.Program, 21, ProgramColor.Pink),
    ItemData(0x, ItemName.Custom1,          ItemClassification.useful, ItemType.Program, 2, ProgramColor.Blue),
    ItemData(0x, ItemName.Custom2,          ItemClassification.useful, ItemType.Program, 3, ProgramColor.White),

    ItemData(0x, ItemName.Fish,          ItemClassification.filler, ItemType.Program, 18, ProgramColor.Blue),
    ItemData(0x, ItemName.FldrPak1,          ItemClassification.filler, ItemType.Program, 29, ProgramColor.Yellow),
    ItemData(0x, ItemName.FldrPak2,          ItemClassification.filler, ItemType.Program, 30, ProgramColor.Pink),
    ItemData(0x, ItemName.FlotShoe,          ItemClassification.filler, ItemType.Program, 11, ProgramColor.Pink),
    ItemData(0x, ItemName.FstBarr,          ItemClassification.filler, ItemType.Program, 7, ProgramColor.Blue),
    ItemData(0x, ItemName.GigFldr1,          ItemClassification.filler, ItemType.Program, 6, ProgramColor.Red),
    ItemData(0x, ItemName.HP_100_Blue,          ItemClassification.filler, ItemType.Program, 42, ProgramColor.Blue),
    ItemData(0x, ItemName.HP_100_Pink,          ItemClassification.filler, ItemType.Program, 42, ProgramColor.Pink),
    ItemData(0x, ItemName.HP_100_White,          ItemClassification.filler, ItemType.Program, 42, ProgramColor.White),
    ItemData(0x, ItemName.HP_200_Blue,          ItemClassification.filler, ItemType.Program, 43, ProgramColor.Blue),

    ItemData(0x, ItemName.HP_200_White,          ItemClassification.filler, ItemType.Program, 43, ProgramColor.White),
    ItemData(0x, ItemName.HP_200_Yellow,          ItemClassification.filler, ItemType.Program, 43, ProgramColor.Yellow),
    ItemData(0x, ItemName.HP_300_Green,          ItemClassification.filler, ItemType.Program, 44, ProgramColor.Green),
    ItemData(0x, ItemName.HP_300_Pink,          ItemClassification.filler, ItemType.Program, 44, ProgramColor.Pink),
    ItemData(0x, ItemName.HP_300_White,          ItemClassification.filler, ItemType.Program, 44, ProgramColor.White),
    ItemData(0x, ItemName.HP_400_Green,          ItemClassification.filler, ItemType.Program, 45, ProgramColor.Green),
    ItemData(0x, ItemName.HP_400_White,          ItemClassification.filler, ItemType.Program, 45, ProgramColor.White),
    ItemData(0x, ItemName.HP_400_Yellow,          ItemClassification.filler, ItemType.Program, 45, ProgramColor.Yellow),
    ItemData(0x, ItemName.HP_50_Blue,          ItemClassification.filler, ItemType.Program, 41, ProgramColor.Blue),
    ItemData(0x, ItemName.HP_50_Pink,          ItemClassification.filler, ItemType.Program, 41, ProgramColor.Pink),

    ItemData(0x, ItemName.HP_50_white,          ItemClassification.filler, ItemType.Program, 41, ProgramColor.white),
    ItemData(0x, ItemName.HP_500_Green,          ItemClassification.filler, ItemType.Program, 46, ProgramColor.Green),
    ItemData(0x, ItemName.HP_500_Pink,          ItemClassification.filler, ItemType.Program, 46, ProgramColor.Pink),
    ItemData(0x, ItemName.HP_500_White,          ItemClassification.filler, ItemType.Program, 46, ProgramColor.White),
    #ItemData(0x, ItemName.Humor,          ItemClassification.filler, ItemType.Program, 23, ProgramColor.Pink),
    ItemData(0x, ItemName.Jungle,          ItemClassification.filler, ItemType.Program, 20, ProgramColor.Green),
    ItemData(0x, ItemName.MegFldr1,          ItemClassification.filler, ItemType.Program, 4, ProgramColor.Green),
    ItemData(0x, ItemName.MegFldr2,          ItemClassification.filler, ItemType.Program, 5, ProgramColor.White),
    ItemData(0x, ItemName.Millions,          ItemClassification.useful, ItemType.Program, 22, ProgramColor.Red),
    ItemData(0x, ItemName.NumbrOpn,          ItemClassification.filler, ItemType.Program, 15, ProgramColor.Pink),

    ItemData(0x, ItemName.OilBody,          ItemClassification.filler, ItemType.Program, 17, ProgramColor.Red),
    #ItemData(0x, ItemName.Poem,          ItemClassification.filler, ItemType.Program, 24, ProgramColor.Yellow),
    ItemData(0x, ItemName.Reflect,          ItemClassification.filler, ItemType.Program, 9, ProgramColor.Green),
    #ItemData(0x, ItemName.Rush,          ItemClassification.filler, ItemType.Program, 32, ProgramColor.Yellow),
    ItemData(0x, ItemName.Shield,          ItemClassification.filler, ItemType.Program, 8, ProgramColor.Blue),
    ItemData(0x, ItemName.SlipRunr,          ItemClassification.useful, ItemType.Program, 25, ProgramColor.Yellow),
    ItemData(0x, ItemName.SneakRun,          ItemClassification.filler, ItemType.Program, 16, ProgramColor.White),
    ItemData(0x, ItemName.Speed_Plus_Blue,          ItemClassification.filler, ItemType.Program, 36, ProgramColor.Blue),
    ItemData(0x, ItemName.Speed_Plus_Pink,          ItemClassification.filler, ItemType.Program, 36, ProgramColor.Pink),
    ItemData(0x, ItemName.Speed_Plus_White,          ItemClassification.filler, ItemType.Program, 36, ProgramColor.White),

    ItemData(0x, ItemName.SpeedMAX,          ItemClassification.filler, ItemType.Program, 39, ProgramColor.Green),
    ItemData(0x, ItemName.SuprArmr,          ItemClassification.useful, ItemType.Program, 1, ProgramColor.Red),
    #ItemData(0x, ItemName.Tango,          ItemClassification.filler, ItemType.Program, 34, ProgramColor.Green),
    ItemData(0x, ItemName.UnderSht,          ItemClassification.useful, ItemType.Program, 13, ProgramColor.White)

]

zennyList: typing.List[ItemData] = [
    ItemData(0x, ItemName.zenny_600z,   ItemClassification.filler, ItemType.Zenny, count=600),
    ItemData(0x, ItemName.zenny_700z,   ItemClassification.filler, ItemType.Zenny, count=700),
    ItemData(0x, ItemName.zenny_1000z,  ItemClassification.filler, ItemType.Zenny, count=1000),
    ItemData(0x, ItemName.zenny_1200z,  ItemClassification.filler, ItemType.Zenny, count=1200),
    ItemData(0x, ItemName.zenny_1600z,  ItemClassification.filler, ItemType.Zenny, count=1600),
    ItemData(0x, ItemName.zenny_2400z,  ItemClassification.filler, ItemType.Zenny, count=2400),
    ItemData(0x, ItemName.zenny_3000z,  ItemClassification.filler, ItemType.Zenny, count=3000),
    ItemData(0x, ItemName.zenny_5000z,  ItemClassification.filler, ItemType.Zenny, count=5000),
    ItemData(0x, ItemName.zenny_6000z,  ItemClassification.filler, ItemType.Zenny, count=6000),
    ItemData(0x, ItemName.zenny_8000z, ItemClassification.filler, ItemType.Zenny, count=8000),
    ItemData(0x, ItemName.zenny_100000z, ItemClassification.useful, ItemType.Zenny, count=100000)
]

bugFragList: typing.List[ItemData] = [
    ItemData(0x, ItemName.bugfrag_10, ItemClassification.filler, ItemType.BugFrag, count=10),
    ItemData(0x, ItemName.bugfrag_03, ItemClassification.filler, ItemType.BugFrag, count=3),
    ItemData(0x, ItemName.bugfrag_01, ItemClassification.filler, ItemType.BugFrag, count=1)
]

item_frequencies: typing.Dict[str, int] = {
    ItemName.ExpMem: 2,
    ItemName.Unlocker: 7,
    ItemName.HPMemory: 27,
    ItemName.RegUP1: 11,
    ItemName.RegUP2: 13,
    ItemName.RegUP3: 3,
    ItemName.Untrap: 3,
    ItemName.SubMem: 4,
    ItemName.MiniEnrg: 3,
    ItemName.FullEnrg: 5,
    ItemName.SneakRun: 3,
    ItemName.LocEnemy: 4,
    ItemName.Charge_Plus_White: 2,
    ItemName.Speed_Plus_White: 2,
    IteName.WhiCapsl: 2,
    ItemName.zenny_3000z: 2,
    ItemName.zenny_5000z: 3,
    IteName.zenny_100000z: 2,
    ItemName.bugfrag_10: 2
}

item_groups: typing.Dict[str, typing.Set[str]] = {
    "Key Items": {loc.itemName for loc in keyItemList},
    "Subchips": {loc.itemName for loc in subChipList},
    "Programs": {loc.itemName for loc in programList},
    "BattleChips": {loc.itemName for loc in chipList},
    "Zenny": {loc.itemName for loc in zennyList},
    "BugFrags": {loc.itemName for loc in bugFragList},
    "Secret Chips": {loc.iteName for loc in secretChipList}
}

all_items: typing.List[ItemData] = keyItemList + subChipList + chipList + programList + zennyList + bugFragList
item_table: typing.Dict[str, ItemData] = {item.itemName: item for item in all_items}
items_by_id: typing.Dict[int, ItemData] = {item.code: item for item in all_items}
