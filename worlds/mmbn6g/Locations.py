import typing

from BaseClasses import Location
from .Names.LocationName import LocationName

class LocationType(str, enum):
    BlueMysteryData = "bmd"
    PurpleMysteryData = "pmd"
    OverWorld = "overworld"
    Request = "request"
    LottoCode = "lotto"
    Boss = "boss"

class LocationData:
    name: str = ""
    id: int = 0x00

    flag_byte: int = 0x2000030
    flag_mask: int = 0x01

    type: LocationType

    update_address: int = 0x00
    text_script_index: int = 0
    text_box_indices: typing.List[int] = [0]
    inject_name: bool = False
    hint_flag: int = None
    hint_flag_mask: int = None

    def __init__(self, name, id, flag, mask, type, update_address=0x0, text_script_index=0x0,
                 text_box_indices=None, inject_name=False, hint_flag=None, hint_flag_mask=None):
        self.name = name
        self.id = id
        self.flag_byte = flag
        self.flag_mask = mask
        self.type = type
        self.update_address = update_address
        self.text_script_index = text_script_index
        if text_box_indices is None:
            text_box_indices = [0]
        self.text_box_indices = text_box_indices
        self.inject_name = inject_name
        self.hint_flag = hint_flag
        self.hint_flag_mask = hint_flag_mask


class MMBN6Location(Location):
    game: str = "MegaMan Battle Network 6"


