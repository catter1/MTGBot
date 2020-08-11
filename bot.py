import discord
import os
import random
from discord.ext import commands, tasks
from itertools import cycle
from datetime import datetime

client = commands.Bot(command_prefix = '.')

version = '1.0.0'
dateedited = 'August 12, 2020, 4:20pm EDT'

@client.event
async def on_ready():
    print('The MTG Bot has been booted up!')

@client.command()
async def dev(ctx):
    await ctx.send('Bot:/tMTG Bot')
    await ctx.send('Developer:/tcatter1')
    await ctx.send('Version:/t', version)
    await ctx.send('/tDate Released:/t', dateedited)

@client.command()
async def instrument(ctx, instr):
    oboe = {
        'name' : 'Oboe',
        'family' : 'woodwind',
        'subfam' : 'double reed'
    }
    flute = {
        'name' : 'Flute',
        'family' : 'woodwind',
        'subfam' : 'double reed'
    }
    bassoon = {
        'name' : 'Flute',
        'family' : 'woodwind',
        'subfam' : 'double reed'
    }
    piccolo = {
        'name' : 'Piccolo',
        'family' : 'woodwind',
        'subfam' : 'double reed'
    }
    coranglais = {
        'name' : 'English Horn',
        'aka' : 'Cor Anglais',
        'family' : 'woodwind',
        'subfam' : 'double reed'
    }
    if instr == oboe:
        await ctx.send(oboe)
    elif instr == flute:
        await ctx.send(flute)
    elif instr == bassoon:
        await ctx.send(bassoon)
    elif instr == piccolo:
        await ctx.send(piccolo)
    elif instr == coranglais:
        await ctx.send(coranglais)

client.run('token here')