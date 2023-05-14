"""
Набор типов для объектов команд, получаемых обработчиками
"""

from disnake.ext.commands import Context as Ctx  # инфо контекста

from disnake.interactions.application_command import \
    ApplicationCommandInteraction as CmdInter  # инфо взаимодействия

from disnake.ext.commands import errors as CmdError  # исключение команды

from disnake.interactions.base import \
    InteractionResponse as InterResponse # ответ на взаимодействие

from disnake.ext.commands.core import Command as Cmd  # команда бота
