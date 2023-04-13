# Встроенные модули
import os
# Основные внешние модули
# Детальный импорт внешних модулей
from disnake.ext import commands
from disnake import Intents

# Вспомогательные со программные модули (с сопутствующим кодом)
# Модули отладки (вне работы программы)

__all__ = ['bot',
           'TOKEN',
           'GUILD_ID', 'WELCOME_CHANNEL_ID',
           'MASTER_ID']

# Создание экземпляра бота
bot = commands.Bot(command_prefix='!',
                   owner_id=int(os.getenv('MASTER_ID')),
                   test_guilds=[int(os.getenv('GUILD_ID'))],
                   help_command=None,
                   intents=Intents.all())

TOKEN: str = str(os.getenv('BOT_TOKEN'))
MASTER_ID: int = int(os.getenv('MASTER_ID'))
GUILD_ID: int = int(os.getenv('GUILD_ID'))
WELCOME_CHANNEL_ID: int = int(os.getenv('WELCOME_CHANNEL'))
