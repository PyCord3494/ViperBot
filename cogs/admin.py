import discord
from discord.ext import commands
from discord.ext.commands import has_permissions


class Admin(commands.Cog):
	def __init__(self, bot):
		self.bot = bot    

	@commands.command(hidden = True)
	#@has_permissions(administrator=True)
	async def end(self, ctx):
		await self.bot.logout()

	# kick mentioned user
	@commands.command()
	#@has_permissions(kick_members=True)
	async def kick(self, ctx, kick_user: discord.Member, reason_for_kick):
		await ctx.guild.kick(kick_user, reason = reason_for_kick)
		await ctx.send(f"User {ctx.author.mention} has kicked {kick_user.name} {kick_user.id} for reason: {reason}")


	# ban mentioned user
	@commands.command()
	#@has_permissions(ban_members=True)
	async def ban(self, ctx, ban_user: discord.Member, reason_for_ban):
		await ctx.guild.ban(ban_user, reason = reason_for_ban)
		await ctx.send(f"User {ctx.author.mention} has banned {ban_user.name} {ban_user.id} for reason: {reason}")


	# mute specific user
	@commands.command()
	#@has_permissions(manage_messages=True)
	async def mute(self, ctx, mute_user: discord.Member):
		guild = ctx.guild
		mute_role = discord.utils.get(guild.roles, name = "Muted")
		await mute_user.add_roles(mute_role) # assign the role
		await ctx.send(f"{ctx.message.author.mention} has muted {mute_user.mention}")


	# unmute specific user
	@commands.command()
	#@has_permissions(manage_messages=True)
	async def unmute(self, ctx, unmute_user: discord.Member):
		try:
			unmute_role = discord.utils.get(ctx.guild.roles, name = "Muted") # get the role to apply
			await unmute_user.remove_roles(unmute_role) # assign the role
			await ctx.send(f"{ctx.message.author.mention} has unmuted {unmute_user.mention}")
		except Exception as e:
			await ctx.send(e)

def setup(bot):
	bot.add_cog(Admin(bot))
