import discord
import os
import const

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    # -d specifies to automatically download
    # Note anything works so -d is not necessary only argv length is checked
    os.system("python3 index.py")

client.run(const.DISCORD_TOKEN)


