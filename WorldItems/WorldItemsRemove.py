import discord
import json
import asyncio
from discord.ext import commands
from filehandler import FileHandler

fh = FileHandler()


class WorldItemsRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
        self.users = fh.load_file('worlditems')
       

# Remove a world item
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 698570403542728714: # Channel id of "item-editor"
            if message.content.startswith('removeitem'):
                # await asyncio.sleep(1)
                channel = message.channel
                await channel.purge(limit=10)
                await channel.send("Type the W-ID number of the item you want to remove")

                self.load_data()

                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                rworldid = msg.content

                if not rworldid in self.users:
                    await channel.purge(limit=10)
                    await channel.send("You have entered a W-ID that's not registered. Check items-in-world channel for W-ID\'s")
                if rworldid in self.users:
                    await channel.purge(limit=10)
                    await channel.send(f"Are you sure you want to delete W-ID **[{rworldid}]**?\n**yes** or **no**")

                    msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)
                    response = msg.content

                    if response == "no":
                        await channel.purge(limit=10)
                        await channel.send("Canceling request")
                    
                    if response == "yes":
                        msg_id = self.users[rworldid]["ItemsInWorldMsgID"]
                        channel = self.bot.get_channel(698570643976880260) # Channel id of "items-in-world"

                        try:
                            msg = await channel.fetch_message(msg_id)
                            await msg.delete()
                        except:
                            print("Item has no message in channel: items-in-world")


                        channel = self.bot.get_channel(698570403542728714) # Channel id of "remove-items-in-world"
                        del self.users[rworldid]
                        fh.save_file(self.users, 'worlditems')
                        await channel.purge(limit=10)
                        await channel.send(f"W-ID [{rworldid}] has successfully been deleted from dictionary.")



def setup(bot):
    bot.add_cog(WorldItemsRemove(bot))


#===============
#JUNK
#===============
                        
    # @commands.command()
    # @commands.has_permissions(manage_messages=True)
    # async def clear(self, ctx, amount: int):
    #     await ctx.channel.purge(limit=amount +1)
    #     await ctx.send(f"{amount} messages got deleted")

                    
                    # if response == "yes":
                    #     msg_id = self.users[rworldid]["ItemsInWorldMsgID"]
                    #     channel = self.bot.get_channel(698570643976880260)

                    #     msg = await channel.fetch_message(msg_id)
                    #     await msg.delete()

                    #     # await message.delete()
                    #     channel = self.bot.get_channel(698571992168660992)
                    #     del self.users[rworldid]
                    #     fh.save_file(self.users, 'worlditems')
                    #     await channel.send(f"W-ID [{rworldid}] has successfully been deleted from dictionary.")


                
