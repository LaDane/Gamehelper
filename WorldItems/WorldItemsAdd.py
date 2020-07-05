import discord
import json
import asyncio
from discord.ext import commands
from filehandler import FileHandler
from jsonhandler import JsonHandler

jh = JsonHandler()
fh = FileHandler()


class WorldItemsAdd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
        self.users = fh.load_file('worlditems')

    def s_wi_t(self):
        return jh.show_worlditem_titles2()

# Used to generate a new unique number from a list
    def Convert(self, string): 
        li = list(string.split(" ")) 
        return li
    

# Create a world item
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 698570403542728714: # Channel id of "item-editor"
            if message.content.startswith('newitem'):
                self.load_data()
                channel = message.channel
                await channel.purge(limit=10)
                
# Generate new unique number from list CODE
                chair_inv_numbers = self.s_wi_t()
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

                worldid = unique_new_number
                await asyncio.sleep(1)

                msg2 = await channel.send(f"**W-ID [{worldid}]** chosen for new item.\nType the **Item Name** for the new item")
                await msg2.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)

# ITEM NAME
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                itemname = msg.content

                if itemname == "cancel":                         # Takes use of CancelMenu cog
                    await channel.purge(limit=10)
                    await channel.send("Command canceled!")
                    return

                await channel.purge(limit=5)
                msg3 = await channel.send(f"Item name **{itemname}** has been given to **W-ID [{worldid}]**.\nType the **Description** for the new item")
                await msg3.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)

# DESCRIPTION
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                description = msg.content

                if description == "cancel":                         # Takes use of CancelMenu cog
                    await channel.purge(limit=10)
                    await channel.send("Command canceled!")
                    return

                await channel.purge(limit=5)
                await channel.send(f"**W-ID [{worldid}]** named **{itemname}** has been given description;\n**{description}**\nWould you like to add **Stats** to this item?\n**yes** or **no**\n \n*If you choose a stat other than a **Custom stat** / **Bag Slots**, the selected stat will be added to a players character sheet when they buy the item and have it in their inventory*\nIf player has multiple of the same items in inventory, the stat wont stack on their character sheet!\nThey will loose the stat once the item is sold or thrown away")
                await asyncio.sleep(1)

