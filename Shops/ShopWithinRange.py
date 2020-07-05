import discord
from discord.ext import commands
from discord.utils import get
from filehandler import FileHandler

fh = FileHandler()

class ShopWithinRange(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
        result = fh.load_file('rangecheck')
        if result != None:
            self.shop_withing_range_msg_id = result['id']


# range check bot message
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def shopwithinrange(self, ctx):
        channel = ctx.channel
        await channel.purge(limit=1)
        shop_withing_range_msg = await ctx.send("When players are within range of a shop and should be able to sell items\nReact to this message with:\n \n:dvd: for **Kreditter**\n:cd: for **Imperille Kreditter**\n:new_moon: for **Skindene Sten**\n \nOnce players have left the shop and no longer should be able to sell\nRemove your reaction below")
        await shop_withing_range_msg.add_reaction(emoji='\U0001F4C0') # dvd
        await shop_withing_range_msg.add_reaction(emoji='\U0001F4BF') # cd
        await shop_withing_range_msg.add_reaction(emoji='\U0001F311') # moon
        self.shop_withing_range_msg_id = shop_withing_range_msg.id
        fh.save_file({'id': self.shop_withing_range_msg_id}, 'rangecheck')



# Reaction Role add
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload): 

        guild = self.bot.get_guild(payload.guild_id)  # You need the guild to get the member who reacted
        member = guild.get_member(payload.user_id)  # the member who reacted to a role
        member_id = member.id # used to check if bot reacted
        botcheck = 698545737880961074 # used to check if bot reacted

        if not payload.guild_id: # In this case, the reaction was added in a DM channel with the bot
            return
        if member_id == botcheck: # In this case, the bot reacted to a message
            return
        if payload.message_id != self.shop_withing_range_msg_id: # ID of the message you want reactions added to.
            return
        if payload.message_id == self.shop_withing_range_msg_id: # ID of the message you want reactions added to.
            reaction = str(payload.emoji.name)

            if reaction == "\U0001F4C0": # dvd
                role = discord.utils.get(guild.roles, name='CanSell Kreditter')
                role2 = discord.utils.get(guild.roles, name='CanSell')
                for guild in self.bot.guilds:
                    for member in guild.members:
                        await member.add_roles(role, role2)

            if reaction == "\U0001F4BF": # cd
                role = discord.utils.get(guild.roles, name='CanSell ImperilleKreditter')
                role2 = discord.utils.get(guild.roles, name='CanSell')
                for guild in self.bot.guilds:
                    for member in guild.members:
                        await member.add_roles(role, role2)

            if reaction == "\U0001F311": # moon
                role = discord.utils.get(guild.roles, name='CanSell SkindeneSten')
                role2 = discord.utils.get(guild.roles, name='CanSell')
                for guild in self.bot.guilds:
                    for member in guild.members:
                        await member.add_roles(role, role2)

# Reaction Role remove
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload): 

        guild = self.bot.get_guild(payload.guild_id)  # You need the guild to get the member who reacted
        member = guild.get_member(payload.user_id)  # the member who reacted to a role
        member_id = member.id # used to check if bot reacted
        botcheck = 698545737880961074 # used to check if bot reacted

        if not payload.guild_id: # In this case, the reaction was added in a DM channel with the bot
            return
        if member_id == botcheck: # In this case, the bot reacted to a message
            return
        if payload.message_id != self.shop_withing_range_msg_id: # ID of the message you want reactions added to.
            return
        if payload.message_id == self.shop_withing_range_msg_id: # ID of the message you want reactions added to.
            reaction = str(payload.emoji.name)

            if reaction == "\U0001F4C0": # dvd
                role = discord.utils.get(guild.roles, name='CanSell Kreditter')
                role2 = discord.utils.get(guild.roles, name='CanSell')
                for guild in self.bot.guilds:
                    for member in guild.members:
                        await member.remove_roles(role, role2)

            if reaction == "\U0001F4BF": # cd
                role = discord.utils.get(guild.roles, name='CanSell ImperilleKreditter')
                role2 = discord.utils.get(guild.roles, name='CanSell')
                for guild in self.bot.guilds:
                    for member in guild.members:
                        await member.remove_roles(role, role2)

            if reaction == "\U0001F311": # moon
                role = discord.utils.get(guild.roles, name='CanSell SkindeneSten')
                role2 = discord.utils.get(guild.roles, name='CanSell')
                for guild in self.bot.guilds:
                    for member in guild.members:
                        await member.remove_roles(role, role2)


def setup(bot):
    bot.add_cog(ShopWithinRange(bot))