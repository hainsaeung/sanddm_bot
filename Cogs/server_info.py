from discord import app_commands, ui
from discord.ext import commands
from discord import Interaction
from discord import Object
import discord
from datetime import datetime

class info(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="info", description="게임정보를 알려줘요!")
    async def info(self, interaction: Interaction) -> None:
        embed = discord.Embed(title="서버정보", description=f"대리88의 사업 서버입니다.\n좋은하루 되시길바랍니다.", color=discord.Color.blue())
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        info(bot),
        guilds=[Object(id=1037252002775846933)]
    )