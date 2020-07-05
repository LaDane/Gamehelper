import discord
import json
import asyncio
from discord.ext import commands
from filehandler import FileHandler
# from jsonhandler import JsonHandler

# jh = JsonHandler()
fh = FileHandler()


class CharacterSheet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
        self.charactersheet = fh.load_file('charactersheet')


# New character command
    @commands.command()
    async def cs(self, message):
        author_id = str(message.author.id)
        self.load_data()
        if author_id in self.charactersheet:
            if message.channel.id == self.charactersheet[author_id]["Character Sheet Channel ID"]:
                channel_id = self.charactersheet[author_id]["Character Sheet Channel ID"]
                channel = self.bot.get_channel(channel_id)
                await channel.purge(limit=20)

# BESKYTTER                
                beskytter_embed = discord.Embed(title=f"__**Beskytter**__", description=f"*Bestyktteren er en lavløs monster-jæger.*\n" + 
                                                                "*Disse fromme og fanatiske sjæle opsøger ofte Mutanter eller de Udødelige med intentioner om at udslette disse vanskabninger for andres sikkerhed.*\n" + 
                                                                "*Disse ildsjæle er oftest lav løse på grund af deres “ekstreme” synspunkter.*\n \n" +
                                                                "__**Evner:**__\n" +
                                                                "**Gudløse Spetakler**\n" +
                                                                "*Beskytteren vil altid have +5 Initiativ OG +1 Udholdenhed i kamp mod “Udødelige” “Stakkel” og “Trolde” fjender. Dog vil de samtidig have INGEN mulighed for at bruge Sociale Evner i interaktioner med Mutant NPC’er*\n" +
                                                                "**Vores sag er Hellig!**\n" +
                                                                "*I interaktioner med “Troende” NPC’er vil Beskytteren altid have +5 Sociale Evner, men -10 med “Ikke-Troende” NPC’er (Specificeres)*\n \n" +
                                                                "__**Pros:**__\n" +
                                                                "+15  **Nærkamp**\n" +
                                                                "+5  **Styrke**\n \n" +
                                                                "__**Cons:**__\n" +
                                                                "Beskytteren kan ikke gøre brug af Skydevåben.", color=0x004CB9)                
                beskytter_embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/701094688144490536/84447639_113161510125112_7795953704867201024_n.png?width=485&height=627")
                await channel.send(embed=beskytter_embed)
                await asyncio.sleep(1)
# CHARLATAN                
                charlatan_embed = discord.Embed(title=f"__**Charlatan**__", description=f"*En tunge af sølv og et flot smil kan gøre en tigger til baron i den rette situation.*\n" + 
                                                                "*Charlataner og andre fupmagere er ikke unormale syn i de mere befærdede og manfolkdige byområder på Gaia.*\n" + 
                                                                "*Med deres rigdom gør de ofte brug af mere “direkte” arbejdskraft hvis en confrontation skulle opstå.*\n \n" +
                                                                "__**Evner:**__\n" +
                                                                "**Den klarer i… jeg skal væk**\n" +
                                                                "*Under kamp med alle “Menneskelige” fjender vil Charlatanen altid have lavest Initiativ i gruppen, men højeste imod “Ikke-Menneskelige” fjender (Specificeres)*\n \n" +
                                                                "__**Pros:**__\n" +
                                                                "+15  **Løgn**\n" +
                                                                "+15  **Smir**\n" +
                                                                "+15  **Handel**\n" +
                                                                "+15  **Snig**\n \n" +
                                                                "__**Cons:**__\n" +
                                                                "Charlatanen kan IKKE bruge to-hånds våben eller rustning.", color=0xFAFBF9)                
                charlatan_embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/701071214403125358/83977493_200402444417514_4410246142369988608_n.png?width=483&height=627")
                await channel.send(embed=charlatan_embed)
                await asyncio.sleep(1)
# INDFØDT
                indfødt_embed = discord.Embed(title=f"__**Indfødt**__", description=f"*Efter Katastrofen er mange mennesker regresseret tilbage til vores primale fortid.*\n" + 
                                                                "*Disse stammefolk er udholdende og krigeriske, men til tider også overtroiske og mindre intelligente end de mere “civiliserede” sorter.*\n \n" + 
                                                                "__**Evner:**__\n" +
                                                                "**Tro til Moder Gaia**\n" +
                                                                "*Hvis den Indfødte kun er iklædt eller gør brug udstyr fundet i naturen eller de selv har skabt, får de +1 på alle **relevante** terningekast (Specificeres)*\n" +
                                                                "**Hærdet legeme**\n" +
                                                                "*Indfødte er immun overfor de fleste gifte (Specificeres)*\n \n" +
                                                                "__**Pros:**__\n" +
                                                                "+5  **Nærkamp**\n" +
                                                                "+5  **Udholdenhed**\n" +
                                                                "+5  **Overlevelse**\n" +
                                                                "+5  **Alkymi**\n" +
                                                                "+5  **Styrke **\n \n" +
                                                                "__**Cons:**__\n" +
                                                                "Den Indfødte kan ALDRIG bruge Videnskab evnen.\n" +
                                                                "-10  **Sociale Evner**", color=0x030303)                
                indfødt_embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/701080791597318154/83949023_2633611816925481_519829439547179008_n.png?width=444&height=627")
                await channel.send(embed=indfødt_embed)
                await asyncio.sleep(1)
# JÆGER
                jæger_embed = discord.Embed(title=f"__**Jæger**__", description=f"*Siden tidernes morgen har mennesket jaget, dette ændrede sig ikke da vi drog ud mellem stjernerne.*\n" + 
                                                                "*Jægeren har brugt sit liv i vildmarken, både som jæger og som bytte.*\n \n" + 
                                                                "__**Evner:**__\n" +
                                                                "**Sikke et eksemplar**\n" +
                                                                "*Jægeren kan altid identificere en Dyrisk fjendes (også Bossers) svagheder. Ydermere kan de oftest skaffe sjældne ressourcer hvis de dressere dyr.*\n" +
                                                                "**Ekspert**\n" +
                                                                "*I kamp mod ‘Dyriske’ fjender har Jægeren altid +1 Initiativ og hvis Jægeren er den første i gruppen til at angribe en ‘Dyrisk’ fjende, kan de ikke misse deres første angreb.*\n \n" +
                                                                "__**Pros:**__\n" +
                                                                "+5  **Kaste/Strenge Våben**\n" +
                                                                "+5  **Fælder**\n" +
                                                                "+5  **Overlevelse**\n \n" +
                                                                "__**Cons:**__\n" +
                                                                "-5  **Videnskab**\n" +
                                                                "-5  **Skydevåben**", color=0xF50404)                
                jæger_embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/701086619729657876/83272722_212026363273452_6715150482186174464_n.png?width=454&height=627")
                await channel.send(embed=jæger_embed)
                await asyncio.sleep(1)
# LANDEVEJSRØVER
                landevejsrøver_embed = discord.Embed(title=f"__**Landevejsrøver**__", description=f"*Sønderlandet og hele Gaia er plaget af gemene banditter der ligger på lur langs befærdede veje.*\n" + 
                                                                "*De berøver folk for alt hvad de er værd og nogen gange ender det med at offeret også må bøde med livet.*\n" +
                                                                "*Nogle af disse lovløse lever således af nødvendighed, mens andre ser det som naturens love.*\n \n" + 
                                                                "__**Evner:**__\n" +
                                                                "**Nu du skulle nævne det…**\n" +
                                                                "*Under snakke eller handel med “Kriminelle” NPC’er har Landevejsrøveren altid +5 i Sociale Evner, men -5 med “Lovlydige” karakterer (Specificeres)*\n" +
                                                                "**Jeg er realist!**\n" +
                                                                "*Hvis Landevejsrøveren kommer under 50% Liv får de +1 Bevægelses handling, så længe det er VÆK fra fjenden.*\n \n" +
                                                                "__**Pros:**__\n" +
                                                                "+5  **Løgn**\n" +
                                                                "+5  **Snig**\n \n" +
                                                                "__**Cons:**__\n" +
                                                                "-10  **Smigre**", color=0x20B5FF)                
                landevejsrøver_embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/701091406424440832/84333690_697893080745801_5555861783052288000_n.png?width=437&height=627")
                await channel.send(embed=landevejsrøver_embed)
                await asyncio.sleep(1)
