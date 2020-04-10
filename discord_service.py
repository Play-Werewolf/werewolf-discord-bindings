import discord
from discord.ext import commands
import secrets
import random
from messages import *
from cmd_parser import *

bot = commands.Bot(command_prefix = '!', description = help_msg)

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.event
async def on_member_join(member):
    print(f'{member} has joined the town.')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left the town.')

@bot.command(aliases=['p'])
async def ping(ctx):
    await ctx.send(f'Pong, {int(bot.latency * 1000)}ms')

@bot.command()
async def pong(ctx):
    await ctx.send(f'Ping, {int(bot.latency * 1000)}ms')

@bot.command(aliases=['8ball'])
async def _8ball(ctx, question):
    await ctx.send(f'q: {question}\na: {random.choice(responses)}')


#@bot.command
#async def clear(ctx, amount):
#    await ctx.channel.purge(limit=amount)

@bot.event
async def on_disconnect(ctx):
    ctx.channel.send("goodbye, it was nice to play with you all")

@bot.command(aliases=['w'])
async def werewolf(ctx, args):
    command, *params = args.split()
    Parser(bot, ctx, command, params)
    

bot.run(secrets.discord_bot_key)