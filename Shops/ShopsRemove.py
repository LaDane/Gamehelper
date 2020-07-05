import discord
import json
import asyncio
from discord.ext import commands
from filehandler import FileHandler
from jsonhandler import JsonHandler

jh = JsonHandler()
fh = FileHandler()


class ShopsRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
        # self.worlditems = fh.load_file('worlditems')
        # self.currency = fh.load_file('currency')
        self.shops = fh.load_file('shops')

    def s_s_t(self):
        return jh.show_shop_titles()

# Remove a shop, including deletion of channels and category
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 699194951535427635: # Channel id of "shop-editor"
            if message.content.startswith('removeshop'):
                channel = message.channel
                await channel.purge(limit=10)
                self.load_data()

                try:
                    await channel.send(f"{self.s_s_t()}")
                    msg1 = await channel.send("-\nAbove is a list of registered [S-ID]\nType the S-ID of the shop you want to remove")

                    await msg1.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                    await asyncio.sleep(1)

                    msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                    rshopid = msg.content
                    await asyncio.sleep(1)

                    if rshopid == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                    if not rshopid in self.shops:
                        await channel.purge(limit=10)
                        await channel.send("You have entered a S-ID that's not registered. Make sure that the entered text is an **exact** match to a shops ID")
                    if rshopid in self.shops:
                        await channel.purge(limit=10)
                        msg2 = await channel.send(f"Are you sure you want to delete the shop **[{rshopid}]**?\n**yes** or **no**")
                        await msg2.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                        await asyncio.sleep(1)

                        msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                        response = msg.content
                        await asyncio.sleep(1)
                    
                        if response == "cancel":                         # Takes use of CancelMenu cog
                            await channel.purge(limit=10)
                            await channel.send("Command canceled!")
                            return
                        if response == "no":
                            await channel.purge(limit=10)
                            await channel.send("Canceling request")
                        if response == "yes":

                            buychannel_id = self.shops[rshopid]["ShopBuyID"]
                            shopcategory_id = self.shops[rshopid]["ShopCategoryID"]

                            try:
                                channel = self.bot.get_channel(buychannel_id) # Channel id of buy channel
                                await channel.delete()
                            except:
                                print("No buy channel exists for this id")

                            try:
                                category = self.bot.get_channel(shopcategory_id) # Category id of the shop
                                await category.delete()
                            except:
                                print("No category exists for this channel")

                            del self.shops[rshopid]
                            fh.save_file(self.shops, 'shops')
                            channel = self.bot.get_channel(699194951535427635) # Channel id of "shop-editor"
                            await channel.purge(limit=10)
                            await channel.send(f"S-ID [{rshopid}] has successfully been deleted from dictionary.")
                except:
                    await channel.send("*No [S-ID] registered yet*\n**Please set up a shop before removing it!**")


def setup(bot):
    bot.add_cog(ShopsRemove(bot))


#================
#JUNK
#================
                        # await delete_channel(buychannel_id)           didnt work
                        # await message.channel.delete(buychannel_id)   didnt work
                        # await self.bot.delete_channel(buychannel_id)  didnt work
                        # message = message.guild
                        # await guild.channel.delete(buychannel_id)

                        # channel = self.bot.get_channel(buychannel_id) # Channel id of ...
                        # await message.delete_channel()


                        # try:
                        #     await bot.delete_channel(buychannel_id)

                        # except:
                        #     print("Delete buy channel failed")

                            

                        # guild = message.guild
                        # shopid = self.shops[rshopid]["ShopCategoryID"]

                        # new_category_id = self.shops[rshopid]["ShopCategoryID"]
                        # category_channel = self.bot.get_channel(new_channel_id)
                        # print(new_category_id)
                        # print(category_channel)
                        # await bot.delete_category(new_category_id)

                        # try:
                        #     await guild.delete_category(new_channel_id)
                        # except:
                        #     print("Shop has no category")

                        # del self.shops[rshopid]
                        # fh.save_file(self.shops, 'shops')
                        # await channel.purge(limit=10)
                        # await channel.send(f"S-ID [{rshopid}] has successfully been deleted from dictionary.")
                    



