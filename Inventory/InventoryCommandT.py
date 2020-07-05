import discord
import json
import asyncio
from discord.ext import commands
from filehandler import FileHandler
from jsonhandler import JsonHandler

jh = JsonHandler()
fh = FileHandler()


class InventoryCommandT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
        self.currency = fh.load_file('currency')
        self.inventory = fh.load_file('inventory')

    def s_i_s_i_c_ids(self):
        return jh.show_inventory_store_items_channel_ids()


# store items in shared inventory
    @commands.command()
    async def t(self, ctx, item, amount: int):
        invetory_storeitems_channel_ids = self.s_i_s_i_c_ids()
        if str(ctx.channel.id) in str(invetory_storeitems_channel_ids):
            channel = ctx.channel
            channel_id = channel.id
            await channel.purge(limit=1)
            self.load_data()

            member = ctx.author
            member_id = str(member.id)

            if not member_id in self.currency:
                await ctx.send("Member doesnt have a coin bag")

            if str(item) == "k":
                currency = "Kreditter"

            if str(item) == "ik":
                currency = "Imperille Kreditter"

            if str(item) == "ss":
                currency = "Skindene Sten"

            for title, value in self.currency.items():                          # for players coing bag
                _ = value
                if title == member_id:
                    inventory_channel_id = self.currency[member_id]['Inventory Channel ID']
                    embed_id = self.currency[member_id]['Currency Embed ID']
                    # break

            for title2, value2 in self.inventory.items():                       # for shared inventory coin bag
                if value2['Store_Items_Channel_ID'] == channel_id:
                    store_items_channel_id = self.inventory[title2]['Store_Items_Channel_ID']
                    shared_inventory_id = self.inventory[title2]['Inventory_Channel_ID']
                    inventory_id = title2
                    # break

            guild = self.bot.get_guild(698522830525956097) # DnD Vandvejen discord ID
            channel = guild.get_channel(inventory_channel_id)
            user_msg = await channel.fetch_message(embed_id)

            if self.inventory[inventory_id][currency] < amount:
                await ctx.send(f"There is not enough {currency} stored in {inventory_id}'s coin bag to withdraw {amount} {currency}!")
                await asyncio.sleep(2)
                channel = guild.get_channel(store_items_channel_id)
                await channel.purge(limit=1)
                return
            else:
                self.currency[member_id][currency] += amount
                self.inventory[inventory_id][currency] -= amount

# Update players coin bag
                current_value = int(self.currency[member_id][currency])

                embed_fields = ["Kreditter", "Imperille Kreditter", "Skindene Sten"]
                word = currency
                word_index = embed_fields.index(word)

                currency_embed = discord.Embed(title=f"{member.nick}\'s coin bag.",color=0xffd700)
                currency_embed.add_field(name="Kreditter", value=self.currency[member_id]["Kreditter"])
                currency_embed.add_field(name="Imperille Kreditter", value=self.currency[member_id]["Imperille Kreditter"])
                currency_embed.add_field(name="Skindene Sten", value=self.currency[member_id]["Skindene Sten"])

                currency_embed.set_field_at(word_index, name=currency, value=current_value)
                await user_msg.edit(embed=currency_embed)

# Update shared inventory coin bag                    
                channel = guild.get_channel(shared_inventory_id)
                shared_items_currency_embed_id = self.inventory[inventory_id]['Currency_Embed_ID']
                user_msg = await channel.fetch_message(shared_items_currency_embed_id)

                current_value = int(self.inventory[inventory_id][currency])

                embed_fields = ["Kreditter", "Imperille Kreditter", "Skindene Sten"]
                word = currency
                word_index = embed_fields.index(word)

                currency_embed = discord.Embed(title=f"{self.inventory[inventory_id]['Inventory_Name']}\'s coin bag.",color=0xffd700)
                currency_embed.add_field(name="Kreditter", value=self.inventory[inventory_id]["Kreditter"])
                currency_embed.add_field(name="Imperille Kreditter", value=self.inventory[inventory_id]["Imperille Kreditter"])
                currency_embed.add_field(name="Skindene Sten", value=self.inventory[inventory_id]["Skindene Sten"])

                currency_embed.set_field_at(word_index, name=currency, value=current_value)
                await user_msg.edit(embed=currency_embed) 

                fh.save_file(self.currency, 'currency')
                fh.save_file(self.inventory, 'inventory')

                await ctx.send(f"{member.nick} has taken {amount} {currency} from this inventory.")
                await asyncio.sleep(2)
                channel = guild.get_channel(store_items_channel_id)
                await channel.purge(limit=1)
                channel = guild.get_channel(698671535606595595) # economy channel id
                await channel.send(f"**{member.nick}** has taken **{amount} {currency}** from **{self.inventory[inventory_id]['Inventory_Name']}'s** inventory!")
                return


def setup(bot):
    bot.add_cog(InventoryCommandT(bot))
