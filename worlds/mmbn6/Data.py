import orjson
import pkgutil
from typing import Dict, List, Any


APWORLD_VERSION = "0.2.0"

def load_json_data(data_name: str) -> List[Any] | Dict[str, Any]:
    return orjson.loads(pkgutil.get_data(__name__, "data/" + data_name).decode("utf-8-sig"))

class MMBN6Data:
    gregar_archive_data: Dict[str, Any]
    falzar_archive_data: Dict[str, Any]
    rom_data_end: int

    def __init__(self):
        self.gregar_archive_data = load_json_data("ArchiveData/gregarArchiveData.json")
        self.falzar_archive_data = load_json_data("ArchiveData/falzarArchiveData.json")

        # This is an arbitrary spot in the ROM data that is far enough out that it should not ever overwrite existing
        # data. It may need to change in the future. Reference the output of patch-rom.py to verify.
        # https://github.com/RischDev/bn6-ap-patch
        self.rom_data_end = 0x810000

data = MMBN6Data()