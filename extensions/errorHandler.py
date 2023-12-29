import discord
from discord.ext import commands

class ExceptionHandler(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

		bot.tree.error(coro = self.__dispatch_to_app_command_handler)

	async def __dispatch_to_app_command_handler(self, interaction: discord.Interaction, error: discord.app_commands.AppCommandError):
		self.bot.dispatch("app_command_error", interaction, error)

	@commands.Cog.listener("on_app_command_error")
	async def get_app_command_error(self, interaction: discord.Interaction, error: discord.app_commands.AppCommandError):
		try:
			await interaction.response.defer()
		except:
			pass
		
		if isinstance(error, discord.app_commands.CommandOnCooldown):
			embed=discord.Embed(title="You are on cooldown", description=f"Wait {error.retry_after} seconds", color=0xed4c40)
			try:
				await interaction.response.edit_message(embed=embed)
			except:
				await interaction.followup.send(embed=embed)
			return

		elif isinstance(error, discord.app_commands.MissingPermissions):
			embed=discord.Embed(title="You aren't allowed to do this", description=f"{error.missing_permissions}", color=0xed4c40)
			try:
				await interaction.response.edit_message(embed=embed)
			except:
				await interaction.followup.send(embed=embed)
			return

		elif isinstance(error, discord.app_commands.BotMissingPermissions):
			embed=discord.Embed(title="I'm not allowed to do this", description=f"{error.missing_permissions}", color=0xed4c40)
			try:
				await interaction.response.edit_message(embed=embed)
			except:
				await interaction.followup.send(embed=embed)
			return
		elif isinstance(error, discord.app_commands.CommandNotFound):
			embed=discord.Embed(title="Command doesn't exist", description=f"I don't know what you want from me", color=0xed4c40)
			try:
				await interaction.response.edit_message(embed=embed)
			except:
				await interaction.followup.send(embed=embed)
			return
		elif isinstance(error, discord.app_commands.MissingAnyRole):
			embed=discord.Embed(title="You're missing some roles", description=f"{error.missing_roles}", color=0xed4c40)
			try:
				await interaction.response.edit_message(embed=embed)
			except:
				await interaction.followup.send(embed=embed)
			return
		elif isinstance(error, discord.app_commands.MissingRole):
			embed=discord.Embed(title="You're missing a role", description=f"{error.missing_role}", color=0xed4c40)
			try:
				await interaction.response.edit_message(embed=embed)
			except:
				await interaction.followup.send(embed=embed)
			return
		embed=discord.Embed(title="ERROR", description=f"I don't know what you are doing\n{error}", color=0xed4c40)
		try:
			await interaction.response.edit_message(embed=embed)
		except:
			await interaction.followup.send(embed=embed)
  

async def setup(bot: commands.Bot):
    await bot.add_cog(ExceptionHandler(bot))