# LEJESOLDAT
                lejesoldat_embed = discord.Embed(title=f"__**Lejesoldat**__", description=f"*Lejesoldaten er en kold og kynisk kriger.*\n" + 
                                                                "*De bruger deres viden inden for krigsførelse til at skabe en tilværelse domineret af død og konflikt.*\n" +
                                                                "*Dog er deres evner til at interagere med andre mennesker forværret, da krig sjældent tillader lange og meningsfulde samtaler.*\n \n" + 
                                                                "__**Evner:**__\n" +
                                                                "**Amatører...**\n" +
                                                                "*I kamp mod ‘Bandit’ og ‘Soldat’ fjender har Lejesoldaten altid +1 Initiativ og +5 på sit første angreb under kampen (medmindre specificeret)*\n" +
                                                                "**Kampplan**\n" +
                                                                "*Ved mulighed kan Lejesoldaten give fif og råd til en medspiller. Dette kan være under en rejse, eller mens i lejr. Kampplan giver den anden spiller plus +10 i deres højeste Kamp Evne under HELE den næste kamp (Kan kun bruges på én spiller pr. kamp og hvis nogle Kamp Evner er lige, vælger spilleren selv)*\n \n" +
                                                                "__**Pros:**__\n" +
                                                                "+10  **Nærkamp**\n" +
                                                                "+10  **Strenge/Kaste Våben**\n" +
                                                                "+10  **Skydevåben**\n" +
                                                                "+10  **Snig**\n \n" +
                                                                "__**Cons:**__\n" +
                                                                "-10  **Smigre**\n" +
                                                                "-10  **Løgn**\n" +
                                                                "-10  **Intimiderer**\n" +
                                                                "-10  **Handel**", color=0xF8AB68)                
                lejesoldat_embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/701150185580920852/84106079_474196929921976_1350826510910488576_n.png?width=337&height=626")
                await channel.send(embed=lejesoldat_embed)
                await asyncio.sleep(1)
# MUTANT
                mutant_embed = discord.Embed(title=f"__**Mutant**__", description=f"*Mutanter er et alment syn på Gaia og iblandt dem er “Brødet” den mest udbredte art.*\n" + 
                                                                "*Disse store og muskuløse spektakler bliver ofte brugt som beskyttelse eller arbejdskraft af folk der ved hvordan man bedst bruger deres “unikke kvalifikationer.”*\n \n" +
                                                                "__**Evner:**__\n" +
                                                                "**En ordentlig Lap**\n" +
                                                                "*Mutanten kan ikke, med mindre specificeret, bruge rustning eller et-hånds våben. Derimod, tæller et alment to-hånds våben som et et-hånds våben for Mutanter. (Specificeres)*\n" +
                                                                "**Bedre end Goliat**\n" +
                                                                "*Mutanten kan ikke blive væltet af  “Menneskelige” fjender i nærkamp.*\n \n" +
                                                                "__**Pros:**__\n" +
                                                                "+10  **Styrke**\n" +
                                                                "+5  **Nærkamp**\n" +
                                                                "+5  **Intimiderer**\n" +
                                                                "+5  **Overlevelse**\n" +
                                                                "+5  **Udholdenhed**\n \n" +
                                                                "__**Cons:**__\n" +
                                                                "Mutanten kan ALDRIG bruge Snig evnen, med mindre specificeret.\n" +
                                                                "-10  **Intelligens**\n" +
                                                                "-10  **Finesse**", color=0xB381FF)                
                mutant_embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/701422344303935578/84281218_167098841248618_601311428783112192_n.png")
                await channel.send(embed=mutant_embed)
                await asyncio.sleep(1)
# PROSPEKTER
                prospekter_embed = discord.Embed(title=f"__**Prospekter**__", description=f"*Prospekteren ved hvad selv det mest almene skrammel er værd for den korrekte køber.*\n" + 
                                                                "*Disse opportunister findes tit i gang med at gennemsøge og plyndre ruiner for hvad andre ville betegne som skrald og skidt.*\n \n" +
                                                                "__**Evner:**__\n" +
                                                                "**Værdi er relativt**\n" +
                                                                "*Prospekteren kan sælge alle vare til alle slags købmænd. Eksempelvis kan de sælge en læge ammunition hvor andre Baggrunde kun ville kunne sælge relevante vare.*\n" +
                                                                "**Lad mig se…**\n" +
                                                                "*Prospektoren kan under Indsamling slå en D6, terningens værdi vil blive lagt til antallet af genstande de er i stand til at finde (Specificeres af GM)*\n \n" +
                                                                "__**Pros:**__\n" +
                                                                "+10  **Handel**\n" +
                                                                "+10  **Reparation**\n" +
                                                                "+10  **Fælder**\n \n" +
                                                                "__**Cons:**__\n" +
                                                                "Prospektoren kan ikke dele ud af sin inventar, med mindre en anden spiller slår om Smir imod dem eller bytter noget af ligende værdi (Aftales mellem Spillere og GM)", color=0x8DDF54)                
                prospekter_embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/701156872094482563/83926999_2565824347032825_6396469320481767424_n.png?width=431&height=629")
                await channel.send(embed=prospekter_embed)
                await asyncio.sleep(1)
# SAMARIT
                samarit_embed = discord.Embed(title=f"__**Samarit**__", description=f"*Omvandrende Samaritter plejer tit deres erhverv i krigshærgede eller lovløse områder.*\n" + 
                                                                "*Oftest er de tidligere læger fra mindre landsbyer, eller simple godhjertede sjæle der er drevet til at hjælpe deres næste.*\n \n" +
                                                                "__**Evner:**__\n" +
                                                                "**Ræk mig den kniv…**\n" +
                                                                "*Samaritten kan altid udøve Seriøs Lægehjælp så længe de er i besiddelse af almene medicinale effekter, bandager, gazebind etc. Mængden af medicinale effekter forøger chancen for succes.*\n" +
                                                                "**Hvor gør det ondt?**\n" +
                                                                "*Samaritten kan, uden brug af Lægevidenskab, altid identificere eller opdage hvis en medspiller er forgiftet og eller syg.*\n \n" +
                                                                "__**Pros:**__\n" +
                                                                "+10  **Lægevidenskab**\n" +
                                                                "+5  **Overlevelse**\n \n" +
                                                                "__**Cons:**__\n" +
                                                                "-20  **Intimidere**\n" +
                                                                "-20  **Løgn**", color=0xF8FF5C)                
                samarit_embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/701159483333673106/83220722_629791384445351_7846450275316400128_n.png?width=459&height=629")
                await channel.send(embed=samarit_embed)
                await asyncio.sleep(1)
# TEKKER
                tekker_embed = discord.Embed(title=f"__**Tekker**__", description=f"*En Tekker lever og dør af teknologien de søger.*\n" + 
                                                                "*Disse personer er tit tidligere prospektere der har indset at værdien ikke ligger i de almene materialer, men i de mange stadig fungerende stykker teknologi der kan samles og sælges for stor profit.*\n" +
                                                                "*Mange er på grund af deres mange interaktioner med Søgerne og andre technofile grupper selv blevet næsten religiøse omkring det de søger.*\n \n" +
                                                                "__**Evner:**__\n" +
                                                                "**Maskinen forblive**\n" +
                                                                "*Tekkere kan uden brug af terninger, altid identificere mere kompliceret teknologi. Ydermere kan de aldrig Katastrofalt Fejle nogle evne-check med Videnskab.*\n" +
                                                                "**Du ved intet…**\n" +
                                                                "*Tekkere vil altid have +10 i Handel under salg eller indkøb af Arkeo-Tek (Specificeres)*\n \n" +
                                                                "__**Pros:**__\n" +
                                                                "+10  **Intelligens**\n" +
                                                                "+10  **Videnskab**\n \n" +
                                                                "__**Cons:**__\n" +
                                                                "-10  **Nærkamp**\n" +
                                                                "-10  **Strenge/Kaste Våben**\n" +
                                                                "-10  **Skydevåben**\n" +
                                                                "-10  **Snig**", color=0xFFA600)                
                tekker_embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/701162087665106974/83045972_174124687257093_8104502798202175488_n.png?width=370&height=629")
                await channel.send(embed=tekker_embed)
                await asyncio.sleep(1) 
