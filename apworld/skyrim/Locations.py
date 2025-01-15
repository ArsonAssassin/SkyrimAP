from enum import IntEnum
from typing import Optional, NamedTuple, Dict

from BaseClasses import Location, Region
from .Items import SkyrimItem

class SkyrimLocationCategory(IntEnum):
    SKIP = 0,
    EVENT = 1,
    CHEESE = 2


class SkyrimLocationData(NamedTuple):
    id: int
    name: str
    default_item: str
    category: SkyrimLocationCategory


class SkyrimLocation(Location):
    game: str = "Skyrim"
    category: SkyrimLocationCategory
    default_item_name: str

    def __init__(
            self,
            player: int,
            name: str,
            category: SkyrimLocationCategory,
            default_item_name: str,
            address: Optional[int] = None,
            parent: Optional[Region] = None):
        super().__init__(player, name, address, parent)
        self.default_item_name = default_item_name
        self.category = category
        self.id = id

    @staticmethod
    def get_name_to_id() -> dict:
        base_id = 512340000
        table_offset = 1000

        table_order = [
           "Cheese"
         ]

        output = {}
        for i, region_name in enumerate(table_order):
            if len(location_tables[region_name]) > table_offset:
                raise Exception("A location table has {} entries, that is more than {} entries (table #{})".format(len(location_tables[region_name]), table_offset, i))
            output.update({location_data.name: location_data.id for location_data in location_tables[region_name]})
        return output

    def place_locked_item(self, item: SkyrimItem):
        self.item = item
        self.locked = True
        item.location = self
location_skip_categories = {
SkyrimLocationCategory.EVENT, SkyrimLocationCategory.SKIP
}

location_tables = {
"Cheese": [
    SkyrimLocationData(512340000, f"Cheese 1", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340001, f"Cheese 2", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340002, f"Cheese 3", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340003, f"Cheese 4", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340004, f"Cheese 5", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340005, f"Cheese 6", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340006, f"Cheese 7", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340007, f"Cheese 8", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340008, f"Cheese 9", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340009, f"Cheese 10", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340010, f"Cheese 11", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340011, f"Cheese 12", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340012, f"Cheese 13", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340013, f"Cheese 14", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340014, f"Cheese 15", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340015, f"Cheese 16", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340016, f"Cheese 17", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340017, f"Cheese 18", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340018, f"Cheese 19", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340019, f"Cheese 20", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340020, f"Cheese 21", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340021, f"Cheese 22", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340022, f"Cheese 23", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340023, f"Cheese 24", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340024, f"Cheese 25", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340025, f"Cheese 26", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340026, f"Cheese 27", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340027, f"Cheese 28", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340028, f"Cheese 29", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340029, f"Cheese 30", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340030, f"Cheese 31", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340031, f"Cheese 32", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340032, f"Cheese 33", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340033, f"Cheese 34", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340034, f"Cheese 35", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340035, f"Cheese 36", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340036, f"Cheese 37", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340037, f"Cheese 38", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340038, f"Cheese 39", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340039, f"Cheese 40", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340040, f"Cheese 41", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340041, f"Cheese 42", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340042, f"Cheese 43", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340043, f"Cheese 44", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340044, f"Cheese 45", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340045, f"Cheese 46", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340046, f"Cheese 47", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340047, f"Cheese 48", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340048, f"Cheese 49", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340049, f"Cheese 50", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340050, f"Cheese 51", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340051, f"Cheese 52", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340052, f"Cheese 53", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340053, f"Cheese 54", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340054, f"Cheese 55", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340055, f"Cheese 56", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340056, f"Cheese 57", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340057, f"Cheese 58", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340058, f"Cheese 59", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340059, f"Cheese 60", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340060, f"Cheese 61", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340061, f"Cheese 62", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340062, f"Cheese 63", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340063, f"Cheese 64", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340064, f"Cheese 65", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340065, f"Cheese 66", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340066, f"Cheese 67", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340067, f"Cheese 68", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340068, f"Cheese 69", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340069, f"Cheese 70", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340070, f"Cheese 71", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340071, f"Cheese 72", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340072, f"Cheese 73", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340073, f"Cheese 74", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340074, f"Cheese 75", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340075, f"Cheese 76", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340076, f"Cheese 77", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340077, f"Cheese 78", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340078, f"Cheese 79", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340079, f"Cheese 80", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340080, f"Cheese 81", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340081, f"Cheese 82", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340082, f"Cheese 83", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340083, f"Cheese 84", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340084, f"Cheese 85", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340085, f"Cheese 86", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340086, f"Cheese 87", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340087, f"Cheese 88", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340088, f"Cheese 89", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340089, f"Cheese 90", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340090, f"Cheese 91", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340091, f"Cheese 92", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340092, f"Cheese 93", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340093, f"Cheese 94", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340094, f"Cheese 95", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340095, f"Cheese 96", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340096, f"Cheese 97", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340097, f"Cheese 98", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340098, f"Cheese 99", f"Cheese", SkyrimLocationCategory.CHEESE),
    SkyrimLocationData(512340099, f"Cheese 100", f"Cheese", SkyrimLocationCategory.CHEESE)
],
}

location_dictionary: Dict[str, SkyrimLocationData] = {}
for location_table in location_tables.values():
    location_dictionary.update({location_data.name: location_data for location_data in location_table})
