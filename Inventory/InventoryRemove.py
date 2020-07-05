import discord
import json
import asyncio
from discord.ext import commands
from filehandler import FileHandler
from jsonhandler import JsonHandler

jh = JsonHandler()
fh = FileHandler()


class InventoryRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
        self.inventory = fh.load_file('inventory')

    def s_i_t_a_v(self):
        return jh.show_inv_titles_and_values()

# Create a new inventory with own category and and channels
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 700842187058970624: # Channel id of "inventory-editor"
            if message.content.startswith('removeinventory'):
                self.load_data()
                channel = message.channel
                await channel.purge(limit=10)

                try:   
                    await channel.send(f"{self.s_i_t_a_v()}")
                    msg1 = await channel.send("-\nAbove is a list of registered inventories (the numbers in bold are the ID's)\nType the inventory ID of the shop you want to remove")

                    await msg1.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                    await asyncio.sleep(1)

                    msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                    rinvid = msg.content
                    await asyncio.sleep(1)

                    if rinvid == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                    if not rinvid in self.inventory:
                        await channel.purge(limit=10)
                        await channel.send("You have entered a S-ID that's not registered. Make sure that the entered text is an **exact** match to a shops ID")
                    if rinvid in self.inventory:
                        await channel.purge(limit=10)
                        msg2 = await channel.send(f"Are you sure you want to delete the shop **[{rinvid}]**?\n**yes** or **no**")
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

                            store_items_id = self.inventory[rinvid]['Store_Items_Channel_ID']
                            inventory_id = self.inventory[rinvid]['Inventory_Channel_ID']
                            category_id = self.inventory[rinvid]['Inventory_Category_ID']

                            try:
                                channel = self.bot.get_channel(store_items_id) # Channel id of store-items channel
                                await channel.delete()
                            except:
                                print("No store-items channel exists for this id")

                            try:
                                channel = self.bot.get_channel(inventory_id) # Channel id of inventory channel
                                await channel.delete()
                            except:
                                print("No inventory channel exists for this id")

                            try:
                                category = self.bot.get_channel(category_id) # Category id
                                await category.delete()
                            except:
                                print("No category exists for this channel")

                            del self.inventory[rinvid]
                            fh.save_file(self.inventory, 'inventory')
                            channel = self.bot.get_channel(700842187058970624) # Channel id of "inventory-editor"
                            await channel.purge(limit=10)
                            await channel.send(f"Inventory ID [{rinvid}] has successfully been deleted from dictionary.")
                except:
                    await channel.send("*No inventories registered yet*\n**Please set up an inventory before removing it!**")

def setup(bot):
    bot.add_cog(InventoryRemove(bot))

