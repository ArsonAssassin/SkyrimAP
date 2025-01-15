from enum import IntEnum
from typing import NamedTuple
import random
from BaseClasses import Item


class SkyrimItemCategory(IntEnum):
    SKIP = 0,
    EVENT = 1,
    CHEESE = 2


class SkyrimItemData(NamedTuple):
    name: str
    skyrim_code: int
    category: SkyrimItemCategory


class SkyrimItem(Item):
    game: str = "Skyrim"

    @staticmethod
    def get_name_to_id() -> dict:
        base_id = 512340000
        return {item_data.name: (base_id + item_data.skyrim_code if item_data.skyrim_code is not None else None) for item_data in _all_items}

key_item_names = {
"Cheese"
}

_all_items = [SkyrimItemData(row[0], row[1], row[2]) for row in [    
   
    ("Cheese", 1000, SkyrimItemCategory.CHEESE),
]]

item_descriptions = {
}

item_dictionary = {item_data.name: item_data for item_data in _all_items}

def BuildItemPool(count, options):
    item_pool = []
    included_itemcount = 0

    if options.guaranteed_items.value:
        for item_name in options.guaranteed_items.value:
            item = item_dictionary[item_name]
            item_pool.append(item)
            included_itemcount = included_itemcount + 1
    remaining_count = count - included_itemcount
    
    filler_items = [item for item in _all_items if item.category not in [SkyrimItemCategory.EVENT, SkyrimItemCategory.KEY_ITEM]]

    for i in range(remaining_count):
        itemList = [item for item in filler_items]
        item = random.choice(itemList)
        item_pool.append(item)
    
    random.shuffle(item_pool)
    return item_pool