# VANDRER
                vandrer_embed = discord.Embed(title=f"__**Vandrer**__", description=f"*Utallige Vandrere søger et bedre liv når deres gamle er gået dem til halsen, eller er blevet dem berøvet.*\n" + 
                                                                "*Disse retningsløse sjæle søger altid over den næste horisont hvor græsset forhåbentligt er grønnere og vandet… mindre grønt.*\n \n" +
                                                                "__**Evner:**__\n" +
                                                                "**Nu mørkere en nat, nu lysere stjerner**\n" +
                                                                "*Vandreren får ingen hæmninger under evne-check i mørke.*\n" +
                                                                "**Jeg har set det meste**\n" +
                                                                "*Vandreren får +5 på alle Frygt check*\n \n" +
                                                                "__**Pros:**__\n" +
                                                                "+5  **Snig**\n" +
                                                                "+5  **Overlevelse**\n" +
                                                                "+5  **Finesse**\n" +
                                                                "+5  **Perception**\n \n" +
                                                                "__**Cons:**__\n" +
                                                                "-10  **Smigre**\n" +
                                                                "-10  **Løgn**\n" +
                                                                "-10  **Intimidere**\n" +
                                                                "-10  **Handel**", color=0x979797)                
                vandrer_embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/701165046566354964/83400007_2515410042066042_1883996204778389504_n.png?width=484&height=629")
                await channel.send(embed=vandrer_embed)
                await asyncio.sleep(1)               


                msg1 = await channel.send("Above is a list of all the characters that you can choose from\nReact to this message with the character you want to play\n" +
                ":radio_button: for **Beskytter**\n" +
                ":white_circle: for **Charlatan**\n" +
                ":black_circle: for **Indfødt**\n" +
                ":red_circle: for **Jæger**\n" +
                ":blue_circle: for **Landevejsrøver**\n" +
                ":brown_circle: for **Lejesoldat**\n" +
                ":purple_circle: for **Mutant**\n" +
                ":green_circle: for **Prospekter**\n" +
                ":yellow_circle: for **Samarit**\n" +
                ":orange_circle: for **Tekker**\n" +
                ":new_moon: for **Vandrer**")

                await msg1.add_reaction(emoji='\U0001F518') #radio_button
                await msg1.add_reaction(emoji='\u26AA') #white_circle
                await msg1.add_reaction(emoji='\u26AB') #black_circle
                await msg1.add_reaction(emoji='\U0001F534') #red_circle
                await msg1.add_reaction(emoji='\U0001F535') #blue_circle
                await msg1.add_reaction(emoji='\U0001F7E4') #brown_circle
                await msg1.add_reaction(emoji='\U0001F7E3') #purple_circle
                await msg1.add_reaction(emoji='\U0001F7E2') #green_circle
                await msg1.add_reaction(emoji='\U0001F7E1') #yellow_circle
                await msg1.add_reaction(emoji='\U0001F7E0') #orange_circle
                await msg1.add_reaction(emoji='\U0001F311') #new_moon
                await asyncio.sleep(1)

                res = await self.bot.wait_for('reaction_add')
                if res:
                    reaction, message.author = res
                    if str(reaction.emoji) == "\U0001F518":
                        ChosenCharacter = "Beskytter"
                    if str(reaction.emoji) == "\u26AA":
                        ChosenCharacter = "Charlatan"
                    if str(reaction.emoji) == "\u26AB":
                        ChosenCharacter = "Indfødt"                
                    if str(reaction.emoji) == "\U0001F534":
                        ChosenCharacter = "Jæger"                  
                    if str(reaction.emoji) == "\U0001F535":
                        ChosenCharacter = "Landevejsrøver" 
                    if str(reaction.emoji) == "\U0001F7E4":
                        ChosenCharacter = "Lejesoldat" 
                    if str(reaction.emoji) == "\U0001F7E3":
                        ChosenCharacter = "Mutant" 
                    if str(reaction.emoji) == "\U0001F7E2":
                        ChosenCharacter = "Prospekter"   
                    if str(reaction.emoji) == "\U0001F7E1":
                        ChosenCharacter = "Samarit"      
                    if str(reaction.emoji) == "\U0001F7E0":
                        ChosenCharacter = "Tekker"      
                    if str(reaction.emoji) == "\U0001F311":
                        ChosenCharacter = "Vandrer"    

                self.charactersheet[author_id]["Character Sheet"]["Chosen Character"] = ChosenCharacter 
                self.charactersheet[author_id]["Character Sheet"]["Level"] = 1 
#       KOMPETENCER
# CHOSEN CHARACTER
                await channel.purge(limit=20)
                msg2 = await channel.send(f"You have chosen to play as **{ChosenCharacter}**\n**Your characters pros and cons will automatically be added/subtracted from __all__ your rolls!**\n*No calculation is needed from your part*\n \nWe're now going to register your **Kompetencer**\nPlease only reply with numbers\nReact with :octagonal_sign: to cancel setup\n \nWhat is your **Styrke**?\n*Styrke - Hvor stærk er din karakter og hvor stor og bred er de?*\nRoll a **D10**")
                await msg2.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)    
# STYRKE
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                styrke = msg.content
                if styrke == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg3 = await channel.send(f"**Styrke** set as **{styrke}**\n \nWhat is your **Udholdenhed**?\n*Udholdenhed - Hvor mange liv har din karakter og kan de håndtere smerte?*\nRoll a **D10**")
                await msg3.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)
                self.charactersheet[author_id]["Character Sheet"]["Styrke"] = styrke 
# UDHOLDENHED
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                udholdenhed = msg.content
                if udholdenhed == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg4 = await channel.send(f"**Udholdenhed** set as **{udholdenhed}**\n \nWhat is your **Intelligens**?\n*Intelligens - Hvor klog er din karakter?*\nRoll a **D10**")
                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)                        
                self.charactersheet[author_id]["Character Sheet"]["Udholdenhed"] = udholdenhed 
# INTELLIGENS 
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                intelligens = msg.content
                if intelligens == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg4 = await channel.send(f"**Intelligens** set as **{intelligens}**\n \nWhat is your **Finesse**?\n*Finesse - Hvor hurtig og smidig er din karakter?*\nRoll a **D10**")
                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)                        
                self.charactersheet[author_id]["Character Sheet"]["Intelligens"] = intelligens 
# FINESSE 
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                finesse = msg.content
                if finesse == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg4 = await channel.send(f"**Finesse** set as **{finesse}**\n \nWhat is your **Perception**?\n*Perception - Hvor kvik/opmærksom er din karakter?*\nRoll a **D10**")
                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)                        
                self.charactersheet[author_id]["Character Sheet"]["Finesse"] = finesse 
# PERCEPTION 
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                perception = msg.content
                if perception == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg4 = await channel.send(f"**Perception** set as **{perception}**\n \nWhat is your **Karisma**?\n*Karisma - Hvor god er din karakter med andre personer?*\nRoll a **D10**")
                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)                        
                self.charactersheet[author_id]["Character Sheet"]["Perception"] = perception 
# KARISMA 
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                karisma = msg.content
                if karisma == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg4 = await channel.send(f"**Karisma** set as **{karisma}**\n \nWhat is your **Initiativ**?\n*Initiativ - Hvor hurtig er din karakter til at handle under pres?*\nRoll a **D10**")
                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)                        
                self.charactersheet[author_id]["Character Sheet"]["Karisma"] = karisma 
# INITIATIV 
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                initiativ = msg.content
                if initiativ == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg4 = await channel.send(f"**Initiativ** set as **{initiativ}**\n \nWe're now going to register your **Kamp Evner**\nPlease only reply with numbers\nReact with :octagonal_sign: to cancel setup\n \nWhat is your **Nærkamp**?\n*Nærkamp - Hvor god er din karakter med nærkampsvåben eller deres næver? (Påvirkes af Styrke)*\nRoll a **D20**")
                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)                        
                self.charactersheet[author_id]["Character Sheet"]["Initiativ"] = initiativ 
#       EVNER
#   KAMP
# NÆRKAMP 
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                nærkamp = msg.content
                if nærkamp == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg4 = await channel.send(f"**Nærkamp** set as **{nærkamp}**\n \nWhat is your **Kaste/Strenge Våben**?\n*Kaste/Strenge Våben - Hvor god er din karakter med en bue, spyd, osv. ?*\nRoll a **D20**")
                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)                        
                self.charactersheet[author_id]["Character Sheet"]["Nærkamp"] = nærkamp 
                self.charactersheet[author_id]["Character Sheet"]["Nærkamp_Bonus"] = 0 
# KASTE / STRENGE VÅBEN 
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                kaste_strenge_våben = msg.content
                if kaste_strenge_våben == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg4 = await channel.send(f"**Kaste/Strenge Våben** set as **{kaste_strenge_våben}**\n \nWhat is your **Skydevåben**?\n*Skydevåben - Hvor god er din karakter med pistoler, rifler osv.*\nRoll a **D20**")
                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)                        
                self.charactersheet[author_id]["Character Sheet"]["Kaste_Strenge_våben"] = kaste_strenge_våben
                self.charactersheet[author_id]["Character Sheet"]["Kaste_Strenge_våben_Bonus"] = 0
