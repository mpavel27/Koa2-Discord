import discord
import os
import platform
from discord.ext import commands
import pyfiglet
from tabulate import tabulate
from dotenv import dotenv_values

config = dotenv_values(".env")
intents = discord.Intents().all()
client  = commands.Bot(command_prefix = config["COMMAND_PREFIX"], intents=intents)
Datas = []
mainColor = 0x5865f2
embedCopyright = "2022 © www.koa2.ro"
client.invites = {}
client.data = {}

client.remove_command("help")
client.config = config

@client.event
async def on_ready():
    discord_bot = pyfiglet.figlet_format("Discord Bot")
    print(discord_bot)
    headers = ["Logged in as","Discord.py API version","Python version","Running on","Extension","Status"]
    #test = [["","","","","",""]]
    Datas.insert(0,[client.user.name, '{0.major}.{0.minor}.{0.micro}-{0.releaselevel}'.format(discord.version_info),platform.python_version(),platform.platform(),"Discord","✅"])
    print(tabulate(Datas, headers, tablefmt="grid"))
    
for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        Datas.append(["","","","",filename[:-3],"✅"])
        
    
client.run(config["TOKEN"])