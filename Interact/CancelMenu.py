import discord

from discord.utils import get
from discord.ext import commands


class CancelMenu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# If two stopsign reactions are given on a message, bot will send "cancel" to cancel interface menu
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        
        if payload.emoji.name == '\U0001F6D1':
            guild = self.bot.get_guild(payload.guild_id)  # You need the guild to get the member who reacted
            channel = guild.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)                      
            reaction = get(message.reactions, emoji=payload.emoji.name)
            if reaction and reaction.count > 1:
                await channel.send("cancel")



def setup(bot):
    bot.add_cog(CancelMenu(bot))


# ===================
# JUNK
# ===================

# Remove a shop, including deletion of channels and category            ATTEMPT 5
    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     if message.channel.id == 699194951535427635: # Channel id of "shop-editor"
    #         if message.content.startswith('test'):
    #             channel = message.channel
    #             await channel.purge(limit=10)

    #             msg1 = await channel.send("-\nAbove is a list of registered [S-ID]\nType the S-ID of the shop you want to remove")

    #             await msg1.add_reaction(emoji='\U0001F6D1')
    #             await asyncio.sleep(1)
                

    #             msg1_id = msg1.id
    #             channel_id = channel.id
    #             cache_msg = await channel_id.fetch_message(msg1_id)
    #             print(cache_msg)
    #             for reactor in cache_msg.reactions:
    #                 reactors = await self.bot.get_reaction_users(reactor)

    #                 #from here you can do whatever you need with the member objects
    #                 for member in reactors:
    #                     await channel.send(member.name)




                # reply = ""                                                                    ATTEMPT 4
                # reactions = msg1.reactions
                # for reaction in reactions:
                #     if (reaction.emoiji.name == '\U0001F6D1'):
                #         users = reaction.users
                #         async for user in users:
                #             reply += "<@" + str(user.id) + ">"
                #         # break
                        
                # print(reply)
                # await channel.send(f"{reply}")
                # msg2 = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                # rshopid = msg2.content
                # await channel.send(f"{rshopid}")





                # check = lambda reaction, user: message.author != user                         ATTEMPT 3
                # while True:
                #     res = await self.bot.wait_for('reaction_add', check=lambda reaction, user: message.author != user)
                #     msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                #     if res:
                #         reaction, message.author = res
                #         if str(reaction.emoji) == '\U0001F6D1':
                #             await channel.purge(limit=10)
                #             await channel.send("Canceling request")
                #             return
                #     if msg:
                #         await channel.send("Continue")
                #         rshopid = msg.content
                #         await channel.send(f"{rshopid}")
                # _ = check






                # reaction = str(payload.emoji.name)         ATTEMPT 1
                # if reaction == "\U0001F6D1":
                #     await channel.purge(limit=10)
                #     await channel.send("Canceling request")                




 
                # res = await self.bot.wait_for('reaction_add')          ATTEMPT 2
                # if res:
                #     reaction, message.author = res
                #     if str(reaction.emoji) == '\U0001F6D1':
                #         await channel.purge(limit=10)
                #         await channel.send("Canceling request")
                #         return


                # # msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                
                # msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                # if msg:
                #     await channel.send("Continue")
                #     rshopid = msg.content
                #     await channel.send(f"{rshopid}")




                # else:
                # await channel.send("Continue")

                # msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                # rshopid = msg.content
                # await asyncio.sleep(1)

                # await channel.send(f"{rshopid}")
