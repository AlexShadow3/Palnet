import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

intents = discord.Intents.all()
client = discord.Client(intents=intents)
channel_id = os.getenv('DISCORD_CHANNEL_ID')

bot = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'Ready! Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hello':
        await message.channel.send('Hello!')

@client.event
async def on_member_join(member):
    channel = client.get_partial_messageable(channel_id)
    await channel.send(f'Welcome to the server, {member.mention}!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# HELP COMMAND + EMBEDDING
@bot.command()
async def aide(context):
    embed = discord.Embed(
        title="Commandes",
        description="Une liste des commandes du serveur",
        colour=discord.Colour.random()
    )
    embed.set_thumbnail(url="https://sp-ao.shortpixel.ai/client/q_glossy,ret_img,w_1068/https://s22908.pcdn.co/wp-content/uploads/2022/02/what-are-bots-1068x706.jpg")
    embed.add_field(name="!ping", value="Répond Pong")
    await context.send(embed=embed)

token = os.getenv('DISCORD_TOKEN')
client.run(token)