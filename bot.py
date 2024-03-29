import os
import random
import json
import requests
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
channel_id = os.getenv('DISCORD_CHANNEL_ID')

# sad_words = [
#     "triste", "déprimé", "malheureux", "en colère", "misérable", "déprimant"
# ]

# starter_encouragements = [
#     "Courage!",
#     "Tiens bon.",
#     "Tu es une personne formidable!",
# ]

yesNo = [
    "Oui",
    "Non",
]

# if "responding" not in db.keys():
#     db["responding"] = True

# if "blagues" not in db.keys():
#     db["blagues"] = True

# if "yesNo" not in db.keys():
#     db["yesNo"] = True

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = "*" + json_data[0]["q"] + "* -" + json_data[0]["a"]
    return (quote)

# def update_encouragements(encouraging_message):
#     if "encouragements" in db.keys():
#         encouragements = db["encouragements"]
#         encouragements.append(encouraging_message)
#         db["encouragements"] = encouragements
#     else:
#         db["encouragements"] = [encouraging_message]


# def delete_encouragement(index):
#     encouragements = list(db["encouragements"])
#     if len(encouragements) > index:
#         del encouragements[index]
#     db["encouragements"] = encouragements

@client.event
async def on_ready():
    print(f'Ready! Logged in as {client.user}')

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content == 'hello':
#         await message.channel.send('Hello!')

