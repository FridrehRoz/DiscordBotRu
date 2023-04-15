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
from special_variables.bot_start_variables import is_imported


class DelayResponseCommands(_types.Cog,
                            name='CogDelayResponseCommands'):
    """
    Ког DelayResponse команд
    """

    def __init__(self, _bot: _types.Bot):
        self.bot = _bot

    @commands.command(name='Ping')
    async def ping_response(self, cmd_ctx: _types.Ctx) -> typing.NoReturn:
        """
        Отправляет Pong :D

        :param cmd_ctx: Принимает контекст команды
        """
        await cmd_ctx.send('Pong! ₍^⌯ᴖⱅᴖ⌯^₎')

    @commands.command(name='Marko')
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
    print(f'\n{__name__} ver {__version__} загружен!')
    is_imported()