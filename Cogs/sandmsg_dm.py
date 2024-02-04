from discord import app_commands, ui
from discord.ext import commands
from discord import Interaction
from discord import Object
import discord
from datetime import datetime


class sanddm(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="sand-dm", description="DM을 보내요!")
    @app_commands.checks.has_any_role(1037673127385247854)
    async def sanddm(self, interaction: Interaction, user: discord.User) -> None:
        await interaction.response.send_modal(msg_modal(user=user))
    
    @sanddm.error
    async def sanddm_error(self, interaction: Interaction, error: commands.CommandError) -> None:
        embed = discord.Embed(title="안내문 발송 실패!", description=f"권한이 없거나 기타 오류가 발생했어요!", color=discord.Color.red())
        await interaction.response.send_message(embed=embed)

class msg_modal(ui.Modal, title="안내문 발송"):
    msg = ui.TextInput(label="보내실 문자", style=discord.TextStyle.long)
    a = None

    def __init__(self, user: discord.User):
        super().__init__()
        self.user = user

    async def interaction_check(self, interaction: Interaction):
        self.a = self.msg.value
        embed = discord.Embed(title="안내문이 발송되었어요!", description=f"{self.msg.value}", color=discord.Color.green())
        await interaction.response.send_message(embed=embed)
        await self.user.send(self.a)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        sanddm(bot),
        guilds=[Object(id=1037252002775846933)]
    )