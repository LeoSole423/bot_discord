# bot_discord
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print("The bot is ready for use")
    print("'''''''''''''''''''''''''")


@client.event
async def on_member_join(member):
    channel = client.get_channel()
    await channel.send("Hola pedaso de gil" + member)


@client.command()
async def hola(ctx):
    await ctx.send('Que onda pa! (Sin ofender)')


@client.command()
async def rock(ctx):
    await ctx.send('.play https://open.spotify.com/playlist/24xWu0yQD4rJbPAR8hcj1B?si=a75f8c758e254693')


@client.command(pass_context=True)
async def veni(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("Entra en un canal de voz salamin")


@client.command(pass_context=True)
async def nv(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("nv")
    else:
        await ctx.send("xd")


my_secret = 'ODk3ODg2NDcwMzU3MDAwMTky.YWcL8A.pHSierZxXmFI8nt0Q5kG7-QPLSU'
client.run(my_secret)