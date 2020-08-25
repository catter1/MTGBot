import discord
import os
import random
from discord.ext import commands, tasks
from itertools import cycle
from datetime import datetime

client = commands.Bot(command_prefix = '.')
token = open("token.txt","r").readline()
client.remove_command('help')

version = 'RELEASE 1.0.0'
dateedited = 'August 25, 2020, 11:38am EDT'

@client.event
async def on_ready():
    print('The Professor has been booted up!')

@client.command(pass_context=True, aliases=['h', 'H'])
async def help(ctx, cmd=None):
    if cmd == None:
        embed = discord.Embed(title='The Professor Help Menu', colour=discord.Colour.blurple(), description='Do `.help <command>` to get more information about a specific command!')
        embed.add_field(name='Prefix', value='`.`', inline=False)
        embed.add_field(name='Help', value='Shows this menu!', inline=False)
        embed.add_field(name='Dev', value='Show information about this bot and its developer.', inline=False)
        embed.add_field(name='Instrument', value='Shows a random instrument!', inline=False)
        embed.add_field(name='Chord', value='Defines a chord based on notes it is given.', inline=False)
        embed.add_field(name='Suggest', value='Suggest a feature to be added to the bot.', inline=False)
        embed.add_field(name='Bug', value='Report a bug with the bot.', inline=False)
        await ctx.send(embed=embed)
    elif cmd == 'Help' or cmd =='help':
        embed = discord.Embed(title='Help', colour=discord.Colour.blurple())
        embed.add_field(name='Syntax', value='.help <command>', inline=False)
        embed.add_field(name='Help Key', value='\t.command = Command\n\t[argument] = Required Argument\n\t<argument> = Optional Argument', inline=False)
        embed.add_field(name='Aliases', value='Help, help, h, H', inline=False)
        embed.add_field(name='Description', value='Shows help menu to show all possible commands available for user to use.', inline=False)
        await ctx.send(embed=embed)
    elif cmd == 'Dev' or cmd =='dev':
        embed = discord.Embed(title='Dev', colour=discord.Colour.blurple())
        embed.add_field(name='Syntax', value='.dev ', inline=False)
        embed.add_field(name='Aliases', value='Dev, dev', inline=False)
        embed.add_field(name='Description', value='Shows the bot name, the developer, the bot\'s current version, and when it was last updated.', inline=False)
        await ctx.send(embed=embed)
    elif cmd == 'Instrument' or cmd =='instrument':
        embed = discord.Embed(title='Instrument', colour=discord.Colour.blurple())
        embed.add_field(name='Syntax', value='.instrument ', inline=False)
        embed.add_field(name='Aliases', value='Instrument, instrument, Instr, instr', inline=False)
        embed.add_field(name='Description', value='Lists a random instrument from an incomplete list.', inline=False)
        await ctx.send(embed=embed)
    elif cmd == 'Chord' or cmd =='chord':
        embed = discord.Embed(title='Chord', colour=discord.Colour.blurple())
        embed.add_field(name='Syntax', value='.chord [note1] [note2] [note3] <note4> <note5> <note6>', inline=False)
        embed.add_field(name='Aliases', value='Chord, chord, C, c', inline=False)
        embed.add_field(name='Description', value='Defines a chord from the notes that the bot is given. Must be a minimum of 3 notes, and maximum of 6. Notes must be capitalized.\n\tFlat = b\n\tSharp = #', inline=False)
        await ctx.send(embed=embed)
    elif cmd == 'Suggest' or cmd =='suggest':
        embed = discord.Embed(title='Suggestion', colour=discord.Colour.blurple())
        embed.add_field(name='Syntax', value='.suggest <suggestion>', inline=False)
        embed.add_field(name='Aliases', value='Suggest, suggest, Sugg, sugg', inline=False)
        embed.add_field(name='Description', value='You can suggest anything; from new features, unrecognized chords, or more! If you found a bug; use `.bug` instead.\nIf suggesting a chord to be added: include the notes (or intervals) it is made of, along with the official (generally accepted) name of the chord.', inline=False)
        await ctx.send(embed=embed)
    elif cmd == 'Bug' or cmd =='bug':
        embed = discord.Embed(title='Bug', colour=discord.Colour.blurple())
        embed.add_field(name='Syntax', value='.bug <bug report>', inline=False)
        embed.add_field(name='Aliases', value='Bug, bug, B, b', inline=False)
        embed.add_field(name='Description', value='Bugs can include any unexpected errors you get, or possibly if the bot simply is not working. If you have a suggestion, use `.suggest` instead.', inline=False)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(colour=discord.Colour.red())
        embed.add_field(name='Error', value='Command not found! Check your spelling, or ask me about something that I can actually do instead!')
        await ctx.send(embed=embed)

