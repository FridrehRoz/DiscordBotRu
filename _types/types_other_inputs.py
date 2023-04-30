"""
Набор иных типов объектов disnake-а
"""

from disnake import Guild  # гильдия
from disnake.member import Member  # участник/пользователь

from disnake.ext.commands import Bot  # клиент бота

from disnake.ext.commands import Cog  # ког, дополнения для бота

from disnake.embeds import Embed  # встраиваемое окно сообщения

from disnake.abc import GuildChannel  # объект канала гильдии
from disnake import TextChannel  # объект текстового канала

from disnake.iterators import BanIterator

from dataclasses import dataclass