bmds = [
    LocationData(LocationName.Robot_Control_Comp_1_BMD_1,     0xB61001, 0x02001F24, 0x80, LocationType.BlueMysteryData, 0x080A13C4)
    LocationData(LocationName.Robot_Control_Comp_1_BMD_2,     0xB61002, 0x02001F24, 0x40, LocationType.BlueMysteryData, 0x080A13D0)
    LocationData(LocationName.Robot_Control_Comp_2_BMD_1,     0xB61003, 0x02001F25, 0x80, LocationType.BlueMysteryData, 0x080A14C8)
    LocationData(LocationName.Robot_Control_Comp_2_BMD_2,     0xB61004, 0x02001F25, 0x40, LocationType.BlueMysteryData, 0x080A14D4)
    LocationData(LocationName.Aquarium_Comp_1_BMD_1,          0xB61005, 0x02001F28, 0x80, LocationType.BlueMysteryData, 0x080A1610)
    LocationData(LocationName.Aquarium_Comp_1_BMD_2,          0xB61006, 0x02001F28, 0x40, LocationType.BlueMysteryData, 0x080A161C)
    LocationData(LocationName.Aquarium_Comp_2_BMD_1,          0xB61007, 0x02001F29, 0x80, LocationType.BlueMysteryData, 0x080A1714)
    LocationData(LocationName.Aquarium_Comp_2_BMD_2,          0xB61008, 0x02001F29, 0x40, LocationType.BlueMysteryData, 0x080A1720)
    LocationData(LocationName.Aquarium_Comp_3_BMD_1,          0xB61009, 0x02001F2A, 0x80, LocationType.BlueMysteryData, 0x080A1818)
    LocationData(LocationName.Aquarium_Comp_3_BMD_2,          0xB6100A, 0x02001F2A, 0x40, LocationType.BlueMysteryData, 0x080A1824)
    LocationData(LocationName.JudgeTree_Comp_1_BMD_1,         0xB6100B, 0x02001F2C, 0x80, LocationType.BlueMysteryData, 0x080A1960)
    LocationData(LocationName.JudgeTree_Comp_1_BMD_2,         0xB6100C, 0x02001F2C, 0x40, LocationType.BlueMysteryData, 0x080A196C)
    LocationData(LocationName.JudgeTree_Comp_2_BMD_1,         0xB6100D, 0x02001F2D, 0x80, LocationType.BlueMysteryData, 0x080A1A64)
    LocationData(LocationName.JudgeTree_Comp_2_BMD_2,         0xB6100E, 0x02001F2D, 0x40, LocationType.BlueMysteryData, 0x080A1A70)
    LocationData(LocationName.JudgeTree_Comp_3_BMD_1,         0xB6100F, 0x02001F2E, 0x80, LocationType.BlueMysteryData, 0x080A1B68)
    LocationData(LocationName.JudgeTree_Comp_3_BMD_2,         0xB61010, 0x02001F2E, 0x40, LocationType.BlueMysteryData, 0x080A1B74)
    LocationData(LocationName.Mr_Weather_Comp_1_BMD_1,        0xB61011, 0x02001F30, 0x80, LocationType.BlueMysteryData, 0x080A1CB0)
    LocationData(LocationName.Mr_Weather_Comp_1_BMD_2,        0xB61012, 0x02001F30, 0x40, LocationType.BlueMysteryData, 0x080A1CBC)
    LocationData(LocationName.Mr_Weather_Comp_2_BMD_1,        0xB61013, 0x02001F31, 0x80, LocationType.BlueMysteryData, 0x080A1DB4)
    LocationData(LocationName.Mr_Weather_Comp_2_BMD_2,        0xB61014, 0x02001F31, 0x40, LocationType.BlueMysteryData, 0x080A1DC0)
    LocationData(LocationName.Mr_Weather_Comp_3_BMD_1,        0xB61015, 0x02001F32, 0x80, LocationType.BlueMysteryData, 0x080A1EB8)
    LocationData(LocationName.Mr_Weather_Comp_3_BMD_2,        0xB61016, 0x02001F32, 0x40, LocationType.BlueMysteryData, 0x080A1EC4)
    LocationData(LocationName.Pavilion_Comp_1_BMD_1,          0xB61017, 0x02001F38, 0x80, LocationType.BlueMysteryData, 0x080A2000)
    LocationData(LocationName.Pavilion_Comp_1_BMD_2,          0xB61018, 0x02001F38, 0x40, LocationType.BlueMysteryData, 0x080A200C)
    LocationData(LocationName.Pavilion_Comp_2_BMD_1,          0xB61019, 0x02001F38, 0x08, LocationType.BlueMysteryData, 0x080A2104)
    LocationData(LocationName.Pavilion_Comp_2_BMD_2,          0xB6101A, 0x02001F38, 0x04, LocationType.BlueMysteryData, 0x080A2110)
    LocationData(LocationName.Pavilion_Comp_3_BMD_1,          0xB6101B, 0x02001F39, 0x80, LocationType.BlueMysteryData, 0x080A2208)
    LocationData(LocationName.Pavilion_Comp_3_BMD_2,          0xB6101C, 0x02001F39, 0x40, LocationType.BlueMysteryData, 0x080A2214)
    LocationData(LocationName.Pavilion_Comp_4_BMD_1,          0xB6101D, 0x02001F39, 0x08, LocationType.BlueMysteryData, 0x080A230C)
    LocationData(LocationName.Pavilion_Comp_4_BMD_2,          0xB6101E, 0x02001F39, 0x04, LocationType.BlueMysteryData, 0x080A2318)
    LocationData(LocationName.ACDC_HP_BMD,                    0xB6101F, 0x02001F40, 0x08, LocationType.BlueMysteryData, 0x080A2458)
    LocationData(LocationName.Aquarium_HP_BMD,                0xB61020, 0x02001F41, 0x08, LocationType.BlueMysteryData, 0x080A24A4)
    LocationData(LocationName.Green_HP_BMD,                   0xB61021, 0x02001F42, 0x08, LocationType.BlueMysteryData, 0x080A24F0)
    LocationData(LocationName.Sky_HP_BMD,                     0xB61022, 0x02001F43, 0x80, LocationType.BlueMysteryData, 0x080A253C)
    LocationData(LocationName.RoboDog_Comp_BMD,               0xB61023, 0x02001F48, 0x80, LocationType.BlueMysteryData, 0x080A25CC)
    LocationData(LocationName.Labs_Comp_1_BMD_1,              0xB61024, 0x02001F48, 0x20, LocationType.BlueMysteryData, 0x080A25F4)
    LocationData(LocationName.Labs_Comp_1_BMD_2,              0xB61025, 0x02001F48, 0x10, LocationType.BlueMysteryData, 0x080A2600)
    LocationData(LocationName.Class_6_1_Comp_BMD_1,           0xB61026, 0x02001F48, 0x08, LocationType.BlueMysteryData, 0x080A2640)
    LocationData(LocationName.Class_6_1_Comp_BMD_2,           0xB61027, 0x02001F48, 0x04, LocationType.BlueMysteryData, 0x080A264C)
    LocationData(LocationName.Class_6_2_Comp_BMD,             0xB61028, 0x02001F48, 0x02, LocationType.BlueMysteryData, 0x080A268C)
    LocationData(LocationName.Class_1_1_Comp_BMD_1,           0xB61029, 0x02001F49, 0x80, LocationType.BlueMysteryData, 0x080A26D8)
    LocationData(LocationName.Class_1_1_Comp_BMD_2,           0xB6102A, 0x02001F49, 0x40, LocationType.BlueMysteryData, 0x080A26E4)
    LocationData(LocationName.Class_1_2_Comp_BMD_1,           0xB6102B, 0x02001F49, 0x20, LocationType.BlueMysteryData, 0x080A2724)
    LocationData(LocationName.Class_1_2_Comp_BMD_2,           0xB6102C, 0x02001F49, 0x10, LocationType.BlueMysteryData, 0x080A2730)
    LocationData(LocationName.Bathroom_Comp_BMD,              0xB6102D, 0x02001F49, 0x08, LocationType.BlueMysteryData, 0x080A2770)
    LocationData(LocationName.Elevator_Comp_BMD,              0xB6102E, 0x02001F49, 0x02, LocationType.BlueMysteryData, 0x080A2798)
    LocationData(LocationName.Fish_Stick_Shop_Comp_BMD_1,     0xB6102F, 0x02001F4A, 0x80, LocationType.BlueMysteryData, 0x080A27C0)
    LocationData(LocationName.Fish_Stick_Shop_Comp_BMD_2,     0xB61030, 0x02001F4A, 0x40, LocationType.BlueMysteryData, 0x080A27CC)
    LocationData(LocationName.Security_Camera_Comp_BMD_1,     0xB61031, 0x02001F4A, 0x20, LocationType.BlueMysteryData, 0x080A280C)
    LocationData(LocationName.Security_Camera_Comp_BMD_2,     0xB61032, 0x02001F4A, 0x10, LocationType.BlueMysteryData, 0x080A2818)
    LocationData(LocationName.Book_Comp_BMD_1,                0xB61033, 0x02001F4A, 0x08, LocationType.BlueMysteryData, 0x080A2858)
    LocationData(LocationName.Book_Comp_BMD_2,                0xB61034, 0x02001F4A, 0x04, LocationType.BlueMysteryData, 0x080A2864)
    LocationData(LocationName.Fan_Comp_BMD_1,                 0xB61035, 0x02001F4A, 0x02, LocationType.BlueMysteryData, 0x080A28A4)
    LocationData(LocationName.Fan_Comp_BMD_2,                 0xB61036, 0x02001F4A, 0x01, LocationType.BlueMysteryData, 0x080A28B0)
    LocationData(LocationName.Air_Conditioner_Comp_BMD_1,     0xB61037, 0x02001F4B, 0x80, LocationType.BlueMysteryData, 0x080A28F0)
    LocationData(LocationName.Air_Conditioner_Comp_BMD_2,     0xB61038, 0x02001F4B, 0x40, LocationType.BlueMysteryData, 0x080A28FC)
    LocationData(LocationName.Heater_Comp_BMD_1,              0xB61039, 0x02001F4B, 0x20, LocationType.BlueMysteryData, 0x080A293C)
    LocationData(LocationName.Heater_Comp_BMD_2,              0xB6103A, 0x02001F4B, 0x10, LocationType.BlueMysteryData, 0x080A2948)
    LocationData(LocationName.Shower_Comp_BMD_1,              0xB6103B, 0x02001F4B, 0x08, LocationType.BlueMysteryData, 0x080A2988)
    LocationData(LocationName.Shower_Comp_BMD_2,              0xB6103C, 0x02001F4B, 0x04, LocationType.BlueMysteryData, 0x080A2994)
    LocationData(LocationName.Heliport_Comp_BMD_1,            0xB6103D, 0x02001F4B, 0x02, LocationType.BlueMysteryData, 0x080A29D4)
    LocationData(LocationName.Heliport_Comp_BMD_2,            0xB6103E, 0x02001F4B, 0x01, LocationType.BlueMysteryData, 0x080A29E0)
    LocationData(LocationName.Labs_Comp_2_BMD,                0xB6103F, 0x02001F4C, 0x80, LocationType.BlueMysteryData, 0x080A2A64)
    LocationData(LocationName.Vending_Machine_Comp_BMD_1,     0xB61040, 0x02001F4C, 0x20, LocationType.BlueMysteryData, 0x080A2AB0)
    LocationData(LocationName.Vending_Machine_Comp_BMD_2,     0xB61041, 0x02001F4C, 0x10, LocationType.BlueMysteryData, 0x080A2ABC)
    LocationData(LocationName.Punish_Chair_Comp_BMD,          0xB61042, 0x02001F4C, 0x08, LocationType.BlueMysteryData, 0x080A2AFC)
    LocationData(LocationName.Water_Machine_Comp_BMD,         0xB61043, 0x02001F4C, 0x02, LocationType.BlueMysteryData, 0x080A2B48)
    LocationData(LocationName.Symbol_Comp_BMD_1,              0xB61044, 0x02001F4D, 0x80, LocationType.BlueMysteryData, 0x080A2B70)
    LocationData(LocationName.Symbol_Comp_BMD_2,              0xB61045, 0x02001F4D, 0x40, LocationType.BlueMysteryData, 0x080A2B7C)
    LocationData(LocationName.Monitor_Comp_BMD,               0xB61046, 0x02001F4D, 0x20, LocationType.BlueMysteryData, 0x080A2BBC)
    LocationData(LocationName.Popcorn_Shop_Comp_BMD,          0xB61047, 0x02001F4D, 0x08, LocationType.BlueMysteryData, 0x080A2BE4)
    LocationData(LocationName.Teachers_Room_Comp_BMD_1,       0xB61048, 0x02001F4D, 0x02, LocationType.BlueMysteryData, 0x080A2C0C)
    LocationData(LocationName.Teachers_Room_Comp_BMD_2,       0xB61049, 0x02001F4D, 0x01, LocationType.BlueMysteryData, 0x080A2C18)
    LocationData(LocationName.Pipe_Comp_BMD,                  0xB6104A, 0x02001F4E, 0x80, LocationType.BlueMysteryData, 0x080A2C58)
    LocationData(LocationName.Observation_Comp_BMD_1,         0xB6104B, 0x02001F4E, 0x20, LocationType.BlueMysteryData, 0x080A2C80)
    LocationData(LocationName.Observation_Comp_BMD_2,         0xB6104C, 0x02001F4E, 0x10, LocationType.BlueMysteryData, 0x080A2C8C)
    LocationData(LocationName.Oxygen_Tank_Comp_BMD,           0xB6104D, 0x02001F4E, 0x08, LocationType.BlueMysteryData, 0x080A2CCC)
    LocationData(LocationName.Principals_Office_Comp_BMD_1,   0xB6104E, 0x02001F4E, 0x02, LocationType.BlueMysteryData, 0x080A2D18)
    LocationData(LocationName.Principals_Office_Comp_BMD_2,   0xB6104F, 0x02001F4E, 0x01, LocationType.BlueMysteryData, 0x080A2D24)
    LocationData(LocationName.Mascot_Comp_BMD_1,              0xB61050, 0x02001F4F, 0x80, LocationType.BlueMysteryData, 0x080A2D64)
    LocationData(LocationName.Mascot_Comp_BMD_2,              0xB61051, 0x02001F4F, 0x40, LocationType.BlueMysteryData, 0x080A2D70)
    LocationData(LocationName.Stuffed_Toy_Shop_Comp_BMD_1,    0xB61052, 0x02001F4F, 0x20, LocationType.BlueMysteryData, 0x080A2DB0)
    LocationData(LocationName.Stuffed_Toy_Shop_Comp_BMD_2,    0xB61053, 0x02001F4F, 0x10, LocationType.BlueMysteryData, 0x080A2DBC)
    LocationData(LocationName.Dog_House_Comp_BMD_1,           0xB61054, 0x02001F4F, 0x08, LocationType.BlueMysteryData, 0x080A2DFC)
    LocationData(LocationName.Dog_House_Comp_BMD_2,           0xB61055, 0x02001F4F, 0x04, LocationType.BlueMysteryData, 0x080A2E08)
    LocationData(LocationName.Guide_Panel_Comp_BMD,           0xB61056, 0x02001F4F, 0x02, LocationType.BlueMysteryData, 0x080A2E48)
    LocationData(LocationName.Central_Area_1_BMD_1,           0xB61057, 0x02001F08, 0x80, LocationType.BlueMysteryData, 0x080A2EB4)
    LocationData(LocationName.Central_Area_1_BMD_2,           0xB61058, 0x02001F08, 0x40, LocationType.BlueMysteryData, 0x080A2EC0)
    LocationData(LocationName.Central_Area_2_BMD_1,           0xB61059, 0x02001F09, 0x80, LocationType.BlueMysteryData, 0x080A2FC8)
    LocationData(LocationName.Central_Area_2_BMD_2,           0xB6105A, 0x02001F09, 0x40, LocationType.BlueMysteryData, 0x080A2FD4)
    LocationData(LocationName.Central_Area_3_BMD,             0xB6105B, 0x02001F0A, 0x80, LocationType.BlueMysteryData, 0x080A30DC)
    LocationData(LocationName.Seaside_Area_1_BMD_1,           0xB6105C, 0x02001F0C, 0x80, LocationType.BlueMysteryData, 0x080A3234)
    LocationData(LocationName.Seaside_Area_1_BMD_2,           0xB6105D, 0x02001F0C, 0x40, LocationType.BlueMysteryData, 0x080A3240)
    LocationData(LocationName.Seaside_Area_1_BMD_3,           0xB6105E, 0x02001F0C, 0x08, LocationType.BlueMysteryData, 0x080A3264)
    LocationData(LocationName.Seaside_Area_2_BMD_1,           0xB6105F, 0x02001F0D, 0x80, LocationType.BlueMysteryData, 0x080A336C)
    LocationData(LocationName.Seaside_Area_2_BMD_2,           0xB61060, 0x02001F0D, 0x40, LocationType.BlueMysteryData, 0x080A3378)
    LocationData(LocationName.Seaside_Area_2_BMD_3,           0xB61061, 0x02001F0D, 0x08, LocationType.BlueMysteryData, 0x080A339C)
    LocationData(LocationName.Seaside_Area_3_BMD,             0xB61062, 0x02001F0E, 0x80, LocationType.BlueMysteryData, 0x080A34A4)
    LocationData(LocationName.Green_Area_1_BMD_1,             0xB61063, 0x02001F10, 0x80, LocationType.BlueMysteryData, 0x080A35FC)
    LocationData(LocationName.Green_Area_1_BMD_2,             0xB61064, 0x02001F10, 0x08, LocationType.BlueMysteryData, 0x080A362C)
    LocationData(LocationName.Green_Area_2_BMD_1,             0xB61065, 0x02001F11, 0x80, LocationType.BlueMysteryData, 0x080A3734)
    LocationData(LocationName.Green_Area_2_BMD_2,             0xB61066, 0x02001F11, 0x40, LocationType.BlueMysteryData, 0x080A3740)
    LocationData(LocationName.Green_Area_2_BMD_3,             0xB61067, 0x02001F11, 0x08, LocationType.BlueMysteryData, 0x080A3764)
    LocationData(LocationName.Underground_2_BMD_1,            0xB61068, 0x02001F15, 0x80, LocationType.BlueMysteryData, 0x080A39C4)
    LocationData(LocationName.Underground_2_BMD_2,            0xB61069, 0x02001F15, 0x08, LocationType.BlueMysteryData, 0x080A39E8)
    LocationData(LocationName.Sky_Area_1_BMD_1,               0xB6106A, 0x02001F18, 0x80, LocationType.BlueMysteryData, 0x080A3B1C)
    LocationData(LocationName.Sky_Area_1_BMD_2,               0xB6106B, 0x02001F18, 0x08, LocationType.BlueMysteryData, 0x080A3B4C)
    LocationData(LocationName.Sky_Area_2_BMD_1,               0xB6106C, 0x02001F19, 0x80, LocationType.BlueMysteryData, 0x080A3C54)
    LocationData(LocationName.Sky_Area_2_BMD_2,               0xB6106D, 0x02001F19, 0x40, LocationType.BlueMysteryData, 0x080A3C60)
    LocationData(LocationName.Sky_Area_2_BMD_3,               0xB6106E, 0x02001F19, 0x08, LocationType.BlueMysteryData, 0x080A3C84)
    LocationData(LocationName.ACDC_Area_BMD_1,                0xB6106F, 0x02001F1A, 0x80, LocationType.BlueMysteryData, 0x080A3D8C)
    LocationData(LocationName.ACDC_Area_BMD_2,                0xB61070, 0x02001F1A, 0x08, LocationType.BlueMysteryData, 0x080A3DBC)
    LocationData(LocationName.Undernet_1_BMD,                 0xB61071, 0x02001F1C, 0x80, LocationType.BlueMysteryData, 0x080A3F08)
    LocationData(LocationName.Undernet_Zero_BMD_1,            0xB61072, 0x02001F1D, 0x80, LocationType.BlueMysteryData, 0x080A401C)
    LocationData(LocationName.Undernet_Zero_BMD_2,            0xB61073, 0x02001F1D, 0x40, LocationType.BlueMysteryData, 0x080A4028)
    LocationData(LocationName.Undernet_Zero_BMD_3,            0xB61074, 0x02001F1D, 0x20, LocationType.BlueMysteryData, 0x080A4034)
    LocationData(LocationName.Undernet_2_BMD,                 0xB61075, 0x02001F1E, 0x80, LocationType.BlueMysteryData, 0x080A4154)
    LocationData(LocationName.Graveyard_BMD_1,                0xB61076, 0x02001F21, 0x80, LocationType.BlueMysteryData, 0x080A4540)
    LocationData(LocationName.Graveyard_BMD_2,                0xB61077, 0x02001F21, 0x40, LocationType.BlueMysteryData, 0x080A454C)
    LocationData(LocationName.Graveyard_BMD_3,                0xB61078, 0x02001F21, 0x10, LocationType.BlueMysteryData, 0x080A4564)
    LocationData(LocationName.Graveyard_BMD_4,                0xB61079, 0x02001F21, 0x08, LocationType.BlueMysteryData, 0x080A4570)
    LocationData(LocationName.Graveyard_BMD_5,                0xB6107A, 0x02001F23, 0x01, LocationType.BlueMysteryData, 0x080A45A0)
]