@client.event
async def on_member_join(member):
    channel = client.get_partial_messageable(channel_id)
    await channel.send(f'Welcome to the server, {member.mention}!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg == 'hello':
        await message.channel.send('Hello!')

    if msg.startswith('!inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    # if "responding" in locals() or "responding" in globals():
    #     options = starter_encouragements
    #     if "encouragements" in db.keys():
    #         options = options + db["encouragements"].value

    #     if any(word in msg for word in sad_words):
    #         await message.channel.send(random.choice(options))

    # if msg.startswith("$new"):
    #     encouraging_message = msg.split("$new ", 1)[1]
    #     update_encouragements(encouraging_message)
    #     await message.channel.send("Nouveau message d'encouragement ajouté")

    # if msg.startswith("$del"):
    #     encouragements = []
    #     if "encouragements" in db.keys():
    #         index = int(msg.split("$del", 1)[1])
    #         delete_encouragement(index)
    #         encouragements = db["encouragements"].value
    #     await message.channel.send(encouragements)

    # if msg.startswith("$list"):
    #     encouragements = []
    #     if "encouragements" in db.keys():
    #         encouragements = db["encouragements"].value
    #     await message.channel.send(encouragements)

    # if msg.startswith("$responding"):
    #     value = msg.split("$responding ", 1)[1]

    #     if value.lower() == "true":
    #         db["responding"] = True
    #         await message.channel.send("Responding is on")
    #     else:
    #         db["responding"] = False
    #         await message.channel.send("Responding is off")

    # if msg.startswith("$blagues"):
    #     value = msg.split("$blagues ", 1)[1]

    #     if value.lower() == "true":
    #         db["blagues"] = True
    #         await message.channel.send("Jokes are on")
    #     else:
    #         db["blagues"] = False
    #         await message.channel.send("Jokes are off")

    # if msg.startswith("$yesNo"):
    #     value = msg.split("$yesNo ", 1)[1]

    #     if value.lower() == "true":
    #         db["yesNo"] = True
    #         await message.channel.send("Yes/No question is on")
    #     else:
    #        db["yesNo"] = False
    #        await message.channel.send("Yes/No question is off")
    
    # if "blagues" in locals() or "blagues" in globals():
    if msg.lower().startswith("palnet") or msg.lower().startswith("marie") or msg.lower().startswith("la menace"):
        await message.channel.send("Tu m'as appelé ?")
        return
    if msg.lower().endswith("cramptés ?"):
        await message.channel.send("Hein ?")
        return
    if msg.endswith("quoi"):
        await message.channel.send("Feur !!!")
        return
    if msg.endswith("quoi?"):
        await message.channel.send("Feur !!!")
        return
    if msg.endswith("quoi ?"):
        await message.channel.send("Feur !!!")
        return
    if msg.endswith("quoii"):
        await message.channel.send("Feur !!!")
        return
    if msg.endswith("quoii?"):
        await message.channel.send("Feur !!!")
        return
    if msg.endswith("quoii ?"):
        await message.channel.send("Feur !!!")
        return
    if msg.endswith("quoiii"):
        await message.channel.send("Feur !!!")
        return
    if msg.endswith("quoiii?"):
        await message.channel.send("Feur !!!")
        return
    if msg.endswith("quoiii ?"):
        await message.channel.send("Feur !!!")
        return
    if msg.lower().endswith("omment?") or msg.lower().endswith("omment ?"):
        await message.channel.send("Taire !!!")
        return
    if msg.endswith("ci"):
        await message.channel.send("Tron !!!")
        return
    if msg.endswith("cii"):
        await message.channel.send("Tron !!!")
        return
    if msg.endswith("ciii"):
        await message.channel.send("Tron !!!")
        return
    if msg.endswith("si"):
        await message.channel.send("Tron !!!")
        return
    if msg.endswith("sii"):
        await message.channel.send("Tron !!!")
        return
    if msg.endswith("siii"):
        await message.channel.send("Tron !!!")
        return
    if msg.endswith("nom"):
        await message.channel.send("Bril !!!")
        return
    if msg.endswith("non"):
        await message.channel.send("Bril !!!")
        return
    if msg.endswith("noon"):
        await message.channel.send("Briil !!!")
        return
    if msg.endswith("nooon"):
        await message.channel.send("Briiil !!!")
        return
    if msg.endswith("noooon"):
        await message.channel.send("Briiiil !!!")
        return
    if msg.endswith("oui"):
        await message.channel.send("stiti !!!")
        return
    if msg.endswith("ouii"):
        await message.channel.send("stitii !!!")
        return
    if msg.endswith("ouiii"):
        await message.channel.send("stiii !!!")
        return
    if msg.endswith("ouiiii"):
        await message.channel.send("stitiiii !!!")
        return
    if msg.endswith("yo"):
        await message.channel.send("plaît !")
        return
    if msg.endswith("yoo"):
        await message.channel.send("plaît !!")
        return
    if msg.endswith("yooo"):
        await message.channel.send("plaît !!!")
        return
    if msg.endswith("yoooo"):
        await message.channel.send("plaît !!!!")
        return
    if msg.lower().endswith("ouais"):
        await message.channel.send("stern !!!")
        return
    if msg.endswith("hein"):
        await message.channel.send("Deux !!!")
        return
    if msg.endswith("heiin"):
        await message.channel.send("Deux !!!")
        return
    if msg.endswith("heiiin"):
        await message.channel.send("Deux !!!")
        return
    if msg.endswith("hein?"):
        await message.channel.send("Deux !!!")
        return
    if msg.endswith("hein??"):
        await message.channel.send("Deux !!!")
        return
    if msg.endswith("hein???"):
        await message.channel.send("Deux !!!")
        return
    if msg.endswith("hein ?"):
        await message.channel.send("Deux !!!")
        return
    if msg.endswith("hein ??"):
        await message.channel.send("Deux !!!")
        return
    if msg.endswith("hein ???"):
        await message.channel.send("Deux !!!")
        return
    if msg.lower().endswith("trois"):
        await message.channel.send("Quatre !!!")
        return
    if msg.endswith("toi"):
        await message.channel.send("ture !!!")
        return
    if msg.endswith("toi?"):
        await message.channel.send("ture !!!")
        return
    if msg.endswith("toi ?"):
        await message.channel.send("ture !!!")
        return
    if msg.endswith("Toi"):
        await message.channel.send("ture !!!")
        return
    if msg.endswith("Toi?"):
        await message.channel.send("ture !!!")
        return
    if msg.endswith("Toi ?"):
        await message.channel.send("ture !!!")
        return
    if msg.endswith("la"):
        await message.channel.send("brador !!!")
        return
    if msg.endswith("là"):
        await message.channel.send("brador !!!")
        return
    if msg.endswith("la?"):
        await message.channel.send("brador !!!")
        return
    if msg.endswith("là?"):
        await message.channel.send("brador !!!")
        return
    if msg.endswith("la ?"):
        await message.channel.send("brador !!!")
        return
    if msg.endswith("là ?"):
        await message.channel.send("brador !!!")
        return
    if msg.lower().endswith("moi"):
        await message.channel.send("sissure !!!")
        return
    if msg.lower().endswith("cheh"):
        await message.channel.send("vre !!!")
        return
    if msg.endswith("qui"):
        await message.channel.send("wi !!!")
        return
    if msg.endswith("qui?"):
        await message.channel.send("wi !!!")
        return
    if msg.endswith("qui??"):
        await message.channel.send("wi !!!")
        return
    if msg.endswith("qui???"):
        await message.channel.send("wi !!!")
        return
    if msg.endswith("qui ?"):
        await message.channel.send("wi !!!")
        return
    if msg.endswith("qui ??"):
        await message.channel.send("wi !!!")
        return
    if msg.endswith("qui ???"):
        await message.channel.send("wi !!!")
        return

    if (msg.lower().startswith("palnet") or msg.lower().startswith("marie") or msg.lower().startswith("la menace")) and msg.endswith("?"):
        await message.channel.send("Mmmmh... " + random.choice(yesNo))
        return

token = os.getenv('DISCORD_TOKEN')
client.run(token)

# bot = commands.Bot(command_prefix='!', intents=intents)

# @bot.command(
#         name='ping',
#         description='Answer Pong!',
# )
# async def ping(ctx):
#     await ctx.send('Pong!')

# EMBED HELP COMMAND
# @bot.command(
#         name='aide',
#         description='Affiche les commandes du serveur',
# )
# async def aide(ctx):
#     embed = discord.Embed(
#         title="Commandes",
#         description="Une liste des commandes du serveur",
#         colour=discord.Colour.random()
#     )
#     embed.set_thumbnail(url="https://sp-ao.shortpixel.ai/client/q_glossy,ret_img,w_1068/https://s22908.pcdn.co/wp-content/uploads/2022/02/what-are-bots-1068x706.jpg")
#     # embed.add_field(name="!ping", value="Répond Pong")

#     commands_list = bot.commands

#     for command in commands_list:
#         embed.add_field(name=command.name, value=command.description, inline=False)

#     await ctx.send(embed=embed) 

# @bot.command(
#         name='hot',
#         description='Flip a coin',
# )
# async def hot(ctx):
#     await ctx.send(random.choice(['Pile', 'Face']))

# @bot.command(
#         name='roll',
#         description='Roll a dice',
# )
# async def roll(ctx):
#     await ctx.send(random.randint(1, 6))

# @bot.command(
#         name='clear',
#         description='Clear messages',
# )
# async def clear(ctx, amount=5):
#     await ctx.channel.purge(limit=amount)

# bot.run(token)