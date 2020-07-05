import discord
import json
import asyncio
from discord.ext import commands
from filehandler import FileHandler
from jsonhandler import JsonHandler

jh = JsonHandler()
fh = FileHandler()


class ShopsAdd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
        # self.worlditems = fh.load_file('worlditems')
        # self.currency = fh.load_file('currency')
        self.shops = fh.load_file('shops')

    def s_s_t(self):
        return jh.show_shop_titles()

# Create a new shop with own category and and channels
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 699194951535427635: # Channel id of "shop-editor"
            if message.content.startswith('newshop'):
                self.load_data()
                channel = message.channel
                await channel.purge(limit=10)

                try:
                    await channel.send(f"{self.s_s_t()}")
                except:
                    await channel.send("No shops set up")

                msg1 = await channel.send("-\nAbove is a list of registered [S-ID]\nType the **unique** name of the new shop you want to make\nThis will be the Shop-ID [S-ID], so dont make it too complicated for when you need to access it again")

                await msg1.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)

                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                shopid = msg.content

                if shopid == "cancel":                         # Takes use of CancelMenu cog
                    await channel.purge(limit=10)
                    await channel.send("Command canceled!")
                    return
                if shopid in self.shops:
                    await channel.purge(limit=5)
                    await channel.send("You have entered a shop ID that's already been registered.")
                if not shopid in self.shops:
                    await asyncio.sleep(1)
                    await channel.purge(limit=5)
                    msg2 = await channel.send(f"**{shopid}** is being registered as a shop.\nWhat is the name of the shop owner?")

                    await msg2.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                    await asyncio.sleep(1)                    

                    msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                    shopowner = msg.content

                    if shopowner == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return

                    await asyncio.sleep(1)
                    await channel.purge(limit=5)
                    shopcurrency_msg = await channel.send(f"**{shopowner}** is the owner of **{shopid}**.\nReact with the currency that the shop trades in;\n:dvd: for **Kreditter**\n:cd: for **Imperille Kreditter**\n:new_moon: for **Skindene Sten**")
                    await shopcurrency_msg.add_reaction(emoji='\U0001F4C0') # dvd
                    await shopcurrency_msg.add_reaction(emoji='\U0001F4BF') # cd
                    await shopcurrency_msg.add_reaction(emoji='\U0001F311') # moon

                    await asyncio.sleep(1)

                    res = await self.bot.wait_for('reaction_add')
                    if res:
                        reaction, message.author = res
                        if str(reaction.emoji) == "\U0001F4C0":
                            currency_chosen = "Kreditter"
                        if str(reaction.emoji) == "\U0001F4BF":
                            currency_chosen = "Imperille Kreditter"
                        if str(reaction.emoji) == "\U0001F311":
                            currency_chosen = "Skindene Sten"

                    await asyncio.sleep(1)
                    await channel.purge(limit=5)
                    msg3 = await channel.send(f"**{shopid}** will trade in currency **{currency_chosen}**\nEnter a picture url of the shop/owner\nEx\nhttps://media.discordapp.net/attachments/698522831083929734/698562251246010468/unknown.png?width=1132&height=0")

                    await msg3.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                    await asyncio.sleep(1) 

                    msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                    picture = msg.content

                    if picture == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return

                    await asyncio.sleep(1)

                    guild = message.guild

                    new_channel = await guild.create_category(shopid)
                    new_channel_id = new_channel.id

                    category_channel = self.bot.get_channel(new_channel_id)                    

                    buy_channel = await guild.create_text_channel('buy', category=category_channel)
                    buy_channel_id = buy_channel.id
# Channel permissions
                    gm_role = discord.utils.get(guild.roles, name='GM')
                    players_role = discord.utils.get(guild.roles, name='Players')
                    await buy_channel.set_permissions(gm_role, read_messages=True, send_messages=True)
                    await buy_channel.set_permissions(players_role, read_messages=False, send_messages=False)
                    await buy_channel.set_permissions(guild.default_role, read_messages=False, send_messages=False)


                    self.shops[shopid] = {}
                    self.shops[shopid]["ShopOwner"] = shopowner
                    self.shops[shopid]["ShopCurrency"] = currency_chosen
                    self.shops[shopid]["ShopPicture"] = picture
                    self.shops[shopid]["Stock"] = {}
                    self.shops[shopid]["ShopCategoryID"] = new_channel_id
                    self.shops[shopid]["ShopBuyID"] = buy_channel_id

                    fh.save_file(self.shops, 'shops')


                    await channel.purge(limit=5)
                    await channel.send(f"**{shopid}** has succesfully completed newshop setup!\n**{shopowner}** is now ready to stock world items in shelves!")


                    embed = discord.Embed(title=f"**{shopid}**", description=f"Welcome to **{shopowner}\'s** shop!\n \nThe currency accepted here is\n**{self.shops[shopid]['ShopCurrency']}**", color=0x303136)
                    embed.set_image(url=f"{picture}")
                    embed.set_footer(text=f"S-ID [{shopid}]")
                    await channel.send(embed=embed)

                    channel = self.bot.get_channel(buy_channel_id)
                    embed = discord.Embed(title=f"**{shopid}**", description=f"Welcome to **{shopowner}\'s** shop!\n \nThe currency accepted here is\n**{self.shops[shopid]['ShopCurrency']}**\n \nBrowse his items below", color=0x303136)
                    embed.set_image(url=f"{picture}")
                    embed.set_footer(text=f"S-ID [{shopid}]")
                    await channel.send(embed=embed)



def setup(bot):
    bot.add_cog(ShopsAdd(bot))