pmds = [
    LocationData(LocationName.ACDC_HP_PMD,                    0xB6107B, 0x02001F40, 0x04, LocationType.PurpleMysteryData, 0x080A2464)
    LocationData(LocationName.Aquarium_HP_PMD,                0xB6107C, 0x02001F41, 0x04, LocationType.PurpleMysteryData, 0x080A24B0)
    LocationData(LocationName.Green_HP_PMD,                   0xB6107D, 0x02001F42, 0x04, LocationType.PurpleMysteryData, 0x080A24FC)
    LocationData(LocationName.Sky_HP_PMD,                     0xB6107E, 0x02001F43, 0x40, LocationType.PurpleMysteryData, 0x080A2548)
    LocationData(LocationName.Class_6_2_Comp_PMD,             0xB6107F, 0x02001F48, 0x01, LocationType.PurpleMysteryData, 0x080A2698)
    LocationData(LocationName.Labs_Comp_2_PMD,                0xB61080, 0x02001F4C, 0x40, LocationType.PurpleMysteryData, 0x080A2A70)
    LocationData(LocationName.Punish_Chair_Comp_PMD,          0xB61081, 0x02001F4C, 0x04, LocationType.PurpleMysteryData, 0x080A2B08)
    LocationData(LocationName.Oxygen_Tank_Comp_PMD,           0xB61082, 0x02001F4E, 0x04, LocationType.PurpleMysteryData, 0x080A2CD8)
    LocationData(LocationName.Central_Area_3_PMD,             0xB61083, 0x02001F0A, 0x40, LocationType.PurpleMysteryData, 0x080A30E8)
    LocationData(LocationName.Seaside_Area_3_PMD,             0xB61084, 0x02001F0E, 0x40, LocationType.PurpleMysteryData, 0x080A34B0)
    LocationData(LocationName.Green_Area_1_PMD,               0xB61085, 0x02001F10, 0x40, LocationType.PurpleMysteryData, 0x080A3608)
    LocationData(LocationName.Underground_1_PMD_1,            0xB61086, 0x02001F14, 0x80, LocationType.PurpleMysteryData, 0x080A38B0)
    LocationData(LocationName.Underground_1_PMD_2,            0xB61087, 0x02001F14, 0x40, LocationType.PurpleMysteryData, 0x080A38BC)
    LocationData(LocationName.Sky_Area_1_PMD,                 0xB61088, 0x02001F18, 0x40, LocationType.PurpleMysteryData, 0x080A3B28)
    LocationData(LocationName.ACDC_Area_PMD,                  0xB61089, 0x02001F1A, 0x40, LocationType.PurpleMysteryData, 0x080A3D98)
    LocationData(LocationName.Undernet_1_PMD,                 0xB6108A, 0x02001F1C, 0x40, LocationType.PurpleMysteryData, 0x080A3F14)
    LocationData(LocationName.Undernet_2_PMD,                 0xB6108B, 0x02001F1E, 0x40, LocationType.PurpleMysteryData, 0x080A4160)
    LocationData(LocationName.Graveyard_PMD_1,                0xB6108C, 0x02001F21, 0x20, LocationType.PurpleMysteryData, 0x080A4558)
    LocationData(LocationName.Graveyard_PMD_2,                0xB6108D, 0x02001F21, 0x04, LocationType.PurpleMysteryData, 0x080A457C)
]

