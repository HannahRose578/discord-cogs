import discord
import string
import random
from asyncio import sleep
from discord.ext import commands

class Roles:
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def createroles(self, ctx, num):
		for i in range(int(num)):
			r=random.randint(0,255)
			g=random.randint(0,255)
			b=random.randint(0,255)
			randomname = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
			await ctx.guild.create_role(name=randomname,colour=discord.Colour.from_rgb(r,g,b))

	@commands.command(pass_context=True)
	async def addroles(self, ctx):
		for role in ctx.guild.roles:
			try:
				await ctx.guild.owner.add_roles(role)
				sleep(1)
			except:
				pass

def setup(bot):
	bot.add_cog(Roles(bot))