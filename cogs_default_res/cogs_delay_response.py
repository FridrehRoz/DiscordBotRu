"""
Набор когов для DelayResponse ответов на сообщения
"""

__version__ = 1.0

# Встроенные модули

# Основные внешние модули
import typing

# Детальный импорт внешних модулей
from disnake.ext import commands

# Вспомогательные со программные модули (с сопутствующим кодом)
from bot_start import *
import _types

# Модули отладки (вне работы программы)
import dev_scripts
from special_variables_scripts.pbar import is_imported
from special_variables_scripts.initialized import is_reg


class DelayResponseCommands(_types.Cog,
                            name='CogDelayResponseCommands'):
    """
    Ког DelayResponse команд
    """

    def __init__(self, _bot: _types.Bot):
        self.bot = _bot

    @commands.command(name='ping')
    async def ping_response(self, cmd_ctx: _types.Ctx) -> typing.NoReturn:
        """
        Отправляет Pong :D

        :param cmd_ctx: Принимает контекст команды
        """
        await cmd_ctx.send('Pong! ₍^⌯ᴖⱅᴖ⌯^₎')

    @commands.command(name='marko')
    async def marko_response(self, cmd_ctx: _types.Ctx) -> typing.NoReturn:
        """
        Отправляет Polo (Это же все знают!)

        :param cmd_ctx: Принимает контекст команды
        """
        await cmd_ctx.send('Polo! /ᐠ. ᴗ.ᐟ\\')


def setup(_bot: _types.Bot):
    """
    Регистрация кога в боте

    :param _bot: объект бота
    """
    _bot.add_cog(DelayResponseCommands(_bot))
    is_reg(__name__, __version__)
    is_imported()
