import json
import os
from filehandler import FileHandler

fh = FileHandler()


class JsonHandler:

    def load_data(self):
        self.worlditems = fh.load_file('worlditems')
        self.currency = fh.load_file('currency')
        self.shops = fh.load_file('shops')
        self.charactersheet = fh.load_file('charactersheet')
        self.characterinventory = fh.load_file('characterinventory')
        self.inventory = fh.load_file('inventory')

    def show_shop_titles(self): # This function is for when you would like to display the titles in shops.json
        self.load_data()
        print_str = ""
        for title, value in self.shops.items():
            print_str += f"{title}\n"
            _ = value # this sets it to nothing and we have no problems in code
        return print_str

    def show_shop_stockid(self): # This function is for when you would like to display shop stock id in shops.json
        self.load_data()
        print_str = ""
        for title, value in self.shops.items():
            print_str += f"{title} -\n"
            for sid, items in value['Stock'].items():
                print_str += f"   **{sid}**\n"
                _ = items # this sets it to nothing and we have no problems in code
        return print_str

    def show_BuyStockMsgID(self): # This function is for when you would like to display all shop BuyStockMsgID under stock in shops.json
        self.load_data()
        print_str = ""
        for title, value in self.shops.items():
            _ = title
            # print_str += f"{title} -\n"
            for sid, items in value['Stock'].items():
                print_str += f"{items['BuyStockMsgID']},"
                _ = sid # this sets it to nothing and we have no problems in code
        return print_str

    def show_BuyStockMsgEmbed(self): # This function is for when you would like to display all shop BuyStockMsgEmbed under stock in shops.json
        self.load_data()
        print_str = ""
        for title, value in self.shops.items():
            _ = title
            # print_str += f"{title} -\n"
            for sid, items in value['Stock'].items():
                print_str += f"{items['BuyStockMsgEmbed']},"
                _ = sid # this sets it to nothing and we have no problems in code
        return print_str        

    def show_worlditem_titles(self): # This function is for when you would like to display the TITLES and VALUES in worlditems.json
        self.load_data()
        print_str = ""
        for title, value in self.worlditems.items():
            print_str += f"**{title}** - {value['ItemName']}\n"
            # _ = value # this sets it to nothing and we have no problems in code
        return print_str

    def show_currency_titles_values(self): # This function is for when you would like to display the TITLES and VALUES in worlditems.json
        self.load_data()
        print_str = ""
        for title, value in self.currency.items():
            print_str += f"**{title}** - {value['Character']}\n"
            # _ = value # this sets it to nothing and we have no problems in code
        return print_str

    def show_character_sheet_embed_ids(self): # This function is for when you would like to display all character sheet embed ID's in charactersheet.json
        self.load_data()
        print_str = ""
        for title, value in self.charactersheet.items():
            _ = title
            print_str += f"{value['Character Sheet Embed ID']},"
            # # print_str += f"{title} -\n"
            # for sid, items in value['Stock'].items():
            #     print_str += f"{items['BuyStockMsgID']},"
            #     _ = sid # this sets it to nothing and we have no problems in code
        return print_str

    def show_char_inv_worldids(self): # This function is for when you would like to display all World Items ID under Inventory in characterinventory.json
        self.load_data()
        print_str = ""
        for title, value in self.characterinventory.items():
            _ = title
            # print_str += f"{title} -\n"
            for sid, items in value['Inventory'].items():
                print_str += f"{items['WorldID']},"
                _ = sid # this sets it to nothing and we have no problems in code
        return print_str

