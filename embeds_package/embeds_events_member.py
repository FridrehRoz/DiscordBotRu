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
    Отправляет embed для приветственного чата.

    :param member: Объект пользователя
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


async def get_good_by_embed(member: _types.Member) -> _types.Embed:
    """
    Возвращает embed для прощального чата.

    :param member: Объект пользователя
    """
    icon_url: str = member.guild.icon.url

    embed: _types.Embed = Embed(
        title='Сбежавший котик!',
        description=f'Кличка: {member.name}',
        color=0x0000FF
    )

    embed.set_thumbnail(url=icon_url)
    embed.set_image(
        url=r'https://media.tenor.com/zDOUtOWpLmcAAAAC/neko-anime.gif')

    return embed


async def get_ban_embed(guild: _types.Guild,
                        member: _types.Member) -> _types.Embed:
    """
    Возвращает embed для прощального чата в честь Бана.

    :param guild: Объект сервера
    :param member: Объект пользователя
    """
    icon_url: str = member.guild.icon.url

    bans: _types.BanIterator = guild.bans()
    ban_list: list = await bans.get_bans(guild_id=guild.id)

    reason: str = ''
    for ban in ban_list:
        if ban['user']['username'] == member.name and \
                ban['user']['discriminator'] == member.discriminator:
            reason = ban['reason']

    embed: _types.Embed = Embed(
        title='Получен БАН!!!!',
        description=f'{member.name + "#" + member.discriminator}\n'
                    '/ᐠ. ｡.ᐟ\\\ᵐᵉᵒʷˎˊ˗ Он был плохим котиком!\n'
                    f'\nПричина Бана: {reason}',
        color=0xA52A2A
    )

    embed.set_thumbnail(url=icon_url)
    embed.set_image(
        url=r'https://media.tenor.com/9T54Y5KVKyMAAAAM/neko-dancing.gif')

    return embed
