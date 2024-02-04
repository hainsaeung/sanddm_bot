from discord import Intents
from discord.ext import commands
from discord import Game
from discord import Status
from discord import Object


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='=',
            intents=Intents.all(),
            sync_command=True,
            application_id=1133971803988054127
        )   
        self.initial_extension = [
            "Cogs.sandmsg_dm",
            "Cogs.server_info",
            "Cogs.server_opne"
        ]

    async def setup_hook(self):
        for ext in self.initial_extension:
            await self.load_extension(ext)
        await bot.tree.sync(guild=Object(id=1037252002775846933))

    async def on_ready(self):
        print("===============")
        print("login")
        print(self.user.name)
        print(self.user.id)
        print("===============")
        game = Game("서버 관리중!")
        await self.change_presence(status=Status.dnd, activity=game)


bot = MyBot()
bot.run('MTEzMzk3MTgwMzk4ODA1NDEyNw.GQd-PM.cbmzl0-1gF5wOO5QlTH-F-el3YRFsPso1kZ9Is')