overworlds = [
    LocationData(LocationName.School_Mr_Quiz,                     0xB6108E, 0x02001EAB, 0x02, LocationType.OverWorld, 0x76C83C,   7, [22]),
    LocationData(LocationName.Aquarium_Quiz_Master,               0xB6108F, 0x02001EAC, 0x80, LocationType.OverWorld, 0x777218,   2, [39]),
    LocationData(LocationName.Green_Quiz_King,                    0xB61090, 0x02001EAC, 0x20, LocationType.OverWorld, 0x77C55C,  12, [53]),
    LocationData(LocationName.Central_Barr100_H_Trade,            0xB61091, 0x02001EAB, 0x80, LocationType.OverWorld, 0x764B38, 107, [3], True, 0x02001EAA, 0x04),
    LocationData(LocationName.Aquarium_PnlRetrn_*_Trade,          0xB61092, 0x02001EAA, 0x02, LocationType.OverWorld, 0x7991F0,   2, [2], True, 0x02001EAA, 0x01),
    LocationData(LocationName.Green_HolyPnl_S_Trade,              0xB61093, 0x02001EAB, 0x08, LocationType.OverWorld, 0x77A888,  52, [2], True, 0x02001EAB, 0x10),
    LocationData(LocationName.AirCon_AuraHed1_B_Trade,            0xB61094, 0x02001EAB, 0x20, LocationType.OverWorld, 0x79E718,   2, [2], True, 0x02001EAB, 0x40),
    LocationData(LocationName.Class_1_2_EnergBom_K_Trade,         0xB61095, 0x02001EAD, 0x80, LocationType.OverWorld, 0x76B554,  10, [1], True, 0x02001EAC, 0x01),
    LocationData(LocationName.Aquarium_DublShot_C_Trade,          0xB61096, 0x02001EAD, 0x20, LocationType.OverWorld, 0x773D3C,  10, [1], True, 0x02001EAD, 0x40),
    LocationData(LocationName.WatrMchn_HiBoomer_V_Trade,          0xB61097, 0x02001EAD, 0x08, LocationType.OverWorld, 0x79F4DC,   2, [1], True, 0x02001EAD, 0x10),
    LocationData(LocationName.Sky_GrabRvng_I_Trade,               0xB61098, 0x02001EAD, 0x02, LocationType.OverWorld, 0x77F4A0,   7, [1], True, 0x02001EAD, 0x04),
    LocationData(LocationName.ACDC_BigBomb_O_Trade,               0xB61099, 0x02001EAE, 0x80, LocationType.OverWorld, 0x798A08,   2, [1], True, 0x02001EAD, 0x01),
    LocationData(LocationName.Class_6_1_Grid,                     0xB6109A, 0x02001CB8, 0x01, LocationType.OverWorld, 0x755468,   0, [4, 5]),
    LocationData(LocationName.Seaside_Auditorium_Trash_Can,       0xB6109B, 0x02001CB9, 0x80, LocationType.OverWorld, 0x758FA0,   3, [2, 3]),
    LocationData(LocationName.Seaside_Control_Room_Ladder,        0xB6109C, 0x02001CB8, 0x04, LocationType.OverWorld, 0x759248,   2, [2]),
    LocationData(LocationName.Green_Foyer_Flowers,                0xB6109D, 0x02001CB9, 0x40, LocationType.OverWorld, 0x756870,   6, [3, 4]),
    LocationData(LocationName.Sky_Air_Tank,                       0xB6109E, 0x02001CB8, 0x02, LocationType.OverWorld, 0x75A3F4,   4, [6]),
    LocationData(LocationName.ACDC_Dexs_Door,                     0xB6109F, 0x02001CB9, 0x08, LocationType.OverWorld, 0x753814,   5, [3]),
    LocationData(LocationName.Principals_Coffee_Table,            0xB610A0, 0x02001CB9, 0x20, LocationType.OverWorld, 0x7573BC,   6, [3, 4]),
    LocationData(LocationName.Seaside_Pavilion_Waterfall,         0xB610A1, 0x02001CB9, 0x10, LocationType.OverWorld, 0x75AF00,   2, [3]),
    LocationData(LocationName.Central_1_Net_Cafe,                 0xB610A2, 0x02001CAA, 0x08, LocationType.OverWorld, 0x782844, 130, [4]),
    LocationData(LocationName.Green_2_Net_Cafe,                   0xB610A3, 0x02001CAB, 0x40, LocationType.OverWorld, 0x78E678,  67, [3]),
    LocationData(LocationName.Sky_1_Net_Cafe,                     0xB610A4, 0x02001CAB, 0x04, LocationType.OverWorld, 0x7903B4,  87, [3]),
    LocationData(LocationName.Central_2_Heel_Navi,                0xB610A5, 0x02001EAE, 0x10, LocationType.OverWorld, 0x784DDC,  53, [3, 4]),
    LocationData(LocationName.Class_1_2_Heel_Navi,                0xB610A6, 0x02001CBA, 0x01, LocationType.OverWorld, 0x790DF4,  11, [2]),
    LocationData(LocationName.Seaside_Auditorium_Man,             0xB610A7, 0x02001EAE, 0x02, LocationType.OverWorld, 0x776A7C,  13, [4]),
    LocationData(LocationName.Aquarium_Comp_1_Navi,               0xB610A8, 0x02001EAF, 0x40, LocationType.OverWorld, 0x795DD0,  13, [5]),
    LocationData(LocationName.Green_1_Heel_Navi,                  0xB610A9, 0x02001EAC, 0x08, LocationType.OverWorld, 0x78D2A0,  21, [2]),
    #LocationData(LocationName.Undernet_0_Heel_Navi,              0xB610AA, 0x02003178, 0x01, LocationType.OverWorld, 0x794404,  11, [1]),
    LocationData(LocationName.Green_Punishment_Room_Prog,         0xB610AB, 0x02001EAC, 0x02, LocationType.OverWorld, 0x77C318,   5, [2]),
    LocationData(LocationName.Sky_1_Brown_Navi,                   0xB610AC, 0x02001CB9, 0x04, LocationType.OverWorld, 0x7903B4,   6, [2]),
    LocationData(LocationName.Bass,                               0xB610AD, 0x02001E89, 0x01, LocationType.OverWorld, 0x7D6DC0,   2, [2]),
    LocationData(LocationName.Talk_To_Mayl,                       0xB610AE, 0x02001CC5, 0x20, LocationType.OverWorld, 0x766E28,  11, [3]),
    LocationData(LocationName.ElecMan_Scenario,                   0xB6111E, 0x02001DDF, 0x10, LocationType.OverWorld, 0x7BFE50,   5, [0]),
    LocationData(LocationName.SlashMan_Scenario,                  0xB6111F, 0x02001D94, 0x80, LocationType.OverWorld, 0x7BA78C,   1, [0]),
    LocationData(LocationName.EraseMan_Scenario,                  0xB61120, 0x02001E23, 0x04, LocationType.OverWorld, 0x7C9D54,   1, [0]),
    LocationData(LocationName.ChargeMan_Scenario,                 0xB61121, 0x02001E24, 0x40, LocationType.OverWorld, 0x7CB584,  1, [0])
]

