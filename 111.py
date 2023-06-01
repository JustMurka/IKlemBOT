import asyncio
import os
import random
import discord
from discord.ext import commands
import sys
sys.path.append('../../')
import config
import pickle
from discord.ext.commands.cooldowns import BucketType
discord_intents = discord.Intents.all()
discord_intents.members = True

config = {
    'token': 'MTExMDgxMjAwODcwMzYxMDk0MQ.Gs9CP2.zmnFZpQswUuwBtKZbOMip1G0BFa6s8F68vuKC4',
    'prefix': '!IKlem ',
}

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("IKlemBOT"))
@bot.command()
async def rand(ctx, *arg):
    await ctx.reply(random.randint(1, 100))
@bot.command()
async def ping(ctx, *arg):
    await ctx.send(f'{ctx.author.mention} Если вы видете это сообщение значит всё в порядке 👍')
@bot.command()
async def say(ctx: commands.Context, *, сказать: str):
    embed = discord.Embed(description=сказать)
    embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar.url)
    await ctx.reply(embed=embed)
@bot.command()
async def test(ctx, *arg):
    await ctx.reply((f'{ctx.author.mention}'))
bot.run('1MTExMDgxMjAwODcwMzYxMDk0MQ.GZ8Y2P.QTSaS3xJpsulZ3Tc2lRZtSJ0h8gQGG0ydBuojo')
