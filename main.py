# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
from config import token
import pafy
from discord import FFmpegPCMAudio, PCMVolumeTransformer
import urllib.request
import re
from youtube_dl import YoutubeDL
import os
from asyncio import sleep

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Bot online")

server, server_id, name_channel = None, None, None
domains = ["https://www.youtube.com/", "http://www.youtube.com/", "https://youtu.be/", "http://youtu.be/"]
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn',}
BEST_AUDIOS = [
    "https://cs3-7v4.vkuseraudio.net/p2/c47bce65e9f085.mp3?extra=QaHF5YyCg95aA7eCiqBDqCGbR0woFgwcZfgkeyi1kq8QIZKppuoA6tD6vsJoR6nYZrCb_lTMgMOBNb5_sIcshnQGghO5cRu5rx3itgfOvo-49HBWYuqh9cmWCZvJwcFl9PKhuPzUapd4A9_3HlGbi0akiQ&long_chunk=1",

]
YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'False'}

async def check_domains(link):
    for x in domains:
        if link.startswith(x):
            return True
    return False


@bot.command()
async def gachi(ctx, *, command = None):
    global server, server_id, name_channel
    author = ctx.author
    if command == None:
        server = ctx.guild
        if ctx.author.voice and ctx.author.voice.channel:
            name_channel = ctx.author.voice.channel.name
        else:
            await ctx.send("Зайди в войс, дурила")
            return
        voice_channel = discord.utils.get(server.voice_channels, name=name_channel)

    if command:
        source = BEST_AUDIOS[int(command)]
        server = ctx.guild
        if ctx.author.voice and ctx.author.voice.channel:
            name_channel = ctx.author.voice.channel.name
        else:
            await ctx.send("Зайди в войс, дурила")
            return
        voice_channel = discord.utils.get(server.voice_channels, name=name_channel)
    else:
        source = BEST_AUDIOS[0]
        server = ctx.guild
        if ctx.author.voice and ctx.author.voice.channel:
            name_channel = ctx.author.voice.channel.name
        else:
            await ctx.send("Зайди в войс, дурила")
            return
        voice_channel = discord.utils.get(server.voice_channels, name=name_channel)

    voice = discord.utils.get(bot.voice_clients, guild=server)
    if voice is None:
        await voice_channel.connect()
        voice = discord.utils.get(bot.voice_clients, guild=server)

        song = FFmpegPCMAudio(source,
                                **FFMPEG_OPTIONS)

        voice.play(song)
    else:
        voice.play(discord.FFmpegPCMAudio(f'{source}'))


@bot.command()
async def play(ctx, *, command = None):
    search = command

    if ctx.message.author.voice == None:
        await ctx.channel.send("Зайди в войс, клоун")
        return

    channel = ctx.message.author.voice.channel

    voice = discord.utils.get(ctx.guild.voice_channels, name=channel.name)

    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    if voice_client == None:
        voice_client = await voice.connect()
    else:
        await voice_client.move_to(channel)

#    search = search.replace(" ", "+")

#    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search)
#    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    video_ids = search

    song = pafy.new(video_ids)  # creates a new pafy object

    audio = song.getbestaudio()  # gets an audio source

    source = FFmpegPCMAudio(audio.url,
                            **FFMPEG_OPTIONS)  # converts the youtube audio source into a source discord can use

    voice_client.play(source)  # play the source

@bot.command()
async def play2(ctx, arg):
    global vc

    try:
        voice_channel = ctx.message.author.voice.channel
        vc = await voice_channel.connect()
    except:
        print('Уже подключен или не удалось подключиться')

    if vc.is_playing():
        await ctx.send(f'{ctx.message.author.mention}, музыка уже проигрывается.')

    else:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(arg, download=False)

        URL = info['formats'][0]['url']

        vc.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=URL, **FFMPEG_OPTIONS))

        while vc.is_playing():
            await sleep(1)
        if not vc.is_paused():
            await vc.disconnect()

bot.run(token)