requests = [
    LocationData(LocationName.Virus_Deletion,           0xB610AF, 0x02002014, 0x80, LocationType.Request, 0x76A1E4,   2, [2]),
    LocationData(LocationName.Find_Keepsake,            0xB610B0, 0x02002014, 0x40, LocationType.Request, 0x764B38, 102, [4, 5]),
    LocationData(LocationName.Errand_Request,           0xB610B1, 0x02002014, 0x20, LocationType.Request, 0x76EDFC,  12, [4]),
    LocationData(LocationName.For_Victory,              0xB610B2, 0x02002014, 0x10, LocationType.Request, 0x782844, 103, [4]),
    LocationData(LocationName.JuvenileDiv,              0xB610B3, 0x02002017, 0x40, LocationType.Request, 0x79FE54,   2, [7]),
    LocationData(LocationName.Somebody_Help,            0xB610B4, 0x02002014, 0x08, LocationType.Request, 0x7953EC,   9, [3]),
    LocationData(LocationName.Get_The_Chip,             0xB610B5, 0x02002014, 0x04, LocationType.Request, 0x78BD44,  17, [2, 3]),
    LocationData(LocationName.Stock_Up,                 0xB610B6, 0x02002014, 0x02, LocationType.Request, 0x773D3C,  16, [5]),
    LocationData(LocationName.StandIn_Recruit,          0xB610B7, 0x02002014, 0x01, LocationType.Request, 0x7991F0,  12, [3]),
    LocationData(LocationName.PenguinsRanAway,          0xB610B8, 0x02002017, 0x08, LocationType.Request, 0x773D3C,  26, [3]),
    LocationData(LocationName.Daughter_Worry,           0xB610B9, 0x02002015, 0x80, LocationType.Request, 0x778738,  32, [7, 8]),
    LocationData(LocationName.Stop_Him,                 0xB610BA, 0x02002015, 0x40, LocationType.Request, 0x77B9F0,  24, [4]),
    LocationData(LocationName.Loan_Collection,          0xB610BB, 0x02002015, 0x20, LocationType.Request, 0x79A664,  12, [6]),
    LocationData(LocationName.Lumber_Merchant,          0xB610BC, 0x02002015, 0x10, LocationType.Request, 0x78E678,  32, [4]),
    LocationData(LocationName.TimeCpsl,                 0xB610BD, 0x02002015, 0x08, LocationType.Request, 0x778738,  37, [13]),
    LocationData(LocationName.DietGood_Money,           0xB610BE, 0x02002017, 0x02, LocationType.Request, 0x76C080,  12, [4]),
    LocationData(LocationName.Find_The_Virus,           0xB610BF, 0x02002017, 0x10, LocationType.Request, 0x764B38, 142, [4]),
    LocationData(LocationName.Got_A_Problem,            0xB610C0, 0x02002015, 0x04, LocationType.Request, 0x776A7C,  22, [16]),
    LocationData(LocationName.Songwriter,               0xB610C1, 0x02002015, 0x02, LocationType.Request, 0x7903B4,  31, [28, 29]),
    LocationData(LocationName.Buy_Whch_Stock,           0xB610C2, 0x02002015, 0x01, LocationType.Request, 0x7903B4,  54, [6]),
    LocationData(LocationName.Cant_Open_Safe,           0xB610C3, 0x02002016, 0x80, LocationType.Request, 0x7A039C,   7, [4]),
    LocationData(LocationName.Get_The_Bad_Guy,          0xB610C4, 0x02002017, 0x20, LocationType.Request, 0x764B38, 126, [5]),
    LocationData(LocationName.Update_Help,              0xB610C5, 0x02002017, 0x04, LocationType.Request, 0x773D3C,  36, [3]),
    LocationData(LocationName.Do_Something,             0xB610C6, 0x02002016, 0x40, LocationType.Request, 0x77246C,  42, [3]),
    LocationData(LocationName.Want_Meet_Dghtr,          0xB610C7, 0x02002016, 0x20, LocationType.Request, 0x79B094,   4, [9]),
    LocationData(LocationName.Not_Engh_Member,          0xB610C8, 0x02002016, 0x10, LocationType.Request, 0x79C598,   2, [4, 5]),
    LocationData(LocationName.Track_The_Crmnl_1,        0xB610C9, 0x02002016, 0x08, LocationType.Request, 0x777218,  12, [4]),
    LocationData(LocationName.Track_The_Crmnl_2,        0xB610CA, 0x02002016, 0x08, LocationType.Request, 0x777218,  12, [4]),
    LocationData(LocationName.Track_The_Crmnl_3,        0xB610CB, 0x02002016, 0x08, LocationType.Request, 0x777218,  12, [4, 5]),
    LocationData(LocationName.Self_Research,            0xB610CC, 0x02002017, 0x01, LocationType.Request, 0x79CAE4,   2, [7]),
    LocationData(LocationName.OfficialRequest_1,        0xB610CD, 0x02002018, 0x80, LocationType.Request, 0x7A0B40,   3, [3, 4]),
    LocationData(LocationName.OfficialRequest_2,        0xB610CE, 0x02002018, 0x80, LocationType.Request, 0x7A0B40,   3, [3, 4]),
    LocationData(LocationName.OfficialRequest_3,        0xB610CF, 0x02002018, 0x80, LocationType.Request, 0x7A0B40,   3, [3, 4]),
    LocationData(LocationName.Wheres_My_Navi,           0xB610D0, 0x02002016, 0x04, LocationType.Request, 0x76AD9C,   2, [4]),
    LocationData(LocationName.One_More_Time,            0xB610D1, 0x02002016, 0x02, LocationType.Request, 0x764B38, 122, [4]),
    LocationData(LocationName.SupportChip_Pls,          0xB610D2, 0x02002016, 0x01, LocationType.Request, 0x77E80C,  12, [4]),
    LocationData(LocationName.Negotiate,                0xB610D3, 0x02002017, 0x80, LocationType.Request, 0x77E80C,  24, [4]),
    LocationData(LocationName.An_Experiment_1,          0xB610D4, 0x02002018, 0x40, LocationType.Request, 0x7755B8,  84, [4, 5]),
    LocationData(LocationName.An_Experiment_2,          0xB610D5, 0x02002018, 0x40, LocationType.Request, 0x7755B8,  84, [4, 5]),
    LocationData(LocationName.An_Experiment_3,          0xB610D6, 0x02002018, 0x40, LocationType.Request, 0x7755B8,  84, [4, 5]),
    LocationData(LocationName.RoadToSoulBtlr,           0xB610D7, 0x02002018, 0x20, LocationType.Request, 0x79A664,  24, [7])
]

