# bot.py
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

prefix = "?"
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Everything's all ready to go~")

@bot.event
async def on_message(message):
    print("The message's content was", message.content)
    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)

@bot.command()
async def echo(ctx, *, content: str):
    await ctx.send(content)

@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='real-python'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

@bot.event
async def on_error(event, *args, **kwargs):
	with open('err.log', 'a') as f:
		if event == 'on_message':
			f.write(f'Unhandled message: {args[0]}\n')
		else:
			raise discord.DiscordException

bot.run(TOKEN)  # Where 'TOKEN' is your bot token
