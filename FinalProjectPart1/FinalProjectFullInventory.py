# Mariam Vaid
# 1477614

import csv
from datetime import datetime

class Inventory_Output:
    def __init__(self, item_list):
        self.item_list = item_list
    def full_inven(self):
        # full inventory part a
        with open('FullInventory(1).csv', 'r') as mynewfile:
            items = self.item_list
            mykeys = sorted(items.keys(), key=lambda s: items[s]['manufacturing'])
            for iteming in mykeys:
                id = iteming
                name_first = items[iteming]['manufacturing']
                item_type = items[iteming]['item_type']
                item_price = items[iteming]['item_price']
                date_service = items[iteming]['date_service']
                item_damaged = items[iteming]['item_damaged']
                mynewfile.write('{},{},{},{},{},{}\n'.format(id,name_first,item_type, item_price,date_service,item_damaged))
