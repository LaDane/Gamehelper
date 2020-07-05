import discord
import json
import asyncio
from discord.ext import commands
from filehandler import FileHandler
from jsonhandler import JsonHandler

fh = FileHandler()
jh = JsonHandler()



class ReactBuy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
        self.worlditems = fh.load_file('worlditems')
        self.currency = fh.load_file('currency')
        self.shops = fh.load_file('shops')
        self.charactersheet = fh.load_file('charactersheet')
        self.characterinventory = fh.load_file('characterinventory')

    def s_bsm_id(self):
        return jh.show_BuyStockMsgID()

    def s_c_i_wid(self):
        return jh.show_char_inv_worldids()

    def s_c_i_n(self):
        return jh.show_char_inv_numbers()

    def s_c_s_s(self):
        return jh.show_character_sheet_stats()

# Used to generate a new unique number from a list
    def Convert(self, string): 
        li = list(string.split(" ")) 
        return li


# Buy stock from shop inventory with "moneybag" reaction
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        self.load_data()
        buy_stock_msg_id = self.s_bsm_id()
        user_reaction_msg_id = payload.message_id

        guild = self.bot.get_guild(payload.guild_id)  # You need the guild to get the member who reacted
        member = guild.get_member(payload.user_id)  # the member who reacted to a role
        member_id = member.id # used to check if bot reacted
        botcheck = 698545737880961074 # used to check if bot reacted
        author_id = str(payload.user_id)


        if not payload.guild_id: # In this case, the reaction was added in a DM channel with the bot
            return
        if member_id == botcheck: # In this case, the bot reacted to a message
            return
        if str(user_reaction_msg_id) not in str(buy_stock_msg_id): # In this case, the reaction was given to a message not in BuyStockMsgID
            return 
        if str(user_reaction_msg_id) in str(buy_stock_msg_id): # In this case the reaction is given to a message in BuyStockMsgID

            reaction = str(payload.emoji.name)
            
            if reaction == "\U0001F4B0": # Moneybag emoji - :moneybag: 
                self.load_data()

                keys = []
                titles = []

                for title, value in self.shops.items():
                    for sid, items in value['Stock'].items():
                        if items['BuyStockMsgID'] == payload.message_id:
                            keys.append(sid)
                            titles.append(title)
                            break

                keys = ''.join(keys)                
                title = ''.join(titles)
                
                worldid = self.shops[title]['Stock'][keys]["WorldID"]
                guild = self.bot.get_guild(payload.guild_id)
                buy_channel_id = self.shops[title]['ShopBuyID']
                channel = guild.get_channel(buy_channel_id)
                message_id = self.shops[title]['Stock'][keys]["BuyStockMsgID"]
                user_msg = await channel.fetch_message(message_id)

                item_required_bag_slots = int(self.worlditems[worldid]['Weight'])
                current_used_bag_slots = self.characterinventory[author_id]['Used slots']
                available_bag_slots = self.characterinventory[author_id]['Bag slots']

                item_required_bag_slots += current_used_bag_slots
                new_used_bag_slots = item_required_bag_slots

# If not enough bag space : return
                if new_used_bag_slots > available_bag_slots:
                    channel = self.bot.get_channel(698671535606595595) # Change channel id to economy channel
                    await channel.send(f"**{member.nick}** does not have enough **bag space** to purchase **{self.worlditems[worldid]['ItemName']}** from shop owner **{self.shops[title]['ShopOwner']}**!")
                    return

                shops_currency = self.shops[title]['ShopCurrency']
                player_has_in_shops_currency = self.currency[author_id][shops_currency]
                cost_of_item = int(self.worlditems[worldid]['Value'])

