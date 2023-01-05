import requests
import json
import discord
from discord.ext import commands , tasks
from discord import app_commands
import config

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

total_supply = 500 ## specific supply 

@tasks.loop(seconds=1)
async def status_task():
    try:
        getir = requests.get(f"https://api.polygonscan.com/api?module=stats&action=tokensupply&contractaddress=0xbac7e3182bb6691f180ef91f7ae4530abb3dc08d&apikey={config.POLYSCAN_TOKEN}").text
        getir = json.loads(getir)
    except : pass
    if int(getir["result"]) > total_supply :
        channel = client.get_channel(int(config.CHANNEL_ID))
        await channel.send("@everyone")
        await channel.send("@everyone")
        await channel.send("@everyone")
        exit()
    else : pass
@client.event
async def on_ready():
    status_task.start()
    print("Ready!")
    
client.run(config.DISCORD_TOKEN)