lotto_codes = [
    LocationData(LocationName.Lotto_Code_01, 0xB610D8, 0x0200214C, 0x80, LocationType.LottoCode, 0x754BD8, 58, [0]),
    LocationData(LocationName.Lotto_Code_02, 0xB610D9, 0x0200214C, 0x40, LocationType.LottoCode, 0x754BD8, 59, [0]),
    LocationData(LocationName.Lotto_Code_03, 0xB610DA, 0x0200214C, 0x20, LocationType.LottoCode, 0x754BD8, 60, [0]),
    LocationData(LocationName.Lotto_Code_04, 0xB610DB, 0x0200214C, 0x10, LocationType.LottoCode, 0x754BD8, 61, [0]),
    LocationData(LocationName.Lotto_Code_05, 0xB610DC, 0x0200214C, 0x08, LocationType.LottoCode, 0x754BD8, 62, [0]),
    LocationData(LocationName.Lotto_Code_06, 0xB610DD, 0x0200214C, 0x04, LocationType.LottoCode, 0x754BD8, 63, [0]),
    LocationData(LocationName.Lotto_Code_07, 0xB610DE, 0x0200214C, 0x02, LocationType.LottoCode, 0x754BD8, 64, [0]),
    LocationData(LocationName.Lotto_Code_08, 0xB610DF, 0x0200214C, 0x01, LocationType.LottoCode, 0x754BD8, 65, [0]),
    LocationData(LocationName.Lotto_Code_09, 0xB610E0, 0x0200214D, 0x80, LocationType.LottoCode, 0x754BD8, 66, [0]),
    LocationData(LocationName.Lotto_Code_10, 0xB610E1, 0x0200214D, 0x40, LocationType.LottoCode, 0x754BD8, 67, [0]),
    LocationData(LocationName.Lotto_Code_11, 0xB610E2, 0x0200214D, 0x20, LocationType.LottoCode, 0x754BD8, 68, [0]),
    LocationData(LocationName.Lotto_Code_12, 0xB610E3, 0x0200214D, 0x10, LocationType.LottoCode, 0x754BD8, 69, [0]),
    LocationData(LocationName.Lotto_Code_13, 0xB610E4, 0x0200214D, 0x08, LocationType.LottoCode, 0x754BD8, 70, [0]),
    LocationData(LocationName.Lotto_Code_14, 0xB610E5, 0x0200214D, 0x04, LocationType.LottoCode, 0x754BD8, 71, [0]),
    LocationData(LocationName.Lotto_Code_15, 0xB610E6, 0x0200214D, 0x02, LocationType.LottoCode, 0x754BD8, 72, [0]),
    LocationData(LocationName.Lotto_Code_16, 0xB610E7, 0x0200214D, 0x01, LocationType.LottoCode, 0x754BD8, 73, [0]),
    LocationData(LocationName.Lotto_Code_17, 0xB610E8, 0x0200214E, 0x80, LocationType.LottoCode, 0x754BD8, 74, [0]),
    LocationData(LocationName.Lotto_Code_18, 0xB610E9, 0x0200214E, 0x40, LocationType.LottoCode, 0x754BD8, 75, [0]),
    LocationData(LocationName.Lotto_Code_19, 0xB610EA, 0x0200214E, 0x20, LocationType.LottoCode, 0x754BD8, 76, [0]),
    LocationData(LocationName.Lotto_Code_20, 0xB610EB, 0x0200214E, 0x10, LocationType.LottoCode, 0x754BD8, 77, [0]),
    LocationData(LocationName.Lotto_Code_21, 0xB610EC, 0x0200214E, 0x08, LocationType.LottoCode, 0x754BD8, 78, [0]),
    LocationData(LocationName.Lotto_Code_22, 0xB610ED, 0x0200214E, 0x04, LocationType.LottoCode, 0x754BD8, 79, [0]),
    LocationData(LocationName.Lotto_Code_23, 0xB610EE, 0x0200214E, 0x02, LocationType.LottoCode, 0x754BD8, 80, [0]),
    LocationData(LocationName.Lotto_Code_24, 0xB610EF, 0x0200214E, 0x01, LocationType.LottoCode, 0x754BD8, 81, [0]),
    LocationData(LocationName.Lotto_Code_25, 0xB610F0, 0x0200214F, 0x80, LocationType.LottoCode, 0x754BD8, 82, [0]),
    LocationData(LocationName.Lotto_Code_26, 0xB610F1, 0x0200214F, 0x40, LocationType.LottoCode, 0x754BD8, 83, [0]),
    LocationData(LocationName.Lotto_Code_27, 0xB610F2, 0x0200214F, 0x20, LocationType.LottoCode, 0x754BD8, 84, [0]),
    LocationData(LocationName.Lotto_Code_28, 0xB610F3, 0x0200214F, 0x10, LocationType.LottoCode, 0x754BD8, 85, [0]),
    LocationData(LocationName.Lotto_Code_29, 0xB610F4, 0x0200214F, 0x08, LocationType.LottoCode, 0x754BD8, 86, [0]),
    LocationData(LocationName.Lotto_Code_30, 0xB610F5, 0x0200214F, 0x04, LocationType.LottoCode, 0x754BD8, 87, [0]),
    LocationData(LocationName.Lotto_Code_31, 0xB610F6, 0x0200214F, 0x02, LocationType.LottoCode, 0x754BD8, 88, [0]),
    LocationData(LocationName.Lotto_Code_32, 0xB610F7, 0x0200214F, 0x01, LocationType.LottoCode, 0x754BD8, 89, [0]),
    LocationData(LocationName.Lotto_Code_33, 0xB610F8, 0x02002150, 0x80, LocationType.LottoCode, 0x754BD8, 90, [0]),
    LocationData(LocationName.Lotto_Code_34, 0xB610F9, 0x02002150, 0x40, LocationType.LottoCode, 0x754BD8, 91, [0]),
    LocationData(LocationName.Lotto_Code_35, 0xB610FA, 0x02002150, 0x20, LocationType.LottoCode, 0x754BD8, 92, [0]),
    LocationData(LocationName.Lotto_Code_36, 0xB610FB, 0x02002150, 0x10, LocationType.LottoCode, 0x754BD8, 93, [0]),
    LocationData(LocationName.Lotto_Code_37, 0xB610FC, 0x02002150, 0x08, LocationType.LottoCode, 0x754BD8, 94, [0]),
    LocationData(LocationName.Lotto_Code_38, 0xB610FD, 0x02002150, 0x04, LocationType.LottoCode, 0x754BD8, 95, [0]),
    LocationData(LocationName.Lotto_Code_39, 0xB610FE, 0x02002150, 0x02, LocationType.LottoCode, 0x754BD8, 96, [0]),
    LocationData(LocationName.Lotto_Code_40, 0xB610FF, 0x02002150, 0x01, LocationType.LottoCode, 0x754BD8, 97, [0]),
    LocationData(LocationName.Lotto_Code_41, 0xB61100, 0x02002151, 0x80, LocationType.LottoCode, 0x754BD8, 98, [0]),
    LocationData(LocationName.Lotto_Code_42, 0xB61101, 0x02002151, 0x40, LocationType.LottoCode, 0x754BD8, 99, [0]),
    LocationData(LocationName.Lotto_Code_43, 0xB61102, 0x02002151, 0x20, LocationType.LottoCode, 0x754BD8, 100, [0]),
    LocationData(LocationName.Lotto_Code_44, 0xB61103, 0x02002151, 0x10, LocationType.LottoCode, 0x754BD8, 101, [0]),
    LocationData(LocationName.Lotto_Code_45, 0xB61104, 0x02002151, 0x08, LocationType.LottoCode, 0x754BD8, 102, [0]),
    LocationData(LocationName.Lotto_Code_46, 0xB61105, 0x02002151, 0x04, LocationType.LottoCode, 0x754BD8, 103, [0]),
    LocationData(LocationName.Lotto_Code_47, 0xB61106, 0x02002151, 0x02, LocationType.LottoCode, 0x754BD8, 104, [0]),
    LocationData(LocationName.Lotto_Code_48, 0xB61107, 0x02002151, 0x01, LocationType.LottoCode, 0x754BD8, 105, [0]),
    LocationData(LocationName.Lotto_Code_49, 0xB61108, 0x02002152, 0x80, LocationType.LottoCode, 0x754BD8, 106, [0]),
    LocationData(LocationName.Lotto_Code_50, 0xB61109, 0x02002152, 0x40, LocationType.LottoCode, 0x754BD8, 107, [0]),
    LocationData(LocationName.Lotto_Code_51, 0xB6110A, 0x02002152, 0x20, LocationType.LottoCode, 0x754BD8, 108, [0]),
    LocationData(LocationName.Lotto_Code_52, 0xB6110B, 0x02002152, 0x10, LocationType.LottoCode, 0x754BD8, 109, [0]),
    LocationData(LocationName.Lotto_Code_53, 0xB6110C, 0x02002152, 0x08, LocationType.LottoCode, 0x754BD8, 110, [0]),
    LocationData(LocationName.Lotto_Code_54, 0xB6110D, 0x02002152, 0x04, LocationType.LottoCode, 0x754BD8, 111, [0]),
    LocationData(LocationName.Lotto_Code_55, 0xB6110E, 0x02002152, 0x02, LocationType.LottoCode, 0x754BD8, 112, [0]),
    LocationData(LocationName.Lotto_Code_56, 0xB6110F, 0x02002152, 0x01, LocationType.LottoCode, 0x754BD8, 113, [0]),
    LocationData(LocationName.Lotto_Code_57, 0xB61110, 0x02002153, 0x80, LocationType.LottoCode, 0x754BD8, 114, [0]),
    LocationData(LocationName.Lotto_Code_58, 0xB61111, 0x02002153, 0x40, LocationType.LottoCode, 0x754BD8, 115, [0])
]

