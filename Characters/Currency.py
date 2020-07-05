import discord
import json
import asyncio
from discord.ext import commands
from filehandler import FileHandler

fh = FileHandler()


class Currency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
        self.currency = fh.load_file('currency')

# check a characters coin bag
    @commands.command()
    async def cb(self, ctx, member: discord.Member = None):
        if ctx.channel.id == 698671535606595595: # Channel id of "economy"
            channel = ctx.channel
            await channel.purge(limit=1)
            self.load_data()

            member = ctx.author if not member else member
            member_id = str(member.id)

            if not member_id in self.currency:
                await ctx.send("Member doesnt have a coin bag")
            else:
                embed = discord.Embed(title=f"{member.nick}\'s coin bag.",color=0xffd700)
                embed.add_field(name="Kreditter", value=self.currency[member_id]["Kreditter"])
                embed.add_field(name="Imperille Kreditter", value=self.currency[member_id]["Imperille Kreditter"])
                embed.add_field(name="Skindene Sten", value=self.currency[member_id]["Skindene Sten"])
                await ctx.send(embed=embed)


#===================================
# ADDING AND REMOVING currency from characters coin bag
#===================================

# ADD "Kreditter" to a characters coin bag
    @commands.command()
    async def addk(self, ctx, amount: int, member: discord.Member = None):
        if ctx.channel.id == 698671535606595595: # Channel id of "economy"
            channel = ctx.channel
            await channel.purge(limit=1)
            self.load_data()

            member = ctx.author if not member else member
            primary_id = str(member.id)
            self.currency[primary_id]["Kreditter"] += amount
            await ctx.send(f"Added **{amount}** Kreditter to {member.nick}\'s coin bag.\n{member.nick} now has **{self.currency[primary_id]['Kreditter']}** Kreditter.")
# Update inventory Coin bag                        
            for title, value in self.currency.items():
                _ = value
                if title == primary_id:
                    inventory_channel_id = self.currency[title]['Inventory Channel ID']
                    embed_id = self.currency[title]['Currency Embed ID']
                # break

            guild = self.bot.get_guild(698522830525956097) # DnD Vandvejen discord ID
            channel = guild.get_channel(inventory_channel_id)
            user_msg = await channel.fetch_message(embed_id)

            current_value = int(self.currency[primary_id]['Kreditter'])

            embed_fields = ["Kreditter", "Imperille Kreditter", "Skindene Sten"]
            word = "Kreditter"
            word_index = embed_fields.index(word)

            currency_embed = discord.Embed(title=f"{member.nick}\'s coin bag.",color=0xffd700)
            currency_embed.add_field(name="Kreditter", value=self.currency[primary_id]["Kreditter"])
            currency_embed.add_field(name="Imperille Kreditter", value=self.currency[primary_id]["Imperille Kreditter"])
            currency_embed.add_field(name="Skindene Sten", value=self.currency[primary_id]["Skindene Sten"])

            currency_embed.set_field_at(word_index, name="Kreditter", value=current_value)
            await user_msg.edit(embed=currency_embed)

            fh.save_file(self.currency, 'currency')

# REMOVE "Kreditter" from a characters coin bag
    @commands.command()
    async def remk(self, ctx, amount: int, member: discord.Member = None):
        if ctx.channel.id == 698671535606595595: # Channel id of "economy"
            channel = ctx.channel
            await channel.purge(limit=1)
            self.load_data()

            member = ctx.author if not member else member
            primary_id = str(member.id)
            self.currency[primary_id]["Kreditter"] -= amount
            await ctx.send(f"Removed **{amount}** Kreditter from {member.nick}\'s coin bag.\n{member.nick} now has **{self.currency[primary_id]['Kreditter']}** Kreditter.")
