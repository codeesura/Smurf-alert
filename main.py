import requests
import json
import discord
from discord.ext import commands , tasks
from discord import app_commands
import config

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tasks.loop(seconds=1)
async def status_task():
    getir = requests.get(f"https://api.polygonscan.com/api?module=stats&action=tokensupply&contractaddress=0xbac7e3182bb6691f180ef91f7ae4530abb3dc08d&apikey={config.POLYSCAN_TOKEN}").text
    getir = json.loads(getir)
    if int(getir["result"]) > 425 :
        channel = client.get_channel(int(config.CHANNE_ID))
        await channel.send("@everyone")
        await channel.send("@everyone")
        await channel.send("@everyone")
        exit()

@client.event
async def on_ready():
    status_task.start()
    print("Ready!")
    
client.run(config.DISCORD_TOKEN)