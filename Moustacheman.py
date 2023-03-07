import discord
from discord import Intents
from discord.ext import tasks, commands
intents = discord.Intents.all()
client = commands.Bot(command_prefix="mo!", description="Moustacheman / créé par Agahnim", intents = intents)

@client.event
async def on_ready():
    print('Connecté !')
    await client.change_presence(activity=discord.Game('moustacher'))
       

#Quand un utilisateur envoie un message
@client.event
async def on_message(message) :
    if message.content.lower()[:3] == "mo!":
        return
    l_tg = ["tg"," tg", "tg "]
    if message.content.lower().strip() in l_tg or message.content.lower() == "tg" or "ta gueule" in message.content.lower() :
        if message.author == client.user :
            return
        else :
            msg = await message.channel.send("Malappri + ratio")
            emojis = ["🔁", "❤️"]
            for emoji in emojis :
                    await msg.add_reaction(emoji)
    else :
        if "ratio" in message.content.lower() :
            if message.author == client.user : 
                return 
            else :
                msg = await message.channel.send("Ratio toi même")
                emojis = ["🔁", "❤️"]
                for emoji in emojis :
                    await msg.add_reaction(emoji)
        else :
            if "genshin" in message.content.lower() :
                if message.author == client.user :
                    return
                else :
                    await message.channel.send("https://tenor.com/bSwNK.gif")
                    await message.channel.send("https://tenor.com/Uoxl.gif")
            else :
                if "carti" in message.content.lower() :
                    if message.author == client.user :
                        return
                    else :
                        await message.channel.send("https://tenor.com/view/carti-gif-23132052")
    await client.process_commands(message)

client.run('OTg3MDY4ODM3MTcyMjE1ODA4.GzU95h.qBcdldFX2vCCEmgapyd_mQ6q3vTFB3BsfZhGSk')








#if message.author.id == 361456145845714944 and "https://cdn.discordapp.com/attachments" in message.content.lower() :
#    await message.delete()
#if message.author.id == 361456145845714944 and "!p" in message.content.lower() or "m!p" in message.content.lower() or "m!play" in message.content.lower() or "!play" in message.content.lower() :
#    await message.guild.ban(412347553141751808, delete_message_days = 0)
#mauvais goûts musicaux = ban
