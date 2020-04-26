import discord
from discord.ext import commands

TOKEN = "NzAyNTE2MzY5NTI2MjI2OTU1.XqBLfQ.Y09NvKCw-u1mdKKCLPfZ-p8z8Og"
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Bot Online")

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.creat_ytdl_player(url)
    players[server.id] = player
    player.start()

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].resume()

@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()

@client.command(pass_context=True)
async def queue(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    players = await voice_client.creat_ytdl_player(url)

    if server.id in queues:
        queues[server.id].append(player)
    else:
        queues[server.id] = [player]
    await client.say("Video queued.")

client.run("NzAyNTE2MzY5NTI2MjI2OTU1.XqBLfQ.Y09NvKCw-u1mdKKCLPfZ-p8z8Og")
