import discord
from discord.ext import commands
import json

from help_cog import help_cog
from music_cog import music_cog

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

bot.remove_command('help')

with open('config.json') as config_file:
    config = json.load(config_file)
    token = config['TOKEN']

async def load_cogs():
    try:
        await bot.load_extension('help_cog')
        await bot.load_extension('music_cog')
    except Exception as e:
        print(f"Error loading cogs: {e}")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await load_cogs()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

try:
    bot.run(token)
except Exception as e:
    raise e