# SKYDEVÅBEN 
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                skydevåben = msg.content
                if skydevåben == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg4 = await channel.send(f"**Skydevåben** set as **{skydevåben}**\n \nWhat is your **Snig**?\n*Snig - Kan din karakter finde ud af at forblive uset? (Påvirkes af Finesse)*\nRoll a **D20**")
                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)                        
                self.charactersheet[author_id]["Character Sheet"]["Skydevåben"] = skydevåben
                self.charactersheet[author_id]["Character Sheet"]["Skydevåben_Bonus"] = 0
# SNIG 
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                snig = msg.content
                if snig == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg4 = await channel.send(f"**Snig** set as **{snig}**\n \nWe're now going to register your **Sociale Evner**\nPlease only reply with numbers\nReact with :octagonal_sign: to cancel setup\n \nWhat is your **Smigre**?\n*Smigre - Kan din karakter få information fra folk, eller manipulere dem?*\nRoll a **D20**")
                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)                        
                self.charactersheet[author_id]["Character Sheet"]["Snig"] = snig
                self.charactersheet[author_id]["Character Sheet"]["Snig_Bonus"] = 0
#       EVNER
#   SOCIALE EVNER
# SMIGRE 
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                smigre = msg.content
                if smigre == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg4 = await channel.send(f"**Smigre** set as **{smigre}**\n \nWhat is your **Løgn**?\n*Løgn - Kan din karakter fortælle en overbevisende løgn?*\nRoll a **D20**")
                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)                        
                self.charactersheet[author_id]["Character Sheet"]["Smigre"] = smigre
                self.charactersheet[author_id]["Character Sheet"]["Smigre_Bonus"] = 0
# LØGN 
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                løgn = msg.content
                if løgn == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg4 = await channel.send(f"**Løgn** set as **{løgn}**\n \nWhat is your **Intimiderer**?\n*Intimiderer - Hvor god er din karakter til skræmme andre omkring dem? (Påvirkes af Karisma eller Styrke)*\nRoll a **D20**")
                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)                        
                self.charactersheet[author_id]["Character Sheet"]["Løgn"] = løgn
                self.charactersheet[author_id]["Character Sheet"]["Løgn_Bonus"] = 0
# INTIMIDERER
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                intimiderer = msg.content
                if intimiderer == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg4 = await channel.send(f"**Intimiderer** set as **{intimiderer}**\n \nWhat is your **Handel**?\n*Handel - Hvor god er din karakter til køb og salg?*\nRoll a **D20**")
                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)                        
                self.charactersheet[author_id]["Character Sheet"]["Intimiderer"] = intimiderer
                self.charactersheet[author_id]["Character Sheet"]["Intimiderer_Bonus"] = 0
# HANDEL 
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                handel = msg.content
                if handel == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg4 = await channel.send(f"**Handel** set as **{handel}**\n \nWe're now going to register your **Håndværks Evner**\nPlease only reply with numbers\nReact with :octagonal_sign: to cancel setup\n \nWhat is your **Reparation**?\n*Reparation - Kan din karakter få ødelagte ting til at virke igen eller vedligeholde udstyr?*\nRoll a **D20**")
                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)                        
                self.charactersheet[author_id]["Character Sheet"]["Handel"] = handel
                self.charactersheet[author_id]["Character Sheet"]["Handel_Bonus"] = 0
#       EVNER
#   HÅNDVÆRKS EVNER
# REPERATION
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                reparation = msg.content
                if reparation == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg4 = await channel.send(f"**Reparation** set as **{reparation}**\n \nWhat is your **Fælder**?\n*Fælder - Kan din karakter armere og desarmere fælder? (Påvirkes af Perception eller Finesse)*\nRoll a **D20**")
                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)                        
                self.charactersheet[author_id]["Character Sheet"]["Reparation"] = reparation
                self.charactersheet[author_id]["Character Sheet"]["Reparation_Bonus"] = 0
# FÆLDER
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                fælder = msg.content
                if fælder == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg4 = await channel.send(f"**Fælder** set as **{fælder}**\n \nWhat is your **Overlevelse**?\n*Overlevelse - Kan din karakter dressere et dyr, lave en rebstige osv.*\nRoll a **D20**")
                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)                        
                self.charactersheet[author_id]["Character Sheet"]["Fælder"] = fælder
                self.charactersheet[author_id]["Character Sheet"]["Fælder_Bonus"] = 0
# OVERLEVELSE
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                overlevelse = msg.content
                if overlevelse == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg4 = await channel.send(f"**Overlevelse** set as **{overlevelse}**\n \nWhat is your **Håndarbejde**?\n*Håndarbejde - Kan din karakter skabe fra skrot eller kombinere ting? (Påvirkes af Intelligens)*\nRoll a **D20**")
                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)                        
                self.charactersheet[author_id]["Character Sheet"]["Overlevelse"] = overlevelse
                self.charactersheet[author_id]["Character Sheet"]["Overlevelse_Bonus"] = 0
# HÅNDARBEJDE 
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                håndarbejde = msg.content
                if håndarbejde == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg4 = await channel.send(f"**Håndarbejde** set as **{håndarbejde}**\n \nWe're now going to register your **Esoteriske Evner**\nPlease only reply with numbers\nReact with :octagonal_sign: to cancel setup\n \nWhat is your **Videnskab**?\n*Videnskab - Hvor god er din karakter med computere, teknologi osv. (Påvirkes af Intelligens)*\nRoll a **D20**")
                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)                        
                self.charactersheet[author_id]["Character Sheet"]["Håndarbejde"] = håndarbejde
                self.charactersheet[author_id]["Character Sheet"]["Håndarbejde_Bonus"] = 0
#       EVNER
#   ESOTERISKE EVNER
# VIDENSKAB
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                videnskab = msg.content
                if videnskab == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg4 = await channel.send(f"**Videnskab** set as **{videnskab}**\n \nWhat is your **Alkymi**?\n*Alkymi - Kan din karakter bruge omverdenen til at hjælpe, eller skade andre? (Påvirkes af Intelligens)*\nRoll a **D20**")
                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)                        
                self.charactersheet[author_id]["Character Sheet"]["Videnskab"] = videnskab
                self.charactersheet[author_id]["Character Sheet"]["Videnskab_Bonus"] = 0
# ALKYMI
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                alkymi = msg.content
                if alkymi == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg4 = await channel.send(f"**Alkymi** set as **{alkymi}**\n \nWhat is your **Lægevidenskab**?\n*Lægevidenskab - Ved din karakter om bandager osv. (Påvirkes af Intelligens)*\nRoll a **D20**")
                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)                        
                self.charactersheet[author_id]["Character Sheet"]["Alkymi"] = alkymi
                self.charactersheet[author_id]["Character Sheet"]["Alkymi_Bonus"] = 0
# LÆGEVIDENSKAB
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                lægevidenskab = msg.content
                if lægevidenskab == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg4 = await channel.send(f"**Lægevidenskab** set as **{lægevidenskab}**\n \nWhat is your **Historie**?\n*Historie - Ved din karakter hvad folk snakker om? (Påvirkes af Intelligens)*\nRoll a **D20**")
                await msg4.add_reaction(emoji='\U0001F6D1')     # Add cancel reaction to message
                await asyncio.sleep(1)                        
                self.charactersheet[author_id]["Character Sheet"]["Lægevidenskab"] = lægevidenskab
                self.charactersheet[author_id]["Character Sheet"]["Lægevidenskab_Bonus"] = 0
# HISTORIE
                msg = await self.bot.wait_for('message', check=lambda message: message.author == message.author and message.channel == channel)    
                historie = msg.content
                if historie == "cancel":                         # Takes use of CancelMenu cog
                        await channel.purge(limit=10)
                        await channel.send("Command canceled!")
                        return
                await channel.purge(limit=5)
                msg4 = await channel.send(f"**Historie** set as **{historie}**")
                await asyncio.sleep(1)                        
                self.charactersheet[author_id]["Character Sheet"]["Historie"] = historie
                self.charactersheet[author_id]["Character Sheet"]["Historie_Bonus"] = 0


                await asyncio.sleep(3)
                await channel.purge(limit=5)

                fh.save_file(self.charactersheet, 'charactersheet')
                self.load_data()

# MESSAGES POSTED IN CHANNELS
# CALCULATION OF BONUSES AND NEGATES

