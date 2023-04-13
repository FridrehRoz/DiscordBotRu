# Встроенные модули

# Основные внешние модули

# Детальный импорт внешних модулей
from disnake.ext import commands
# Вспомогательные со программные модули (с сопутствующим кодом)
from bot_start import *
from _types import *
# Модули отладки (вне работы программы)
import dev_scripts


@bot.slash_command(name='owner',
                   description="Отправляет информацию об владельце сервера")
async def owner_response(cmd_inter: cmd.CmdInter) -> None:
    await cmd_inter.response.send_message(
        f'Хозяин этого борделя ฅ^•ﻌ•^ฅ {bot.get_user(MASTER_ID)}\n'
        f'https://github.com/FridrehRoz')


@bot.slash_command(name='server',
                   description='Отображает информацию о сервере.')
async def server_response(cmd_inter: cmd.CmdInter) -> None:
    await cmd_inter.response.send_message(
        f'Сервер: {cmd_inter.guild.name} ₍^ .ω. ^₎⟆\n'
        f'Участников на сервере: {cmd_inter.guild.member_count}\n'
        f'Хозяин сервера ฅ^•ﻌ•^ฅ: {cmd_inter.guild.owner.name}\n'
        'Github хозяина: https://github.com/FridrehRoz')