# If not enough currency                
                if new_used_bag_slots <= available_bag_slots:

                    player_has_in_shops_currency -= cost_of_item
                    new_player_currency = player_has_in_shops_currency

                    if new_player_currency < 0:
                        channel = self.bot.get_channel(698671535606595595) # Change channel id to economy channel
                        await channel.send(f"**{member.nick}** does not have enough **{shops_currency}** to purchase **{self.worlditems[worldid]['ItemName']}** from shop owner **{self.shops[title]['ShopOwner']}**!")
                        return

                    if new_player_currency >= 0:
                        self.load_data()
# Player has succesfully purchased item                        
                        current_value = int(self.shops[title]['Stock'][keys]['Quantity'])
                        buy_one_from_stock = 1
                        if current_value == 0:
                            return                
                        current_value -= buy_one_from_stock

# Updating stock embed QUANTITY
                        stock_embed = discord.Embed(title=f"**{self.worlditems[worldid]['ItemName']}**", description=f"*{self.worlditems[worldid]['Description']}*", color=discord.Color.red())
                        stock_embed.set_image(url=f"{self.worlditems[worldid]['Picture']}")
                        stock_embed.set_footer(text=f"W-ID [{worldid}]\nSE-ID [{keys}]")
                        stock_embed.add_field(name="Stats", value=f"{self.worlditems[worldid]['StatsModifier']} {self.worlditems[worldid]['Stats']}", inline=False)
                        stock_embed.add_field(name="Type", value=f"{self.worlditems[worldid]['Type']}", inline=True)
                        stock_embed.add_field(name="Weight", value=f"{self.worlditems[worldid]['Weight']} slots")
                        stock_embed.add_field(name="Value", value=f"{self.worlditems[worldid]['Value']}")
                        stock_embed.add_field(name="Amount in stock", value=f"{self.shops[title]['Stock'][keys]['Quantity']}")

                        embed_fields = ["Stats", "Type", "Weight", "Value", "Amount in stock"]
                        word = "Amount in stock"
                        word_index = embed_fields.index(word)

                        stock_embed.set_field_at(word_index, name="Amount in stock", value=current_value)

                        channel = self.bot.get_channel(698671535606595595) # Change channel id to economy channel
                        await channel.send(f"**{member.nick}** has purchased **{self.worlditems[worldid]['ItemName']}** for **{cost_of_item} {shops_currency}** from shop owner **{self.shops[title]['ShopOwner']}**!")
                        

                        self.shops[title]["Stock"][keys]["Quantity"] = current_value
                        fh.save_file(self.shops, 'shops')
                        await user_msg.edit(embed=stock_embed)

# Updating players currency
                        currency_channel_id = self.currency[author_id]['Inventory Channel ID']
                        channel = guild.get_channel(currency_channel_id)
                        message_id = self.currency[author_id]['Currency Embed ID']
                        currency_user_msg = await channel.fetch_message(message_id)

                        currency_embed = discord.Embed(title=f"{member.nick}\'s coin bag.",color=0xffd700)
                        currency_embed.add_field(name="Kreditter", value=self.currency[author_id]["Kreditter"])
                        currency_embed.add_field(name="Imperille Kreditter", value=self.currency[author_id]["Imperille Kreditter"])
                        currency_embed.add_field(name="Skindene Sten", value=self.currency[author_id]["Skindene Sten"])

                        embed_fields = ["Kreditter", "Imperille Kreditter", "Skindene Sten"]
                        word = shops_currency
                        word_index = embed_fields.index(word)

                        currency_embed.set_field_at(word_index, name=shops_currency, value=new_player_currency)

                        self.currency[author_id][shops_currency] = new_player_currency
                        fh.save_file(self.currency, 'currency')
                        await currency_user_msg.edit(embed=currency_embed)


                        # char_inv_world_ids = self.s_c_i_wid()