# BESKYTTER
                if self.charactersheet[author_id]["Character Sheet"]["Chosen Character"] == "Beskytter":
                        beskytter_embed = discord.Embed(title=f"__**Beskytter**__", description=f"*Bestyktteren er en lavløs monster-jæger.*\n" + 
                                                                "*Disse fromme og fanatiske sjæle opsøger ofte Mutanter eller de Udødelige med intentioner om at udslette disse vanskabninger for andres sikkerhed.*\n" + 
                                                                "*Disse ildsjæle er oftest lav løse på grund af deres “ekstreme” synspunkter.*\n \n" +
                                                                "__**Evner:**__\n" +
                                                                "**Gudløse Spetakler**\n" +
                                                                "*Beskytteren vil altid have +5 Initiativ OG +1 Udholdenhed i kamp mod “Udødelige” “Stakkel” og “Trolde” fjender. Dog vil de samtidig have INGEN mulighed for at bruge Sociale Evner i interaktioner med Mutant NPC’er*\n" +
                                                                "**Vores sag er Hellig!**\n" +
                                                                "*I interaktioner med “Troende” NPC’er vil Beskytteren altid have +5 Sociale Evner, men -10 med “Ikke-Troende” NPC’er (Specificeres)*\n \n" +
                                                                "__**Pros:**__\n" +
                                                                "+15  **Nærkamp**\n" +
                                                                "+5  **Styrke**\n \n" +
                                                                "__**Cons:**__\n" +
                                                                "Beskytteren kan ikke gøre brug af Skydevåben.", color=0x004CB9)                
                        beskytter_embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/701094688144490536/84447639_113161510125112_7795953704867201024_n.png?width=485&height=627")
                        await channel.send(embed=beskytter_embed)
                        await asyncio.sleep(1)
        # BONUS
                        nærkamp_value = int(self.charactersheet[author_id]["Character Sheet"]["Nærkamp"])
                        nærkamp_bonus = 15
                        nærkamp_value += nærkamp_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Nærkamp"] = nærkamp_value

                        styrke_value = int(self.charactersheet[author_id]["Character Sheet"]["Styrke"])
                        styrke_bonus = 5
                        styrke_value += styrke_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Styrke"] = styrke_value

                        fh.save_file(self.charactersheet, 'charactersheet')
# CHARLATAN
                if self.charactersheet[author_id]["Character Sheet"]["Chosen Character"] == "Charlatan":
                        charlatan_embed = discord.Embed(title=f"__**Charlatan**__", description=f"*En tunge af sølv og et flot smil kan gøre en tigger til baron i den rette situation.*\n" + 
                                                                "*Charlataner og andre fupmagere er ikke unormale syn i de mere befærdede og manfolkdige byområder på Gaia.*\n" + 
                                                                "*Med deres rigdom gør de ofte brug af mere “direkte” arbejdskraft hvis en confrontation skulle opstå.*\n \n" +
                                                                "__**Evner:**__\n" +
                                                                "**Den klarer i… jeg skal væk**\n" +
                                                                "*Under kamp med alle “Menneskelige” fjender vil Charlatanen altid have lavest Initiativ i gruppen, men højeste imod “Ikke-Menneskelige” fjender (Specificeres)*\n \n" +
                                                                "__**Pros:**__\n" +
                                                                "+15  **Løgn**\n" +
                                                                "+15  **Smir**\n" +
                                                                "+15  **Handel**\n" +
                                                                "+15  **Snig**\n \n" +
                                                                "__**Cons:**__\n" +
                                                                "Charlatanen kan IKKE bruge to-hånds våben eller rustning.", color=0xFAFBF9)                
                        charlatan_embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/701071214403125358/83977493_200402444417514_4410246142369988608_n.png?width=483&height=627")
                        await channel.send(embed=charlatan_embed)
                        await asyncio.sleep(1)
        # BONUS
                        løgn_value = int(self.charactersheet[author_id]["Character Sheet"]["Løgn"])
                        løgn_bonus = 15
                        løgn_value += løgn_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Løgn"] = løgn_value

                        smigre_value = int(self.charactersheet[author_id]["Character Sheet"]["Smigre"])
                        smigre_bonus = 15
                        smigre_value += smigre_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Smigre"] = smigre_value

                        handel_value = int(self.charactersheet[author_id]["Character Sheet"]["Handel"])
                        handel_bonus = 15
                        handel_value += handel_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Handel"] = handel_value

                        snig_value = int(self.charactersheet[author_id]["Character Sheet"]["Snig"])
                        snig_bonus = 15
                        snig_value += snig_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Snig"] = snig_value

                        fh.save_file(self.charactersheet, 'charactersheet')
# INDFØDT
                if self.charactersheet[author_id]["Character Sheet"]["Chosen Character"] == "Indfødt":
                        indfødt_embed = discord.Embed(title=f"__**Indfødt**__", description=f"*Efter Katastrofen er mange mennesker regresseret tilbage til vores primale fortid.*\n" + 
                                                                "*Disse stammefolk er udholdende og krigeriske, men til tider også overtroiske og mindre intelligente end de mere “civiliserede” sorter.*\n \n" + 
                                                                "__**Evner:**__\n" +
                                                                "**Tro til Moder Gaia**\n" +
                                                                "*Hvis den Indfødte kun er iklædt eller gør brug udstyr fundet i naturen eller de selv har skabt, får de +1 på alle **relevante** terningekast (Specificeres)*\n" +
                                                                "**Hærdet legeme**\n" +
                                                                "*Indfødte er immun overfor de fleste gifte (Specificeres)*\n \n" +
                                                                "__**Pros:**__\n" +
                                                                "+5  **Nærkamp**\n" +
                                                                "+5  **Udholdenhed**\n" +
                                                                "+5  **Overlevelse**\n" +
                                                                "+5  **Alkymi**\n" +
                                                                "+5  **Styrke **\n \n" +
                                                                "__**Cons:**__\n" +
                                                                "Den Indfødte kan ALDRIG bruge Videnskab evnen.\n" +
                                                                "-10  **Sociale Evner**", color=0x030303)                
                        indfødt_embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/701080791597318154/83949023_2633611816925481_519829439547179008_n.png?width=444&height=627")
                        await channel.send(embed=indfødt_embed)
                        await asyncio.sleep(1)
        # BONUS
                        nærkamp_value = int(self.charactersheet[author_id]["Character Sheet"]["Nærkamp"])
                        nærkamp_bonus = 5
                        nærkamp_value += nærkamp_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Nærkamp"] = nærkamp_value

                        udholdenhed_value = int(self.charactersheet[author_id]["Character Sheet"]["Udholdenhed"])
                        udholdenhed_bonus = 5
                        udholdenhed_value += udholdenhed_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Udholdenhed"] = udholdenhed_value

                        alkymi_value = int(self.charactersheet[author_id]["Character Sheet"]["Alkymi"])
                        alkymi_bonus = 5
                        alkymi_value += alkymi_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Alkymi"] = alkymi_value

                        alkymi_value = int(self.charactersheet[author_id]["Character Sheet"]["Alkymi"])
                        alkymi_bonus = 5
                        alkymi_value += alkymi_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Alkymi"] = alkymi_value

                        styrke_value = int(self.charactersheet[author_id]["Character Sheet"]["Styrke"])
                        styrke_bonus = 5
                        styrke_value += styrke_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Styrke"] = styrke_value
        # NEGATE
                        smigre_value = int(self.charactersheet[author_id]["Character Sheet"]["Smigre"])
                        smigre_negate = 10
                        smigre_value -= smigre_negate
                        if smigre_value < 0:
                                smigre_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Smigre"] = smigre_value

                        løgn_value = int(self.charactersheet[author_id]["Character Sheet"]["Løgn"])
                        løgn_negate = 10
                        løgn_value -= løgn_negate
                        if løgn_value < 0:
                                løgn_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Løgn"] = løgn_value

                        intimiderer_value = int(self.charactersheet[author_id]["Character Sheet"]["Intimiderer"])
                        intimiderer_negate = 10
                        intimiderer_value -= intimiderer_negate
                        if intimiderer_value < 0:
                                intimiderer_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Intimiderer"] = intimiderer_value

                        handel_value = int(self.charactersheet[author_id]["Character Sheet"]["Handel"])
                        handel_negate = 10
                        handel_value -= handel_negate
                        if handel_value < 0:
                                handel_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Handel"] = handel_value

                        fh.save_file(self.charactersheet, 'charactersheet')
