# Встроенные модули

# Основные внешние модули

# Детальный импорт внешних модулей
from disnake.ext import commands
# Вспомогательные со программные модули (с сопутствующим кодом)
from bot_start import *
from _types import *
# Модули отладки (вне работы программы)
import dev_scripts


class DelayResponseCommand(commands.Cog):
    def __init__(self, _bot: commands.Bot):
        self.bot = _bot

    @commands.command(name='Ping')
    async def ping_response(self, cmd_ctx: cmd.ctx) -> None:
        """
        Отправляет Pong :D

        :param cmd_ctx: Принимает контекст команды
        """
        await cmd_ctx.send('Pong! ₍^⌯ᴖⱅᴖ⌯^₎')

    @commands.command(name='Marko')
    async def marko_response(self, cmd_ctx: cmd.ctx) -> None:
        """
        Отправляет Polo (Это же все знают!)

        :param cmd_ctx: Принимает контекст команды
        """
        await cmd_ctx.send('Polo! /ᐠ. ᴗ.ᐟ\\')


def setup(_bot: commands.Bot):
    _bot.add_cog(DelayResponseCommand(_bot))
