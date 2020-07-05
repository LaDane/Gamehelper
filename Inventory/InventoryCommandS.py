import discord
import json
import asyncio
from discord.ext import commands
from filehandler import FileHandler
from jsonhandler import JsonHandler

jh = JsonHandler()
fh = FileHandler()


class InventoryCommandS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
        self.currency = fh.load_file('currency')
        self.inventory = fh.load_file('inventory')
        self.characterinventory = fh.load_file('characterinventory')
        self.worlditems = fh.load_file('worlditems')
        self.charactersheet  = fh.load_file('charactersheet')

    def s_i_s_i_c_ids(self):
        return jh.show_inventory_store_items_channel_ids()

    def s_c_i_w_ids(self):
        return jh.show_char_inv_worldids()

    def s_c_s_s(self):
        return jh.show_character_sheet_stats()

    def s_s_i_i_wids(self):
        return jh.show_shared_inv_inv_worldids()

    def s_s_i_i_n(self):
        return jh.show_shared_inv_inv_numbers()

# Used to generate a new unique number from a list
    def Convert(self, string): 
        li = list(string.split(" ")) 
        return li
    

# store items in shared inventory
    @commands.command()
    async def s(self, ctx, item, amount: int = None):
        invetory_storeitems_channel_ids = self.s_i_s_i_c_ids()
        if str(ctx.channel.id) in str(invetory_storeitems_channel_ids):
            channel = ctx.channel
            channel_id = channel.id
            await channel.purge(limit=1)
            self.load_data()

            amount = amount if not None else amount
            member = ctx.author
            member_id = str(member.id)

            if not member_id in self.currency:
                await ctx.send("Member doesnt have a coin bag")

            char_inv_world_ids = self.s_c_i_w_ids()

# THE ITEM IS NOT A WORLD ITEM            
            if str(item) not in str(char_inv_world_ids):
                if str(item) == "k":
                    currency = "Kreditter"

                if str(item) == "ik":
                    currency = "Imperille Kreditter"

                if str(item) == "ss":
                    currency = "Skindene Sten"

                for title, value in self.currency.items():                          # for players coing bag
                    _ = value
                    if title == member_id:
                        inventory_channel_id = self.currency[member_id]['Inventory Channel ID']
                        embed_id = self.currency[member_id]['Currency Embed ID']
                        # break

                for title2, value2 in self.inventory.items():                       # for shared inventory coin bag
                    if value2['Store_Items_Channel_ID'] == channel_id:
                        store_items_channel_id = self.inventory[title2]['Store_Items_Channel_ID']
                        shared_inventory_id = self.inventory[title2]['Inventory_Channel_ID']
                        inventory_id = title2
                        # break

                guild = self.bot.get_guild(698522830525956097) # DnD Vandvejen discord ID
                channel = guild.get_channel(inventory_channel_id)
                user_msg = await channel.fetch_message(embed_id)

                if self.currency[member_id][currency] < amount:
                    await ctx.send(f"{member.nick} does not have enough {currency} to store in this inventory")
                    await asyncio.sleep(2)
                    channel = guild.get_channel(store_items_channel_id)
                    await channel.purge(limit=1)
                    return
                else:
                    self.currency[member_id][currency] -= amount
                    self.inventory[inventory_id][currency] += amount

# Update players coin bag
                    current_value = int(self.currency[member_id][currency])

                    embed_fields = ["Kreditter", "Imperille Kreditter", "Skindene Sten"]
                    word = currency
                    word_index = embed_fields.index(word)

                    currency_embed = discord.Embed(title=f"{member.nick}\'s coin bag.",color=0xffd700)
                    currency_embed.add_field(name="Kreditter", value=self.currency[member_id]["Kreditter"])
                    currency_embed.add_field(name="Imperille Kreditter", value=self.currency[member_id]["Imperille Kreditter"])
                    currency_embed.add_field(name="Skindene Sten", value=self.currency[member_id]["Skindene Sten"])

                    currency_embed.set_field_at(word_index, name=currency, value=current_value)
                    await user_msg.edit(embed=currency_embed)
                    