# JÆGER
                if self.charactersheet[author_id]["Character Sheet"]["Chosen Character"] == "Jæger":
                        jæger_embed = discord.Embed(title=f"__**Jæger**__", description=f"*Siden tidernes morgen har mennesket jaget, dette ændrede sig ikke da vi drog ud mellem stjernerne.*\n" + 
                                                                "*Jægeren har brugt sit liv i vildmarken, både som jæger og som bytte.*\n \n" + 
                                                                "__**Evner:**__\n" +
                                                                "**Sikke et eksemplar**\n" +
                                                                "*Jægeren kan altid identificere en Dyrisk fjendes (også Bossers) svagheder. Ydermere kan de oftest skaffe sjældne ressourcer hvis de dressere dyr.*\n" +
                                                                "**Ekspert**\n" +
                                                                "*I kamp mod ‘Dyriske’ fjender har Jægeren altid +1 Initiativ og hvis Jægeren er den første i gruppen til at angribe en ‘Dyrisk’ fjende, kan de ikke misse deres første angreb.*\n \n" +
                                                                "__**Pros:**__\n" +
                                                                "+5  **Kaste/Strenge Våben**\n" +
                                                                "+5  **Fælder**\n" +
                                                                "+5  **Overlevelse**\n \n" +
                                                                "__**Cons:**__\n" +
                                                                "-5  **Videnskab**\n" +
                                                                "-5  **Skydevåben**", color=0xF50404)                
                        jæger_embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/701086619729657876/83272722_212026363273452_6715150482186174464_n.png?width=454&height=627")
                        await channel.send(embed=jæger_embed)
                        await asyncio.sleep(1) 
        # BONUS
                        kaste_strenge_våben_value = int(self.charactersheet[author_id]["Character Sheet"]["Kaste_Strenge_våben"])
                        kaste_strenge_våben_bonus = 5
                        kaste_strenge_våben_value += kaste_strenge_våben_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Kaste_Strenge_våben"] = kaste_strenge_våben_value   

                        fælder_value = int(self.charactersheet[author_id]["Character Sheet"]["Fælder"])
                        fælder_bonus = 5
                        fælder_value += fælder_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Fælder"] = fælder_value     

                        overlevelse_value = int(self.charactersheet[author_id]["Character Sheet"]["Overlevelse"])
                        overlevelse_bonus = 5
                        overlevelse_value += overlevelse_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Overlevelse"] = overlevelse_value   
        # NEGATE
                        videnskab_value = int(self.charactersheet[author_id]["Character Sheet"]["Videnskab"])
                        videnskab_negate = 5
                        videnskab_value -= videnskab_negate
                        if videnskab_value < 0:
                                videnskab_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Videnskab"] = videnskab_value  

                        skydevåben_value = int(self.charactersheet[author_id]["Character Sheet"]["Skydevåben"])
                        skydevåben_negate = 5
                        skydevåben_value -= skydevåben_negate
                        if skydevåben_value < 0:
                                skydevåben_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Skydevåben"] = skydevåben_value   

                        fh.save_file(self.charactersheet, 'charactersheet')         
# LANDEVEJSRØVER
                if self.charactersheet[author_id]["Character Sheet"]["Chosen Character"] == "Landevejsrøver":
                        landevejsrøver_embed = discord.Embed(title=f"__**Landevejsrøver**__", description=f"*Sønderlandet og hele Gaia er plaget af gemene banditter der ligger på lur langs befærdede veje.*\n" + 
                                                                "*De berøver folk for alt hvad de er værd og nogen gange ender det med at offeret også må bøde med livet.*\n" +
                                                                "*Nogle af disse lovløse lever således af nødvendighed, mens andre ser det som naturens love.*\n \n" + 
                                                                "__**Evner:**__\n" +
                                                                "**Nu du skulle nævne det…**\n" +
                                                                "*Under snakke eller handel med “Kriminelle” NPC’er har Landevejsrøveren altid +5 i Sociale Evner, men -5 med “Lovlydige” karakterer (Specificeres)*\n" +
                                                                "**Jeg er realist!**\n" +
                                                                "*Hvis Landevejsrøveren kommer under 50% Liv får de +1 Bevægelses handling, så længe det er VÆK fra fjenden.*\n \n" +
                                                                "__**Pros:**__\n" +
                                                                "+5  **Løgn**\n" +
                                                                "+5  **Snig**\n \n" +
                                                                "__**Cons:**__\n" +
                                                                "-10  **Smigre**", color=0x20B5FF)                
                        landevejsrøver_embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/701091406424440832/84333690_697893080745801_5555861783052288000_n.png?width=437&height=627")
                        await channel.send(embed=landevejsrøver_embed)
                        await asyncio.sleep(1) 

                # BONUS
                        løgn_value = int(self.charactersheet[author_id]["Character Sheet"]["Løgn"])
                        løgn_bonus = 5
                        løgn_value += løgn_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Løgn"] = løgn_value 

                        snig_value = int(self.charactersheet[author_id]["Character Sheet"]["Snig"])
                        snig_bonus = 5
                        snig_value += snig_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Snig"] = snig_value 

                # NEGATE
                        smigre_value = int(self.charactersheet[author_id]["Character Sheet"]["Smigre"])
                        smigre_negate = 10
                        smigre_value -= smigre_negate
                        if smigre_value < 0:
                                smigre_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Smigre"] = smigre_value

                        fh.save_file(self.charactersheet, 'charactersheet') 
# LEJESOLDAT
                if self.charactersheet[author_id]["Character Sheet"]["Chosen Character"] == "Lejesoldat":
                        lejesoldat_embed = discord.Embed(title=f"__**Lejesoldat**__", description=f"*Lejesoldaten er en kold og kynisk kriger.*\n" + 
                                                                "*De bruger deres viden inden for krigsførelse til at skabe en tilværelse domineret af død og konflikt.*\n" +
                                                                "*Dog er deres evner til at interagere med andre mennesker forværret, da krig sjældent tillader lange og meningsfulde samtaler.*\n \n" + 
                                                                "__**Evner:**__\n" +
                                                                "**Amatører...**\n" +
                                                                "*I kamp mod ‘Bandit’ og ‘Soldat’ fjender har Lejesoldaten altid +1 Initiativ og +5 på sit første angreb under kampen (medmindre specificeret)*\n" +
                                                                "**Kampplan**\n" +
                                                                "*Ved mulighed kan Lejesoldaten give fif og råd til en medspiller. Dette kan være under en rejse, eller mens i lejr. Kampplan giver den anden spiller plus +10 i deres højeste Kamp Evne under HELE den næste kamp (Kan kun bruges på én spiller pr. kamp og hvis nogle Kamp Evner er lige, vælger spilleren selv)*\n \n" +
                                                                "__**Pros:**__\n" +
                                                                "+10  **Nærkamp**\n" +
                                                                "+10  **Strenge/Kaste Våben**\n" +
                                                                "+10  **Skydevåben**\n" +
                                                                "+10  **Snig**\n \n" +
                                                                "__**Cons:**__\n" +
                                                                "-10  **Smigre**\n" +
                                                                "-10  **Løgn**\n" +
                                                                "-10  **Intimiderer**\n" +
                                                                "-10  **Handel**", color=0xF8AB68)                
                        lejesoldat_embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/701150185580920852/84106079_474196929921976_1350826510910488576_n.png?width=337&height=626")
                        await channel.send(embed=lejesoldat_embed)
                        await asyncio.sleep(1)

                # BONUS
                        nærkamp_value = int(self.charactersheet[author_id]["Character Sheet"]["Nærkamp"])
                        nærkamp_bonus = 10
                        nærkamp_value += nærkamp_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Nærkamp"] = nærkamp_value

                        kaste_strenge_våben_value = int(self.charactersheet[author_id]["Character Sheet"]["Kaste_Strenge_våben"])
                        kaste_strenge_våben_bonus = 10
                        kaste_strenge_våben_value += kaste_strenge_våben_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Kaste_Strenge_våben"] = kaste_strenge_våben_value

                        skydevåben_value = int(self.charactersheet[author_id]["Character Sheet"]["Skydevåben"])
                        skydevåben_bonus = 10
                        skydevåben_value += skydevåben_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Skydevåben"] = skydevåben_value

                        snig_value = int(self.charactersheet[author_id]["Character Sheet"]["Snig"])
                        snig_bonus = 10
                        snig_value += snig_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Snig"] = snig_value
                 # NEGATE
                        smigre_value = int(self.charactersheet[author_id]["Character Sheet"]["Smigre"])
                        smigre_negate = 10
                        smigre_value -= smigre_negate
                        if smigre_value < 0:
                                smigre_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Smigre"] = smigre_value

                        løgn_value = int(self.charactersheet[author_id]["Character Sheet"]["Løgn"])
                        løgn_negate = 10
                        løgn_value -= løgn_negate
                        if løgn_value < 0:
                                løgn_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Løgn"] = løgn_value

                        intimiderer_value = int(self.charactersheet[author_id]["Character Sheet"]["Intimiderer"])
                        intimiderer_negate = 10
                        intimiderer_value -= intimiderer_negate
                        if intimiderer_value < 0:
                                intimiderer_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Intimiderer"] = intimiderer_value

                        handel_value = int(self.charactersheet[author_id]["Character Sheet"]["Handel"])
                        handel_negate = 10
                        handel_value -= handel_negate
                        if handel_value < 0:
                                handel_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Handel"] = handel_value

                        fh.save_file(self.charactersheet, 'charactersheet') 