# STATS
                msg_stat_check = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                msg_stat_check_c = msg_stat_check.content

                if msg_stat_check_c.lower() == "no":
                    stats = "None"
                    stats_modifier = ""

                if msg_stat_check_c.lower() == "yes":
                    msg_stat_react = await channel.send(f"React to this message with the corresponding **Evner** that you would like the item to have stats in\n \n*Please wait for the bot to add all reactions before you react! (last one is :beginner:)*\n \n" +
                            "__**Kamp Evner**__\n" +
                            ":crossed_swords: for **Nærkamp**\n" +
                            ":bow_and_arrow: for **Kaste/Strenge Våben**\n" +
                            ":gun: for **Skydevåben**\n" +
                            ":man_detective: for **Snig**\n" +
                            "__**Sociale Evner**__\n" +
                            ":kiss: for **Smigre**\n" +
                            ":lying_face: for **Løgn**\n" +
                            ":muscle: for **Intimiderer**\n" +
                            ":money_mouth: for **Handel**\n" +
                            "__**Håndværks Evner**__\n" +
                            ":wrench: for **Reparation**\n" +
                            ":chains: for **Fælder**\n" +
                            ":fishing_pole_and_fish: for **Overlevelse**\n" +
                            ":hand_splayed: for **Håndarbejde**\n" +
                            "__**Esoteriske Evner**__\n" +
                            ":books: for **Videnskab**\n" +
                            ":sake: for **Alkymi**\n" +
                            ":medical_symbol: for **Lægevidenskab**\n" +
                            ":clock: for **Historie**\n" +
                            "__**If you want the stat to increase bag slots**__\n" +
                            ":package: for **Bag Slots**\n" +
                            "__**If you want to add a custom stat;**__\n" +
                            ":beginner: for **Custom stat**")
                    await asyncio.sleep(1) 

                    await msg_stat_react.add_reaction(emoji='\u2694') # crossed_swords
                    await msg_stat_react.add_reaction(emoji='\U0001F3F9') # bow_and_arrow
                    await msg_stat_react.add_reaction(emoji='\U0001F52B') # gun
                    await msg_stat_react.add_reaction(emoji='\U0001F575') # man_detective
                    await msg_stat_react.add_reaction(emoji='\U0001F48B') # :kiss: U0001F48B
                    await msg_stat_react.add_reaction(emoji='\U0001F925') # lying_face
                    await msg_stat_react.add_reaction(emoji='\U0001F4AA') # muscle
                    await msg_stat_react.add_reaction(emoji='\U0001F911') # money_mouth
                    await msg_stat_react.add_reaction(emoji='\U0001F527') # wrench
                    await msg_stat_react.add_reaction(emoji='\U000026D3') # chains
                    await msg_stat_react.add_reaction(emoji='\U0001F3A3') # fishing_pole_and_fish
                    await msg_stat_react.add_reaction(emoji='\U0001F590') # hand_splayed
                    await msg_stat_react.add_reaction(emoji='\U0001F4DA') # books
                    await msg_stat_react.add_reaction(emoji='\U0001F376') # sake
                    await msg_stat_react.add_reaction(emoji='\U00002695') # medical_symbol
                    await msg_stat_react.add_reaction(emoji='\U0001F570') # clock
                    await msg_stat_react.add_reaction(emoji='\U0001F4E6') # package
                    await msg_stat_react.add_reaction(emoji='\U0001F530') # beginner

                    await asyncio.sleep(1)

                    res = await self.bot.wait_for('reaction_add')
                    # if member_id == botcheck: # In this case, the bot reacted to a message
                    #     return
                    if res:
                        reaction, message.author = res
                        if str(reaction.emoji) == "\u2694":
                            chosen_stat = "Nærkamp"
                        if str(reaction.emoji) == "\U0001F3F9":
                            chosen_stat = "Kaste_Strenge_våben"
                        if str(reaction.emoji) == "\U0001F52B":
                            chosen_stat = "Skydevåben"                
                        if str(reaction.emoji) == "\U0001F575":
                            chosen_stat = "Snig" 
                        if str(reaction.emoji) == "\U0001F48B":
                            chosen_stat = "Smigre"
                        if str(reaction.emoji) == "\U0001F925":
                            chosen_stat = "Løgn"
                        if str(reaction.emoji) == "\U0001F4AA":
                            chosen_stat = "Intimiderer"                
                        if str(reaction.emoji) == "\U0001F911":
                            chosen_stat = "Handel"
                        if str(reaction.emoji) == "\U0001F527":
                            chosen_stat = "Reparation"
                        if str(reaction.emoji) == "\U000026D3":
                            chosen_stat = "Fælder"
                        if str(reaction.emoji) == "\U0001F3A3":
                            chosen_stat = "Overlevelse"                
                        if str(reaction.emoji) == "\U0001F590":
                            chosen_stat = "Håndarbejde"   
                        if str(reaction.emoji) == "\U0001F4DA":
                            chosen_stat = "Videnskab"
                        if str(reaction.emoji) == "\U0001F376":
                            chosen_stat = "Alkymi"
                        if str(reaction.emoji) == "\U00002695":
                            chosen_stat = "Lægevidenskab"                
                        if str(reaction.emoji) == "\U0001F570":
                            chosen_stat = "Historie"  
                        if str(reaction.emoji) == "\U0001F4E6":
                            chosen_stat = "Bag slots" 
                        if str(reaction.emoji) == "\U0001F530":
                            chosen_stat = "Custom"

                    await asyncio.sleep(1)
                    if chosen_stat == "Custom":
                        await channel.purge(limit=5)
                        await asyncio.sleep(1)
                        await channel.send(f"You have chosen to add a custom stat to this item\nThis stat will not be added to character sheets!\n \nWhat would you like the custom stat to be?")
                        await asyncio.sleep(1)
                        msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                        stats = msg.content
                        stats_modifier = ""

                    if chosen_stat != "Custom":
                        await channel.purge(limit=5)
                        await asyncio.sleep(1)
                        await channel.send(f"You have chosen to add a stat in the form of **{chosen_stat}** to this item\nThis stat will be added to character sheets!\n \nType the number that you want this **{chosen_stat}** modifer to have\n \nEx;\n**+7**")
                        await asyncio.sleep(1)
                        msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                        stats = chosen_stat
                        stats_modifier = msg.content


                await channel.purge(limit=5)
                itemtype_msg = await channel.send(f"**W-ID [{worldid}]** named **{itemname}** has been given the following stats;\n**{stats_modifier} {stats}**\nReact to this coment with the type of item you're creating\n:canned_food: for Consumable\n:bow_and_arrow: for Weapon\n:lab_coat: for Armor\n:bone: for Static items\nNote: Ammunition and grenades are consumables")
                await itemtype_msg.add_reaction(emoji='\U0001F96B')
                await itemtype_msg.add_reaction(emoji='\U0001F3F9')
                await itemtype_msg.add_reaction(emoji='\U0001F97C')
                await itemtype_msg.add_reaction(emoji='\U0001F9B4')
                await asyncio.sleep(1)
