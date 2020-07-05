import discord
import json
import asyncio
from discord.ext import commands
from filehandler import FileHandler
from jsonhandler import JsonHandler

fh = FileHandler()
jh = JsonHandler()



class ReactPlus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
        self.worlditems = fh.load_file('worlditems')
        # self.currency = fh.load_file('currency')
        self.shops = fh.load_file('shops')

    def s_bsm_id(self):
        return jh.show_BuyStockMsgID()

    def s_bsm_e(self):
        return jh.show_BuyStockMsgEmbed()


# Add 1 to stock with "HEAVY PLUS SIGN" reaction
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        self.load_data()
        buy_stock_msg_id = self.s_bsm_id()
        user_reaction_msg_id = payload.message_id

        guild = self.bot.get_guild(payload.guild_id)  # You need the guild to get the member who reacted
        member = guild.get_member(payload.user_id)  # the member who reacted to a role
        member_id = member.id # used to check if bot reacted
        botcheck = 698545737880961074 # used to check if bot reacted


        if not payload.guild_id: # In this case, the reaction was added in a DM channel with the bot
            return
        if member_id == botcheck: # In this case, the bot reacted to a message
            return
        if str(user_reaction_msg_id) not in str(buy_stock_msg_id): # In this case, the reaction was given to a message not in BuyStockMsgID
            return 
        if str(user_reaction_msg_id) in str(buy_stock_msg_id): # In this case the reaction is given to a message in BuyStockMsgID

            reaction = str(payload.emoji.name)
            
            if reaction == "\u2795": # Heavy Plus Sign - :heavy_plus_sign: 
                self.load_data()

                titles = []
                sids = []

                for title, value in self.shops.items():
                    for sid, items in value['Stock'].items():
                        if items['BuyStockMsgID'] == payload.message_id:
                            titles.append(title)
                            sids.append(sid)
                            break
                
                title = ''.join(titles)
                sid = ''.join(sids)

                worldid = self.shops[title]['Stock'][sid]["WorldID"]
                guild = self.bot.get_guild(payload.guild_id)
                buy_channel_id = self.shops[title]['ShopBuyID']
                channel = guild.get_channel(buy_channel_id)
                message_id = self.shops[title]['Stock'][sid]["BuyStockMsgID"]
                user_msg = await channel.fetch_message(message_id)

                stock_embed = discord.Embed(title=f"**{self.worlditems[worldid]['ItemName']}**", description=f"*{self.worlditems[worldid]['Description']}*", color=discord.Color.red())
                stock_embed.set_image(url=f"{self.worlditems[worldid]['Picture']}")
                stock_embed.set_footer(text=f"W-ID [{worldid}]\nSE-ID [{sid}]")
                stock_embed.add_field(name="Stats", value=f"{self.worlditems[worldid]['StatsModifier']} {self.worlditems[worldid]['Stats']}", inline=False)
                stock_embed.add_field(name="Type", value=f"{self.worlditems[worldid]['Type']}", inline=True)
                stock_embed.add_field(name="Weight", value=f"{self.worlditems[worldid]['Weight']} slots")
                stock_embed.add_field(name="Value", value=f"{self.worlditems[worldid]['Value']}")
                stock_embed.add_field(name="Amount in stock", value=f"{self.shops[title]['Stock'][sid]['Quantity']}")
                               

                current_value = int(self.shops[title]['Stock'][sid]['Quantity'])
                # print(current_value)
                buy_one_from_stock = 1
                if current_value == 0:
                    return                
                current_value += buy_one_from_stock
                # print(current_value)

                embed_fields = ["Stats", "Type", "Weight", "Value", "Amount in stock"]
                word = "Amount in stock"
                word_index = embed_fields.index(word)

                stock_embed.set_field_at(word_index, name="Amount in stock", value=current_value)
                
                # print("something here")

                self.shops[title]["Stock"][sid]["Quantity"] = current_value
                fh.save_file(self.shops, 'shops')
                await user_msg.edit(embed=stock_embed)

        else:
            print("something failed in detecting reaction :o")


def setup(bot):
    bot.add_cog(ReactPlus(bot))

