"""
Определяет обработчики on_* событий.
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
import dev_scripts


@bot.event
async def on_ready() -> typing.NoReturn:
    """Реагирует на готовность бота к работе."""
    print('Черничка проснулась!')


@bot.event
async def on_member_join(member: _types.Member) -> typing.NoReturn:
    """
    Реагирует на присоединение к серверу нового пользователя.

    :param member: Объект пользователя
    """
    welcome_channel: _types.GuildChannel = bot.get_channel(WELCOME_CHANNEL_ID)
    welcome_channel: _types.TextChannel

    embed: _types.Embed = await embeds_base.get_welcome_embed(member)
    await welcome_channel.send(embed=embed)
