import nextcord
from nextcord.ext import commands, tasks
import json
import asyncio
import os


import random
import string

file = open('config.json', 'r')
config = json.load(file)

prefix = config["prefix"]
token = os.environ["token"]
intents = nextcord.Intents.all()

bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
  print('> Bot is ready;')
  status.start()


@tasks.loop(seconds=5)
async def status():
  await bot.change_presence(
    status=nextcord.Status.idle,
    activity=nextcord.Game("nagiz qazaqtyn oleni shshs"))

  await asyncio.sleep(5)

  await bot.change_presence(status=nextcord.Status.idle,
                            activity=nextcord.Game("tpts.netlify.app"))

  await asyncio.sleep(5)


@bot.command(name="ping")
async def ping_cmd(ctx):
  embed = nextcord.Embed(
    description=f"My ping is `{round(bot.latency * 1000)}ms`",
    color=nextcord.Color.from_rgb(47, 47, 47))
  await ctx.reply(embed=embed)


@bot.command(name="send")
async def send_cmd(ctx, member: nextcord.User, *, message):
  if ctx.author.id == 1060182408797896763:
    await member.send(f"{message}")
    await ctx.reply('Command executed!')
  else:
    return



bot.run(token)