# ITEM TYPE
                res = await self.bot.wait_for('reaction_add')
                if res:
                    reaction, message.author = res
                    if str(reaction.emoji) == "\U0001F96B":
                        itemtype = "Consumable"
                    if str(reaction.emoji) == "\U0001F3F9":
                        itemtype = "Weapon"
                    if str(reaction.emoji) == "\U0001F97C":
                        itemtype = "Armor"
                    if str(reaction.emoji) == "\U0001F9B4":
                        itemtype = "Static Items"

                await asyncio.sleep(1)
                await channel.purge(limit=5)
                msg6 = await channel.send(f"**W-ID [{worldid}]** named **{itemname}** has been given item type;\n**{itemtype}**\n \nType the **weight** of the item in the form of bag slots.")
                await msg6.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)

# WEIGHT
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                weight = msg.content

                if weight == "cancel":                         # Takes use of CancelMenu cog
                    await channel.purge(limit=10)
                    await channel.send("Command canceled!")
                    return

                await channel.purge(limit=5)
                msg4 = await channel.send(f"**W-ID [{worldid}]** named **{itemname}** has been given weight;\n**{weight}** slots.\nType the value of the item")
                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)

# VALUE
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                value = msg.content

                if value == "cancel":                         # Takes use of CancelMenu cog
                    await channel.purge(limit=10)
                    await channel.send("Command canceled!")
                    return

                await channel.purge(limit=5)
                msg5 = await channel.send(f"**W-ID [{worldid}]** named **{itemname}** has been given a value of;\n**{value}**.\nEnter a picture url of the item\nEx\nhttps://media.discordapp.net/attachments/698522831083929734/698562251246010468/unknown.png?width=1132&height=0")
                await msg5.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)

# PICTURE
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                picture = msg.content

                if picture == "cancel":                         # Takes use of CancelMenu cog
                    await channel.purge(limit=10)
                    await channel.send("Command canceled!")
                    return                    

                await channel.purge(limit=5)
                await channel.send(f"Successfully created new world item!")
                await asyncio.sleep(1)


                embed = discord.Embed(title=f"**{itemname}**", description=f"*{description}*", color=discord.Color.red())
                embed.set_image(url=f"{picture}")
                embed.set_footer(text=f"W-ID [{worldid}]")
                embed.add_field(name="Stats", value=f"{stats_modifier} {stats}", inline=False)
                embed.add_field(name="Type", value=f"{itemtype}", inline=True)
                embed.add_field(name="Weight", value=f"{weight} slots")
                embed.add_field(name="Value", value=f"{value}")
                await channel.send(embed=embed)

                channel = self.bot.get_channel(698570643976880260) # Change channel id to items-in-world channel
                embed = discord.Embed(title=f"**{itemname}**", description=f"*{description}*", color=discord.Color.red())
                embed.set_image(url=f"{picture}")
                embed.set_footer(text=f"W-ID [{worldid}]")
                embed.add_field(name="Stats", value=f"{stats_modifier} {stats}", inline=False)
                embed.add_field(name="Type", value=f"{itemtype}", inline=True)
                embed.add_field(name="Weight", value=f"{weight} slots")
                embed.add_field(name="Value", value=f"{value}")
                iiw_msg = await channel.send(embed=embed)
                iiw_msg_id = iiw_msg.id  

                
                self.users[worldid] = {}
                self.users[worldid]["ItemName"] = itemname
                self.users[worldid]["Description"] = description                    
                self.users[worldid]["Stats"] = stats
                self.users[worldid]["StatsModifier"] = stats_modifier
                self.users[worldid]["Type"] = itemtype
                self.users[worldid]["Weight"] = weight
                self.users[worldid]["Value"] = value
                self.users[worldid]["Picture"] = picture
                self.users[worldid]["ItemsInWorldMsgID"] = iiw_msg_id
                fh.save_file(self.users, 'worlditems')
                await asyncio.sleep(1)




def setup(bot):
    bot.add_cog(WorldItemsAdd(bot))


