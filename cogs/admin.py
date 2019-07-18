import discord
from discord.ext import commands


class Admin(commands.Cog):
	def __init__(self, bot):
		self.bot = bot    


	# kick mentioned user
	@commands.command()
	@has_permissions(kick_members=True)
	async def kick(self, ctx, kick_user: discord.Member, reason_for_kick):
		await ctx.guild.kick(kick_user, reason = reason_for_kick)


	# ban mentioned user
	@commands.command()
	@has_permissions(ban_members=True)
	async def ban(self, ctx, ban_user: discord.Member, reason_for_ban):
		await ctx.guild.ban(ban_user, reason = reason_for_ban)


	# mute specific user
	@commands.command()
	@has_permissions(manage_messages=True)
	async def mute(self, ctx, mute_user: discord.Member):
		guild = ctx.guild
		try:
			# try selecting role if exist
			mute_role = discord.utils.get(guild.roles, name = "Muted")
		except:
			# create role if not exist, then select it
			perms = discord.Permissions(send_messages=False)
			await guild.create_role(name="Muted", permissions=perms)
			mute_role = discord.utils.get(guild.roles, name = "Muted")
		try:
			# add role to user and send msg
			await mute_user.add_roles(mute_role) # assign the role
			await ctx.send(f"{ctx.message.author} has muted {mute_user}")
		except discord.Forbidden:
			# if bot not allowed
			await ctx.send("Unable to mute user. Maybe I don't have the `Manage Roles` permission, "
                              "or you're trying to mute somebody higher than me.")


	# unmute specific user
	@commands.command()
	@has_permissions(manage_messages=True)
	async def unmute(self, ctx, unmute_user: discord.Member):
		try:
			unmute_role = discord.utils.get(ctx.guild.roles, name = "Muted") # get the role to apply
			await unmute_user.remove_roles(unmute_role) # assign the role
			await ctx.send(f"{ctx.message.author} has unmuted {unmute_user}")
		except Exception as e:
			await ctx.send(e)

def setup(bot):
	bot.add_cog(Admin(bot))