# Update inventory Coin bag
            for title, value in self.currency.items():
                _ = value
                if title == primary_id:
                    inventory_channel_id = self.currency[primary_id]['Inventory Channel ID']
                    embed_id = self.currency[primary_id]['Currency Embed ID']
                    break

            guild = self.bot.get_guild(698522830525956097) # DnD Vandvejen discord ID
            channel = guild.get_channel(inventory_channel_id)
            user_msg = await channel.fetch_message(embed_id)

            current_value = int(self.currency[primary_id]['Kreditter'])

            embed_fields = ["Kreditter", "Imperille Kreditter", "Skindene Sten"]
            word = "Kreditter"
            word_index = embed_fields.index(word)

            currency_embed = discord.Embed(title=f"{member.nick}\'s coin bag.",color=0xffd700)
            currency_embed.add_field(name="Kreditter", value=self.currency[primary_id]["Kreditter"])
            currency_embed.add_field(name="Imperille Kreditter", value=self.currency[primary_id]["Imperille Kreditter"])
            currency_embed.add_field(name="Skindene Sten", value=self.currency[primary_id]["Skindene Sten"])

            currency_embed.set_field_at(word_index, name="Kreditter", value=current_value)
            await user_msg.edit(embed=currency_embed)

            fh.save_file(self.currency, 'currency')

# ADD "Imperille Kreditter" to a characters coin bag
    @commands.command()
    async def addik(self, ctx, amount: int, member: discord.Member = None):
        if ctx.channel.id == 698671535606595595: # Channel id of "economy"
            channel = ctx.channel
            await channel.purge(limit=1)
            self.load_data()

            member = ctx.author if not member else member
            primary_id = str(member.id)
            self.currency[primary_id]["Imperille Kreditter"] += amount
            await ctx.send(f"Added **{amount}** Imperille Kreditter to {member.nick}\'s coin bag.\n{member.nick} now has **{self.currency[primary_id]['Imperille Kreditter']}** Imperille Kreditter.")
# Update inventory Coin bag                                    
            for title, value in self.currency.items():
                _ = value
                if title == primary_id:
                    inventory_channel_id = self.currency[primary_id]['Inventory Channel ID']
                    embed_id = self.currency[primary_id]['Currency Embed ID']
                    break

            guild = self.bot.get_guild(698522830525956097) # DnD Vandvejen discord ID
            channel = guild.get_channel(inventory_channel_id)
            user_msg = await channel.fetch_message(embed_id)

            current_value = int(self.currency[primary_id]['Imperille Kreditter'])

            embed_fields = ["Kreditter", "Imperille Kreditter", "Skindene Sten"]
            word = "Imperille Kreditter"
            word_index = embed_fields.index(word)

            currency_embed = discord.Embed(title=f"{member.nick}\'s coin bag.",color=0xffd700)
            currency_embed.add_field(name="Kreditter", value=self.currency[primary_id]["Kreditter"])
            currency_embed.add_field(name="Imperille Kreditter", value=self.currency[primary_id]["Imperille Kreditter"])
            currency_embed.add_field(name="Skindene Sten", value=self.currency[primary_id]["Skindene Sten"])

            currency_embed.set_field_at(word_index, name="Imperille Kreditter", value=current_value)
            await user_msg.edit(embed=currency_embed)            
            
            fh.save_file(self.currency, 'currency')

# REMOVE "Imperille Kreditter" from a characters coin bag
    @commands.command()
    async def remik(self, ctx, amount: int, member: discord.Member = None):
        if ctx.channel.id == 698671535606595595: # Channel id of "economy"
            channel = ctx.channel
            await channel.purge(limit=1)
            self.load_data()

            member = ctx.author if not member else member
            primary_id = str(member.id)
            self.currency[primary_id]["Imperille Kreditter"] -= amount
            await ctx.send(f"Removed **{amount}** Imperille Kreditter from {member.nick}\'s coin bag.\n{member.nick} now has **{self.currency[primary_id]['Imperille Kreditter']}** Imperille Kreditter.")
# Update inventory Coin bag            
            for title, value in self.currency.items():
                _ = value
                if title == primary_id:
                    inventory_channel_id = self.currency[primary_id]['Inventory Channel ID']
                    embed_id = self.currency[primary_id]['Currency Embed ID']
                    break

            guild = self.bot.get_guild(698522830525956097) # DnD Vandvejen discord ID
            channel = guild.get_channel(inventory_channel_id)
            user_msg = await channel.fetch_message(embed_id)

            current_value = int(self.currency[primary_id]['Imperille Kreditter'])

            embed_fields = ["Kreditter", "Imperille Kreditter", "Skindene Sten"]
            word = "Imperille Kreditter"
            word_index = embed_fields.index(word)

            currency_embed = discord.Embed(title=f"{member.nick}\'s coin bag.",color=0xffd700)
            currency_embed.add_field(name="Kreditter", value=self.currency[primary_id]["Kreditter"])
            currency_embed.add_field(name="Imperille Kreditter", value=self.currency[primary_id]["Imperille Kreditter"])
            currency_embed.add_field(name="Skindene Sten", value=self.currency[primary_id]["Skindene Sten"])

            currency_embed.set_field_at(word_index, name="Imperille Kreditter", value=current_value)
            await user_msg.edit(embed=currency_embed)              
            
            fh.save_file(self.currency, 'currency')

