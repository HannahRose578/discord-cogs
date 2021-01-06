import discord
from discord.ext import commands

class Channels:
	def __init__(self, bot):
		self.bot = bot

	# @commands.command(pass_context=True)
	# async def hidden(self, ctx, id):
	# 	guild = self.bot.get_guild(int(id))
	# 	msg = ""
	# 	for channel in guild.channels:
	# 		if ctx.author.permissions_in(channel) != 67108896:
	# 			await ctx.send(channel.name)

	@commands.command(pass_context=True)
	async def channels(self, ctx, id):
		guild = self.bot.get_guild(int(id))
		channels = ""
		msg = discord.Embed(title="Channels")
		for channel in guild.text_channels:
			channels += channel.name + "\n"
		msg.add_field(name="Channels", value=channels)
		await ctx.send(embed=msg)

	@commands.command(pass_context=True)
	async def desc(self, ctx, id):
		guild = self.bot.get_guild(int(id))
		topics = ""
		for channel in guild.text_channels:
			try:
				topics += channel.name + "    " + channel.topic + "\n"
			except:
				pass
		file = open("topics.txt", "w")
		#file.write(topics)
		print(topics)
		file.close()


def setup(bot):
	bot.add_cog(Channels(bot))