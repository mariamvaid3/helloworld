#Mariam Vaid
#1477614
    
    
    def damage(self):
        # damaged inventory part d
        with open('DamagedInventory(1).csv', 'r') as myfile:
            items = self.item_list
        mykeys = sorted(items.keys(), key=lambda s: items[s]['item_price'], reverse=True)
        for iteming in mykeys:
            id = iteming
            name_first = items[iteming]['manufacturing']
            item_type = items[iteming]['item_type']
            item_price = items[iteming]['item_price']
            date_service = items[iteming]['date_service']
            item_damaged = items[iteming]['item_damaged']
            if item_damaged:
                myfile.write('{},{},{},{},{}\n'.format(id, name_first, item_price, item_type, date_service))