# ADD "Skindene Sten" to a characters coin bag
    @commands.command()
    async def addss(self, ctx, amount: int, member: discord.Member = None):
        if ctx.channel.id == 698671535606595595: # Channel id of "economy"
            channel = ctx.channel
            await channel.purge(limit=1)
            self.load_data()

            member = ctx.author if not member else member
            primary_id = str(member.id)
            self.currency[primary_id]["Skindene Sten"] += amount
            await ctx.send(f"Added **{amount}** Skindene Sten to {member.nick}\'s coin bag.\n{member.nick} now has **{self.currency[primary_id]['Skindene Sten']}** Skindene Sten.")            
# Update inventory Coin bag            
            for title, value in self.currency.items():
                _ = value
                if title == primary_id:
                    inventory_channel_id = self.currency[primary_id]['Inventory Channel ID']
                    embed_id = self.currency[primary_id]['Currency Embed ID']
                    break

            guild = self.bot.get_guild(698522830525956097) # DnD Vandvejen discord ID
            channel = guild.get_channel(inventory_channel_id)
            user_msg = await channel.fetch_message(embed_id)

            current_value = int(self.currency[primary_id]['Skindene Sten'])

            embed_fields = ["Kreditter", "Imperille Kreditter", "Skindene Sten"]
            word = "Skindene Sten"
            word_index = embed_fields.index(word)

            currency_embed = discord.Embed(title=f"{member.nick}\'s coin bag.",color=0xffd700)
            currency_embed.add_field(name="Kreditter", value=self.currency[primary_id]["Kreditter"])
            currency_embed.add_field(name="Imperille Kreditter", value=self.currency[primary_id]["Imperille Kreditter"])
            currency_embed.add_field(name="Skindene Sten", value=self.currency[primary_id]["Skindene Sten"])

            currency_embed.set_field_at(word_index, name="Skindene Sten", value=current_value)
            await user_msg.edit(embed=currency_embed)            

            fh.save_file(self.currency, 'currency')

# REMOVE "Skindene Sten" from a characters coin bag
    @commands.command()
    async def remss(self, ctx, amount: int, member: discord.Member = None):
        if ctx.channel.id == 698671535606595595: # Channel id of "economy"
            channel = ctx.channel
            await channel.purge(limit=1)
            self.load_data()

            member = ctx.author if not member else member
            primary_id = str(member.id)
            self.currency[primary_id]["Skindene Sten"] -= amount
            await ctx.send(f"Removed **{amount}** Skindene Sten from {member.nick}\'s coin bag.\n{member.nick} now has **{self.currency[primary_id]['Skindene Sten']}** Skindene Sten.")            
# Update inventory Coin bag            
            for title, value in self.currency.items():
                _ = value
                if title == primary_id:
                    inventory_channel_id = self.currency[primary_id]['Inventory Channel ID']
                    embed_id = self.currency[primary_id]['Currency Embed ID']
                    break

            guild = self.bot.get_guild(698522830525956097) # DnD Vandvejen discord ID
            channel = guild.get_channel(inventory_channel_id)
            user_msg = await channel.fetch_message(embed_id)

            current_value = int(self.currency[primary_id]['Skindene Sten'])

            embed_fields = ["Kreditter", "Imperille Kreditter", "Skindene Sten"]
            word = "Skindene Sten"
            word_index = embed_fields.index(word)

            currency_embed = discord.Embed(title=f"{member.nick}\'s coin bag.",color=0xffd700)
            currency_embed.add_field(name="Kreditter", value=self.currency[primary_id]["Kreditter"])
            currency_embed.add_field(name="Imperille Kreditter", value=self.currency[primary_id]["Imperille Kreditter"])
            currency_embed.add_field(name="Skindene Sten", value=self.currency[primary_id]["Skindene Sten"])

            currency_embed.set_field_at(word_index, name="Skindene Sten", value=current_value)
            await user_msg.edit(embed=currency_embed)             
            
            fh.save_file(self.currency, 'currency')


