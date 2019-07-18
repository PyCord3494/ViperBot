import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

import ztoken
import config


bot = commands.Bot(command_prefix = config.prefix)
bot.remove_command('help')
extensions = ["cogs.admin"] 

@bot.event
async def on_ready():
	print(f"{bot.user.name} - {bot.user.id}")
	print(discord.__version__)
	print("Ready...")


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
