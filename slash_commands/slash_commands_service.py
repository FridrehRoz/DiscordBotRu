# Встроенные модули

# Основные внешние модули

# Детальный импорт внешних модулей
from disnake.ext import commands
# Вспомогательные со программные модули (с сопутствующим кодом)
from bot_start import *
from _types import *
# Модули отладки (вне работы программы)
import dev_scripts


@commands.has_any_role(1095625852735213608, 1095630062528766053)
@bot.slash_command(
    name='help',
    description='При имении docstring у запрашиваемой команды отправляет её.')
async def help_response(cmd_inter: cmd.CmdInter,
                        cmd_name: str = 'команда') -> None:
    command: commands.core.Command = bot.get_command(cmd_name.capitalize())
    if command is None:
        await cmd_inter.response.send_message(
            f'Команды {cmd_name.capitalize()} нет!')
    else:
        doc_response = 'Документации нет.' if command.help is None else \
            command.help

        await cmd_inter.response.send_message(doc_response)


@help_response.error
async def help_error(cmd_inter: cmd.CmdInter, error: errors.MissingAnyRole):
    await cmd_inter.response.send_message(
        'Проходи мимо котик, у тебя недостаточно прав! /ᐠᵕ ‸ᵕᐟ\\ﾉ')
