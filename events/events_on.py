# Встроенные модули

# Основные внешние модули

# Детальный импорт внешних модулей

# Вспомогательные со программные модули (с сопутствующим кодом)
from bot_start import *
from _types import *
from embed_package import *
# Модули отладки (вне работы программы)
import dev_scripts


@bot.event
async def on_ready():
    print('Черничка проснулась!')


@bot.event
async def on_member_join(member: other_inputs.Member) -> None:
    """
    Реагирует на присоединение к серверу нового пользователя.

    :param member: Пользователь
    """
    welcome_channel = bot.get_channel(WELCOME_CHANNEL_ID)

    embed = await embed_welcome.get_embed(member)
    await welcome_channel.send(embed=embed)
