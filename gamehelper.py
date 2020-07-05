import discord
import random
import asyncio
import os
from discord.ext import commands
from itertools import cycle

bot = commands.Bot(command_prefix=".")
bot.remove_command("help")

# ready check
@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)


# change bot status
async def chng_pr():
    await bot.wait_until_ready()
    statuses = ["for shitty rolls", "players hit nat 20s"]
    statuses = cycle(statuses)
    while not bot.is_closed():
        status = next(statuses)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=(status)))
        await asyncio.sleep(10)

# cog startup - Characters
for cog in os.listdir(".\\Characters"):
    if cog.endswith(".py"):
        try:
            cog = f"Characters.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} can not be loaded:")
            raise e

# cog startup - CharacterSheet
for cog in os.listdir(".\\CharacterSheet"):
    if cog.endswith(".py"):
        try:
            cog = f"CharacterSheet.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} can not be loaded:")
            raise e

# cog startup - Interact
for cog in os.listdir(".\\Interact"):
    if cog.endswith(".py"):
        try:
            cog = f"Interact.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} can not be loaded:")
            raise e

# cog startup - Shops
for cog in os.listdir(".\\Shops"):
    if cog.endswith(".py"):
        try:
            cog = f"Shops.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} can not be loaded:")
            raise e    

# cog startup - Stock
for cog in os.listdir(".\\Stock"):
    if cog.endswith(".py"):
        try:
            cog = f"Stock.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} can not be loaded:")
            raise e          

# cog startup - WorldItems
for cog in os.listdir(".\\WorldItems"):
    if cog.endswith(".py"):
        try:
            cog = f"WorldItems.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} can not be loaded:")
            raise e 

# cog startup - Inventory
for cog in os.listdir(".\\Inventory"):
    if cog.endswith(".py"):
        try:
            cog = f"Inventory.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} can not be loaded:")
            raise e 


# # cog startup - test
# for cog in os.listdir(".\\test"):
#     if cog.endswith(".py"):
#         try:
#             cog = f"test.{cog.replace('.py', '')}"
#             bot.load_extension(cog)
#         except Exception as e:
#             print(f"{cog} can not be loaded:")
#             raise e 

bot.loop.create_task(chng_pr()) # loops bot status change
bot.run("Njk4NTQ1NzM3ODgwOTYxMDc0.XpHZjQ.kq2OtsAOMdz9QFfMTTvR5AOTLt0")


# 6348 lines of code total - 23-04-2020