bosses = [
    LocationData(LocationName.BlastMan_EX,   0xB61112, 0x0200206C, 0x40, LocationType.Boss)
    LocationData(LocationName.DiveMan_EX,    0xB61113, 0x0200206C, 0x08, LocationType.Boss)
    LocationData(LocationName.CircusMan_EX,  0xB61114, 0x0200206C, 0x01, LocationType.Boss)
    LocationData(LocationName.JudgeMan_EX,   0xB61115, 0x0200206D, 0x20, LocationType.Boss)
    LocationData(LocationName.ElementMan_EX, 0xB61116, 0x0200206D, 0x04, LocationType.Boss)
    LocationData(LocationName.Colonel_EX,    0xB61117, 0x0200206E, 0x80, LocationType.Boss)
    LocationData(LocationName.BlastMan_SP,   0xB61118, 0x02001CF0, 0x04, LocationType.Boss)
    LocationData(LocationName.DiveMan_SP,    0xB61119, 0x02001CF1, 0x10, LocationType.Boss)
    LocationData(LocationName.CircusMan_SP,  0xB6111A, 0x02001CF2, 0x40, LocationType.Boss)
    LocationData(LocationName.JudgeMan_SP,   0xB6111B, 0x02001CF2, 0x01, LocationType.Boss)
    LocationData(LocationName.ElementMan_SP, 0xB6111C, 0x02001CF3, 0x04, LocationType.Boss)
    LocationData(LocationName.Colonel_SP,    0xB6111D, 0x02001CF5, 0x40, LocationType.Boss)
]

graveyard_locations = {
    Graveyard_BMD_1,
    Graveyard_BMD_2,
    Graveyard_BMD_3,
    Graveyard_BMD_4,
    Graveyard_BMD_5
}

location_groups: typing.Dict[str, typing.Set[str]] = {
    "BMDs": {loc.name for loc in bmds},
    "PMDs": {loc.name for loc in pmds},
    "OverWorlds": {loc.name for loc in overworlds}
    "Jobs": {loc.name for loc in requests},
    "Lotto Codes": {loc.name for loc in lotto_codes},
    "Bosses": {loc.name for loc in bosses},
    "Graveyard Area": {LocationName.Graveyard_BMD_1, LocationName.Graveyard_BMD_2,
                    LocationName.Graveyard_BMD_3, LocationName.Graveyard_BMD_4, LocationName.Graveyard_BMD_5},
}

all_locations: typing.List[LocationData] = bmds + pmds + overworlds + jobs + lotto_codes + bosses
scoutable_locations: typing.List[LocationData] = [loc for loc in all_locations if loc.hint_flag is not None]
location_table: typing.Dict[str, int] = {locData.name: locData.id for locData in all_locations}
location_data_table: typing.Dict[str, LocationData] = {locData.name: locData for locData in all_locations}
