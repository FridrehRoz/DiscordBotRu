"""
Набор когов с командами для текстовых игр
"""

__version__ = 0.2

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


class DiceCommands(_types.Cog,
                   name='CogDiceCommands'):
    """
    Отвечает за игру в кости
    """

    def __init__(self, _bot: _types.Bot):
        self.bot = _bot

    @commands.command(name='throw',
                      description='Бросает кости.')
    async def throw_response(self, cmd_ctx: _types.Ctx) -> typing.NoReturn:
        """
        Бросает кости

        :param cmd_ctx: контекст команды
        """
        from random import randint

        result = randint(1, 6)
        await cmd_ctx.send(f'ᓚᘏᗢ\nВам выпало: {result}')


def setup(_bot: _types.Bot):
    """
    Регистрация кога в боте

    :param _bot: объект бота
    """
    _bot.add_cog(DiceCommands(_bot))
    is_reg(__name__, __version__)
    is_imported()
