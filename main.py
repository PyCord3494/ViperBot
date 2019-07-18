import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

import ztoken
import config


bot = commands.Bot(command_prefix = config.prefix)
bot.remove_command('help')
extensions = ["cogs.admin", "cogs.tempCmds", "utils.errHandle", "utils.other"] 

@bot.event
async def on_ready():
	print(f"{bot.user.name} - {bot.user.id}")
	print(discord.__version__)
	print("Ready...")

@bot.event
async def on_guild_join(guild):
	print(f"Connected to guild: {guild.name}!")

	mute_role = discord.utils.get(guild.roles, name = "Muted")

	# creates role if not exist
	if not mute_role:
		mute_role = await guild.create_role(name="Muted")

	# moves it to bottom of the roles
	await mute_role.edit(position=1)

	# defines Muted role's permissions
	overwrite = discord.PermissionOverwrite()
	overwrite.send_messages = False

	# adds permissions for Muted to every channel
	for channel in guild.text_channels:
		await channel.set_permissions(mute_role, overwrite=overwrite)

@bot.event
async def on_guild_channel_create(channel):
	mute_role = discord.utils.get(channel.guild.roles, name = "Muted")
	overwrite = discord.PermissionOverwrite()
	overwrite.send_messages = False
	await channel.set_permissions(mute_role, overwrite=overwrite)



@bot.command(pass_context=True)
async def help(ctx):
	await ctx.send("Insert Help Menu Here")


# manually reload a cog
@bot.command(hidden = True)
@has_permissions(administrator=True)
async def reload(ctx, extension):
	try:
		bot.reload_extension(extension)
		print(f"Reloaded {extension}.\n")
	except Exception as error:
		print(f"{extension} could not be reloaded. [{error}]")


if __name__ == '__main__':
	for extension in extensions:
		try:
			bot.load_extension(extension)
			print(f"Loaded cog: {extension}")
		except Exception as error:
			print(f"{extension} could not be loaded. [{error}]")
	bot.run(ztoken.token)
