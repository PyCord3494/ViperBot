import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

import config


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
		try:
			await ban_user.send(f"{config.banMsg}")
			await ctx.guild.ban(ban_user, reason = reason_for_ban)
			await ctx.send(f"User {ctx.author.mention} has banned {ban_user.name} {ban_user.id} for reason: {reason}")
		except discord.Forbidden:
			await ctx.send("But I can't, muh permissions >:c")
		except discord.HTTPException:
			await ctx.send("Sorry, I failed to unban that user!") 


	# get ban list
	@commands.command()
	#@has_permissions(ban_members=True)
	async def banlist(self, ctx):
		bans = await ctx.guild.bans()
		if bans:
			users = "**Username | Reason**\n"
			for ban in bans:
				users += f"{ban[1]} | {ban[0]}\n"
			await ctx.send(users)
		else:
			await ctx.send("No bans found!")


	@commands.command()
	#@has_permissions(ban_members=True)
	async def unban(self, ctx, member_id: int):
		try:
			member = self.bot.get_user(member_id)
			await ctx.guild.unban(member)
			await ctx.send(f"User {ctx.author.mention} has unbanned {member.name} {member.id}")
		except discord.Forbidden:
			await ctx.send("But I can't, muh permissions >:c")
		except discord.HTTPException:
			await ctx.send("Sorry, I failed to unban that user!") 
		except Exception as e:
			await ctx.send(e)


	# mute specific user
	@commands.command()
	#@has_permissions(manage_messages=True)
	async def mute(self, ctx, member):
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
