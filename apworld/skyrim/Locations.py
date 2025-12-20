from enum import IntEnum
from typing import Optional, NamedTuple, Dict

from BaseClasses import Location, Region
from .Items import SkyrimItem

class SkyrimLocationCategory(IntEnum):
    SKIP = 0,
    EVENT = 1,
    MAIN_QUEST = 2


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
           "Main Quest"
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
"Main Quest": [
    SkyrimLocationData(512340000, f"Unbound", f"Potion of Vigorous Healing", SkyrimLocationCategory.MAIN_QUEST),
    SkyrimLocationData(512340001, f"Before the Storm", f"Potion of Vigorous Healing", SkyrimLocationCategory.MAIN_QUEST),
    SkyrimLocationData(512340002, f"Bleak Falls Barrow", f"Potion of Vigorous Healing", SkyrimLocationCategory.MAIN_QUEST),
    SkyrimLocationData(512340003, f"Dragon Rising", f"Potion of Vigorous Healing", SkyrimLocationCategory.MAIN_QUEST),
    SkyrimLocationData(512340004, f"The Way of the Voice", f"Potion of Vigorous Healing", SkyrimLocationCategory.MAIN_QUEST),
    SkyrimLocationData(512340005, f"The Horn of Jurgen Windcaller", f"Potion of Vigorous Healing", SkyrimLocationCategory.MAIN_QUEST),
    SkyrimLocationData(512340006, f"A Blade in the Dark", f"Potion of Vigorous Healing", SkyrimLocationCategory.MAIN_QUEST),
    SkyrimLocationData(512340007, f"Diplomatic Immunity", f"Potion of Vigorous Healing", SkyrimLocationCategory.MAIN_QUEST),
    SkyrimLocationData(512340008, f"Find the Thalmor Assassin", f"Potion of Vigorous Healing", SkyrimLocationCategory.MAIN_QUEST),
    SkyrimLocationData(512340009, f"A Cornered Rat", f"Potion of Vigorous Healing", SkyrimLocationCategory.MAIN_QUEST),
    SkyrimLocationData(512340010, f"Alduin's Wall", f"Potion of Vigorous Healing", SkyrimLocationCategory.MAIN_QUEST),
    SkyrimLocationData(512340011, f"The Throat of the World", f"Potion of Vigorous Healing", SkyrimLocationCategory.MAIN_QUEST),
    SkyrimLocationData(512340012, f"Elder Knowledge", f"Potion of Vigorous Healing", SkyrimLocationCategory.MAIN_QUEST),
    SkyrimLocationData(512340013, f"Alduin's Bane", f"Potion of Vigorous Healing", SkyrimLocationCategory.MAIN_QUEST),
    SkyrimLocationData(512340014, f"The Fallen", f"Potion of Vigorous Healing", SkyrimLocationCategory.MAIN_QUEST),
    SkyrimLocationData(512340015, f"Season Unending", f"Potion of Vigorous Healing", SkyrimLocationCategory.MAIN_QUEST),
    SkyrimLocationData(512340016, f"Paarthurnax", f"Potion of Vigorous Healing", SkyrimLocationCategory.MAIN_QUEST),
    SkyrimLocationData(512340017, f"The World-Eater's Eyrie", f"Potion of Vigorous Healing", SkyrimLocationCategory.MAIN_QUEST),
    SkyrimLocationData(512340018, f"Sovngarde", f"Potion of Vigorous Healing", SkyrimLocationCategory.MAIN_QUEST),
    SkyrimLocationData(512340019, f"Dragonslayer", f"Potion of Vigorous Healing", SkyrimLocationCategory.MAIN_QUEST),
],
}

location_dictionary: Dict[str, SkyrimLocationData] = {}
for location_table in location_tables.values():
    location_dictionary.update({location_data.name: location_data for location_data in location_table})
