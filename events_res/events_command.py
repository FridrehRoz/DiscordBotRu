"""
Определяет обработчики on_* событий для команд бота.
"""

# Встроенные модули

# Основные внешние модули
import typing

import special_bot_scripts.bot_emotion
# Детальный импорт внешних модулей

# Вспомогательные со программные модули (с сопутствующим кодом)
from bot_start import *
import _types

# Модули отладки (вне работы программы)
import dev_scripts

__all__ = ['on_command_error', 'on_slash_command_error']


@bot.event
async def on_command_error(ctx: _types.Ctx, error: _types.CmdError):
    """
    Обработчик ошибки команды.
    :param ctx: Контекст команды
    :param error: ошибка команды (тип)
    """
    if isinstance(error, _types.MissingAnyRole):
        await ctx.send(
            'Проходи мимо котик, у тебя недостаточно прав! /ᐠᵕ ‸ᵕᐟ\\ﾉ')


@bot.event
async def on_slash_command_error(inter: _types.CmdInter,
                                 error: _types.CmdError):
    """
    Обработчик ошибки slash команд.
    :param inter: Контекст взаимодействия
    :param error: ошибка команды (тип)
    """
    if isinstance(error, _types.MissingAnyRole):
        await inter.send(
            'Проходи мимо котик, у тебя недостаточно прав! /ᐠᵕ ‸ᵕᐟ\\ﾉ')
