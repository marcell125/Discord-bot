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


#chat_filter  = ("CHAT", "CHAT1")
#bypass_list = ()

#@client.event
#async def on_message(message) :
    #await client.process_commands(message)
    #contents = message.content.split(" ")
    #for word in contents:
        #if word.upper() in chat_filter:
            #if not message.author.id in bypass_list:
                #try:
                    #await client.delete_message(message)
                    #await client.send_message(message.channel, " :eyes: **HÉKÁS** Te nem beszélhetsz így, mivel az nem szép dolog! Ha nem hagyod abba a csúnya szavak használatát, mute-ot is kaphatsz! :angry:")
                #except discord.errors.NotFound:
                    #return



Client = discord.Client() 
client = commands.Bot(command_prefix = "!")

@client.command(pass_context=True)
async def meghivó(ctx):
          await client.say("https://discordapp.com/api/oauth2/authorize?client_id=529367467068489770&permissions=8&scope=bot")

@client.event
async def on_ready():
    print("Ez a bot készen áll a használatra")
    print("A bot jelenlegi verziója: v1")
    print("Nev: " + client.user.name)
    print ("ID: " + client.user.id)
    counter = 0
    while not counter > 0:
        await client.change_presence(game=discord.Game(name='Parancsokért: !help', type=3))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='A bot jelenlegi verziója: v1', type=3))
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
    try:
        server = ctx.message.server
        voice_client = client.voice_client_in(server)
        player = await voice_client.create_ytdl_player("ytsearch: {}".format(url), before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5")
        players[server.id] = player
        await client.say("A zene azonnal indul!")
        player.start()
    except discord.errors.ConnectionClosed:
        return    



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
		
@client.command(pass_context=True)
async def playlist(ctx, aliases=['p', 'start']):
    await client.say("Kérlek várj, indítom az első zenét! :musical_note: ")
    await client.say("A jelenlegi zene: [SFM FNAF] STAY CALM - FNaF Song by Griffinilla (2018 REMAKE)")
    try:
        server = ctx.message.server
        url = "https://www.youtube.com/watch?v=fUSJxnRzTQY"
        voice_client = client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        players[server.id] = player
        player.start()
        await client.say("Szép napot kívánok {}!".format(ctx.message.author.mention))
    except:
        await client.say("Hiba történt! Kérlek próbáld meg a *modkilépés* parancsot, majd a *modbelépés* parancsot! :x:")
        playlist.cancel()
    while not player.is_done():
        await asyncio.sleep(1)
    await client.say("Kérlek várj, indítom a következő zenét! :musical_note: ")
    await client.say("A jelenlegi zene: The Chainsmokers - Don't Let Me Down - Launchpad Cover")
    try:
        server = ctx.message.server
        url = "https://www.youtube.com/watch?v=_xK1Rb4xUPE"
        voice_client = client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        players[server.id] = player
        player.start()
        await client.say("Azonnal indul! :thumbsup:")
    except:
        await client.say("Hiba történt! Kérlek próbáld meg a *modkilépés* parancsot, majd a *modbelépés* parancsot! :x:")
        playlist.cancel()
    while not player.is_done():
        await asyncio.sleep(1)
    await client.say("Kérlek várj, indítom a következő zenét! :musical_note: ")
    await client.say("A jelenlegi zene: SZABYEST - SZERELEM KELL – HIVATALOS VIDEOKLIP – 2016")
    try:
        server = ctx.message.server
        url = "https://www.youtube.com/watch?v=ntGx-pHNL2Y"
        voice_client = client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        players[server.id] = player
        player.start()
        await client.say("Azonnal indul! :thumbsup:")
    except:
        await client.say("Hiba történt! Kérlek próbáld meg a *modkilépés* parancsot, majd a *modbelépés* parancsot! :x:")
        playlist.cancel()
    while not player.is_done():
        await asyncio.sleep(1) 
    await client.say("Kérlek várj, indítom a következő zenét! :musical_note: ")
    await client.say("A jelenlegi zene: MISSH feat. RAUL & HORVÁTH TAMÁS - BELÉD ESTEM (Official Music Video)")
    try:
        server = ctx.message.server
        url = "https://www.youtube.com/watch?v=520LNy1n5XU"
        voice_client = client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        players[server.id] = player
        player.start()
        await client.say("Azonnal indul! :thumbsup:")
    except:
        await client.say("Hiba történt! Kérlek próbáld meg a *modkilépés* parancsot, majd a *modbelépés* parancsot! :x:")
        playlist.cancel()
    while not player.is_done():
        await asyncio.sleep(1)                  
    await client.say("Ennek vége köszi hogy meghalgatál remélem tetszetek a zenék")


client.run(os.environ.get('TOKEN'))
