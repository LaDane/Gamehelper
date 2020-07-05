import discord
import json
import asyncio
from discord.ext import commands
from filehandler import FileHandler
from jsonhandler import JsonHandler

jh = JsonHandler()
fh = FileHandler()


class InventoryAdd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
        self.inventory = fh.load_file('inventory')

    def s_i_ids(self):
        return jh.show_inv_ids()

# Create a new inventory with own category and and channels
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 700842187058970624: # Channel id of "inventory-editor"
            if message.content.startswith('newinventory'):
                self.load_data()
                channel = message.channel
                await channel.purge(limit=10)

                inventory_ids = self.s_i_ids()
                if len(inventory_ids) == 0:
                    inventory_ids = [0]
                unique_inv_id = int(max(inventory_ids)) + 1

# Inventory name
                msg1 = await channel.send("You have chosen to setup a new inventory that all players will have access to once you unhide the channel from players\n**What should the name if the inventory be?**\n \n*Ex;*\n*Mark-3*")

                await msg1.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)

                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                inventory_name = msg.content

                if inventory_name == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return

                await asyncio.sleep(1)
                await channel.purge(limit=5)

# Inventory description
                msg2 = await channel.send(f"Inventory has been given name **{inventory_name}**\n \nEnter a **description** for the inventory")

                await msg2.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)

                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                description = msg.content

                if description == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return

                await asyncio.sleep(1)
                await channel.purge(limit=5)     

# Inventory bag slots
                msg2 = await channel.send(f"**{inventory_name}** has been given the following description;\n \n*{description}*\n \nHow many **bag slots** should the inventory have?\nReply with a number")

                await msg2.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)

                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                bag_slots = msg.content

                if bag_slots == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return

                await asyncio.sleep(1)
                await channel.purge(limit=5)               

# Picture
                msg3 = await channel.send(f"**{inventory_name}** will have **{bag_slots}** bag slots\n \nEnter a picture url of the inventory\n \nEx\nhttps://media.discordapp.net/attachments/698522831083929734/698562251246010468/unknown.png?width=1132&height=0")
 
                await msg3.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1) 

                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                picture = msg.content

                if picture == "cancel":                         # Takes use of CancelMenu cog
                    await channel.purge(limit=10)
                    await channel.send("Command canceled!")
                    return

                await asyncio.sleep(1)
                await channel.purge(limit=5) 

# Category setup
                guild = message.guild

                new_category = await guild.create_category(inventory_name)     
                new_category_id = new_category.id

                category_channel = self.bot.get_channel(new_category_id)

# Store-items channel setup
                store_items_channel = await guild.create_text_channel(f'{inventory_name}-store-items', category=category_channel)    
                store_items_channel_id = store_items_channel.id    
# Store-items permissions
                gm_role = discord.utils.get(guild.roles, name='GM')
                players_role = discord.utils.get(guild.roles, name='Players')
                await store_items_channel.set_permissions(gm_role, read_messages=True, send_messages=True)
                await store_items_channel.set_permissions(players_role, read_messages=False, send_messages=False)
                await store_items_channel.set_permissions(guild.default_role, read_messages=False, send_messages=False)

# Inventory channel setup
                inventory_channel = await guild.create_text_channel(f'{inventory_name}-inventory', category=category_channel)    
                inventory_channel_id = inventory_channel.id    
# Inventory permissions
                await inventory_channel.set_permissions(gm_role, read_messages=True, send_messages=True)
                await inventory_channel.set_permissions(players_role, read_messages=False, send_messages=False)
                await inventory_channel.set_permissions(guild.default_role, read_messages=False, send_messages=False)   

                self.inventory[unique_inv_id] = {}       
                self.inventory[unique_inv_id]['Inventory_Name'] = inventory_name
                self.inventory[unique_inv_id]['Description'] = description
                self.inventory[unique_inv_id]['Used_Slots'] = 0
                self.inventory[unique_inv_id]['Bag_Slots'] = bag_slots
                self.inventory[unique_inv_id]['Picture'] = picture
                self.inventory[unique_inv_id]['Kreditter'] = 0
                self.inventory[unique_inv_id]['Imperille Kreditter'] = 0
                self.inventory[unique_inv_id]['Skindene Sten'] = 0
                self.inventory[unique_inv_id]['Inventory_Category_ID'] = new_category_id
                self.inventory[unique_inv_id]['Store_Items_Channel_ID'] = store_items_channel_id
                self.inventory[unique_inv_id]['Inventory_Channel_ID'] = inventory_channel_id
                fh.save_file(self.inventory, 'inventory')

                await channel.purge(limit=5)
                await channel.send(f"**{inventory_name}** has succesfully completed newinventory setup!\nUnhide the channels for users with **Players** role if you would like them to able to see the channels!")

# Send coin bag embed in inventory channel
                currency_embed = discord.Embed(title=f"{inventory_name}\'s coin bag.",color=0xffd700)
                currency_embed.add_field(name="Kreditter", value=self.inventory[unique_inv_id]["Kreditter"])
                currency_embed.add_field(name="Imperille Kreditter", value=self.inventory[unique_inv_id]["Imperille Kreditter"])
                currency_embed.add_field(name="Skindene Sten", value=self.inventory[unique_inv_id]["Skindene Sten"])
                currency_embed_msg = await inventory_channel.send(embed=currency_embed)
                currency_embed_msg_id = currency_embed_msg.id

                self.inventory[unique_inv_id]["Currency_Embed_ID"] = currency_embed_msg_id
                fh.save_file(self.inventory, 'inventory')

# Send backpack embed in inventory channel
                inventory_embed = discord.Embed(title=f"{inventory_name}\'s storeage space",color=0x8B4513)
                inventory_embed.add_field(name="Storage slots", value=f"{self.inventory[unique_inv_id]['Used_Slots']} / {self.inventory[unique_inv_id]['Bag_Slots']}", inline=False)
                inventory_embed_msg = await inventory_channel.send(embed=inventory_embed)
                inventory_embed_msg_id = inventory_embed_msg.id

                self.inventory[unique_inv_id]["Storage_Space_Embed_ID"] = inventory_embed_msg_id                    
                self.inventory[unique_inv_id]["Inventory"] = {}
                fh.save_file(self.inventory, 'inventory')

# Send embed description to store-items channel
                embed = discord.Embed(title=f"**{inventory_name}**", description=f"{description}", color=0x303136)                
                embed.set_image(url=f"{picture}")
                await store_items_channel.send(embed=embed)

# Send intro to store-items channel
                await store_items_channel.send(f"In this channel you can;\n**.s [W-ID]** to store items from your inventory\n**.s k [amount]** to store Kreditter\n**.s ik [amount]** to store Imperille Kreditter\n**.s ss [amount]** to store Skindene Sten\n \n use .t to take currency from storage. To take items, react in {inventory_name}\'s inventory")            




def setup(bot):
    bot.add_cog(InventoryAdd(bot))

