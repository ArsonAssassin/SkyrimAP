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
# Last id used = 714
location_tables = {
"Cheese": [

],
}

location_dictionary: Dict[str, SkyrimLocationData] = {}
for location_table in location_tables.values():
    location_dictionary.update({location_data.name: location_data for location_data in location_table})
