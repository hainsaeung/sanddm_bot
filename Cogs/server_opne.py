from discord import app_commands, ui
from discord.ext import commands
from discord import Interaction
from discord import Object
import discord
from datetime import datetime

class server_open(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="server-open", description="서버 오픈을 알려줘요!")
    @app_commands.checks.has_any_role(1037673127385247854)
    async def info(self, interaction: Interaction) -> None:
        await interaction.response.send_message("<@&1133722715451302028>\n\n오늘은 교육이 예정 되있으니 통영 서버가 열릴때 참석 부탁드립니다.")

    @info.error
    async def info_error(self, interaction: Interaction, error: commands.CommandError) -> None:
        embed = discord.Embed(title="서버 오픈 알림 실패!", description=f"권한이 없거나 기타 오류가 발생했어요!", color=discord.Color.red())
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        server_open(bot),
        guilds=[Object(id=1037252002775846933)]
    )