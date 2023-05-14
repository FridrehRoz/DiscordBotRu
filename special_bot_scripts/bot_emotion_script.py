r"""
Модуль для работы с эмоциональной реакцией бота.

Material\Expression's
"""

__version__ = 1.0

# Встроенные модули
import dataclasses
import os
# Основные внешние модули
import typing
import _types
import disnake

# Детальный импорт внешних модулей

# Вспомогательные со программные модули (с сопутствующим кодом)
from bot_start import *

# Модули отладки (вне работы программы)
import dev_scripts

DIRECTORY_PATH = (DEFAULT_PATH + BOT_EXPRESSION_PATH)

__all__ = ['Emotion',
           'set_expression', 'set_pose']


@dataclasses.dataclass
class Emotion:
    """
    Отвечает за эмоцию которая будет отправлена.

    Настраивается при помощи функций.
    """

    expression: str  # выражение лица модели
    pose: str  # поза модели

    @classmethod
    async def get_file(cls):
        """Возвращает файл с изображением."""
        with open(rf'{DIRECTORY_PATH}\{cls.expression}\{cls.pose}.png',
                  'rb') as file:
            img: _types.File = disnake.File(file)
            return img


async def set_expression(name: str) -> typing.NoReturn:
    """
    Устанавливает выражение лица модели.

    :param name: Название выражения ~(Angry, happy)
    """

    expression_name = name.capitalize().strip()

    if expression_name not in os.listdir(DIRECTORY_PATH):
        Emotion.expression = 'Neutral'
    else:
        Emotion.expression = expression_name


async def set_pose(name: str) -> typing.NoReturn:
    """
    Устанавливает позу модели.

    :param name: Название позы ~()
    """

    pose_name = name.capitalize().strip()

    if pose_name not in os.listdir(DIRECTORY_PATH + rf'\{Emotion.expression}'):
        Emotion.pose = 'Greeting'
    else:
        Emotion.pose = pose_name
