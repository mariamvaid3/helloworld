#Mariam Vaid
#1477614
    
    def servi_past(self):
        # past service date inventory part c
        with open('PastServiceDateInventory(1).csv', 'r') as mynewfile:
            items = self.item_list
        mykeys = sorted(items.keys(), key=lambda s: datetime.strptime(items[s]['date_service'], "%m/%d/%y").date(), reverse=True)
        for iteming in mykeys:
            id = iteming
            name_first = items[iteming]['manufacturing']
            item_price = items[iteming]['item_price']
            item_type = items[iteming]['item_type']
            date_service = items[iteming]['date_service']
            item_damaged = items[iteming]['item_damaged']
            todaydate = datetime.now().date()
            serv_expire = datetime.strptime(date_service, "%m/%d/%y").date()
            expire = serv_expire < todaydate
            if expire:
                mynewfile.write('{},{},{},{},{}\n'.format(id, name_first, item_price, item_type, date_service, item_damaged))