# Update player bag space    
                        backpack_message_id = self.characterinventory[author_id]["Backpack Embed ID"]
                        backpack_user_msg = await channel.fetch_message(backpack_message_id)

                        backpack_embed = discord.Embed(title=f"{member.nick}\'s backpack",color=0x8B4513)
                        backpack_embed.add_field(name="Bag slots", value=f"{self.characterinventory[author_id]['Used slots']} / {self.characterinventory[author_id]['Bag slots']}", inline=False)

                        embed_fields = ["Bag slots"]
                        word = "Bag slots"
                        word_index = embed_fields.index(word)

                        backpack_embed.set_field_at(word_index, name="Bag slots", value=f"{new_used_bag_slots} / {self.characterinventory[author_id]['Bag slots']}")
                        self.characterinventory[author_id]["Used slots"] = new_used_bag_slots

                        fh.save_file(self.characterinventory, 'characterinventory')
                        await backpack_user_msg.edit(embed=backpack_embed)


# Adding item to players inventory
                        print_char_str = ""
                        for title, value in self.characterinventory.items():
                            for sid, items in value['Inventory'].items():
                                if author_id == title:
                                    # print(items['WorldID'])
                                    print_char_str += f"{items['WorldID']},"
                                    # break
                        

                        if str(worldid) not in str(print_char_str):
                            quantity = 1

                            inventory_embed = discord.Embed(title=f"**{self.worlditems[worldid]['ItemName']}**", description=f"*{self.worlditems[worldid]['Description']}*", color=discord.Color.red())
                            inventory_embed.set_image(url=f"{self.worlditems[worldid]['Picture']}")
                            inventory_embed.set_footer(text=f"W-ID [{worldid}]")
                            inventory_embed.add_field(name="Stats", value=f"{self.worlditems[worldid]['StatsModifier']} {self.worlditems[worldid]['Stats']}", inline=False)
                            inventory_embed.add_field(name="Type", value=f"{self.worlditems[worldid]['Type']}", inline=True)
                            inventory_embed.add_field(name="Weight", value=f"{self.worlditems[worldid]['Weight']} slots")
                            inventory_embed.add_field(name="Value", value=f"{self.worlditems[worldid]['Value']}")
                            inventory_embed.add_field(name="Amount in inventory", value=quantity)
                            char_inv_msg = await channel.send(embed=inventory_embed)
                            char_inv_msg_id  = char_inv_msg.id  

                            await asyncio.sleep(1)
                            await char_inv_msg.add_reaction(emoji='\U0001F6AE')     # Add put_litter_in_its_place reaction to message
                            await char_inv_msg.add_reaction(emoji='\U0001F4B5')     # Add dollar reaction to message   

# Generate new unique number from list CODE
                            chair_inv_numbers = self.s_c_i_n()
                            if len(chair_inv_numbers) == 0:
                                new_number = 0

                            if len(chair_inv_numbers) != 0:                    
                                chair_inv_numbers = chair_inv_numbers.strip(' ')
                                convert_chair_inv_numbers = self.Convert(chair_inv_numbers)

                                sorted(convert_chair_inv_numbers)
                                sorted(map(int,convert_chair_inv_numbers))
                                max(convert_chair_inv_numbers)
                                new_number = max(map(int,convert_chair_inv_numbers))

                            unique_new_number = int(new_number) + 1                            
# Generate code above REMEMBER def Convert at top!!!               
#               
                            unique_inv_number = unique_new_number
# Save inventory entry to characterinventory.json
                            self.characterinventory[author_id]["Inventory"][unique_inv_number] = {}
                            self.characterinventory[author_id]["Inventory"][unique_inv_number]["WorldID"] = worldid
                            self.characterinventory[author_id]["Inventory"][unique_inv_number]["Quantity"] = quantity                            
                            self.characterinventory[author_id]["Inventory"][unique_inv_number]["Character Inventory Embed"] = char_inv_msg_id
                            fh.save_file(self.characterinventory, 'characterinventory')              