# MUTANT
                if self.charactersheet[author_id]["Character Sheet"]["Chosen Character"] == "Mutant":
                        mutant_embed = discord.Embed(title=f"__**Mutant**__", description=f"*Mutanter er et alment syn på Gaia og iblandt dem er “Brødet” den mest udbredte art.*\n" + 
                                                                "*Disse store og muskuløse spektakler bliver ofte brugt som beskyttelse eller arbejdskraft af folk der ved hvordan man bedst bruger deres “unikke kvalifikationer.”*\n \n" +
                                                                "__**Evner:**__\n" +
                                                                "**En ordentlig Lap**\n" +
                                                                "*Mutanten kan ikke, med mindre specificeret, bruge rustning eller et-hånds våben. Derimod, tæller et alment to-hånds våben som et et-hånds våben for Mutanter. (Specificeres)*\n" +
                                                                "**Bedre end Goliat**\n" +
                                                                "*Mutanten kan ikke blive væltet af  “Menneskelige” fjender i nærkamp.*\n \n" +
                                                                "__**Pros:**__\n" +
                                                                "+10  **Styrke**\n" +
                                                                "+5  **Nærkamp**\n" +
                                                                "+5  **Intimiderer**\n" +
                                                                "+5  **Overlevelse**\n" +
                                                                "+5  **Udholdenhed**\n \n" +
                                                                "__**Cons:**__\n" +
                                                                "Mutanten kan ALDRIG bruge Snig evnen, med mindre specificeret.\n" +
                                                                "-10  **Intelligens**\n" +
                                                                "-10  **Finesse**", color=0xB381FF)                
                        mutant_embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/701422344303935578/84281218_167098841248618_601311428783112192_n.png")
                        await channel.send(embed=mutant_embed)
                        await asyncio.sleep(1) 

                # BONUS
                        styrke_value = int(self.charactersheet[author_id]["Character Sheet"]["Styrke"])
                        syrke_bonus = 10
                        styrke_value += syrke_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Styrke"] = styrke_value

                        nærkamp_value = int(self.charactersheet[author_id]["Character Sheet"]["Nærkamp"])
                        nærkamp_bonus = 5
                        nærkamp_value += nærkamp_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Nærkamp"] = nærkamp_value

                        intimiderer_value = int(self.charactersheet[author_id]["Character Sheet"]["Intimiderer"])
                        intimiderer_bonus = 5
                        intimiderer_value += intimiderer_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Intimiderer"] = intimiderer_value

                        overlevelse_value = int(self.charactersheet[author_id]["Character Sheet"]["Overlevelse"])
                        overlevelse_bonus = 5
                        overlevelse_value += overlevelse_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Overlevelse"] = overlevelse_value

                        udholdenhed_value = int(self.charactersheet[author_id]["Character Sheet"]["Udholdenhed"])
                        udholdenhed_bonus = 5
                        udholdenhed_value += udholdenhed_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Udholdenhed"] = udholdenhed_value 
                # NEGATE
                        intelligens_value = int(self.charactersheet[author_id]["Character Sheet"]["Intelligens"])
                        intelligens_negate = 10
                        intelligens_value -= intelligens_negate
                        if intelligens_value < 0:
                                intelligens_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Intelligens"] = intelligens_value

                        finesse_value = int(self.charactersheet[author_id]["Character Sheet"]["Finesse"])
                        finesse_negate = 10
                        finesse_value -= finesse_negate
                        if finesse_value < 0:
                                finesse_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Finesse"] = finesse_value

                        fh.save_file(self.charactersheet, 'charactersheet')
# PROSPEKTER
                if self.charactersheet[author_id]["Character Sheet"]["Chosen Character"] == "Prospekter":
                        prospekter_embed = discord.Embed(title=f"__**Prospekter**__", description=f"*Prospekteren ved hvad selv det mest almene skrammel er værd for den korrekte køber.*\n" + 
                                                                "*Disse opportunister findes tit i gang med at gennemsøge og plyndre ruiner for hvad andre ville betegne som skrald og skidt.*\n \n" +
                                                                "__**Evner:**__\n" +
                                                                "**Værdi er relativt**\n" +
                                                                "*Prospekteren kan sælge alle vare til alle slags købmænd. Eksempelvis kan de sælge en læge ammunition hvor andre Baggrunde kun ville kunne sælge relevante vare.*\n" +
                                                                "**Lad mig se…**\n" +
                                                                "*Prospektoren kan under Indsamling slå en D6, terningens værdi vil blive lagt til antallet af genstande de er i stand til at finde (Specificeres af GM)*\n \n" +
                                                                "__**Pros:**__\n" +
                                                                "+10  **Handel**\n" +
                                                                "+10  **Reparation**\n" +
                                                                "+10  **Fælder**\n \n" +
                                                                "__**Cons:**__\n" +
                                                                "Prospektoren kan ikke dele ud af sin inventar, med mindre en anden spiller slår om Smir imod dem eller bytter noget af ligende værdi (Aftales mellem Spillere og GM)", color=0x8DDF54)                
                        prospekter_embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/701156872094482563/83926999_2565824347032825_6396469320481767424_n.png?width=431&height=629")
                        await channel.send(embed=prospekter_embed)
                        await asyncio.sleep(1)

                # BONUS
                        handel_value = int(self.charactersheet[author_id]["Character Sheet"]["Handel"])
                        handel_bonus = 10
                        handel_value += handel_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Handel"] = handel_value

                        reparation_value = int(self.charactersheet[author_id]["Character Sheet"]["Reparation"])
                        reparation_bonus = 10
                        reparation_value += reparation_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Reparation"] = reparation_value

                        fælder_value = int(self.charactersheet[author_id]["Character Sheet"]["Fælder"])
                        fælder_bonus = 10
                        fælder_value += fælder_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Fælder"] = fælder_value

                        fh.save_file(self.charactersheet, 'charactersheet')                         
