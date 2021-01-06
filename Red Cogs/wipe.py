import discord
from discord.ext import commands

class Wipe:
	def __init__(self, bot):
		self.bot = bot

	def predicate(message):
		return message.author.id == 196304053725167616

	@commands.command(pass_context=True)
	async def wipe(self, ctx):
		#arr = [dog,doggy,dogs,doggies,beastiality,bestiality,zoophilia,mount,knot,breed,smash]
		channels = [462371471449391106,462382962483134475,462400796533719060]
		# async for msg in ctx.message.channel.history(limit=20).filter(predicate):
		# 	print(msg)
		# messages = await ctx.message.channel.history(limit=20).flatten()
		# print(messages)
		print(discord.__version__)


def setup(bot):
	bot.add_cog(Wipe(bot))