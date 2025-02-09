import discord
from discord.ext import commands
from chatgpt import send_to_chatgpt

import os
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  messages = [{"role": "user", "content": message.content}]
  response = send_to_chatgpt(messages)
  await message.channel.send(responses)
bot.run(DISCORD_TOKEN)
