import asyncio
import discord
import sys
from discord.ext import commands


class ErrHandle(commands.Cog):
	def __init__(self, bot):
		self.bot = bot



def setup(bot):
	bot.add_cog(ErrHandle(bot))
