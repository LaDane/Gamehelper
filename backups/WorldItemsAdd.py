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
        return jh.show_worlditem_titles()

    

# Create a world item
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 698570403542728714: # Channel id of "item-editor"
            if message.content.startswith('newitem'):
                self.load_data()
                channel = message.channel
                await channel.purge(limit=10)
                
                await channel.send(f"{self.s_wi_t()}")
                msg1 = await channel.send("-\nAbove is a list of registered [W-ID]\nType the **World-ID** [W-ID] for the item you would like to add\nW-ID **MUST** be a unique number!")               
                await msg1.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)
# WORLD ID
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                worldid = msg.content

                if worldid == "cancel":                         # Takes use of CancelMenu cog
                    await channel.purge(limit=10)
                    await channel.send("Command canceled!")
                    return
                if worldid in self.users:
                    await channel.purge(limit=5)
                    await channel.send("You have entered a W-ID that's already been registered. If W-ID item is not visible in items-in-world channel, try removing it in remove-items-in-world channel.")
                if not worldid in self.users:

                    await channel.purge(limit=5)
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
                    await channel.send(f"**W-ID [{worldid}]** named **{itemname}** has been given description;\n**{description}**\nType the **Stats** for the new item (ex. + 1 Ranged Attack)")
                    await asyncio.sleep(1)

# STATS
                    msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                    stats = msg.content

                    await channel.purge(limit=5)
                    itemtype_msg = await channel.send(f"**W-ID [{worldid}]** named **{itemname}** has been given the following stats;\n**{stats}**\nReact to this coment with the type of item you're creating\n:canned_food: for Consumable\n:bow_and_arrow: for Weapon\n:lab_coat: for Armor\n:bone: for Static items\nNote: Ammunition and grenades are consumables")
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
                    embed.add_field(name="Stats", value=f"{stats}", inline=False)
                    embed.add_field(name="Type", value=f"{itemtype}", inline=True)
                    embed.add_field(name="Weight", value=f"{weight} slots")
                    embed.add_field(name="Value", value=f"{value}")
                    await channel.send(embed=embed)

                    channel = self.bot.get_channel(698570643976880260) # Change channel id to items-in-world channel
                    embed = discord.Embed(title=f"**{itemname}**", description=f"*{description}*", color=discord.Color.red())
                    embed.set_image(url=f"{picture}")
                    embed.set_footer(text=f"W-ID [{worldid}]")
                    embed.add_field(name="Stats", value=f"{stats}", inline=False)
                    embed.add_field(name="Type", value=f"{itemtype}", inline=True)
                    embed.add_field(name="Weight", value=f"{weight} slots")
                    embed.add_field(name="Value", value=f"{value}")
                    iiw_msg = await channel.send(embed=embed)
                    iiw_msg_id = iiw_msg.id  

                    
                    self.users[worldid] = {}
                    self.users[worldid]["ItemName"] = itemname
                    self.users[worldid]["Description"] = description
                    self.users[worldid]["Stats"] = stats
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

                    



