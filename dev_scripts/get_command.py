"""
Модуль используется для запроса команд
"""

# Встроенные модули

# Основные внешние модули
import typing

# Детальный импорт внешних модулей

# Вспомогательные со программные модули (с сопутствующим кодом)
from bot_start import *
import _types

# Модули отладки (вне работы программы)

__all__ = ['check_cmd', 'request_cmd']


async def check_cmd(command_name: str) -> bool:
    """
    Проверяет существование команды.

    :param command_name: Название команды
    :return bool:
    """
    if command_name in (command.name for command in bot.commands):
        return True
    return False


async def request_cmd(command_name: str) -> typing.Union[_types.Cmd, None]:
    """
    Используется для запроса на получение команды.

    :param command_name: Название команды
    """
    if await check_cmd(command_name):
        return bot.get_command(command_name)
    else:
        return None