@client.command(aliases=['Dev'])
async def dev(ctx):
    embed = discord.Embed(title='Bot Information', colour=discord.Colour.blurple(), description='Information about the Bot and Developer.')
    embed.add_field(name='Bot Name', value='The Professor', inline=False)
    embed.add_field(name='Developer', value='catter1', inline=False)
    embed.add_field(name='Version', value=version, inline=False)
    embed.add_field(name='Last Updated', value=dateedited, inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['instr', 'Instrument', 'Instr'])
async def instrument(ctx):
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
    fulllist = ['Bassoon', 'Clarinet', 'Contrabassoon', 'Flute', 'French Horn', 'Guitar', 'Harp', 'Harpsichord', 'Lute', 'Mandolin', 'Oboe', 'Organ', 'Piano', 'Pipe Organ', 'Soprano Saxophone', 'Alto Saxophone', 'Tenor Saxophone', 'Baritone Saxophone', 'Timpani', 'Trombone', 'Trumpet', 'Tuba', 'Viola', 'Violin', 'Cello', 'Acoustic Bass', 'Bagpipe', 'Baritone', 'Electric Bass', 'Bassoon', 'Bass Clarinet', 'Bugle', 'English Horn', 'Euphonium', 'Piccolo', 'Recorder', 'Ukulele', 'Voice', 'Marimba', 'Xylophone', 'Glockenspiel', 'Vibraphone', 'Bass Drum', 'Snare Drum', 'Cymbals', 'Drum Set', 'Claves', 'Slapstick', 'Triangle', 'Bells']
    randinstr = random.choice(fulllist)
    embed = discord.Embed(title='Random Instrument Generator', colour=discord.Colour.blurple())
    embed.add_field(name=randinstr, value="Here's your random instrument!")
    await ctx.send(embed=embed)

@client.command(aliases=['Suggest', 'sugg', 'Sugg'])
async def suggest(ctx, *, suggestion=None):
    if suggestion == None:
        embed = discord.Embed(colour=discord.Colour.blurple())
        embed.add_field(name='Follow `.suggestion` with your suggestion!', value='You can suggest anything; from new features, unrecognized chords, or more! If you found a bug; use `.bug` instead.')
        await ctx.send(embed=embed)
    else:
        embed1 = discord.Embed(title='Your Suggestion Has Been Submitted.', colour=discord.Colour.blurple())
        embed1.add_field(name='Thank you!', value=f'"{suggestion}"')
        embed1.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed1)
        channel = client.get_channel(747626471819968554)
        embed2 = discord.Embed(colour=discord.Colour.dark_green())
        embed2.add_field(name='New Suggestion for **The Professor**', value=f'"{suggestion}"')
        embed2.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await channel.send(embed=embed2)
    

@client.command(aliases=['Bug', 'b', 'B'])
async def bug(ctx, *, bug=None):
    if bug == None:
        embed = discord.Embed(colour=discord.Colour.blurple())
        embed.add_field(name='Follow `.bug` with your bug!', value='Bugs can include any unexpected errors you get, or possibly if the bot simply is not working. If you have a suggestion, use `.suggest`!')
        await ctx.send(embed=embed)
    else:
        embed1 = discord.Embed(title='Your Bug Has Been Submitted.', colour=discord.Colour.blurple())
        embed1.add_field(name='Thank you!', value=f'"{bug}"')
        embed1.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed1)
        channel = client.get_channel(747626471819968554)
        embed2 = discord.Embed(colour=discord.Colour.dark_red())
        embed2.add_field(name='New Bug for **The Professor**', value=f'"{bug}"')
        embed2.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await channel.send(embed=embed2)

