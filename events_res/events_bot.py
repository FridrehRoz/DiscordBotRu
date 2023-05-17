"""
Определяет обработчики on_* событий для клиента бота.
"""

# Встроенные модули

# Основные внешние модули
import typing

import special_bot_scripts.bot_emotion
# Детальный импорт внешних модулей

# Вспомогательные со программные модули (с сопутствующим кодом)
from bot_start import *
from embeds_res import *

# Модули отладки (вне работы программы)
import dev_scripts

__all__ = ['on_connect', 'on_ready']


@bot.event
async def on_connect() -> typing.NoReturn:
    """Реагирует на подключение бота к серверу Discord"""
    import os
    print('Клиент бота успешно подключён!')
    print(os.getcwd())


@bot.event
async def on_ready() -> typing.NoReturn:
    """Реагирует на готовность бота к работе."""
    print('Черничка проснулась!\n')