# Update shared inventory coin bag                    
                    channel = guild.get_channel(shared_inventory_id)
                    shared_items_currency_embed_id = self.inventory[inventory_id]['Currency_Embed_ID']
                    user_msg = await channel.fetch_message(shared_items_currency_embed_id)

                    current_value = int(self.inventory[inventory_id][currency])

                    embed_fields = ["Kreditter", "Imperille Kreditter", "Skindene Sten"]
                    word = currency
                    word_index = embed_fields.index(word)

                    currency_embed = discord.Embed(title=f"{self.inventory[inventory_id]['Inventory_Name']}\'s coin bag.",color=0xffd700)
                    currency_embed.add_field(name="Kreditter", value=self.inventory[inventory_id]["Kreditter"])
                    currency_embed.add_field(name="Imperille Kreditter", value=self.inventory[inventory_id]["Imperille Kreditter"])
                    currency_embed.add_field(name="Skindene Sten", value=self.inventory[inventory_id]["Skindene Sten"])

                    currency_embed.set_field_at(word_index, name=currency, value=current_value)
                    await user_msg.edit(embed=currency_embed) 

                    fh.save_file(self.currency, 'currency')
                    fh.save_file(self.inventory, 'inventory')

                    await ctx.send(f"{member.nick} has stored {amount} {currency} in this inventory.")
                    await asyncio.sleep(2)
                    channel = guild.get_channel(store_items_channel_id)
                    await channel.purge(limit=1)
                    channel = guild.get_channel(698671535606595595) # economy channel id
                    await channel.send(f"**{member.nick}** has stored **{amount} {currency}** in **{self.inventory[inventory_id]['Inventory_Name']}'s** inventory!")
                    return


# THE ITEM IS A WORLD ITEM                
            if str(item) in str(char_inv_world_ids):
                worldid = item
                guild = self.bot.get_guild(698522830525956097)
                author_id = member_id

                titles = []
                sids = []
                titles2 = []

                for title, value in self.characterinventory.items():
                    for sid, items in value['Inventory'].items():
                        if value['User'] == str(member):
                            if items['WorldID'] == worldid:
                                titles.append(title)
                                sids.append(sid)
                                break

                for title2, value2 in self.inventory.items():
                    if value2['Store_Items_Channel_ID'] == channel_id:
                        titles2.append(title2)
                        break

                title = ''.join(titles)
                sid = ''.join(sids)
                title2 = ''.join(titles2)

                worldid = self.characterinventory[title]['Inventory'][sid]["WorldID"]
                shared_items_channel_id = self.inventory[title2]['Store_Items_Channel_ID']
                inventory_channel_id = self.characterinventory[title]['inventory Channel ID']
                inventory_channel = guild.get_channel(inventory_channel_id)
                message_id_embed = self.characterinventory[title]['Inventory'][sid]["Character Inventory Embed"]

# players bag slots
                item_required_bag_slots = int(self.worlditems[worldid]['Weight'])
                current_used_bag_slots = self.characterinventory[author_id]['Used slots']

# shared inventory bag slots
                shared_inventory_used_bag_slots = self.inventory[title2]['Used_Slots']
                shared_inventory_available_bag_slots = int(self.inventory[title2]['Bag_Slots'])

# calculate player bag space
                current_used_bag_slots -= item_required_bag_slots
                new_used_bag_slots = current_used_bag_slots 

# calculate shared inventory bag space
                shared_inventory_used_bag_slots += item_required_bag_slots
                new_shared_inventory_used_bag_slots = shared_inventory_used_bag_slots

# If not enough storage space in shared inventory 
                shared_items_channel = guild.get_channel(shared_items_channel_id)
                if new_shared_inventory_used_bag_slots > shared_inventory_available_bag_slots:
                    await shared_items_channel.send("There's not enough space in this inventory to store the selected item!")
                    await asyncio.sleep(2)
                    await shared_items_channel.purge(limit=1)
                    return

# Update player bag space 
                backpack_message_id = self.characterinventory[author_id]["Backpack Embed ID"]
                backpack_user_msg = await inventory_channel.fetch_message(backpack_message_id)

                backpack_embed = discord.Embed(title=f"{member.nick}\'s backpack",color=0x8B4513)
                backpack_embed.add_field(name="Bag slots", value=f"{self.characterinventory[author_id]['Used slots']} / {self.characterinventory[author_id]['Bag slots']}", inline=False)

                embed_fields = ["Bag slots"]
                word = "Bag slots"
                word_index = embed_fields.index(word)

                backpack_embed.set_field_at(word_index, name="Bag slots", value=f"{new_used_bag_slots} / {self.characterinventory[author_id]['Bag slots']}")
                self.characterinventory[author_id]["Used slots"] = new_used_bag_slots

                fh.save_file(self.characterinventory, 'characterinventory')
                await backpack_user_msg.edit(embed=backpack_embed)

# change amount in inventory
                unique_inv_number2 = []

                for title, value in self.characterinventory.items():
                    for sid, items in value['Inventory'].items():
                        if value['User'] == str(member):
                            if items['WorldID'] == worldid:
                                unique_inv_number2.append(sid)
                                break

                unique_inv_number2 = ''.join(unique_inv_number2)

                amount_in_inventory = self.characterinventory[author_id]["Inventory"][unique_inv_number2]["Quantity"]
                remove_one_to_inventory = 1
                amount_in_inventory -= remove_one_to_inventory        

