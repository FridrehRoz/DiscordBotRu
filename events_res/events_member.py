"""
Определяет обработчики on_* событий для участников сервера.
"""

# Встроенные модули

# Основные внешние модули
import typing

import disnake

# Детальный импорт внешних модулей

# Вспомогательные со программные модули (с сопутствующим кодом)
from bot_start import *
import _types
from embeds_res import embeds_events_member as embeds

# Модули отладки (вне работы программы)
import dev_scripts

__all__ = ['on_member_join', 'on_member_remove', 'on_member_ban']


@bot.event
async def on_member_join(member: _types.Member) -> typing.NoReturn:
    """
    Реагирует на присоединение к серверу нового пользователя.

    :param member: Объект пользователя
    """
    welcome_channel: _types.GuildChannel = bot.get_channel(WELCOME_CHANNEL_ID)
    welcome_channel: _types.TextChannel

    embed: _types.Embed = await embeds.get_welcome_embed(member)
    await welcome_channel.send(embed=embed)


@bot.event
async def on_member_ban(guild: _types.Guild,
                        member: _types.Member) -> typing.NoReturn:
    """
    Реагирует на Бан пользователя сервера.

    :param guild: Объект гильдии
    :param member: Объект пользователя
    """
    ban_channel: _types.GuildChannel = bot.get_channel(
        GRAVEYARD_CHANNEL_ID)
    ban_channel: _types.TextChannel

    embed: _types.Embed = await embeds.get_ban_embed(guild, member)
    await ban_channel.send(embed=embed)


@bot.event
async def on_member_remove(member: _types.Member) -> typing.NoReturn:
    """
    Реагирует на выход участника с сервера.

    :param member: Объект пользователя
    """
    # Проверка Бана
    async for entry in member.guild.audit_logs(
            limit=1,
            action=disnake.AuditLogAction.ban):
        if entry.target == member:
            # Пользователь забанен, мы с ним не прощаемся.
            return

    good_by_channel: _types.GuildChannel = bot.get_channel(
        GOOD_BY_CHANNEL_ID)
    good_by_channel: _types.TextChannel

    embed: _types.Embed = await embeds.get_good_by_embed(member)
    await good_by_channel.send(embed=embed)
