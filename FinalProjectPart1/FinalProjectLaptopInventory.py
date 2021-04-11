    
   #Mariam Vaid 
   # 1477614
    
    def my_type(self):
        # item type inventory list part b
        with open('LaptopInventory(1).csv', 'r') as mynewfile:
            items = self.item_list
        types = []
        mykeys = sorted(items.keys())
        for iteming in items:
            item_type = items[iteming]['item_type']
            if item_type not in types:
                types.append(item_type)
        for type in types:
            name_file = type.capitalize() + 'FullInventory(1).csv'
            id = iteming
            name_first = items[iteming]['manufacturing']
            item_price = items[iteming]['item_price']
            item_type = items[iteming]['item_type']
            date_service = items[iteming]['date_service']
            item_damaged = items[iteming]['item_damaged']
            if type == item_type:
                mynewfile.write('{},{},{},{},{}\n'.format(id,name_first,item_price,date_service,item_damaged))
