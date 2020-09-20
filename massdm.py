import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('MESSAGE HERE')
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")

client.run('TOKEN HERE', bot=False)