#===================================
#PAYING another character from their own coin bags
#===================================

# PAY another character with "Kreditter"
    @commands.command()
    async def payk(self, ctx, amount: int, other: discord.Member):
        if ctx.channel.id == 698671535606595595: # Channel id of "economy"
            channel = ctx.channel
            await channel.purge(limit=1)
            self.load_data()

            primary_id = str(ctx.message.author.id)
            other_id = str(other.id)
            if self.currency[primary_id]["Kreditter"] < amount:
                await ctx.send(f"{ctx.message.author.nick} does not have enough Kreditter to complete this transaction.")
            else:
                self.currency[primary_id]["Kreditter"] -= amount
                self.currency[other_id]["Kreditter"] += amount
                await ctx.send(f"{ctx.message.author.nick} has paid {other.nick} **{amount}** Kreditter.\n{other.nick} now has **{self.currency[other_id]['Kreditter']}** Kreditter.\n{ctx.message.author.nick} has **{self.currency[primary_id]['Kreditter']}** Kreditter left.")
                
# Update primary_id inventory Coin bag                            
                for title, value in self.currency.items():
                    _ = value
                    if title == primary_id:
                        inventory_channel_id = self.currency[primary_id]['Inventory Channel ID']
                        embed_id = self.currency[primary_id]['Currency Embed ID']
                        break

                guild = self.bot.get_guild(698522830525956097) # DnD Vandvejen discord ID
                channel = guild.get_channel(inventory_channel_id)
                user_msg = await channel.fetch_message(embed_id)
                member = ctx.author


                current_value = int(self.currency[primary_id]['Kreditter'])

                embed_fields = ["Kreditter", "Imperille Kreditter", "Skindene Sten"]
                word = "Kreditter"
                word_index = embed_fields.index(word)

                currency_embed = discord.Embed(title=f"{member.nick}\'s coin bag.",color=0xffd700)
                currency_embed.add_field(name="Kreditter", value=self.currency[primary_id]["Kreditter"])
                currency_embed.add_field(name="Imperille Kreditter", value=self.currency[primary_id]["Imperille Kreditter"])
                currency_embed.add_field(name="Skindene Sten", value=self.currency[primary_id]["Skindene Sten"])

                currency_embed.set_field_at(word_index, name="Kreditter", value=current_value)
                await user_msg.edit(embed=currency_embed)                 

# Update other_id inventory Coin bag                             
                for title, value in self.currency.items():
                    _ = value
                    if title == other_id:
                        inventory_channel_id = self.currency[other_id]['Inventory Channel ID']
                        embed_id = self.currency[other_id]['Currency Embed ID']
                        break

                guild = self.bot.get_guild(698522830525956097) # DnD Vandvejen discord ID
                channel = guild.get_channel(inventory_channel_id)
                user_msg = await channel.fetch_message(embed_id)

                current_value = int(self.currency[other_id]['Kreditter'])

                embed_fields = ["Kreditter", "Imperille Kreditter", "Skindene Sten"]
                word = "Kreditter"
                word_index = embed_fields.index(word)

                currency_embed = discord.Embed(title=f"{other.nick}\'s coin bag.",color=0xffd700)
                currency_embed.add_field(name="Kreditter", value=self.currency[other_id]["Kreditter"])
                currency_embed.add_field(name="Imperille Kreditter", value=self.currency[other_id]["Imperille Kreditter"])
                currency_embed.add_field(name="Skindene Sten", value=self.currency[other_id]["Skindene Sten"])

                currency_embed.set_field_at(word_index, name="Kreditter", value=current_value)
                await user_msg.edit(embed=currency_embed) 

                fh.save_file(self.currency, 'currency')