# used to auto generate id in react buy
    def show_char_inv_numbers(self): # This function is for when you would like to display all Inventory IDS in characterinventory.json
        self.load_data()
        print_str = ""
        for title, value in self.characterinventory.items():
            _ = title
            # print_str += f"{title} -\n"
            for sid, items in value['Inventory'].items():
                print_str += f"{sid} "
                _ = items # this sets it to nothing and we have no problems in code
        return print_str

    def show_shop_stockid2(self): # This function is for when you would like to display shop stock id in shops.json
        self.load_data()
        print_str = ""
        for title, value in self.shops.items():
            _ = title
            # print_str += f"{title} -\n"
            for sid, items in value['Stock'].items():
                print_str += f"{sid} "
                _ = items # this sets it to nothing and we have no problems in code
        return print_str

    def show_worlditem_titles2(self): # This function is for when you would like to display the TITLES and in worlditems.json
        self.load_data()
        print_str = ""
        for title, value in self.worlditems.items():
            print_str += f"{title} "
            _ = value # this sets it to nothing and we have no problems in code
        return print_str

    def show_character_sheet_stats(self): # This function is for when you would like to display all character sheet stats categories in charactersheet.json
        self.load_data()
        print_str = ""
        for title, value in self.charactersheet.items():
            _ = title
            for sid, items in value['Character Sheet'].items():
                str_sid = str(sid)
                print_str += f"{str_sid},"
                _ = items # this sets it to nothing and we have no problems in code
        return print_str   

    def show_character_inventory_embed_ids(self): # This function is for when you would like to display all the character inventory embed IDs in characterinventory.json
        self.load_data()
        print_str = ""
        for title, value in self.characterinventory.items():
            _ = title
            # print_str += f"{title} -\n"
            for sid, items in value['Inventory'].items():
                print_str += f"{items['Character Inventory Embed']},"
                _ = sid # this sets it to nothing and we have no problems in code
        return print_str     

    def show_inv_ids(self): # This function is for when you would like to display all Inventory IDS in inventory.json
        self.load_data()
        print_str = ""
        for title, value in self.inventory.items():
            _ = value
            print_str += f"{title},"
            # for sid, items in value['Inventory'].items():
            #     print_str += f"{sid},"
            #     _ = items # this sets it to nothing and we have no problems in code
        return print_str

    def show_inv_titles_and_values(self): # This function is for when you would like to display the titles with the inventory names in inventory.json
        self.load_data()
        print_str = ""
        for title, value in self.inventory.items():
            print_str += f"**{title}** - {value['Inventory_Name']}\n"
        return print_str        

    def show_inventory_store_items_channel_ids(self): # This function is for when you would like list all the store-items channel ids in inventory.json
        self.load_data()
        print_str = ""
        for title, value in self.inventory.items():
            _ = title
            print_str += f"{value['Store_Items_Channel_ID']},"
        return print_str    

    def show_shared_inv_inv_worldids(self): # This function is for when you would like to display all World Items ID under Inventory in inventory.json
        self.load_data()
        print_str = ""
        for title, value in self.inventory.items():
            _ = title
            # print_str += f"{title} -\n"
            for sid, items in value['Inventory'].items():
                print_str += f"{items['WorldID']},"
                _ = sid # this sets it to nothing and we have no problems in code
        return print_str
        
    def show_shared_inv_inv_numbers(self): # This function is for when you would like to display all Inventory IDS in inventory.json
        self.load_data()
        print_str = ""
        for title, value in self.inventory.items():
            _ = title
            # print_str += f"{title} -\n"
            for sid, items in value['Inventory'].items():
                print_str += f"{sid} "
                _ = items # this sets it to nothing and we have no problems in code
        return print_str

    def show_inventory_inventory_embed_ids(self): # This function is for when you would like to display all the inventory inventory embed IDs in characterinventory.json
        self.load_data()
        print_str = ""
        for value in self.inventory.values():
            for items in value['Inventory'].values():
                print_str += f"{items['Character_Inventory_Embed']},"
        return print_str         




# Fjerne title
#     def show_inventory_inventory_embed_ids(self): # This function is for when you would like to display all the inventory inventory embed IDs in characterinventory.json
#         self.load_data()
#         print_str = ""
#         for value in self.inventory.values():
#             # print_str += f"{title} -\n"
#             for sid, items in value['Inventory'].items():
#                 print_str += f"{items['Character_Inventory_Embed']},"
#                 _ = sid # this sets it to nothing and we have no problems in code
#         return print_str         


# Fjerne value
#     def show_inventory_inventory_embed_ids(self): # This function is for when you would like to display all the inventory inventory embed IDs in characterinventory.json
#         self.load_data()
#         print_str = ""
#         for value in self.inventory.keys():
#             # print_str += f"{title} -\n"
#             for sid, items in value['Inventory'].items():
#                 print_str += f"{items['Character_Inventory_Embed']},"
#                 _ = sid # this sets it to nothing and we have no problems in code
#         return print_str    