# SAMARIT
                if self.charactersheet[author_id]["Character Sheet"]["Chosen Character"] == "Samarit":
                        samarit_embed = discord.Embed(title=f"__**Samarit**__", description=f"*Omvandrende Samaritter plejer tit deres erhverv i krigshærgede eller lovløse områder.*\n" + 
                                                                "*Oftest er de tidligere læger fra mindre landsbyer, eller simple godhjertede sjæle der er drevet til at hjælpe deres næste.*\n \n" +
                                                                "__**Evner:**__\n" +
                                                                "**Ræk mig den kniv…**\n" +
                                                                "*Samaritten kan altid udøve Seriøs Lægehjælp så længe de er i besiddelse af almene medicinale effekter, bandager, gazebind etc. Mængden af medicinale effekter forøger chancen for succes.*\n" +
                                                                "**Hvor gør det ondt?**\n" +
                                                                "*Samaritten kan, uden brug af Lægevidenskab, altid identificere eller opdage hvis en medspiller er forgiftet og eller syg.*\n \n" +
                                                                "__**Pros:**__\n" +
                                                                "+10  **Lægevidenskab**\n" +
                                                                "+5  **Overlevelse**\n \n" +
                                                                "__**Cons:**__\n" +
                                                                "-20  **Intimidere**\n" +
                                                                "-20  **Løgn**", color=0xF8FF5C)                
                        samarit_embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/701159483333673106/83220722_629791384445351_7846450275316400128_n.png?width=459&height=629")
                        await channel.send(embed=samarit_embed)
                        await asyncio.sleep(1)  

                # BONUS
                        lægevidenskab_value = int(self.charactersheet[author_id]["Character Sheet"]["Lægevidenskab"])
                        lægevidenskab_bonus = 10
                        lægevidenskab_value += lægevidenskab_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Lægevidenskab"] = lægevidenskab_value

                        overlevelse_value = int(self.charactersheet[author_id]["Character Sheet"]["Overlevelse"])
                        overlevelse_bonus = 5
                        overlevelse_value += overlevelse_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Overlevelse"] = overlevelse_value
                # NEGATE
                        intimiderer_value = int(self.charactersheet[author_id]["Character Sheet"]["Intimiderer"])
                        intimiderer_negate = 20
                        intimiderer_value -= intimiderer_negate
                        if intimiderer_value < 0:
                                intimiderer_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Intimiderer"] = intimiderer_value

                        løgn_value = int(self.charactersheet[author_id]["Character Sheet"]["Løgn"])
                        løgn_negate = 20
                        løgn_value -= løgn_negate
                        if løgn_value < 0:
                                løgn_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Løgn"] = løgn_value

                        fh.save_file(self.charactersheet, 'charactersheet')   

                if self.charactersheet[author_id]["Character Sheet"]["Chosen Character"] == "Tekker":
                        tekker_embed = discord.Embed(title=f"__**Tekker**__", description=f"*En Tekker lever og dør af teknologien de søger.*\n" + 
                                                                "*Disse personer er tit tidligere prospektere der har indset at værdien ikke ligger i de almene materialer, men i de mange stadig fungerende stykker teknologi der kan samles og sælges for stor profit.*\n" +
                                                                "*Mange er på grund af deres mange interaktioner med Søgerne og andre technofile grupper selv blevet næsten religiøse omkring det de søger.*\n \n" +
                                                                "__**Evner:**__\n" +
                                                                "**Maskinen forblive**\n" +
                                                                "*Tekkere kan uden brug af terninger, altid identificere mere kompliceret teknologi. Ydermere kan de aldrig Katastrofalt Fejle nogle evne-check med Videnskab.*\n" +
                                                                "**Du ved intet…**\n" +
                                                                "*Tekkere vil altid have +10 i Handel under salg eller indkøb af Arkeo-Tek (Specificeres)*\n \n" +
                                                                "__**Pros:**__\n" +
                                                                "+10  **Intelligens**\n" +
                                                                "+10  **Videnskab**\n \n" +
                                                                "__**Cons:**__\n" +
                                                                "-10  **Nærkamp**\n" +
                                                                "-10  **Strenge/Kaste Våben**\n" +
                                                                "-10  **Skydevåben**\n" +
                                                                "-10  **Snig**", color=0xFFA600)                
                        tekker_embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/701162087665106974/83045972_174124687257093_8104502798202175488_n.png?width=370&height=629")
                        await channel.send(embed=tekker_embed)
                        await asyncio.sleep(1)   

                # BONUS
                        intelligens_value = int(self.charactersheet[author_id]["Character Sheet"]["Intelligens"])
                        intelligens_bonus = 10
                        intelligens_value += intelligens_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Intelligens"] = intelligens_value

                        videnskab_value = int(self.charactersheet[author_id]["Character Sheet"]["Videnskab"])
                        videnskab_bonus = 10
                        videnskab_value += videnskab_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Videnskab"] = videnskab_value
                # NEGATE
                        nærkamp_value = int(self.charactersheet[author_id]["Character Sheet"]["Nærkamp"])
                        nærkamp_negate = 10
                        nærkamp_value -= nærkamp_negate
                        if nærkamp_value < 0:
                                nærkamp_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Nærkamp"] = nærkamp_value

                        kaste_strenge_våben_value = int(self.charactersheet[author_id]["Character Sheet"]["Kaste_Strenge_våben"])
                        kaste_strenge_våben_negate = 10
                        kaste_strenge_våben_value -= kaste_strenge_våben_negate
                        if kaste_strenge_våben_value < 0:
                                kaste_strenge_våben_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Kaste_Strenge_våben"] = kaste_strenge_våben_value

                        skydevåben_value = int(self.charactersheet[author_id]["Character Sheet"]["Skydevåben"])
                        skydevåben_negate = 10
                        skydevåben_value -= skydevåben_negate
                        if skydevåben_value < 0:
                                skydevåben_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Skydevåben"] = skydevåben_value

                        snig_value = int(self.charactersheet[author_id]["Character Sheet"]["Snig"])
                        snig_negate = 10
                        snig_value -= snig_negate
                        if snig_value < 0:
                                snig_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Snig"] = snig_value  

                        fh.save_file(self.charactersheet, 'charactersheet')  

                if self.charactersheet[author_id]["Character Sheet"]["Chosen Character"] == "Vandrer":
                        vandrer_embed = discord.Embed(title=f"__**Vandrer**__", description=f"*Utallige Vandrere søger et bedre liv når deres gamle er gået dem til halsen, eller er blevet dem berøvet.*\n" + 
                                                                "*Disse retningsløse sjæle søger altid over den næste horisont hvor græsset forhåbentligt er grønnere og vandet… mindre grønt.*\n \n" +
                                                                "__**Evner:**__\n" +
                                                                "**Nu mørkere en nat, nu lysere stjerner**\n" +
                                                                "*Vandreren får ingen hæmninger under evne-check i mørke.*\n" +
                                                                "**Jeg har set det meste**\n" +
                                                                "*Vandreren får +5 på alle Frygt check*\n \n" +
                                                                "__**Pros:**__\n" +
                                                                "+5  **Snig**\n" +
                                                                "+5  **Overlevelse**\n" +
                                                                "+5  **Finesse**\n" +
                                                                "+5  **Perception**\n \n" +
                                                                "__**Cons:**__\n" +
                                                                "-10  **Smigre**\n" +
                                                                "-10  **Løgn**\n" +
                                                                "-10  **Intimidere**\n" +
                                                                "-10  **Handel**", color=0x979797)                
                        vandrer_embed.set_image(url="https://media.discordapp.net/attachments/698522831083929734/701165046566354964/83400007_2515410042066042_1883996204778389504_n.png?width=484&height=629")
                        await channel.send(embed=vandrer_embed)
                        await asyncio.sleep(1) 

                # BONUS
                        snig_value = int(self.charactersheet[author_id]["Character Sheet"]["Snig"])
                        snig_bonus = 5
                        snig_value += snig_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Snig"] = snig_value   

                        overlevelse_value = int(self.charactersheet[author_id]["Character Sheet"]["Overlevelse"])
                        overlevelse_bonus = 5
                        overlevelse_value += overlevelse_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Overlevelse"] = overlevelse_value  

                        finesse_value = int(self.charactersheet[author_id]["Character Sheet"]["Finesse"])
                        finesse_bonus = 5
                        finesse_value += finesse_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Finesse"] = finesse_value 

                        perception_value = int(self.charactersheet[author_id]["Character Sheet"]["Perception"])
                        perception_bonus = 5
                        perception_value += perception_bonus
                        self.charactersheet[author_id]["Character Sheet"]["Perception"] = perception_value 
                # NEGATE
                        smigre_value = int(self.charactersheet[author_id]["Character Sheet"]["Smigre"])
                        smigre_negate = 10
                        smigre_value -= smigre_negate
                        if smigre_value < 0:
                                smigre_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Smigre"] = smigre_value

                        løgn_value = int(self.charactersheet[author_id]["Character Sheet"]["Løgn"])
                        løgn_negate = 10
                        løgn_value -= løgn_negate
                        if løgn_value < 0:
                                løgn_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Løgn"] = løgn_value

                        intimiderer_value = int(self.charactersheet[author_id]["Character Sheet"]["Intimiderer"])
                        intimiderer_negate = 10
                        intimiderer_value -= intimiderer_negate
                        if intimiderer_value < 0:
                                intimiderer_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Intimiderer"] = intimiderer_value

                        handel_value = int(self.charactersheet[author_id]["Character Sheet"]["Handel"])
                        handel_negate = 10
                        handel_value -= handel_negate
                        if handel_value < 0:
                                handel_value = 0
                        self.charactersheet[author_id]["Character Sheet"]["Handel"] = handel_value

                        fh.save_file(self.charactersheet, 'charactersheet')  

                self.load_data()


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
                cs_msg = await channel.send(embed=cs_embed)
                cs_msg_id = cs_msg.id
                await asyncio.sleep(1)
                await cs_msg.add_reaction(emoji='\U0001F514')     # Add bell reaction to message

                self.charactersheet[author_id]["Character Sheet Embed ID"] = cs_msg_id

                fh.save_file(self.charactersheet, 'charactersheet') 


# X Beskytter
# X Charlatan
# X Indfødt
# X Jæger
# X Landevejsrøver
# X Lejesoldat
# X Mutant
# X Prospekter
# X Samarit
# X Tekker
# X Vandrer
                                #     stock_embed.add_field(name="Stats", value=f"{self.worlditems[worldid]['Stats']}", inline=False)
                                #     stock_embed.add_field(name="Type", value=f"{self.worlditems[worldid]['Type']}", inline=True)

def setup(bot):
    bot.add_cog(CharacterSheet(bot))

