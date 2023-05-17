"""
Набор когов для эмоциональной функциональности бота
"""

__version__ = 1.0

# Встроенные модули

# Основные внешние модули
import typing
from special_bot_scripts.bot_emotion import *

# Детальный импорт внешних модулей
from disnake.ext import commands

# Вспомогательные со программные модули (с сопутствующим кодом)
from bot_start import *
import _types

# Модули отладки (вне работы программы)
import dev_scripts
from checkout_scripts.pbar import is_imported
from checkout_scripts.initialized import is_reg


class EmotionCommands(_types.Cog,
                      name='CogEmotionCommands'):
    """
    Набор команд для получения информации разработчику
    """

    def __init__(self, _bot: _types.Bot):
        self.bot = _bot

    @commands.has_any_role(1095625852735213608, 1095630062528766053)
    @commands.slash_command(
        name='request_emotion',
        description='запрос эмоциональной реакции.')
    async def request_emotion_response(
            self,
            cmd_inter: _types.CmdInter,
            data: str = commands.Param(
                description='expression и pose, '
                            'разделитель ","')) -> typing.NoReturn:
        """
        Обработчик команды request_emotion

        :param cmd_inter: объект сообщения
        :param data: выражение лица и поза
        """
        expression, pose = data.split(',')

        await set_expression(expression)
        await set_pose(pose)
        await cmd_inter.send(file=await Emotion.get_file())


def setup(_bot: _types.Bot) -> typing.NoReturn:
    """
    Регистрация кога в боте

    :param _bot: объект бота
    """
    _bot.add_cog(EmotionCommands(_bot))
    is_reg(__name__, __version__)
    is_imported()