# Check if player already has item in inventory
                        if str(worldid) in str(print_char_str):

                            unique_inv_number2 = []

                            for title, value in self.characterinventory.items():
                                for sid, items in value['Inventory'].items():
                                    if value['User'] == str(member):
                                        if items['WorldID'] == worldid:
                                            unique_inv_number2.append(sid)
                                            break

                            unique_inv_number2 = ''.join(unique_inv_number2)

                            amount_in_inventory = self.characterinventory[author_id]["Inventory"][unique_inv_number2]["Quantity"]
                            add_one_to_inventory = 1
                            amount_in_inventory += add_one_to_inventory

                            message_id = self.characterinventory[author_id]["Inventory"][unique_inv_number2]["Character Inventory Embed"]
                            user_msg = await channel.fetch_message(message_id)

                            inventory_embed = discord.Embed(title=f"**{self.worlditems[worldid]['ItemName']}**", description=f"*{self.worlditems[worldid]['Description']}*", color=discord.Color.red())
                            inventory_embed.set_image(url=f"{self.worlditems[worldid]['Picture']}")
                            inventory_embed.set_footer(text=f"W-ID [{worldid}]")
                            inventory_embed.add_field(name="Stats", value=f"{self.worlditems[worldid]['StatsModifier']} {self.worlditems[worldid]['Stats']}", inline=False)
                            inventory_embed.add_field(name="Type", value=f"{self.worlditems[worldid]['Type']}", inline=True)
                            inventory_embed.add_field(name="Weight", value=f"{self.worlditems[worldid]['Weight']} slots")
                            inventory_embed.add_field(name="Value", value=f"{self.worlditems[worldid]['Value']}")
                            inventory_embed.add_field(name="Amount in inventory", value=f"{self.characterinventory[author_id]['Inventory'][unique_inv_number2]['Quantity']}")

                            embed_fields = ["Stats", "Type", "Weight", "Value", "Amount in inventory"]
                            word = "Amount in inventory"
                            word_index = embed_fields.index(word)

                            inventory_embed.set_field_at(word_index, name="Amount in inventory", value=amount_in_inventory)

                            self.characterinventory[author_id]["Inventory"][unique_inv_number2]["Quantity"] = amount_in_inventory
                            fh.save_file(self.characterinventory, 'characterinventory')  
                            await user_msg.edit(embed=inventory_embed)
                            return

# Update player character sheet

                        item_stat = self.worlditems[worldid]['Stats']
                        item_stat_field_name = f"**{self.worlditems[worldid]['Stats']}**"
                        item_stat_modifier_from_worditems = self.worlditems[worldid]['StatsModifier']
                        
                        

    # If item_stat is none : return
                        if self.worlditems[worldid]['Stats'] == "None":
                            return

    # If item_stat is not in character_sheet list : return ( stat is = CUSTOM STAT )
                        character_sheet_available_stats = self.s_c_s_s()

                        if item_stat not in character_sheet_available_stats:
                            return


                        item_stat_modifier_without_plus = (item_stat_modifier_from_worditems[1:])
                        item_stat_modifier = int(item_stat_modifier_without_plus) 

    # If item_stat is Bag slots   
                        if self.worlditems[worldid]['Stats'] == "Bag slots": 
                            
                            self.load_data()
                            backpack_current_space = int(self.characterinventory[author_id]['Bag slots'])
                            backpack_current_space += item_stat_modifier
                            upgraded_backpack_space = backpack_current_space

                            backpack_message_id = self.characterinventory[author_id]["Backpack Embed ID"]
                            backpack_user_msg = await channel.fetch_message(backpack_message_id)

                            backpack_embed = discord.Embed(title=f"{member.nick}\'s backpack",color=0x8B4513)
                            backpack_embed.add_field(name="Bag slots", value=f"{self.characterinventory[author_id]['Used slots']} / {self.characterinventory[author_id]['Bag slots']}", inline=False)

                            embed_fields = ["Bag slots"]
                            word = "Bag slots"
                            word_index = embed_fields.index(word)

                            backpack_embed.set_field_at(word_index, name="Bag slots", value=f"{self.characterinventory[author_id]['Used slots']} / {upgraded_backpack_space}")
                            self.characterinventory[author_id]["Bag slots"] = upgraded_backpack_space

                            fh.save_file(self.characterinventory, 'characterinventory')
                            await backpack_user_msg.edit(embed=backpack_embed)

                            return                   