# PAY another character with "Imperille Kreditter"
    @commands.command()
    async def payik(self, ctx, amount: int, other: discord.Member):
        if ctx.channel.id == 698671535606595595: # Channel id of "economy"
            channel = ctx.channel
            await channel.purge(limit=1)
            self.load_data()    

            primary_id = str(ctx.message.author.id)
            other_id = str(other.id)
            if self.currency[primary_id]["Imperille Kreditter"] < amount:
                await ctx.send(f"{ctx.message.author.nick} does not have enough Imperille Kreditter to complete this transaction.")
            else:
                self.currency[primary_id]["Imperille Kreditter"] -= amount
                self.currency[other_id]["Imperille Kreditter"] += amount
                await ctx.send(f"{ctx.message.author.nick} has paid {other.nick} **{amount}** Imperille Kreditter.\n{other.nick} now has **{self.currency[other_id]['Imperille Kreditter']}** Imperille Kreditter.\n{ctx.message.author.nick} has **{self.currency[primary_id]['Imperille Kreditter']}** Imperille Kreditter left.")
# Update primary_id inventory Coin bag                            
                for title, value in self.currency.items():
                    _ = value
                    if title == primary_id:
                        inventory_channel_id = self.currency[primary_id]['Inventory Channel ID']
                        embed_id = self.currency[primary_id]['Currency Embed ID']
                        break

                guild = self.bot.get_guild(698522830525956097) # DnD Vandvejen discord ID
                channel = guild.get_channel(inventory_channel_id)
                user_msg = await channel.fetch_message(embed_id)
                member = ctx.author


                current_value = int(self.currency[primary_id]['Kreditter'])

                embed_fields = ["Kreditter", "Imperille Kreditter", "Skindene Sten"]
                word = "Imperille Kreditter"
                word_index = embed_fields.index(word)

                currency_embed = discord.Embed(title=f"{member.nick}\'s coin bag.",color=0xffd700)
                currency_embed.add_field(name="Kreditter", value=self.currency[primary_id]["Kreditter"])
                currency_embed.add_field(name="Imperille Kreditter", value=self.currency[primary_id]["Imperille Kreditter"])
                currency_embed.add_field(name="Skindene Sten", value=self.currency[primary_id]["Skindene Sten"])

                currency_embed.set_field_at(word_index, name="Imperille Kreditter", value=current_value)
                await user_msg.edit(embed=currency_embed)                 
# Update other_id inventory Coin bag                             
                for title, value in self.currency.items():
                    _ = value
                    if title == other_id:
                        inventory_channel_id = self.currency[other_id]['Inventory Channel ID']
                        embed_id = self.currency[other_id]['Currency Embed ID']
                        break

                guild = self.bot.get_guild(698522830525956097) # DnD Vandvejen discord ID
                channel = guild.get_channel(inventory_channel_id)
                user_msg = await channel.fetch_message(embed_id)

                current_value = int(self.currency[other_id]['Imperille Kreditter'])

                embed_fields = ["Kreditter", "Imperille Kreditter", "Skindene Sten"]
                word = "Imperille Kreditter"
                word_index = embed_fields.index(word)

                currency_embed = discord.Embed(title=f"{other.nick}\'s coin bag.",color=0xffd700)
                currency_embed.add_field(name="Kreditter", value=self.currency[other_id]["Kreditter"])
                currency_embed.add_field(name="Imperille Kreditter", value=self.currency[other_id]["Imperille Kreditter"])
                currency_embed.add_field(name="Skindene Sten", value=self.currency[other_id]["Skindene Sten"])

                currency_embed.set_field_at(word_index, name="Imperille Kreditter", value=current_value)
                await user_msg.edit(embed=currency_embed)

                fh.save_file(self.currency, 'currency')

# PAY another character with "Skindene Sten"
    @commands.command()
    async def payss(self, ctx, amount: int, other: discord.Member):
        if ctx.channel.id == 698671535606595595: # Channel id of "economy"
            channel = ctx.channel
            await channel.purge(limit=1)
            self.load_data()      

            primary_id = str(ctx.message.author.id)
            other_id = str(other.id)
            if self.currency[primary_id]["Skindene Sten"] < amount:
                await ctx.send(f"{ctx.message.author.nick} does not have enough Skindene Sten to complete this transaction.")
            else:
                self.currency[primary_id]["Skindene Sten"] -= amount
                self.currency[other_id]["Skindene Sten"] += amount
                await ctx.send(f"{ctx.message.author.nick} has paid {other.nick} **{amount}** Skindene Sten.\n{other.nick} now has **{self.currency[other_id]['Skindene Sten']}** Skindene Sten.\n{ctx.message.author.nick} has **{self.currency[primary_id]['Skindene Sten']}** Skindene Sten left.")