# if more than 1 left in inventory
                if amount_in_inventory >= 1:
                    
                    message_id = self.characterinventory[author_id]["Inventory"][unique_inv_number2]["Character Inventory Embed"]
                    channel = guild.get_channel(inventory_channel_id)
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

# if 0 left in inventory
# Delete inventory embed
                if amount_in_inventory <= 0:
                    # msg_id = self.characterinventory[author_id]["Inventory"][unique_inv_number2]["Character Inventory Embed"]
                    # channel = self.bot.get_channel(698570643976880260) # Channel id of "items-in-world"
                    try:
                        msg = await inventory_channel.fetch_message(message_id_embed)
                        await msg.delete()
                    except:
                        print("Item has no message in channel: items-in-world")


                    del self.characterinventory[author_id]["Inventory"][unique_inv_number2]
                    fh.save_file(self.characterinventory, 'characterinventory') 



                    item_stat = self.worlditems[worldid]['Stats']
                    item_stat_field_name = f"**{self.worlditems[worldid]['Stats']}**"
                    item_stat_modifier_from_worditems = self.worlditems[worldid]['StatsModifier']                    

# If item_stat is none : return
                    if self.worlditems[worldid]['Stats'] == "None":
                        print("Stats are none")                    

# If item_stat is not in character_sheet list : return ( stat is = CUSTOM STAT )
                    character_sheet_available_stats = self.s_c_s_s()

                    if item_stat not in character_sheet_available_stats:
                        print("Stats are custom")  

# If item_stat is Bag slots   
                    # item_stat_modifier_without_plus = (item_stat_modifier_from_worditems[1:])
                    # item_stat_modifier = int(item_stat_modifier_without_plus) 

                    if self.worlditems[worldid]['Stats'] == "Bag slots": 

                        item_stat_modifier_without_plus = (item_stat_modifier_from_worditems[1:])
                        item_stat_modifier = int(item_stat_modifier_without_plus) 
                        
                        self.load_data()
                        backpack_current_space = int(self.characterinventory[author_id]['Bag slots'])
                        backpack_current_space -= item_stat_modifier
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

# Downgrade character sheet
                    if item_stat in character_sheet_available_stats:     
                        item_stat_bonus = f"{item_stat}_Bonus"

                        item_stat_modifier_without_plus = (item_stat_modifier_from_worditems[1:])
                        item_stat_modifier = int(item_stat_modifier_without_plus)

                        character_sheet_current_skill = int(self.charactersheet[author_id]['Character Sheet'][item_stat_bonus])                        
                        character_sheet_current_skill -= item_stat_modifier
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

# Adding item to shared inventory
                shared_inventory_inventory_channel_id = self.inventory[title2]['Inventory_Channel_ID']
                shared_inventory_inventory_channel = guild.get_channel(shared_inventory_inventory_channel_id)

                # shared_inv_inv_worldids = self.s_s_i_i_wids()

                shared_inv_inv_worldids = ""
                for title, value in self.inventory.items():                            
                    for sid, items in value['Inventory'].items():
                        if value['Store_Items_Channel_ID'] == channel_id:
                            # print(items['WorldID'])
                            shared_inv_inv_worldids += f"{items['WorldID']},"
                            # break

# If item is not already in shared inventory
                if str(worldid) not in str(shared_inv_inv_worldids):
                    quantity = 1

                    shared_inventory_embed = discord.Embed(title=f"**{self.worlditems[worldid]['ItemName']}**", description=f"*{self.worlditems[worldid]['Description']}*", color=discord.Color.red())
                    shared_inventory_embed.set_image(url=f"{self.worlditems[worldid]['Picture']}")
                    shared_inventory_embed.set_footer(text=f"W-ID [{worldid}]")
                    shared_inventory_embed.add_field(name="Stats", value=f"{self.worlditems[worldid]['StatsModifier']} {self.worlditems[worldid]['Stats']}", inline=False)
                    shared_inventory_embed.add_field(name="Type", value=f"{self.worlditems[worldid]['Type']}", inline=True)
                    shared_inventory_embed.add_field(name="Weight", value=f"{self.worlditems[worldid]['Weight']} slots")
                    shared_inventory_embed.add_field(name="Value", value=f"{self.worlditems[worldid]['Value']}")
                    shared_inventory_embed.add_field(name="Amount in inventory", value=quantity)
                    shared_inv_msg = await shared_inventory_inventory_channel.send(embed=shared_inventory_embed)
                    shared_inv_msg_id  = shared_inv_msg.id  

                    await asyncio.sleep(1)
                    await shared_inv_msg.add_reaction(emoji='\U0001F392')     # Add school_satchel reaction to message


