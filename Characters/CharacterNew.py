import discord
import json
import asyncio
from discord.ext import commands
from filehandler import FileHandler
from jsonhandler import JsonHandler

fh = FileHandler()
jh = JsonHandler()






class CharacterNew(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
        self.characterinventory = fh.load_file('characterinventory')
        self.currency = fh.load_file('currency')
        self.charactersheet = fh.load_file('charactersheet')
        # self.shops = fh.load_file('shops')


# New character command
    @commands.command()
    async def newcharacter(self, message):
        if message.channel.id == 700719183184527380: # Channel id of "welcome"
            channel = self.bot.get_channel(700719183184527380)  # Channel id of "welcome"
            await channel.purge(limit=1)
            if message.author == self.bot.user:
                return
            self.load_data()
            author_id = str(message.author.id)

# setup user currency
            if not author_id in self.currency:
                guild = message.guild

                member = guild.get_member(message.author.id)
                member_nick = member.nick
# create role
                await guild.create_role(name=member_nick)
                await asyncio.sleep(1)
                member_role = discord.utils.get(guild.roles, name=member_nick)
                await asyncio.sleep(1)
                await message.author.add_roles(member_role)
# create category
                
                new_category = await guild.create_category(member_nick)
                new_category_id = new_category.id

                await asyncio.sleep(2)
                await new_category.edit(position=2)

                category_channel = self.bot.get_channel(new_category_id)

                gm_role = discord.utils.get(guild.roles, name='GM')
                players_role = discord.utils.get(guild.roles, name='Players')
                character_sheet_channel = await guild.create_text_channel('character-sheet', category=category_channel)
                await character_sheet_channel.set_permissions(member_role, read_messages=True, send_messages=True)
                await character_sheet_channel.set_permissions(gm_role, read_messages=True, send_messages=True)
                await character_sheet_channel.set_permissions(players_role, read_messages=False, send_messages=False)
                await character_sheet_channel.set_permissions(guild.default_role, read_messages=False, send_messages=False)
                                                      
                character_sheet_channel_id = character_sheet_channel.id

                inventory_channel = await guild.create_text_channel('inventory', category=category_channel)
                await inventory_channel.set_permissions(member_role, read_messages=True, send_messages=True)
                await inventory_channel.set_permissions(gm_role, read_messages=True, send_messages=True)
                await inventory_channel.set_permissions(players_role, read_messages=False, send_messages=False)
                await inventory_channel.set_permissions(guild.default_role, read_messages=False, send_messages=False)

                inventory_channel_id = inventory_channel.id
                                        
                self.currency[author_id] = {}
                self.currency[author_id]["User"] = f"{message.author}"
                self.currency[author_id]["Character"] = f"{message.author.nick}"
                self.currency[author_id]["Kreditter"] = 0
                self.currency[author_id]["Imperille Kreditter"] = 0
                self.currency[author_id]["Skindene Sten"] = 0
                self.currency[author_id]["Inventory Channel ID"] = inventory_channel_id
                self.currency[author_id]["Character Category ID"] = new_category_id

                currency_embed = discord.Embed(title=f"{message.author.nick}\'s coin bag.",color=0xffd700)
                currency_embed.add_field(name="Kreditter", value=self.currency[author_id]["Kreditter"])
                currency_embed.add_field(name="Imperille Kreditter", value=self.currency[author_id]["Imperille Kreditter"])
                currency_embed.add_field(name="Skindene Sten", value=self.currency[author_id]["Skindene Sten"])
                currency_embed_msg = await inventory_channel.send(embed=currency_embed)
                currency_embed_msg_id = currency_embed_msg.id
                self.currency[author_id]["Currency Embed ID"] = currency_embed_msg_id
                fh.save_file(self.currency, 'currency')

# setup user inventory
                if not author_id in self.characterinventory:
                    self.characterinventory[author_id] = {}
                    self.characterinventory[author_id]["User"] = f"{message.author}"
                    self.characterinventory[author_id]["Character"] = f"{message.author.nick}"
                    self.characterinventory[author_id]["inventory Channel ID"] = inventory_channel_id
                    self.characterinventory[author_id]["Used slots"] = 0
                    self.characterinventory[author_id]["Bag slots"] = 50

                    inventory_embed = discord.Embed(title=f"{message.author.nick}\'s backpack",color=0x8B4513)
                    inventory_embed.add_field(name="Bag slots", value=f"{self.characterinventory[author_id]['Used slots']} / {self.characterinventory[author_id]['Bag slots']}", inline=False)
                    inventory_embed_msg = await inventory_channel.send(embed=inventory_embed)
                    inventory_embed_msg_id = inventory_embed_msg.id
                    self.characterinventory[author_id]["Backpack Embed ID"] = inventory_embed_msg_id                    
                    self.characterinventory[author_id]["Inventory"] = {}
                    fh.save_file(self.characterinventory, 'characterinventory')

# setup character sheet    
                    if not author_id in self.charactersheet:
                        self.charactersheet[author_id] = {}
                        self.charactersheet[author_id]["User"] = f"{message.author}"
                        self.charactersheet[author_id]["Character"] = f"{message.author.nick}"
                        self.charactersheet[author_id]["Character Sheet Channel ID"] = character_sheet_channel_id
                        self.charactersheet[author_id]["Character Sheet"] = {}
                        fh.save_file(self.charactersheet, 'charactersheet')

                        channel = self.bot.get_channel(700719183184527380)  # Channel id of "welcome"
                        await channel.send(f"**New character created!**\nPlease go to your newly created '**{message.author.nick}**' category and fill out your character sheet, in the **character-sheet** channel!")
                        await asyncio.sleep(2)
                        await channel.purge(limit=1)

                        channel = self.bot.get_channel(character_sheet_channel_id)
                        await channel.send(f"Type ''**.cs**'' to create your character sheet!")

                    else:
                        print("author_id already in charactersheet.json")
                else:
                    print("author_id already in characterinventory.json")                    
            else:
                print("author_id already in currency.json")
                channel = self.bot.get_channel(700719183184527380)  # Channel id of "welcome"
                await channel.send("You already have a character registered!")
                return


def setup(bot):
    bot.add_cog(CharacterNew(bot))