#======================
#JUNK
#======================

                    # for channel in member.guild.channels:
                    #     if channel.id == 698570643976880260: # Change channel id to items-in-world
                    #         embed = discord.Embed(title=f"**{itemname}**", description=f"*{description}*", color=discord.Color.red())
                    #         embed.set_image(url=f"{picture}")
                    #         embed.set_footer(text=f"W-ID [{worldid}]")
                    #         embed.add_field(name="Stats", value=f"{stats}", inline=False)
                    #         embed.add_field(name="Type", value=f"{self.users[worldid]['Type']}", inline=True)
                    #         embed.add_field(name="Weight", value=f"{weight} slots")
                    #         embed.add_field(name="Value", value=f"{value}")
                    #         await channel.send(embed=embed)

                #self.bot.wait_for_message(author=message.author)
                #response = self.bot.wait_for_message(author=message.author, timeout=30)
                #msg = 
                 
                #response = self.bot.wait_for_message(author=message.author, timeout=30)
                #print (response)
                #def check(m):
                #    print (m.content)
                #    return m.content == message.author and m.channel == channel
                 #   #print (m.content)

                #msg = await self.bot.wait_for('message', check=check)
                #await channel.send('Hello {.author}!'.format(msg))



                    #msg = await bot.send_message(ctx.message.channel, 'test')
                    # emoji1 = discord.utils.get(self.bot.get_all_emojis(), name='\U0001F96B')
                    # emoji2 = discord.utils.get(self.bot.get_all_emojis(), name='\U0001F3F9')
                    # emoji3 = discord.utils.get(self.bot.get_all_emojis(), name='\U0001F97C')
                    # emoji4 = discord.utils.get(self.bot.get_all_emojis(), name='\U0001F9B4')
                    #await bot.add_reaction(msg, emoji1)
                    #await bot.add_reaction(msg, emoji2)

                    # reaction = await self.bot.wait_for(['\U0001F96B', '\U0001F3F9', '\U0001F97C', '\U0001F9B4'])
                    # await channel.send("You responded with {}".format(reaction.emoji))


                    # def make_sequence(seq):
                    #     if seq is None:
                    #         return ()
                    #     if isinstance(seq, Sequence) and not isinstance(seq, str):
                    #         return seq
                    #     else:
                    #         return (seq,)

                    # def reaction_check(message=None, emoji=None, author=None, ignore_bot=True):
                    #     message = make_sequence(message)
                    #     message = tuple(m.id for m in message)
                    #     emoji = make_sequence(emoji)
                    #     author = make_sequence(author)
                    #     def check(reaction, user):
                    #         if ignore_bot and user.bot:
                    #             return False
                    #         if message and reaction.message.id not in message:
                    #             return False
                    #         if emoji and reaction.emoji not in emoji:
                    #             return False
                    #         if author and user not in author:
                    #             return False
                    #         return True
                    #     return check

                    # check = reaction_check(message=msg, author=message.author, emoji=('\U0001F96B', '\U0001F3F9', '\U0001F97C', '\U0001F9B4'))
                    # try: 
                    #     reaction, user = await self.bot.wait_for('reaction_add', timeout=10.0, check=check)
                    #     if reaction.emoji == '\U0001F96B':
                    #         self.users[worldid]["Type"] = "Consumable"
                    #     elif reaction.emoji == '\U0001F3F9':
                    #         self.users[worldid]["Type"] = "Weapon"
                    #     elif reaction.emoji == '\U0001F97C':
                    #         self.users[worldid]["Type"] = "Armor"
                    #     elif reaction.emoji == '\U0001F97C':
                    #         self.users[worldid]["Type"] = "Static Item"
                    # except TimeoutError:
                    #     await channel.send(f"User took too long to respond. Item setup failed, please delete **W-ID [{worldid}]**")

                    



                    # def check_consumable(reaction, user):
                    #     return user == message.author and str(reaction.emoji) == '\U0001F96B'
                    # try:
                    #     await self.bot.wait_for('reaction_add', timeout=30.0, check=check_consumable)
                    # except asyncio.TimeoutError:
                    #     await channel.send(f"User took too long to respond. Item setup failed, please delete **W-ID [{worldid}]**")
                    # else:
                    #     self.users[worldid]["Type"] = "Consumable"

                    # def check_weapon(reaction, user):
                    #     return user == message.author and str(reaction.emoji) == '\U0001F3F9'
                    # try:
                    #     await self.bot.wait_for('reaction_add', timeout=30.0, check=check_weapon)
                    # except asyncio.TimeoutError:
                    #     await channel.send(f"User took too long to respond. Item setup failed, please delete **W-ID [{worldid}]**")
                    # else:
                    #     self.users[worldid]["Type"] = "Weapon"

                    # def check_armor(reaction, user):
                    #     return user == message.author and str(reaction.emoji) == '\U0001F97C'
                    # try:
                    #     await self.bot.wait_for('reaction_add', timeout=30.0, check=check_armor)
                    # except asyncio.TimeoutError:
                    #     await channel.send(f"User took too long to respond. Item setup failed, please delete **W-ID [{worldid}]**")
                    # else:
                    #     self.users[worldid]["Type"] = "Armor"

                    # def check_static(reaction, user):
                    #     return user == message.author and str(reaction.emoji) == '\U0001F9B4'
                    # try:
                    #     await self.bot.wait_for('reaction_add', timeout=30.0, check=check_static)
                    # except asyncio.TimeoutError:
                    #     await channel.send(f"User took too long to respond. Item setup failed, please delete **W-ID [{worldid}]**")
                    # else:
                    #     self.users[worldid]["Type"] = "Static Item"

                    # await asyncio.sleep(50)
                    # await channel.send(f"**W-ID [{worldid}]** named **{itemname}** has been given item type;\n**{self.users[worldid]['Type']}**\nType the weight of the item in the form of bag slots.")
                    # await asyncio.sleep(1)

                    



