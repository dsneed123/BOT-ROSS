import discord
from discord.ext import commands
import os
import asyncio
from src.quotes import get_quote
from src.weather import get_weather_for_spokane,get_daily_forecast_for_spokane
from src.meme import get_random_meme
from datetime import datetime
import json

# Load environment variables from config.json file
with open('.gitignore/config.json.gitignore') as config_file:
    config = json.load(config_file)

TOKEN = config.get('TOKEN')
Weather_api_token = config.get('Weather-API')

# Setup bot with intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    channel = discord.utils.get(bot.get_all_channels(), name='bot-ross-dev')#channel name. change to bot-ross for depolyment
    if channel:
        current_date = datetime.now().strftime("%Y-%m-%d")
        message = (
            f'🌞 **Good Morning @everyone!** 🌞\n\n'
            f'📅 **Date:** {current_date}\n\n'
            f'Here\'s your daily report:\n\n'
            f'**Quote of the day:** {get_quote()}\n\n'
            f'**Weather Currently:** {get_weather_for_spokane(Weather_api_token)}\n'
            f'**Daily Forecast:** {get_daily_forecast_for_spokane(Weather_api_token)}\n\n'
            f'**Random Meme:** {get_random_meme()}'
        )
        await channel.send(message)
    else:
        print("Error: Channel 'BOT-ROSS' not found.")


if TOKEN:
    bot.run(TOKEN)
else:
    print("Error: DISCORD_TOKEN not found. Please check your .env file.")