# Upgrade character sheet
                        # CHANGE item_stat TO INCLUDE _BONUS
                        item_stat_bonus = f"{item_stat}_Bonus"

                        character_sheet_current_skill = int(self.charactersheet[author_id]['Character Sheet'][item_stat_bonus])                        
                        character_sheet_current_skill += item_stat_modifier
                        upgraded_character_sheet_skill = character_sheet_current_skill



                        character_sheet_channel_id = self.charactersheet[author_id]["Character Sheet Channel ID"]
                        channel = guild.get_channel(character_sheet_channel_id)
                        message_id = self.charactersheet[author_id]["Character Sheet Embed ID"]
                        character_sheet_user_msg = await channel.fetch_message(message_id)      

                        cs_embed = discord.Embed(title=f"**{self.charactersheet[author_id]['Character']}'s character sheet**", description=f"*React with :bell: to level up*", color=0x303136)
                        cs_embed.add_field(name="**Level**", value=f"{self.charactersheet[author_id]['Character Sheet']['Level']}")
                        cs_embed.add_field(name="**\u200b**", value=f"__**Kompetencer**__", inline=False)
                        cs_embed.add_field(name="**Styrke**", value=f"{self.charactersheet[author_id]['Character Sheet']['Styrke']}", inline=True)
                        cs_embed.add_field(name="**Udholdenhed**", value=f"{self.charactersheet[author_id]['Character Sheet']['Udholdenhed']}")
                        cs_embed.add_field(name="**Intelligens**", value=f"{self.charactersheet[author_id]['Character Sheet']['Intelligens']}")
                        cs_embed.add_field(name="**Finesse**", value=f"{self.charactersheet[author_id]['Character Sheet']['Finesse']}")
                        cs_embed.add_field(name="**Perception**", value=f"{self.charactersheet[author_id]['Character Sheet']['Perception']}")
                        cs_embed.add_field(name="**Karisma**", value=f"{self.charactersheet[author_id]['Character Sheet']['Karisma']}")
                        cs_embed.add_field(name="**Initiativ**", value=f"{self.charactersheet[author_id]['Character Sheet']['Initiativ']}\n \n__**Kamp Evner**__", inline=False)

                        cs_embed.add_field(name="**Nærkamp**", value=f"{self.charactersheet[author_id]['Character Sheet']['Nærkamp']} *(+{self.charactersheet[author_id]['Character Sheet']['Nærkamp_Bonus']})*", inline=True)
                        cs_embed.add_field(name="**Kaste/Strenge Våben**", value=f"{self.charactersheet[author_id]['Character Sheet']['Kaste_Strenge_våben']} *(+{self.charactersheet[author_id]['Character Sheet']['Kaste_Strenge_våben_Bonus']})*")
                        cs_embed.add_field(name="**Skydevåben**", value=f"{self.charactersheet[author_id]['Character Sheet']['Skydevåben']} *(+{self.charactersheet[author_id]['Character Sheet']['Skydevåben_Bonus']})*")
                        cs_embed.add_field(name="**Snig**", value=f"{self.charactersheet[author_id]['Character Sheet']['Snig']} *(+{self.charactersheet[author_id]['Character Sheet']['Snig_Bonus']})*\n \n__**Sociale Evner**__", inline=False)

                        cs_embed.add_field(name="**Smigre**", value=f"{self.charactersheet[author_id]['Character Sheet']['Smigre']} *(+{self.charactersheet[author_id]['Character Sheet']['Smigre_Bonus']})*", inline=True)
                        cs_embed.add_field(name="**Løgn**", value=f"{self.charactersheet[author_id]['Character Sheet']['Løgn']} *(+{self.charactersheet[author_id]['Character Sheet']['Løgn_Bonus']})*")
                        cs_embed.add_field(name="**Intimiderer**", value=f"{self.charactersheet[author_id]['Character Sheet']['Intimiderer']} *(+{self.charactersheet[author_id]['Character Sheet']['Intimiderer_Bonus']})*")
                        cs_embed.add_field(name="**Handel**", value=f"{self.charactersheet[author_id]['Character Sheet']['Handel']} *(+{self.charactersheet[author_id]['Character Sheet']['Handel_Bonus']})*\n \n__**Håndværks Evner**__", inline=False)

                        cs_embed.add_field(name="**Reparation**", value=f"{self.charactersheet[author_id]['Character Sheet']['Reparation']} *(+{self.charactersheet[author_id]['Character Sheet']['Reparation_Bonus']})*", inline=True)
                        cs_embed.add_field(name="**Fælder**", value=f"{self.charactersheet[author_id]['Character Sheet']['Fælder']} *(+{self.charactersheet[author_id]['Character Sheet']['Fælder_Bonus']})*")
                        cs_embed.add_field(name="**Overlevelse**", value=f"{self.charactersheet[author_id]['Character Sheet']['Overlevelse']} *(+{self.charactersheet[author_id]['Character Sheet']['Overlevelse_Bonus']})*")
                        cs_embed.add_field(name="**Håndarbejde**", value=f"{self.charactersheet[author_id]['Character Sheet']['Håndarbejde']} *(+{self.charactersheet[author_id]['Character Sheet']['Håndarbejde_Bonus']})*\n \n__**Esoteriske Evner**__", inline=False)

                        cs_embed.add_field(name="**Videnskab**", value=f"{self.charactersheet[author_id]['Character Sheet']['Videnskab']} *(+{self.charactersheet[author_id]['Character Sheet']['Videnskab_Bonus']})*", inline=True)
                        cs_embed.add_field(name="**Alkymi**", value=f"{self.charactersheet[author_id]['Character Sheet']['Alkymi']} *(+{self.charactersheet[author_id]['Character Sheet']['Alkymi_Bonus']})*")
                        cs_embed.add_field(name="**Lægevidenskab**", value=f"{self.charactersheet[author_id]['Character Sheet']['Lægevidenskab']} *(+{self.charactersheet[author_id]['Character Sheet']['Lægevidenskab_Bonus']})*")
                        cs_embed.add_field(name="**Historie**", value=f"{self.charactersheet[author_id]['Character Sheet']['Historie']} *(+{self.charactersheet[author_id]['Character Sheet']['Historie_Bonus']})*") 

                        embed_fields = ["**Level**", "**\u200b**", "**Styrke**", "**Udholdenhed**", "**Intelligens**", "**Finesse**", "**Perception**", "**Karisma**", "**Initiativ**", "**Nærkamp**", "**Kaste/Strenge Våben**", "**Skydevåben**", "**Snig**", "**Smigre**", "**Løgn**", "**Intimiderer**", "**Handel**", "**Reparation**", "**Fælder**", "**Overlevelse**", "**Håndarbejde**", "**Videnskab**", "**Alkymi**", "**Lægevidenskab**", "**Historie**", ]
                        word = item_stat_field_name
                        word_index = embed_fields.index(word) 

                        cs_embed.set_field_at(word_index, name=item_stat_field_name, value=f"{self.charactersheet[author_id]['Character Sheet'][item_stat]} *(+{upgraded_character_sheet_skill})*")    

                        self.charactersheet[author_id]['Character Sheet'][item_stat_bonus] = upgraded_character_sheet_skill  
                        fh.save_file(self.charactersheet, 'charactersheet')     

                        await character_sheet_user_msg.edit(embed=cs_embed)

        else:
            print("something failed in detecting reaction :o")


def setup(bot):
    bot.add_cog(ReactBuy(bot))

