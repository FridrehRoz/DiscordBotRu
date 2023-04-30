r"""
Набор когов для проявления эмоций бота в чате.

Material\Expression's
"""

__version__ = 1.0

import dataclasses
import os
import time
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


@dataclasses.dataclass
class Emotion:
    """
    Отвечает за эмоцию которая будет отправлена.

    Настраивается при помощи кога EmotionCommands.
    """

    expression: str  # выражение лица модели
    pose: str  # поза модели


class EmotionCommands(_types.Cog,
                      name='CogEmotionCommands'):
    """
    Набор команд для работы с эмоциональными реакциями бота
    """

    def __init__(self, _bot: _types.Bot):
        self.bot = _bot

    @commands.has_any_role(1095625852735213608, 1095630062528766053)
    @commands.slash_command(
        name='expression',
        description='Выбирает вид выражения лица.')
    async def expression_response(
            self,
            cmd_inter: _types.CmdInter,
            expression_name: str = commands.Param(
                description='название эмоции')) -> typing.NoReturn:
        """
        Обработчик команды expression
        :param cmd_inter: объект сообщения
        :param expression_name: название выражения ~(Angry, happy)
        """

        expression_name = expression_name.capitalize()
        expression_types: list = os.listdir(DEFAULT_PATH + BOT_EXPRESSION_PATH)

        if expression_name not in expression_types:
            Emotion.expression = 'Neutral'
        else:
            Emotion.expression = expression_name

        await cmd_inter.delete_original_response()


def setup(_bot: _types.Bot) -> typing.NoReturn:
    """
    Регистрация кога в боте

    :param _bot: объект бота
    """
    _bot.add_cog(EmotionCommands(_bot))
    print(f'\n{__name__} ver {__version__} загружен!')
    is_imported()
