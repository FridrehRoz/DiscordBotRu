"""
Набор базовых/общих embed-ов
"""

# Встроенные модули

# Основные внешние модули

# Детальный импорт внешних модулей
from disnake import Embed
# Вспомогательные со программные модули (с сопутствующим кодом)
import _types
# Модули отладки (вне работы программы)
import dev_scripts

__all__ = ['get_welcome_embed']


async def get_welcome_embed(member: _types.Member) -> _types.Embed:
    """
    Отправляет embed в приветственный чат.

    :param member:
    """
    from datetime import datetime

    icon_url: str = member.guild.icon.url

    embed: _types.Embed = Embed(
        title='Новый котик!',
        description=f'Кличка: {member.name}\n'
                    f'Позывной: {member.discriminator}\n'
                    f'Проскользнул {datetime.now():%d.%m.%Y %H:%M}',
        color=0xbf19a4
    )

    embed.set_author(
        name='MasterNeko',
        url='https://github.com/FridrehRoz',
        icon_url='https://avatars.githubusercontent.com/u/130528675?v=4'
    )

    embed.set_thumbnail(url=member.avatar.url)
    embed.set_image(url=icon_url)

    return embed
