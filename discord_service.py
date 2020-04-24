import discord
from discord.ext import commands
import secrets
import random
from messages import *
from cmd_parser import *
import json

PREFIXES_FILE_PATH = 'prefixes.json'


def get_prefixes():
    with open(PREFIXES_FILE_PATH, 'r') as prefixes_file:
        return json.load(prefixes_file)

def set_prefixes(prefixes):
    with open(PREFIXES_FILE_PATH, 'w') as prefixes_file:
        json.dump(prefixes, prefixes_file, indent =4)


def get_prefix(client, message):
    prefixes = get_prefixes()

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix = get_prefix, description = help_msg)

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.event
async def on_member_join(member):
    print(f'{member} has joined the town.')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left the town.')

@bot.event
async def on_guild_join(guild):
    prefixes = get_prefixes()
    prefixes[str(guild.id)] = '!'
    set_prefixes(prefixes)


@bot.event
async def on_guild_remove(guild):
    prefixes = get_prefixes()
    prefixes.pop(str(guild.id))
    set_prefixes(prefixes)


@bot.command(aliases=['cp'])
async def change_prefix(ctx, *, prefix):
    prefixes = get_prefixes()
    prefixes[str(ctx.guild.id)] = prefix
    set_prefixes(prefixes)


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
    print(command, params)
    Parser(bot, ctx, command, params)
    

bot.run(secrets.discord_bot_key)