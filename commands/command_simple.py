# Встроенные модули

# Основные внешние модули

# Детальный импорт внешних модулей

# Вспомогательные со программные модули (с сопутствующим кодом)
from bot_start import *
from _types import *
# Модули отладки (вне работы программы)
import dev_scripts


@bot.command(name='Ping')
async def ping_response(cmd_ctx: cmd.ctx) -> None:
    """
    Отправляет Pong :D

    :param cmd_ctx: Принимает контекст команды
    """
    await cmd_ctx.send('Pong! ₍^⌯ᴖⱅᴖ⌯^₎')


@bot.command(name='Marko')
async def marko_response(cmd_ctx: cmd.ctx) -> None:
    """
    Отправляет Polo (Это же все знают!)

    :param cmd_ctx: Принимает контекст команды
    """
    await cmd_ctx.send('Polo! /ᐠ. ᴗ.ᐟ\\')
