import discord
import asyncio
from discord.ext import commands



# five_letter_words = [str:ctx.message]  # Made the variable name a plural

class zEmbedTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def testembed(self, ctx):

        five_letter_words = [str(ctx.message)]  # Made the variable name a plural


    # channel = self.bot.get_channel(698522831083929734) # Change channel id to general channel
        # print("testembed")
        user_msg_embed = discord.Embed(color=0x0000ff)
        user_msg_embed.add_field(name="\u200b", value="\u200b", inline=True)
        user_msg = await ctx.send(embed=user_msg_embed)

# Function now outside of the while loop
# Will also now return false if the message isn't 5 characters long
# This will also not delete messages with more or less than five characters - if you want it to do that then you'll have to change that for yourself

        def check(m):
            if len(m.content) == 5:
                print(f"{m.author} Word Is: {m.content}")
                return True
            return False

        game_embed = discord.Embed(color=discord.Color.red())

        # print(game_embed)

        while not self.bot.is_closed():
            try:
                msg = await self.bot.wait_for("message", check=check, timeout=10)
                try: await msg.delete()
                except Exception: pass
                try:
                    word = msg.content.lower()
                    if word not in five_letter_words:
                        game_embed.add_field(name=f"Word: {word}",value=f"{msg.author.mention}")
                        await user_msg.edit(embed=game_embed)  # You want to edit the embed you already sent
                        five_letter_words.append(word)
                    elif word in five_letter_words:
                        word_index = five_letter_words.index(word)  # See when you added the word to your list
                        current_value = game_embed.fields[word_index].value  # Get the value from the field
                        game_embed.set_field_at(word_index, name=f"Word: {word}", value=current_value + f"\n{msg.author.mention}")
                        await user_msg.edit(embed=game_embed)  # Send updated embed

                        print(f"This is word index \n{word_index}")

                except IndexError:
                    print("Error Index")
            except asyncio.TimeoutError:
                print("Stopped - timeout error")




def setup(bot):
    bot.add_cog(zEmbedTest(bot))