@client.command(aliases=['Chord', 'c', 'C'])
async def chord(ctx, one, two, three, four=None, five=None, six=None):
    notes = {
        'B#' : '1',
        'C' : '1',
        'C#' : '2',
        'Db' : '2',
        'D' : '3',
        'D#' : '4',
        'Eb' : '4',
        'E' : '5',
        'Fb' : '5',
        'E#' : '6',
        'F' : '6',
        'F#' : '7',
        'Gb' : '7',
        'G' : '8',
        'G#' : '9',
        'Ab' : '9',
        'A' : '10',
        'A#' : '11',
        'Bb' : '11',
        'B' : '12',
        'Cb' : '12',
        'Abb' : '8',
        'A##' : '12',
        'Bbb' : '10',
        'B##' : '2',
        'Cbb' : '11',
        'C##' : '3',
        'Dbb' : '1',
        'D##' : '5',
        'Ebb' : '3',
        'E##' : '6',
        'Fbb' : '4',
        'F##' : '8',
        'Gbb' : '6',
        'G##' : '10'
        }
    note1 = int(notes[one])
    note2 = int(notes[two])
    note3 = int(notes[three])
    if four == None:
        if note1 > note2:
            diff1 = ((note2 + 12) - note1)
        else:
            diff1 = (note2 - note1)
        if note2 > note3:
            diff2 = ((note3 + 12) - note2)
        else:
            diff2 = (note3 - note2)
        
        if diff1 == 4 and diff2 == 3:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Major chord!', value=f'{one}, {two}, {three}')
            await ctx.send(embed = embed)
        elif diff1 == 3 and diff2 == 4:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Minor chord!', value=f'{one}, {two}, {three}')
            await ctx.send(embed = embed)
        elif diff1 == 3 and diff2 == 3:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Diminished chord!', value=f'{one}, {two}, {three}')
            await ctx.send(embed = embed)
        elif diff1 == 4 and diff2 == 4:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Augmented chord!', value=f'{one}, {two}, {three}')
            await ctx.send(embed = embed)
        elif diff1 == 2 and diff2 == 5:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Suspended 2nd chord!', value=f'{one}, {two}, {three}')
            await ctx.send(embed = embed)
        elif diff1 == 5 and diff2 == 2:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Suspended 4th chord!', value=f'{one}, {two}, {three}')
            await ctx.send(embed = embed)
        elif diff1 == 4 and diff2 == 6:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Italian Augmented 6th chord!', value=f'{one}, {two}, {three}')
            await ctx.send(embed = embed)
        elif diff1 == 3 and diff2 == 5:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Neopolitan chord!', value=f'{one}, {two}, {three}')
            await ctx.send(embed = embed)
        elif diff1 == 7 and diff2 == 5:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Power (1-5-1) chord!', value=f'{one}, {two}, {three}')
            await ctx.send(embed = embed)
        elif diff1 == 4 and diff2 == 2:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Major Flat 5 chord!', value=f'{one}, {two}, {three}')
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.red())
            embed.add_field(name='Sorry, but I don\'t recognize that chord (yet)!', value=f'Suggest that this be recognized using `.suggest`! {one}, {two}, {three}')
            await ctx.send(embed = embed)
    elif five == None:
        note4 = int(notes[four])
        if note1 > note2:
            diff1 = ((note2 + 12) - note1)
        else:
            diff1 = (note2 - note1)
        if note2 > note3:
            diff2 = ((note3 + 12) - note2)
        else:
            diff2 = (note3 - note2)
        if note3 > note4:
            diff3 = ((note4 + 12) - note3)
        else:
            diff3 = (note4 - note3)
        
        if diff1 == 4 and diff2 == 3 and diff3 == 4:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Major 7th chord!', value=f'{one}, {two}, {three}, {four}')
            await ctx.send(embed = embed)
        elif diff1 == 3 and diff2 == 4 and diff3 == 3:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Minor 7th chord!', value=f'{one}, {two}, {three}, {four}')
            await ctx.send(embed = embed)
        elif diff1 == 3 and diff2 == 4 and diff3 == 4:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Minor/Major 7th chord!', value=f'{one}, {two}, {three}, {four}')
            await ctx.send(embed = embed)
        elif diff1 == 4 and diff2 == 3 and diff3 == 3:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Dominant 7th (French Augmented 6th) chord!', value=f'{one}, {two}, {three}, {four}')
            await ctx.send(embed = embed)
        elif diff1 == 4 and diff2 == 4 and diff3 == 3:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Augmented 7th chord!', value=f'{one}, {two}, {three}, {four}')
            await ctx.send(embed = embed)
        elif diff1 == 4 and diff2 == 2 and diff3 == 4:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Dominant 7th Flat 5 (French Augmented 6th) chord!', value=f'{one}, {two}, {three}, {four}')
            await ctx.send(embed = embed)
        elif diff1 == 3 and diff2 == 3 and diff3 == 5:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Diminshed Major 7th chord!', value=f'{one}, {two}, {three}, {four}')
            await ctx.send(embed = embed)
        elif diff1 == 3 and diff2 == 3 and diff3 == 3:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Diminished 7th chord!', value=f'{one}, {two}, {three}, {four}')
            await ctx.send(embed = embed)
        elif diff1 == 3 and diff2 == 3 and diff3 == 3:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Diminished 7th chord!', value=f'{one}, {two}, {three}, {four}')
            await ctx.send(embed = embed)
        elif diff1 == 3 and diff2 == 3 and diff3 == 4:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Half-Diminished 7th chord!', value=f'{one}, {two}, {three}, {four}')
            await ctx.send(embed = embed)
        elif diff1 == 4 and diff2 == 3 and diff3 == 2:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Major 6th chord!', value=f'{one}, {two}, {three}, {four}')
            await ctx.send(embed = embed)
        elif diff1 == 3 and diff2 == 4 and diff3 == 2:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Major 6th chord!', value=f'{one}, {two}, {three}, {four}')
            await ctx.send(embed = embed)
        elif diff1 == 2 and diff2 == 2 and diff3 == 3:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Mu chord!', value=f'{one}, {two}, {three}, {four}')
            await ctx.send(embed = embed)
        elif diff1 == 5 and diff2 == 2 and diff3 == 3:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} 7th Suspended 4th chord!', value=f'{one}, {two}, {three}, {four}')
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.red())
            embed.add_field(name='Sorry, but I don\'t recognize that chord (yet)!', value=f'Suggest that this be recognized using `.suggest`! {one}, {two}, {three}, {four}')
            await ctx.send(embed = embed)
    elif six == None:
        note4 = int(notes[four])
        note5 = int(notes[five])
        if note1 > note2:
            diff1 = ((note2 + 12) - note1)
        else:
            diff1 = (note2 - note1)
        if note2 > note3:
            diff2 = ((note3 + 12) - note2)
        else:
            diff2 = (note3 - note2)
        if note3 > note4:
            diff3 = ((note4 + 12) - note3)
        else:
            diff3 = (note4 - note3)
        if note4 > note5:
            diff4 = ((note5 + 12) - note4)
        else:
            diff4 = (note5 - note4)
        
        if diff1 == 4 and diff2 == 3 and diff3 == 3 and diff4 == 4:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Dominant 9th chord!', value=f'{one}, {two}, {three}, {four}, {five}')
            await ctx.send(embed = embed)
        elif diff1 == 4 and diff2 == 3 and diff3 == 3 and diff4 == 3:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Dominant Minor 9th chord!', value=f'{one}, {two}, {three}, {four}, {five}')
            await ctx.send(embed = embed)
        elif diff1 == 4 and diff2 == 3 and diff3 == 3 and diff4 == 5:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Dominant 7th Sharp 9 (Hendrix) chord!', value=f'{one}, {two}, {three}, {four}, {five}')
            await ctx.send(embed = embed)
        elif diff1 == 8 and diff2 == 3 and diff3 == 5 and diff4 == 5:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Farben chord!', value=f'{one}, {two}, {three}, {four}, {five}')
            await ctx.send(embed = embed)
        elif diff1 == 4 and diff2 == 3 and diff3 == 4 and diff4 == 7:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Lydian chord!', value=f'{one}, {two}, {three}, {four}, {five}')
            await ctx.send(embed = embed)
        elif diff1 == 4 and diff2 == 4 and diff3 == 3 and diff4 == 7:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Major 7th Sharp 11 chord!', value=f'{one}, {two}, {three}, {four}, {five}')
            await ctx.send(embed = embed)
        elif diff1 == 4 and diff2 == 3 and diff3 == 2 and diff4 == 5:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Major 6/9 chord!', value=f'{one}, {two}, {three}, {four}, {five}')
            await ctx.send(embed = embed)
        elif diff1 == 3 and diff2 == 4 and diff3 == 2 and diff4 == 5:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Minor 6/9 chord!', value=f'{one}, {two}, {three}, {four}, {five}')
            await ctx.send(embed = embed)
        elif diff1 == 4 and diff2 == 3 and diff3 == 4 and diff4 == 3:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Major 9th chord!', value=f'{one}, {two}, {three}, {four}, {five}')
            await ctx.send(embed = embed)
        elif diff1 == 3 and diff2 == 4 and diff3 == 3 and diff4 == 4:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Minor 9th chord!', value=f'{one}, {two}, {three}, {four}, {five}')
            await ctx.send(embed = embed)
        elif diff1 == 4 and diff2 == 4 and diff3 == 2 and diff4 == 4:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} 9th Augmented 5th chord!', value=f'{one}, {two}, {three}, {four}, {five}')
            await ctx.send(embed = embed)
        elif diff1 == 4 and diff2 == 2 and diff3 == 4 and diff4 == 4:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} 9th Flat 5 chord!', value=f'{one}, {two}, {three}, {four}, {five}')
            await ctx.send(embed = embed)
        elif diff1 == 4 and diff2 == 3 and diff3 == 2 and diff4 == 1:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Seven Six chord!', value=f'{one}, {two}, {three}, {four}, {five}')
            await ctx.send(embed = embed)
        elif diff1 == 5 and diff2 == 5 and diff3 == 5 and diff4 == 4:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} So What chord!', value=f'{one}, {two}, {three}, {four}, {five}')
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.red())
            embed.add_field(name='Sorry, but I don\'t recognize that chord (yet)!', value=f'Suggest that this be recognized using `.suggest`! {one}, {two}, {three}, {four}, {five}')
            await ctx.send(embed = embed)
    else:
        note4 = int(notes[four])
        note5 = int(notes[five])
        note6 = int(notes[six])
        if note1 > note2:
            diff1 = ((note2 + 12) - note1)
        else:
            diff1 = (note2 - note1)
        if note2 > note3:
            diff2 = ((note3 + 12) - note2)
        else:
            diff2 = (note3 - note2)
        if note3 > note4:
            diff3 = ((note4 + 12) - note3)
        else:
            diff3 = (note4 - note3)
        if note4 > note5:
            diff4 = ((note5 + 12) - note4)
        else:
            diff4 = (note5 - note4)
        if note5 > note6:
            diff5 = ((note6 + 12) - note5)
        else:
            diff5 = (note6 - note5)
        
        if diff1 == 4 and diff2 == 3 and diff3 == 4 and diff4 == 3 and diff5 == 3:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Major 11th chord!', value=f'{one}, {two}, {three}, {four}, {five}, {six}')
            await ctx.send(embed = embed)
        elif diff1 == 4 and diff2 == 3 and diff3 == 3 and diff4 == 4 and diff5 == 4:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Augmented 11th chord!', value=f'{one}, {two}, {three}, {four}, {five}, {six}')
            await ctx.send(embed = embed)
        elif diff1 == 4 and diff2 == 3 and diff3 == 3 and diff4 == 4 and diff5 == 3:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Dominant 11th chord!', value=f'{one}, {two}, {three}, {four}, {five}, {six}')
            await ctx.send(embed = embed)
        elif diff1 == 6 and diff2 == 4 and diff3 == 6 and diff4 == 5 and diff5 == 5:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Mystic chord!', value=f'{one}, {two}, {three}, {four}, {five}, {six}')
            await ctx.send(embed = embed)
        elif diff1 == 1 and diff2 == 3 and diff3 == 1 and diff4 == 3 and diff5 == 1:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} Hexachord!', value=f'{one}, {two}, {three}, {four}, {five}, {six}')
            await ctx.send(embed = embed)
        elif diff1 == 4 and diff2 == 3 and diff3 == 3 and diff4 == 3 and diff5 == 8:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} 13th Flat 9 chord!', value=f'{one}, {two}, {three}, {four}, {five}, {six}')
            await ctx.send(embed = embed)
        elif diff1 == 4 and diff2 == 2 and diff3 == 4 and diff4 == 3 and diff5 == 8:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.green())
            embed.add_field(name=f'That is a {one} 13th Flat 9 Flat 5 chord!', value=f'{one}, {two}, {three}, {four}, {five}, {six}')
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(title='Chord Identifier', colour=discord.Colour.red())
            embed.add_field(name='Sorry, but I don\'t recognize that chord (yet)!', value=f'Suggest that this be recognized using `.suggest`! {one}, {two}, {three}, {four}, {five}, {six}')
            await ctx.send(embed = embed)

@chord.error
async def chord_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        embed = discord.Embed(title='Chord Identifier Error', colour=discord.Colour.red())
        embed.add_field(name='You did not enter a valid note!', value='If you think this is NOT an error, contact catter1.')
        await ctx.send(embed=embed)


client.run(token)