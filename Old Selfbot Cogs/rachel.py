import discord
from discord.ext import commands

class Rachel:
	def __init__(self, bot):
		self.bot = bot

	async def on_message(self, message):
		if message.author.id != 196304053725167616:
			return

		if "best" in message.content.lower():
			newContent = message.content.replace("best", "event")
			print(newContent)
			await message.edit(content=str(newContent))

def setup(bot):
	bot.add_cog(Rachel(bot))