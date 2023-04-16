"""
Определяет обработчики on_* событий для клиента бота.
"""

# Встроенные модули

# Основные внешние модули
import typing
# Детальный импорт внешних модулей

# Вспомогательные со программные модули (с сопутствующим кодом)
from bot_start import *
import _types
from embeds_package import *


# Модули отладки (вне работы программы)


@bot.event
async def on_connect() -> typing.NoReturn:
    """Реагирует на подключение бота к серверу Discord"""
    print('Клиент бота успешно подключён!')


@bot.event
async def on_ready() -> typing.NoReturn:
    """Реагирует на готовность бота к работе."""
    print('Черничка проснулась!')
