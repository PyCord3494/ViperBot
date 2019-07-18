import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

import ztoken


bot = commands.Bot(command_prefix = "$")
bot.remove_command('help')
extensions = [] 

@bot.event
async def on_ready():
	print(f"{bot.user.name} - {bot.user.id}")
	print(discord.__version__)
	print("Ready...")


@bot.command(pass_context=True)
async def help(ctx):
	await ctx.send("Insert Help Menu Here")


if __name__ == '__main__':
	for extension in extensions:
		try:
			bot.load_extension(extension)
			print(f"Loaded cog: {extension}")
		except Exception as error:
			print(f"{extension} could not be loaded. [{error}]")
	bot.run(ztoken.token)
