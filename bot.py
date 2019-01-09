import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import youtube_dl
from discord.voice_client import VoiceClient
bot_prefix= "!"
client = commands.Bot(command_prefix=bot_prefix)
Client = discord.Client()
vc_clients = {}

players = {}
queues = {}

def check_queue(id):
    if queues[id] != []:
        players = queues[id].pop(0)
        players[id] = players
        players.start()


Client = discord.Client() 
client = commands.Bot(command_prefix = "!")

@client.command(pass_context=True)
async def meghivó(ctx):
          await client.say("https://discordapp.com/api/oauth2/authorize?client_id=529367467068489770&permissions=8&scope=bot")

@client.event
async def on_ready():
    print("Ez a bot készen áll a használatra")
    print("A bot jelenlegi verziója: beta1")
    print("Nev: " + client.user.name)
    print ("ID: " + client.user.id)
    counter = 0
    while not counter > 0:
        await client.change_presence(game=discord.Game(name='Parancsokért: !parancsok', type=3))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='A bot jelenlegi verziója: beta1', type=3))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='Support server: Marcell125 server.', type=3))
        await asyncio.sleep(5) 
        await client.change_presence(game=discord.Game(name='Meghívóért: !meghívó ', type=3))
        await asyncio.sleep(5)
		
@client.command(pass_context=True)
async def belépés(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    await client.say("Beléptem a hangcsatornába, indíthatjátok a zenéket!")



@client.command(pass_context=True)
async def kilépés(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()
    await client.say("Elhagytam a hangcsatornát, remélem tetszettek a zenék!")


@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
    players[server.id] = player
    await client.say("A zene azonnal indul!")
    player.start()
    


@client.command(pass_context=True)
async def szünet(ctx):
    id = ctx.message.server.id
    players[id].pause()
    await client.say("A zenét megállítottam!")


@client.command(pass_context=True)
async def leállítás(ctx):
    id = ctx.message.server.id
    players[id].stop()
    await client.say("A zenét leállítottam!")



@client.command(pass_context=True)
async def folytatás(ctx):
    id = ctx.message.server.id
    players[id].resume()
    await client.say("A zene folytatódik!")


@client.command(pass_context=True)
async def skip(ctx):
    try:
        id = ctx.message.server.id
        players[id].stop()
    except:
        return False




client.run("TOKEN")
