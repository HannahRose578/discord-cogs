import discord
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix="-")

# @client.event
# async def on_connect():
# 	print('We have logged in as {0.user}'.format(client))
print("test")

@bot.command(pass_context=True)
async def test(ctx):
	await ctx.send("test")


# @client.event
# async def on_message(message):
# 	if message.author == client.user:
# 		return

# 	if message.content.startswith('$hello'):
# 		await message.channel.send('Hello!')


client.run("MjU3NTIxMjEwMjU3MTc4NjI0.DluCkQ.uM9e3e_7iluqjC-9MKQpvA6OKEk")