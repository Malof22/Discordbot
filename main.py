import time
import discord
import aiohttp
import io
import re
import os
import random
from urllib.request import Request,urlopen
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="boolmi.", description="test", intents=intents)



@bot.event
async def on_ready():
    activity = discord.Game(name="se faire des amis ^^", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("ready")


@bot.command(name="demotivator")
async def demotivator(ctx):
    os.remove('fichier.txt')

    with open('fichier.txt', 'w') as f:
        with open('fichier_image.txt', 'w') as f2:
            async for item in ctx.history(limit = 150000):
                if not re.search("^g\..", item.content):
                    if not re.search("^boolmi\..", item.content):
                        if item.author.name != 'Mibot^^' and item.author.name != 'GenAi' and item.author.name != 'Deleted User':
                            try:
                                if not re.search("^\s.", item.content):
                                    if item.content:
                                        f.write(f'{item.content}\n')
                            except:
                                print("erreur 1")
                            if item.attachments != []:
                                try:
                                    f2.write(f'{item.attachments[0]}\n')
                                except:
                                    print("erreur 2")

    await ctx.send("Je prends mon temps bouge pas")

    list = []
    with open("fichier_image.txt", "r") as filin:
        for ligne in filin:
            list.append(ligne[:-1])
    print(list)

    url = random.choice(list)

    req = Request(
        url=url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )


    img = Image.open(urlopen(req))
    img = img.resize((1280,720))

    font = ImageFont.truetype("Font.ttf", 80)
    other_font = ImageFont.truetype("Font.ttf", 50)
    dmtvtr = Image.new('RGB', (1920, 1080), color='black')

    draw = ImageDraw.Draw(dmtvtr)

    draw.rectangle(((315,90),(1615,830)),outline = 'white')

    dmtvtr.paste(img,(325,100))

    list2 = []
    with open("fichier.txt", "r") as filn:
        for ligne2 in filn:
            list2.append(ligne2[:-1])

    text1 = random.choice(list2)
    text2 = random.choice(list2)

    _, _, w, h = draw.textbbox((0, 0), text1, font=font)
    draw.text(((dmtvtr.width - w) / 2, 850), text1, font=font)

    _, _, w, h = draw.textbbox((0, 0), text2, font=other_font)
    draw.text(((dmtvtr.width - w) / 2, 950), text2, font=other_font)

    dmtvtr.save('demotivator.png')

    async with aiohttp.ClientSession() as session:  # creates session
        async with session.get(url) as resp:  # gets image from url
            img = await resp.read()  # reads image from response
            with io.BytesIO(img) as file:  # converts to file-like object
                await ctx.send(file=discord.File("demotivator.png") )


@bot.command(name="zizi")
async def zizi(ctx):
    taillezizi = random.randint(0,100)

    await ctx.send("Je mesure ton zizi...")
    time.sleep(5)
    phrase = "il mesure " + str(taillezizi) + "cm, pas mal !! ^^"
    await ctx.send(phrase)
    time.sleep(5)
    formezizi = "Il ressemble à ça : 8"
    for i in range(taillezizi):
        formezizi += '='
    await ctx.send(formezizi)

@bot.command(name="insulte")
async def insulte(ctx):
    liste_insulte = ["Putain","Pute","Fils de pute","Pétasse","Catin","Morue","Con","Conne","Connard","Connasse",
    "Enculé","Pédé", "PD","Pédale","Tapette","Tantouze","Fiotte","Tafiole","Tarlouze","Sac à foutre", "Petite bite","Couille molle",
    "Salope","Salopard","Saloperie","Chienne","Bitch","Biatch","Cagole","Shemale","Travelo","Gouine","Chintoque","Bouffeur de chiens",
    "Bougnoul","Mongol","Mongolien","Débile","Abruti","Imbécile","Idiot","Autiste","Trisomique","Triso","Attardé","Taré",
    "Crétin","Benêt","Nigaud","Fou","Folle","Fol","Pochtron","Ivrogne","Clochard","Clodo","Pisseuse","Morveux","Merdeux"
    ,"Bouffon","Bordille","Buse","Chauffard","Crevure","Enfoiré","Enflure","Étron" ,"Flaque de parvo","Fripouille",
    "Fumier","Mange-merde","Merde","Naze","Pourriture","Punaise","Raclure","Sagouin","Salaud","Saleté","Tache",
    "Tas de purin","Vaurien","Pignouf","Trou du cul"]

    insult = random.choice(liste_insulte)
    if re.search("^[AEIOUYÉ]", insult):
        phrase = "Espèce d'" + insult + "!"
    else:
        phrase = "Espèce de " + insult + "!"
    await ctx.send(phrase)

@bot.command(name="casino")
async def casino(ctx):
    await ctx.send("Bienvenue au Casino !")
    time.sleep(1)
    await ctx.send("Vous pouvez jouer à la roulette ! (boolmi.roulette)")
    time.sleep(1)
    await ctx.send("Vous pouvez jouer au pile ou face ! (boolmi.pileface)")
    time.sleep(1)
    await ctx.send("Voici votre argent de départ : 1000 bonins !")
    time.sleep(1)
    await ctx.send("Je vous souhaite bonne chance !")
    file = open("casino.txt", "r")
    for ligne in file:
        if ligne.startswith(ctx.author.name):
            await ctx.send("Vous avez déjà un compte !")
            file.close()
            return
    file.close()
    file = open("casino.txt", "r")
    data = []
    for ligne in file:
        data.append(ligne)
    file.close()
    file = open("casino.txt", "w")
    for ligne in data:
        print(ligne)
        file.write(ligne)
    file.write(str(ctx.author.name) + " : 1000\n")
    file.close()

@bot.command(name="roulette")
async def roulette(ctx):
    content = ctx.message.content[16:]
    if content == "":
        await ctx.send("Vous n'avez pas misé !")
        return
    content = content.split(" ")
    if len(content) != 2:
        await ctx.send("Vous n'avez pas misé correctement !")
        return
    file = open("casino.txt", "r")
    for ligne in file:
        if ligne.startswith(ctx.author.name):
            argent = ligne.split(" : ")[1]
            argent = int(argent[:-1])
            if argent < int(content[0]):
                await ctx.send("Vous n'avez pas assez d'argent !")
                file.close()
                return
            argent -= int(content[0])
            argent = str(argent) + "\n"
            file.close()
            file = open("casino.txt", "r")
            data = []
            for ligne in file:
                data.append(ligne)
            file.close()
            file = open("casino.txt", "w")
            for ligne in data:
                if ligne.startswith(ctx.author.name):
                    file.write(ctx.author.name + " : " + argent)
                else:
                    file.write(ligne)
            file.close()
            await ctx.send("Vous avez misé " + content[0] + " bonins sur le " + content[1] + " !")
            await ctx.send("La roulette tourne...")
            time.sleep(3)
            result = random.randint(0,36)
            await ctx.send("Et s'arrête sur le " + str(result) + " !")
            if content[1] == "pair":
                if result% 2 == 0:
                    await ctx.send("Vous avez gagné !")
                    argent = int(argent[:-1])
                    argent += int(content[0]) * 2
                    argent = str(argent) + "\n"
                else:
                    await ctx.send("Vous avez perdu !")
            elif content[1] == "impair":
                if result % 2 == 1:
                    await ctx.send("Vous avez gagné !")
                    argent = int(argent[:-1])
                    argent += int(content[0]) * 2
                    argent = str(argent) + "\n"
                else:
                    await ctx.send("Vous avez perdu !")
            elif content[1] == "rouge":
                if result in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
                    await ctx.send("Vous avez gagné !")
                    argent = int(argent[:-1])
                    argent += int(content[0]) * 2
                    argent = str(argent) + "\n"
                else:
                    await ctx.send("Vous avez perdu !")
            elif content[1] == "noir":
                if result in [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]:
                    await ctx.send("Vous avez gagné !")
                    argent = int(argent[:-1])
                    argent += int(content[0]) * 2
                    argent = str(argent) + "\n"
                else:
                    await ctx.send("Vous avez perdu !")
            elif content[1]==result:
                await ctx.send("Vous avez gagné !")
                argent = int(argent[:-1])
                argent += int(content[0]) * 36
                argent = str(argent) + "\n"
            else:
                await ctx.send("Vous avez perdu !")
            file = open("casino.txt", "r")
            data = []
            for ligne in file:
                data.append(ligne)
            file.close()
            file = open("casino.txt", "w")
            for ligne in data:
                if ligne.startswith(ctx.author.name):
                    file.write(ctx.author.name + " : " + argent)
                else:
                    file.write(ligne)
            file.close()
            return

@bot.command(name="argent")
async def argent(ctx):
    file = open("casino.txt", "r")
    for ligne in file:
        if ligne.startswith(ctx.author.name):
            argent = ligne.split(" : ")[1]
            argent = int(argent[:-1])
            await ctx.send("Vous avez " + str(argent) + " bonins !")
            file.close()
            return
    await ctx.send("Vous n'avez pas de compte !")
    file.close()

@bot.command(name="motherlode")
async def motherlode(ctx):
    file = open("casino.txt", "r")
    for ligne in file:
        if ligne.startswith(ctx.author.name):
            argent = ligne.split(" : ")[1]
            argent = int(argent[:-1])
            argent += 1000000
            argent = str(argent) + "\n"
            file.close()
            file = open("casino.txt", "r")
            data = []
            for ligne in file:
                data.append(ligne)
            file.close()
            file = open("casino.txt", "w")
            for ligne in data:
                if ligne.startswith(ctx.author.name):
                    file.write(ctx.author.name + " : " + argent)
                else:
                    file.write(ligne)
            file.close()
            await ctx.send("Vous avez reçu 1 million de bonins !")
            return
    await ctx.send("Vous n'avez pas de compte !")
    file.close()

@bot.command(name="pileface")
async def pileface(ctx):
    content = ctx.message.content[16:]
    if content == "":
        await ctx.send("Vous n'avez pas misé !")
        return
    content = content.split(" ")
    if len(content) != 2:
        await ctx.send("Vous n'avez pas misé correctement !")
        return
    file = open("casino.txt", "r")
    for ligne in file:
        if ligne.startswith(ctx.author.name):
            argent = ligne.split(" : ")[1]
            argent = int(argent[:-1])
            if argent < int(content[0]):
                await ctx.send("Vous n'avez pas assez d'argent !")
                file.close()
                return
            argent -= int(content[0])
            argent = str(argent) + "\n"
            file.close()
            file = open("casino.txt", "r")
            data = []
            for ligne in file:
                data.append(ligne)
            file.close()
            file = open("casino.txt", "w")
            for ligne in data:
                if ligne.startswith(ctx.author.name):
                    file.write(ctx.author.name + " : " + argent)
                else:
                    file.write(ligne)
            file.close()
            await ctx.send("Vous avez misé " + content[0] + " bonins sur " + content[1] + " !")
            await ctx.send("La pièce tourne...")
            time.sleep(3)
            result = random.randint(0,1)
            if result == 0:
                await ctx.send("Et s'arrête sur pile !")
            else:
                await ctx.send("Et s'arrête sur face !")
            if content[1] == "pile":
                if result == 0:
                    await ctx.send("Vous avez gagné !")
                    argent = int(argent[:-1])
                    argent += int(content[0]) * 2
                    argent = str(argent) + "\n"
                else:
                    await ctx.send("Vous avez perdu !")
            elif content[1] == "face":
                if result == 1:
                    await ctx.send("Vous avez gagné !")
                    argent = int(argent[:-1])
                    argent += int(content[0]) * 2
                    argent = str(argent) + "\n"
                else:
                    await ctx.send("Vous avez perdu !")
            else:
                await ctx.send("Vous avez perdu !")
            file = open("casino.txt", "r")
            data = []
            for ligne in file:
                data.append(ligne)
            file.close()
            file = open("casino.txt", "w")
            for ligne in data:
                if ligne.startswith(ctx.author.name):
                    file.write(ctx.author.name + " : " + argent)
                else:
                    file.write(ligne)
            file.close()
            return

bot.run("MTA5MzIwNDM4MzI5MTkzMjc4NA.GFZTL1.Kv_Qn0HuJDCgrzjnbuxnS1y9kCQYCqozaJ_1Hk")

