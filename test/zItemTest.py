import discord
from discord.ext import commands

class zItemTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # test embed
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def testitem(self, ctx):
        embed = discord.Embed(title="**Bang På Pind**", description="**En lille granat monteret på en pind**\n*+1 Ranged Weapons*", color=discord.Color.red())
        embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/698562251246010468/unknown.png?width=1132&height=637")
        embed.set_footer(text="W-ID [ 17 ]")

        embed.add_field(name="Type", value="consumable")
        embed.add_field(name="Weight", value="**1** slot")
        embed.add_field(name="Value", value="**5** credits")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(zItemTest(bot))