import discord
import json
import asyncio
from discord.ext import commands
from filehandler import FileHandler
from jsonhandler import JsonHandler

fh = FileHandler()
jh = JsonHandler()



class CharacterRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
        self.characterinventory = fh.load_file('characterinventory')
        self.currency = fh.load_file('currency')
        self.charactersheet = fh.load_file('charactersheet')

    def s_c_t_v(self):
        return jh.show_currency_titles_values()

# Remove a shop, including deletion of channels and category
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 700842187058970624: # Channel id of "inventory-editor"
            if message.content.startswith('removecharacter'):
                channel = message.channel
                await channel.purge(limit=10)
                self.load_data()

                try:
                    await channel.send(f"{self.s_c_t_v()}")
                    msg1 = await channel.send("-\nAbove is a list of registered characters\nThe numbers in bold are the character ID's\nType the character ID that you would like to delete")

                    await msg1.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                    await asyncio.sleep(1)

                    msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                    character_id = msg.content
                    await asyncio.sleep(1)
                    print(character_id)

                    if character_id == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                    if not character_id in self.characterinventory:
                        await channel.purge(limit=10)
                        await channel.send("You have entered a S-ID that's not registered. Make sure that the entered text is an **exact** match to a shops ID")    
                    if character_id in self.characterinventory:
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

                            character_sheet_channel = self.charactersheet[character_id]["Character Sheet Channel ID"]
                            inventory_channel = self.characterinventory[character_id]["inventory Channel ID"]
                            category = self.currency[character_id]["Character Category ID"]

                            try:
                                channel = self.bot.get_channel(character_sheet_channel) # Channel id of character sheet
                                await channel.delete()
                            except:
                                print("No character sheet channel exists for this id") 

                            try:
                                channel = self.bot.get_channel(inventory_channel) # Channel id of character sheet
                                await channel.delete()
                            except:
                                print("No inventory channel exists for this id") 

                            try:
                                category = self.bot.get_channel(category) # Category id of the character
                                await category.delete()
                            except:
                                print("No category exists for this channel")      

                            try:
                                del self.charactersheet[character_id]  
                            except:
                                print("charactersheet deletion failed")

                            try:
                                del self.characterinventory[character_id]  
                            except:
                                print("characterinventory deletion failed")
                            
                            try:
                                del self.currency[character_id]            
                            except:
                                print("currency deletion failed")

                            fh.save_file(self.characterinventory, 'characterinventory')
                            fh.save_file(self.currency, 'currency')
                            fh.save_file(self.charactersheet, 'charactersheet')

                            await channel.purge(limit=10)
                            await channel.send(f"Character ID [{character_id}] has successfully been deleted from dictionary.")
                except:
                    await channel.send("*No characters registered yet*\n**Please set up a character before removing it!**")



def setup(bot):
    bot.add_cog(CharacterRemove(bot))
