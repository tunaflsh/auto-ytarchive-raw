import discord
import os
import const

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    os.system("python index.py")

client.run(const.DISCORD_TOKEN)