# Generate new unique number from list CODE
                    chair_inv_numbers = self.s_s_i_i_n()
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

                    unique_inv_number = unique_new_number

    # Save inventory entry to inventory.json
                    self.inventory[title2]['Inventory'][unique_inv_number] = {}
                    self.inventory[title2]['Inventory'][unique_inv_number]['WorldID'] = worldid
                    self.inventory[title2]['Inventory'][unique_inv_number]['Quantity'] = quantity
                    self.inventory[title2]['Inventory'][unique_inv_number]['Character_Inventory_Embed'] = shared_inv_msg_id
                    fh.save_file(self.inventory, 'inventory')

# If item is already in shared inventory
                if str(worldid) in str(shared_inv_inv_worldids):

                    unique_inv_number2 = []

                    for title, value in self.inventory.items():
                        for sid, items in value['Inventory'].items():
                            if value['Store_Items_Channel_ID'] == channel_id:
                                if items['WorldID'] == worldid:
                                    unique_inv_number2 = sid
                                    break

                    unique_inv_number2 = ''.join(unique_inv_number2)
                    
                    amount_in_inventory = self.inventory[title2]["Inventory"][unique_inv_number2]["Quantity"]
                    add_one_to_inventory = 1
                    amount_in_inventory += add_one_to_inventory

                    message_id = self.inventory[title2]["Inventory"][unique_inv_number2]["Character_Inventory_Embed"]
                    user_msg = await shared_inventory_inventory_channel.fetch_message(message_id)

                    shared_inventory_embed2 = discord.Embed(title=f"**{self.worlditems[worldid]['ItemName']}**", description=f"*{self.worlditems[worldid]['Description']}*", color=discord.Color.red())
                    shared_inventory_embed2.set_image(url=f"{self.worlditems[worldid]['Picture']}")
                    shared_inventory_embed2.set_footer(text=f"W-ID [{worldid}]")
                    shared_inventory_embed2.add_field(name="Stats", value=f"{self.worlditems[worldid]['StatsModifier']} {self.worlditems[worldid]['Stats']}", inline=False)
                    shared_inventory_embed2.add_field(name="Type", value=f"{self.worlditems[worldid]['Type']}", inline=True)
                    shared_inventory_embed2.add_field(name="Weight", value=f"{self.worlditems[worldid]['Weight']} slots")
                    shared_inventory_embed2.add_field(name="Value", value=f"{self.worlditems[worldid]['Value']}")
                    shared_inventory_embed2.add_field(name="Amount in inventory", value=f"{self.inventory[title2]['Inventory'][unique_inv_number2]['Quantity']}")

                    embed_fields = ["Stats", "Type", "Weight", "Value", "Amount in inventory"]
                    word = "Amount in inventory"
                    word_index = embed_fields.index(word)

                    shared_inventory_embed2.set_field_at(word_index, name="Amount in inventory", value=amount_in_inventory)

                    self.inventory[title2]["Inventory"][unique_inv_number2]["Quantity"] = amount_in_inventory
                    fh.save_file(self.inventory, 'inventory')
                    await user_msg.edit(embed=shared_inventory_embed2)

# Update shared inventory bag slots
                # start here
                shared_inventory_storage_message_id = self.inventory[title2]["Storage_Space_Embed_ID"]
                shared_inventory_storage_message = await shared_inventory_inventory_channel.fetch_message(shared_inventory_storage_message_id)

                storeage_inventory_embed = discord.Embed(title=f"{self.inventory[title2]['Inventory_Name']}\'s storeage space",color=0x8B4513)
                storeage_inventory_embed.add_field(name="Storage slots", value=f"{self.inventory[title2]['Used_Slots']} / {self.inventory[title2]['Bag_Slots']}", inline=False)

                embed_fields = ["Storage slots"]
                word = "Storage slots"
                word_index = embed_fields.index(word)

                storeage_inventory_embed.set_field_at(word_index, name="Storage slots", value=f"{new_shared_inventory_used_bag_slots} / {self.inventory[title2]['Bag_Slots']}")
                self.inventory[title2]["Used_Slots"] = new_shared_inventory_used_bag_slots

                fh.save_file(self.inventory, 'inventory')
                await shared_inventory_storage_message.edit(embed=storeage_inventory_embed)

def setup(bot):
    bot.add_cog(InventoryCommandS(bot))
