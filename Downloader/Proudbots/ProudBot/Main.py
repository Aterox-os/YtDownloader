import discord
import random
from discord.ext import commands
from discord.utils import get
import os
import youtube_dl

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Login succesful")

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'unbanned {user.mention}')
            return

client.run("NzAxODkwNTc4NzA2NzI2OTkz.Xp8Obg.UIN-1BsUd4B1RLfbVycVkzCiehQ")
