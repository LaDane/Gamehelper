import discord
import json
import asyncio
from discord.ext import commands
from filehandler import FileHandler
from jsonhandler import JsonHandler

fh = FileHandler()
jh = JsonHandler()

class StockRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
        # self.worlditems = fh.load_file('worlditems')
        # self.currency = fh.load_file('currency')
        self.shops = fh.load_file('shops')

    def s_bsm_id(self):
        return jh.show_BuyStockMsgID()


# Remove stock from shop inventory with "end" reaction
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
            # print("bot reacted")
            return
        if str(user_reaction_msg_id) not in str(buy_stock_msg_id): # In this case, the reaction was given to a message not in BuyStockMsgID
            # print("not in buy msg id")
            return 
        if str(user_reaction_msg_id) in str(buy_stock_msg_id): # In this case the reaction is given to a message in BuyStockMsgID
            # print("succes!")

            reaction = str(payload.emoji.name)
            
            if reaction == "\U0001F51A": # End emoji - :end: 
                # print("reaction is End")

                msg_id = user_reaction_msg_id
                channel = guild.get_channel(payload.channel_id)

                try:
                    msg = await channel.fetch_message(msg_id)
                    await msg.delete()
                except:
                    print("Message deletion failed")

                self.load_data()

                for title, value in self.shops.items():
                    # print_str += f"{title} -\n"
                    for sid, items in value['Stock'].items():
                        if items['BuyStockMsgID'] == payload.message_id:
                            del self.shops[title]['Stock'][sid]
                            fh.save_file(self.shops, 'shops')
                            # print("This is END")
                            # print (sid)
                            break
                        # _ = sid # this sets it to nothing and we have no problems in code



            # else:
            #     print("Emoji was not end")
        else:
            print("something failed in detecting reaction :o")



def setup(bot):
    bot.add_cog(StockRemove(bot))


# ==================
# JUNK
# ==================

    # def show_BuyStockMsgID(self): # This function is for when you would like to display shop BuyStockMsgID in shops.json
    #     print_str = ""
    #     for title, value in self.shops.items():
    #         _ = title
    #         # print_str += f"{title} -\n"
    #         for sid, items in value['Stock'].items():
    #             print_str += f"{items['BuyStockMsgID']}\n"
    #             _ = sid # this sets it to nothing and we have no problems in code
    #     return print_str


# # FOR TESTING
#     @commands.Cog.listener()
#     async def on_message(self, message):
#         if message.channel.id == 699194951535427635: # Channel id of "shop-editor"
#             if message.content.startswith('test'):
#                 channel = message.channel
#                 await channel.send(self.show_BuyStockMsgID())


# #for testing is the bot reacted
#     @commands.Cog.listener()
#     async def on_message(self, message):
#         if message.channel.id == 698522831083929734: # general channel for testing
#             if message.content.startswith('test'):
#                 channel = self.bot.get_channel(698522831083929734) # general channel for testing
#                 bot_react_msg = await channel.send("Bot will react to this message")
#                 await bot_react_msg.add_reaction(emoji='\U0001F51A')

