import discord
import json
import asyncio
from discord.ext import commands
from filehandler import FileHandler
from jsonhandler import JsonHandler

jh = JsonHandler()
fh = FileHandler()


class ShopsStockAdd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
        self.worlditems = fh.load_file('worlditems')
        # self.currency = fh.load_file('currency')
        self.shops = fh.load_file('shops')

    def s_s_t(self):
        return jh.show_shop_titles()

    def s_s_sid(self):
        return jh.show_shop_stockid()

    def s_wi_t(self):
        return jh.show_worlditem_titles()


# Add items as stock to a shop
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 699194951535427635: # Channel id of "shop-editor"
            if message.content.startswith('stockshop'):
                channel = message.channel
                await channel.purge(limit=10)
                self.load_data()

                try:
                    await channel.send(self.s_s_t())                
                    msg1 = await channel.send("-\nAbove is a list of registered [S-ID] \nType the **Shop-ID** [S-ID] that you would like to add items to")

                    await msg1.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                    await asyncio.sleep(1)

                    msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                    shopid = msg.content

                    if shopid == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                    if not shopid in self.shops:
                        await channel.purge(limit=10)
                        await channel.send("You have entered a S-ID that's not registered. Make sure that the entered text is an **exact** match to a Shop-ID\nCanceling request...")
                    if shopid in self.shops:
                        await channel.purge(limit=10)
                        await channel.send(f"You have chosen to stock the shelves of **{shopid}**")
                        await asyncio.sleep(3)
                        await channel.purge(limit=10)


                        try:
                            await channel.send(self.s_s_sid())
                        except:
                            await channel.send("*No [SE-ID] registered yet*")
                        
                        await channel.send(f"-\nAbove is a list of registered [SE-ID] (bold numbers). If none are shown, no numbers are registered\nNew [SE-ID] cannot be the same as already registered [SE-ID] in;\n      **{shopid}**")
                        msg2 = await channel.send("A unique **Shop-Entry-ID** [SE-ID] must be created for the shop entry\nWhat should the **[SE-ID]** be?")
                        
                        await msg2.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                        await asyncio.sleep(1)

                        msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                        shopentryid = msg.content
                        
                        if shopentryid == "cancel":                         # Takes use of CancelMenu cog
                            await channel.purge(limit=10)
                            await channel.send("Command canceled!")
                            return
                        if shopentryid in self.shops[shopid]["Stock"]:
                            await channel.purge(limit=10)
                            await channel.send("You have entered a SE-ID that's already been registered. Make sure that the entered text is a unique Shop-Entry-ID (SE-ID)\nCanceling request...")
                        if not shopentryid in self.shops[shopid]["Stock"]:
                            await channel.purge(limit=10)
                            await channel.send(f"You have chosen Shop-Entry-ID;\n**{shopentryid}**")
                            await asyncio.sleep(3)
                            await channel.purge(limit=10)

                            try:
                                await channel.send(self.s_wi_t())
                            except:
                                await channel.send("*No [W-ID] registered yet*")

                            msg3 = await channel.send(f"-\nAbove is a list of registered [W-ID] (numbers in bold)\nWhich **W-ID** would you like to add to the shop?")
                            
                            await msg3.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                            await asyncio.sleep(1)

                            msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                            worldid = msg.content

                            if worldid == "cancel":                         # Takes use of CancelMenu cog
                                await channel.purge(limit=10)
                                await channel.send("Command canceled!")
                                return
                            if not worldid in self.worlditems:
                                await channel.purge(limit=10)
                                await channel.send("You have entered a W-ID that's not registered. Make sure that the entered text is an **exact** match to a world ID\nCanceling request...")
                            if worldid in self.worlditems:
                                await channel.purge(limit=10)
                                await channel.send(f"You have chosen to add **{self.worlditems[worldid]['ItemName']}** to **{shopid}**")

                                embed = discord.Embed(title=f"**{self.worlditems[worldid]['ItemName']}**", description=f"*{self.worlditems[worldid]['Description']}*", color=discord.Color.red())
                                embed.set_image(url=f"{self.worlditems[worldid]['Picture']}")
                                embed.set_footer(text=f"W-ID [{worldid}]")
                                embed.add_field(name="Stats", value=f"{self.worlditems[worldid]['Stats']}", inline=False)
                                embed.add_field(name="Type", value=f"{self.worlditems[worldid]['Type']}", inline=True)
                                embed.add_field(name="Weight", value=f"{self.worlditems[worldid]['Weight']} slots")
                                embed.add_field(name="Value", value=f"{self.worlditems[worldid]['Value']}")
                                await channel.send(embed=embed)

                                msg4 = await channel.send(f"How many of '{self.worlditems[worldid]['ItemName']}' would you like to stock in {shopid}")
                                
                                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                                await asyncio.sleep(1)

                                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                                quantity = msg.content

                                if quantity == "cancel":                         # Takes use of CancelMenu cog
                                    await channel.purge(limit=10)
                                    await channel.send("Command canceled!")
                                    return

                                await channel.purge(limit=10)

                                buy_channel_id = self.shops[shopid]["ShopBuyID"]
                                buy_channel = self.bot.get_channel(buy_channel_id)

                                try:
                                    embed = discord.Embed(title=f"**{self.worlditems[worldid]['ItemName']}**", description=f"*{self.worlditems[worldid]['Description']}*", color=discord.Color.red())
                                    embed.set_image(url=f"{self.worlditems[worldid]['Picture']}")
                                    embed.set_footer(text=f"W-ID [{worldid}]\nSE-ID [{shopentryid}]")
                                    embed.add_field(name="Stats", value=f"{self.worlditems[worldid]['Stats']}", inline=False)
                                    embed.add_field(name="Type", value=f"{self.worlditems[worldid]['Type']}", inline=True)
                                    embed.add_field(name="Weight", value=f"{self.worlditems[worldid]['Weight']} slots")
                                    embed.add_field(name="Value", value=f"{self.worlditems[worldid]['Value']}")
                                    embed.add_field(name="Amount in stock", value=f"{quantity}")
                                    shop_stock_msg = await buy_channel.send(embed=embed)
                                    shop_stock_msg_id = shop_stock_msg.id 

                                    self.shops[shopid]["Stock"][shopentryid] = {}
                                    self.shops[shopid]["Stock"][shopentryid]["WorldID"] = worldid
                                    self.shops[shopid]["Stock"][shopentryid]["Quantity"] = quantity                            
                                    self.shops[shopid]["Stock"][shopentryid]["BuyStockMsgID"] = shop_stock_msg_id 
                                    fh.save_file(self.shops, 'shops')

                                    await asyncio.sleep(1)
                                    await channel.send(f"Shop entry **{shopentryid}** has succesfully been added to **{shopid}**!")

                                except:
                                    await channel.send("No buy channel exists for this shop, please set up shop properly\nEntry failed...")
                except:
                    await channel.send("*No [S-ID] registered yet*\n**Please set up a shop before adding stock!**")
   




def setup(bot):
    bot.add_cog(ShopsStockAdd(bot))

# =======================
# JUNK
#========================


# MeM data handler
#     def format_shop(self):
#         print_str = ""
#         for title, value in self.shops.items():
#             print_str += f"{title} {value['ShopOwner']}\n"
#         return print_str

# Written in code below
#       await channel.send(self.format_shop())



# HELP HERE!
    # def show_shop_stockid(self): # This function is for when you would like to display the titles in shops.json
    #     print_str = ""
    #     for title, value in self.shops.items():
    #         print_str += f"{title} {value['Stock']['ShopEntryID']}\n"
    #         show_shop_stockid_title = title # since title is not used in this command, this sets it to nothing and we have no problems in code
    #     return print_str

