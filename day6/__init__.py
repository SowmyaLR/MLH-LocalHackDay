import discord
from decouple import config
import random

DISCORD_TOKEN = config("DISCORD_TOKEN")
DISCORD_GUILD = config("DISCORD_GUILD")

client = discord.Client()
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, Welcome to {DISCORD_GUILD}'
    )

@client.event
async def on_message(message):
    greetings = ["hello", "hi", "hai", "good morning", "good afternoon", "good night", "what's up"]
    print(message.content.lower())
    if message.content.lower() in greetings:
        print("Inside content: {}".format(message))
        channel = message.channel
        await channel.send(f'{message.content.lower()}. Nice to have you!')

client.run(DISCORD_TOKEN)