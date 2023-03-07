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

client.run('your token')