# Update primary_id inventory Coin bag                            
                for title, value in self.currency.items():
                    _ = value
                    if title == primary_id:
                        inventory_channel_id = self.currency[primary_id]['Inventory Channel ID']
                        embed_id = self.currency[primary_id]['Currency Embed ID']
                        break

                guild = self.bot.get_guild(698522830525956097) # DnD Vandvejen discord ID
                channel = guild.get_channel(inventory_channel_id)
                user_msg = await channel.fetch_message(embed_id)
                member = ctx.author


                current_value = int(self.currency[primary_id]['Skindene Sten'])

                embed_fields = ["Kreditter", "Imperille Kreditter", "Skindene Sten"]
                word = "Skindene Sten"
                word_index = embed_fields.index(word)

                currency_embed = discord.Embed(title=f"{member.nick}\'s coin bag.",color=0xffd700)
                currency_embed.add_field(name="Kreditter", value=self.currency[primary_id]["Kreditter"])
                currency_embed.add_field(name="Imperille Kreditter", value=self.currency[primary_id]["Imperille Kreditter"])
                currency_embed.add_field(name="Skindene Sten", value=self.currency[primary_id]["Skindene Sten"])

                currency_embed.set_field_at(word_index, name="Skindene Sten", value=current_value)
                await user_msg.edit(embed=currency_embed)                 
# Update other_id inventory Coin bag                             
                for title, value in self.currency.items():
                    _ = value
                    if title == other_id:
                        inventory_channel_id = self.currency[other_id]['Inventory Channel ID']
                        embed_id = self.currency[other_id]['Currency Embed ID']
                        break

                guild = self.bot.get_guild(698522830525956097) # DnD Vandvejen discord ID
                channel = guild.get_channel(inventory_channel_id)
                user_msg = await channel.fetch_message(embed_id)

                current_value = int(self.currency[other_id]['Skindene Sten'])

                embed_fields = ["Kreditter", "Imperille Kreditter", "Skindene Sten"]
                word = "Skindene Sten"
                word_index = embed_fields.index(word)

                currency_embed = discord.Embed(title=f"{other.nick}\'s coin bag.",color=0xffd700)
                currency_embed.add_field(name="Kreditter", value=self.currency[other_id]["Kreditter"])
                currency_embed.add_field(name="Imperille Kreditter", value=self.currency[other_id]["Imperille Kreditter"])
                currency_embed.add_field(name="Skindene Sten", value=self.currency[other_id]["Skindene Sten"])

                currency_embed.set_field_at(word_index, name="Skindene Sten", value=current_value)
                await user_msg.edit(embed=currency_embed) 

                fh.save_file(self.currency, 'currency')

def setup(bot):
    bot.add_cog(Currency(bot))


#================
#JUNK
#================

# PAY another character with "Kreditter"
#    @commands.command()
#    async def payk(self, ctx, amount: int, other: discord.Member):
#        primary_id = str(ctx.message.author.id)
#        other_id = str(other.id)
#        if primary_id not in self.currency[primary_id]["Kreditter"]:
#            await ctx.send("You do not have an account")
#        elif other_id not in self.currency[other_id]["Kreditter"]:
#            await ctx.send("The other party does not have an account")
#        elif self.currency[primary_id]["Kreditter"] < amount:
#            await ctx.send("You cannot afford this transaction")
#        else:
#            self.currency[primary_id]["Kreditter"] -= amount
#            self.currency[other_id]["Kreditter"] += amount
#            await ctx.send("Transaction complete")

#    @commands.command()
#    async def payss(self, ctx, amount: int, member: discord.Member = None):
#        member_id = ctx.author if not member else member
#        primary_id = str(ctx.message.author.id)
#        self.currency[primary_id]["Skindene Sten"] -= amount
#        #self.currency[member_id]["Skindene Sten"] += amount
#        print (member_id)
#        await ctx.send(f"Removed **{amount}** Skindene Sten from {primary_id}\'s coin bag.\n{member.nick} now has **{self.currency[primary_id]['Skindene Sten']}** Skindene Sten.")
