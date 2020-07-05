import discord
import asyncio
from discord.ext import commands

class WelcomeMsg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


# New character command
    @commands.command()
    async def welcomemsg(self, message):
        if message.channel.id == 700719183184527380: # Channel id of "welcome"
            channel = self.bot.get_channel(700719183184527380)  # Channel id of "welcome"
            await channel.purge(limit=50)


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

# HISTORY
            history_embed = discord.Embed(title="Vandvejen", description=f"*I Sønderlandet, en af de få uafhængige stater tilbage på Gaia, ligger handels-metropolitten: Vandvejen*", color=0x303136)
            history_embed.add_field(name="\u200b", value="*For mange år siden var byen et mekka for handel og gennemrejse, da den lå på den eneste sikre route mellem det østlige og vestlige central-Gaia, denne var også kendt som “Himmelvejen.” Med en befolkning på mange tusinde er Vandvejen den største og til en vis grad eneste by i den ellers uciviliserede Sønderlandske vildmark. Byens rigdom og omtale kommer som et resultat af dens livsfarlige omgivelser og den sikre passage den tilbyder.*", inline=False)
            history_embed.add_field(name="\u200b", value="*Mod nord ligger det gigantiske og ildevarslende “Kadaver,” en monolitisk ruin efterladt af “Forfædrene” som oprindeligt koloniserede Gaia efter de forlod Jorden for mange hundrede år siden. Ingen rejser igennem Kadaveret, da den destruktive kraft der næsten udslettede menneskeligheden på Gaia, siges at stamme derfra.*", inline=False)
            history_embed.add_field(name="\u200b", value="*Vælger man at rejse uden brug af Himmelvejen, men stadig ønsker at komme udenom Kadaveret, skal man enten sejle over Det Lille Hav mod syd, hvis farvand er domineret af pirater, eller forsøge sig med at navigere igennem “Troldelandet.” Denne gigantiske blanding af urskov, vildmark og ruiner udgør næsten 80 procent af Sønderlandets totale areal, og strækker fra grænse til grænse, med undtagelse af Kadaveret, hvis ruiner dominere de nordlige områder.*", inline=False)            
            history_embed.add_field(name="\u200b", value="*Det farlige og utilgængelige terræn omkring den har gjort Vandvejen til Sønderlandets ypperste knudepunkt, men dette har også resulteret i at mange stormagter fra andre dele af Gaia har fået interesse i at komme i besiddelse af byen, på den ene eller anden måde. To rivaliserende stormagter, det Edsvorne Kejserrige fra de vestlige Hjerte Stater og Centralmagterne fra østen.*", inline=False)
            history_embed.add_field(name="\u200b", value="*Disse to fraktioner har indenfor de sidste få år udkæmpet en blodig krig på tværs af Sønderlandet, men har med vilje holdt Vandvejen ude af deres konflikt. I stedet har begge magter fået sig presset ind i Vandvejen med diplomatiske mener og bruger deres indflydelse i håbet om at få Vandvejens regerende elite til at tage deres parti. Denne kolde trekants-krig har destabiliseret livet i Vandvejen og resten af Sønderlandet til sådan en grad at det har fået tilstedeværelsen i Vandvejen til næsten at kollapse.*", inline=False)
            history_embed.add_field(name="\u200b", value="*Flygtningestrømme fra de krigshærgede områder af Sønderlandet har presset utallige nye indbyggere ind i Vandvejen og har medført skabelsen af nyere slum og ghettoer både inde og udenfor byens murer. Visse dele af byen er enten faldet under kontrol af enten Centralmagterne eller Kejserriget, eller er blevet drevet i fordærv, overtaget af anarki og lovløshed. De områder af byen der forbliver stabile er få og eliten har ud af desperation gemt sig i den inderste del af byen, hvorom de har bygget en sekundær mur. Det Frie Folk, som de resterende indbyggere kalder sig selv kæmper en brav men hård kamp for at vedligeholde deres levevilkår og frihed.*", inline=False)
            history_embed.add_field(name="\u200b", value="*I er om bord på en af de mange karavane tog der ankommer til Pilgrim Pladsen, det sidste sted for mange håbløse flygtninge forsøger at starte et liv i Vandvejen og hvorfra endnu flere bliver fordrevet af de nuværende indbyggere som jager dem ind de lovløse områder. Til jeres held bliver i stoppet på vej ud af jeres vogn af en tykpandet tyrenakke af en mand som rækker jeg hver især en notits...*", inline=False)
            history_embed.add_field(name="\u200b", value="*Velkommen til Gaia og velkommen til Vandvejen.*\n \n \nÆndrer dit nickname til det din character hedder og skriv **.newcharacter** i chatten for at komme igang!", inline=False)
            history_embed.set_image(url="https://media.discordapp.net/attachments/533766932491534348/701213948661334016/vandvejen2.png")
            await channel.send(embed=history_embed)
                        

# history_embed.add_field(name="\u200b", value="**", inline=False)

def setup(bot):
    bot.add_cog(WelcomeMsg(bot))

