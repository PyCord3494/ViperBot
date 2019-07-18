import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import time

import config


class Other(commands.Cog):
	def __init__(self, bot):
		self.bot = bot    

	@commands.command(pass_context=True)
	async def bug(self, ctx, bug: str):
		chnl = self.bot.get_channel(601522581606105126)
		await chnl.send(f"***NEW BUG REPORTED***\n**Server Name:** {ctx.guild.name}\n**User:** {ctx.author.name}#{ctx.author.discriminator} {ctx.author.id}\n**Bug:** {bug}")


	@commands.command(pass_context=True)
	async def idea(self, ctx, idea: str):
		chnl = self.bot.get_channel(597698007370301460)
		await chnl.send(f"Rquested by: {ctx.author.name}\n**Idea:** {idea}")


	@commands.command(pass_context=True)
	async def getid(self, ctx, member: discord.Member):
		await ctx.send(f"ID of user: {member.id}")


	@commands.command(pass_context=True)
	async def inviteme(self, ctx):
		await ctx.send(f"Thanks for liking me! Here's my invite: *[invlinkhere]*")


	@commands.command(pass_context=True)
	async def mutelist(self, ctx):
		mute_role = discord.utils.get(ctx.guild.roles, name = "Muted")
		muteNum = len(mute_role.members)
		await ctx.send(muteNum)
		

	@commands.command(pass_context=True)
	async def ping(self, ctx):
		before = time.monotonic()
		message = await ctx.send("Pong!")
		ping = (time.monotonic() - before) * 1000
		await message.edit(content=f"Pong!  `{round(ping,9)} ms`")


	@commands.command(pass_context=True)
	async def say(self, ctx, *, msg="Tell me what to say!"):
		await ctx.send(f"{msg}")


def setup(bot):
	bot.add_cog(Other(bot))