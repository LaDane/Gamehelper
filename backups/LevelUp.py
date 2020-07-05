import discord
import json
import asyncio
from discord.ext import commands
from filehandler import FileHandler
from jsonhandler import JsonHandler

fh = FileHandler()
jh = JsonHandler()


class LevelUp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
        self.charactersheet = fh.load_file('charactersheet')

    def s_c_s_e_ids(self):
        return jh.show_character_sheet_embed_ids()



# Level up character sheet
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        self.load_data()
        
        user_reaction_msg_id = payload.message_id

        guild = self.bot.get_guild(payload.guild_id)  # You need the guild to get the member who reacted
        member = guild.get_member(payload.user_id)  # the member who reacted to a role
        member_id = member.id # used to check if bot reacted
        botcheck = 698545737880961074 # used to check if bot reacted

        embed_ids = self.s_c_s_e_ids()

        if not payload.guild_id: # In this case, the reaction was added in a DM channel with the bot
            return
        if member_id == botcheck: # In this case, the bot reacted to a message
            return
        if str(user_reaction_msg_id) not in str(embed_ids): # In this case, the reaction was given to a message not in BuyStockMsgID
            return 
        if str(user_reaction_msg_id) in str(embed_ids): # In this case the reaction is given to a message in BuyStockMsgID

            reaction = str(payload.emoji.name)
            
            if reaction == "\U0001F514": # Bell emoji - :bell: 
                self.load_data()


                for title, value in self.charactersheet.items():
                    if title == member_id:
                        _ = value
                        author_id = title
                        break   

                embed_channel_id = self.charactersheet[title]['Character Sheet Channel ID']
                channel = guild.get_channel(embed_channel_id)
                message_id = self.charactersheet[title]['Character Sheet Embed ID']
                user_msg = await channel.fetch_message(message_id) 
                author_id = title

                cs_embed = discord.Embed(title=f"**{self.charactersheet[author_id]['Character']}'s character sheet**", description=f"*React with :bell: to level up*", color=0x303136)
                cs_embed.add_field(name="**Level**", value=f"{self.charactersheet[author_id]['Character Sheet']['Level']}")
                cs_embed.add_field(name="**\u200b**", value=f"__**Kompetencer**__", inline=False)
                cs_embed.add_field(name="**Styrke**", value=f"{self.charactersheet[author_id]['Character Sheet']['Styrke']}", inline=True)
                cs_embed.add_field(name="**Udholdenhed**", value=f"{self.charactersheet[author_id]['Character Sheet']['Udholdenhed']}")
                cs_embed.add_field(name="**Intelligens**", value=f"{self.charactersheet[author_id]['Character Sheet']['Intelligens']}")
                cs_embed.add_field(name="**Finesse**", value=f"{self.charactersheet[author_id]['Character Sheet']['Finesse']}")
                cs_embed.add_field(name="**Perception**", value=f"{self.charactersheet[author_id]['Character Sheet']['Perception']}")
                cs_embed.add_field(name="**Karisma**", value=f"{self.charactersheet[author_id]['Character Sheet']['Karisma']}")
                cs_embed.add_field(name="**Initiativ**", value=f"{self.charactersheet[author_id]['Character Sheet']['Initiativ']}\n \n__**Kamp Evner**__", inline=False)

                cs_embed.add_field(name="**Nærkamp**", value=f"{self.charactersheet[author_id]['Character Sheet']['Nærkamp']} *(+{self.charactersheet[author_id]['Character Sheet']['Nærkamp_Bonus']})*", inline=True)
                cs_embed.add_field(name="**Kaste/Strenge Våben**", value=f"{self.charactersheet[author_id]['Character Sheet']['Kaste_Strenge_våben']} *(+{self.charactersheet[author_id]['Character Sheet']['Kaste_Strenge_våben_Bonus']})*")
                cs_embed.add_field(name="**Skydevåben**", value=f"{self.charactersheet[author_id]['Character Sheet']['Skydevåben']} *(+{self.charactersheet[author_id]['Character Sheet']['Skydevåben_Bonus']})*")
                cs_embed.add_field(name="**Snig**", value=f"{self.charactersheet[author_id]['Character Sheet']['Snig']} *(+{self.charactersheet[author_id]['Character Sheet']['Snig_Bonus']})*\n \n__**Sociale Evner**__", inline=False)

                cs_embed.add_field(name="**Smigre**", value=f"{self.charactersheet[author_id]['Character Sheet']['Smigre']} *(+{self.charactersheet[author_id]['Character Sheet']['Smigre_Bonus']})*", inline=True)
                cs_embed.add_field(name="**Løgn**", value=f"{self.charactersheet[author_id]['Character Sheet']['Løgn']} *(+{self.charactersheet[author_id]['Character Sheet']['Løgn_Bonus']})*")
                cs_embed.add_field(name="**Intimiderer**", value=f"{self.charactersheet[author_id]['Character Sheet']['Intimiderer']} *(+{self.charactersheet[author_id]['Character Sheet']['Intimiderer_Bonus']})*")
                cs_embed.add_field(name="**Handel**", value=f"{self.charactersheet[author_id]['Character Sheet']['Handel']} *(+{self.charactersheet[author_id]['Character Sheet']['Handel_Bonus']})*\n \n__**Håndværks Evner**__", inline=False)

                cs_embed.add_field(name="**Reparation**", value=f"{self.charactersheet[author_id]['Character Sheet']['Reparation']} *(+{self.charactersheet[author_id]['Character Sheet']['Reparation_Bonus']})*", inline=True)
                cs_embed.add_field(name="**Fælder**", value=f"{self.charactersheet[author_id]['Character Sheet']['Fælder']} *(+{self.charactersheet[author_id]['Character Sheet']['Fælder_Bonus']})*")
                cs_embed.add_field(name="**Overlevelse**", value=f"{self.charactersheet[author_id]['Character Sheet']['Overlevelse']} *(+{self.charactersheet[author_id]['Character Sheet']['Overlevelse_Bonus']})*")
                cs_embed.add_field(name="**Håndarbejde**", value=f"{self.charactersheet[author_id]['Character Sheet']['Håndarbejde']} *(+{self.charactersheet[author_id]['Character Sheet']['Håndarbejde_Bonus']})*\n \n__**Esoteriske Evner**__", inline=False)

                cs_embed.add_field(name="**Videnskab**", value=f"{self.charactersheet[author_id]['Character Sheet']['Videnskab']} *(+{self.charactersheet[author_id]['Character Sheet']['Videnskab_Bonus']})*", inline=True)
                cs_embed.add_field(name="**Alkymi**", value=f"{self.charactersheet[author_id]['Character Sheet']['Alkymi']} *(+{self.charactersheet[author_id]['Character Sheet']['Alkymi_Bonus']})*")
                cs_embed.add_field(name="**Lægevidenskab**", value=f"{self.charactersheet[author_id]['Character Sheet']['Lægevidenskab']} *(+{self.charactersheet[author_id]['Character Sheet']['Lægevidenskab_Bonus']})*")
                cs_embed.add_field(name="**Historie**", value=f"{self.charactersheet[author_id]['Character Sheet']['Historie']} *(+{self.charactersheet[author_id]['Character Sheet']['Historie_Bonus']})*")


                current_level = int(self.charactersheet[author_id]['Character Sheet']['Level'])
                level_up = 1
                current_level += level_up

                embed_fields = ["**Level**", "**\u200b**", "**Styrke**", "**Udholdenhed**", "**Intelligens**", "**Finesse**", "**Perception**", "**Karisma**", "**Initiativ**", "**Nærkamp**", "**Kaste/Strenge Våben**", "**Skydevåben**", "**Snig**", "**Smigre**", "**Løgn**", "**Intimiderer**", "**Handel**", "**Reparation**", "**Fælder**", "**Overlevelse**", "**Håndarbejde**", "**Videnskab**", "**Alkymi**", "**Lægevidenskab**", "**Historie**", ]
                word = "**Level**"
                word_index = embed_fields.index(word)

                cs_embed.set_field_at(word_index, name="**Level**", value=current_level)

                self.charactersheet[author_id]['Character Sheet']['Level'] = current_level
                fh.save_file(self.charactersheet, 'charactersheet')

                await user_msg.edit(embed=cs_embed)

    # LEVEL UP STATS
                await asyncio.sleep(1)
                msg3 = await channel.send(f"You have dinged level **{current_level}**!\nYou are now able to put **5** points into one of your **Evner**\n \n" +
                                    "Which skill would you like to put your points into?\nReact to this message with the corresponding **Evner**\n \n*Please wait for the bot to add all reactions before you react! (last one is :clock:)*\n \n" +
                                    "__**Kamp Evner**__\n" +
                                    ":crossed_swords: for **Nærkamp**\n" +
                                    ":bow_and_arrow: for **Kaste/Strenge Våben**\n" +
                                    ":gun: for **Skydevåben**\n" +
                                    ":man_detective: for **Snig**\n" +
                                    "__**Sociale Evner**__\n" +
                                    ":kiss: for **Smigre**\n" +
                                    ":lying_face: for **Løgn**\n" +
                                    ":muscle: for **Intimiderer**\n" +
                                    ":money_mouth: for **Handel**\n" +
                                    "__**Håndværks Evner**__\n" +
                                    ":wrench: for **Reparation**\n" +
                                    ":chains: for **Fælder**\n" +
                                    ":fishing_pole_and_fish: for **Overlevelse**\n" +
                                    ":hand_splayed: for **Håndarbejde**\n" +
                                    "__**Esoteriske Evner**__\n" +
                                    ":books: for **Videnskab**\n" +
                                    ":sake: for **Alkymi**\n" +
                                    ":medical_symbol: for **Lægevidenskab**\n" +
                                    ":clock: for **Historie**")


                await asyncio.sleep(1) 

                await msg3.add_reaction(emoji='\u2694') # crossed_swords
                await msg3.add_reaction(emoji='\U0001F3F9') # bow_and_arrow
                await msg3.add_reaction(emoji='\U0001F52B') # gun
                await msg3.add_reaction(emoji='\U0001F575') # man_detective
                await msg3.add_reaction(emoji='\U0001F48B') # :kiss: U0001F48B
                await msg3.add_reaction(emoji='\U0001F925') # lying_face
                await msg3.add_reaction(emoji='\U0001F4AA') # muscle
                await msg3.add_reaction(emoji='\U0001F911') # money_mouth
                await msg3.add_reaction(emoji='\U0001F527') # wrench
                await msg3.add_reaction(emoji='\U000026D3') # chains
                await msg3.add_reaction(emoji='\U0001F3A3') # fishing_pole_and_fish
                await msg3.add_reaction(emoji='\U0001F590') # hand_splayed
                await msg3.add_reaction(emoji='\U0001F4DA') # books
                await msg3.add_reaction(emoji='\U0001F376') # sake
                await msg3.add_reaction(emoji='\U00002695') # medical_symbol
                await msg3.add_reaction(emoji='\U0001F570') # clock

                await asyncio.sleep(1)

                res = await self.bot.wait_for('reaction_add')
                if member_id == botcheck: # In this case, the bot reacted to a message
                    return
                if res:
                    reaction, member = res
                    if str(reaction.emoji) == "\u2694":
                        chosen_evner = "**Nærkamp**"
                    if str(reaction.emoji) == "\U0001F3F9":
                        chosen_evner = "**Kaste/Strenge Våben**"
                    if str(reaction.emoji) == "\U0001F52B":
                        chosen_evner = "**Skydevåben**"                
                    if str(reaction.emoji) == "\U0001F575":
                        chosen_evner = "**Snig**" 
                    if str(reaction.emoji) == "\U0001F48B":
                        chosen_evner = "**Smigre**"
                    if str(reaction.emoji) == "\U0001F925":
                        chosen_evner = "**Løgn**"
                    if str(reaction.emoji) == "\U0001F4AA":
                        chosen_evner = "**Intimiderer**"                
                    if str(reaction.emoji) == "\U0001F911":
                        chosen_evner = "**Handel**"
                    if str(reaction.emoji) == "\U0001F527":
                        chosen_evner = "**Reparation**"
                    if str(reaction.emoji) == "\U000026D3":
                        chosen_evner = "**Fælder**"
                    if str(reaction.emoji) == "\U0001F3A3":
                        chosen_evner = "**Overlevelse**"                
                    if str(reaction.emoji) == "\U0001F590":
                        chosen_evner = "**Håndarbejde**"   
                    if str(reaction.emoji) == "\U0001F4DA":
                        chosen_evner = "**Videnskab**"
                    if str(reaction.emoji) == "\U0001F376":
                        chosen_evner = "**Alkymi**"
                    if str(reaction.emoji) == "\U00002695":
                        chosen_evner = "**Lægevidenskab**"                
                    if str(reaction.emoji) == "\U0001F570":
                        chosen_evner = "**Historie**"                                       
    
    # UPGRADE EVNER
                evner = chosen_evner
                
                data_evner_fr = (evner[2:])
                data_evner = (data_evner_fr[:-2])

                if evner == "**Kaste/Strenge Våben**":
                    data_evner = "Kaste_Strenge_våben"

                current_evner = int(self.charactersheet[author_id]['Character Sheet'][data_evner])
                evner_level_up = 5
                current_evner += evner_level_up                

                evner_index = embed_fields.index(evner)

                item_stat_bonus = f"{data_evner}_Bonus"

                cs_embed.set_field_at(evner_index, name=evner, value=f"{current_evner} *(+{self.charactersheet[author_id]['Character Sheet'][item_stat_bonus]})*")

                self.charactersheet[author_id]['Character Sheet'][data_evner] = current_evner
                fh.save_file(self.charactersheet, 'charactersheet')

                await user_msg.edit(embed=cs_embed)

                await asyncio.sleep(1)
                await channel.purge(limit=1)

                await channel.send(f"You have chosen to put **5** points into {evner}!")
                await asyncio.sleep(4)
                await channel.purge(limit=1)



    # HITTING A LEVEL DIVISBLE BY 5
                if current_level % 5 == 0:
                    msg1 = await channel.send(f"When hitting a level divisible by 5, you're able to put **1** point into one of your **Kompetencer**\n \n" +
                                    "Which one of your **Kompetencer** would you like to upgrade?\nReact to this message with the corresponding **Kompetence**\n \n" +
                                    ":radio_button: for **Styrke**\n" +
                                    ":white_circle: for **Udholdenhed**\n" +
                                    ":black_circle: for **Intelligens**\n" +
                                    ":red_circle: for **Finesse**\n" +
                                    ":blue_circle: for **Perception**\n" +
                                    ":brown_circle: for **Karisma**\n" +
                                    ":purple_circle: for **Initiativ**")

                    await msg1.add_reaction(emoji='\U0001F518') #radio_button
                    await msg1.add_reaction(emoji='\u26AA') #white_circle
                    await msg1.add_reaction(emoji='\u26AB') #black_circle
                    await msg1.add_reaction(emoji='\U0001F534') #red_circle
                    await msg1.add_reaction(emoji='\U0001F535') #blue_circle
                    await msg1.add_reaction(emoji='\U0001F7E4') #brown_circle
                    await msg1.add_reaction(emoji='\U0001F7E3') #purple_circle
                    await asyncio.sleep(1)

                    res = await self.bot.wait_for('reaction_add')
                    if res:
                        reaction, member = res
                        if str(reaction.emoji) == "\U0001F518":
                            chosen_kompetence = "**Styrke**"
                        if str(reaction.emoji) == "\u26AA":
                            chosen_kompetence = "**Udholdenhed**"
                        if str(reaction.emoji) == "\u26AB":
                            chosen_kompetence = "**Intelligens**"                
                        if str(reaction.emoji) == "\U0001F534":
                            chosen_kompetence = "**Finesse**"                  
                        if str(reaction.emoji) == "\U0001F535":
                            chosen_kompetence = "**Perception**" 
                        if str(reaction.emoji) == "\U0001F7E4":
                            chosen_kompetence = "**Karisma**" 
                        if str(reaction.emoji) == "\U0001F7E3":
                            chosen_kompetence = "**Initiativ**" 
                                    
                    kompetence = chosen_kompetence
                    data_kompetence_fr = (kompetence[2:])
                    data_kompetence = (data_kompetence_fr[:-2])

                    current_kompetence = int(self.charactersheet[author_id]['Character Sheet'][data_kompetence])
                    kompetence_level_up = 1
                    current_kompetence += kompetence_level_up                

                    kompetence_index = embed_fields.index(kompetence)

                    cs_embed.set_field_at(kompetence_index, name=kompetence, value=current_kompetence)

                    self.charactersheet[author_id]['Character Sheet'][data_kompetence] = current_kompetence
                    fh.save_file(self.charactersheet, 'charactersheet')

                    await user_msg.edit(embed=cs_embed)

                    await asyncio.sleep(1)
                    await channel.purge(limit=1)

                    await channel.send(f"You have chosen to put **1** point into {kompetence}!")
                    await asyncio.sleep(4)
                    await channel.purge(limit=1)



def setup(bot):
    bot.add_cog(LevelUp(bot))
