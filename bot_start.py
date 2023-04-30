"""
Отвечает за регистрацию свойств клиента бота
"""

__version__ = 1.0

# Встроенные модули
import os

if __name__ != '__main__':
    print(f'\nБот инициализирован {__name__} ver-{__version__}',
          '*' * 30, sep='\n')

# Основные внешние модули
# Детальный импорт внешних модулей
from disnake.ext import commands
from disnake import Intents
# Вспомогательные со программные модули (с сопутствующим кодом)
import _types

# Модули отладки (вне работы программы)
from special_variables.bot_start_variables import is_imported

__all__ = ['bot',
           'TOKEN',
           'GUILD_ID', 'GRAVEYARD_CHANNEL_ID',
           'WELCOME_CHANNEL_ID', 'GOOD_BY_CHANNEL_ID',
           'MASTER_ID',
           'DEFAULT_PATH', 'BOT_EXPRESSION_PATH',]

sync_flags = commands.CommandSyncFlags(
    sync_commands_debug=True
)
# Создание экземпляра бота
bot: _types.Bot = commands.Bot(command_prefix='!',
                               owner_id=int(os.getenv('MASTER_ID')),
                               help_command=None,
                               intents=Intents.all(),
                               command_sync_flags=sync_flags)

TOKEN: str = str(os.getenv('BOT_TOKEN'))
MASTER_ID: int = int(os.getenv('MASTER_ID'))
GUILD_ID: int = int(os.getenv('GUILD_ID'))
WELCOME_CHANNEL_ID: int = int(os.getenv('WELCOME_CHANNEL_ID'))
GOOD_BY_CHANNEL_ID: int = int(os.getenv('GOOD_BY_CHANNEL_ID'))
GRAVEYARD_CHANNEL_ID: int = int(os.getenv('GRAVEYARD_CHANNEL_ID'))
DEFAULT_PATH: str = str(os.getenv('DEFAULT_PATH'))

BOT_EXPRESSION_PATH: str = r"\Material\Expression's"

is_imported()
print('\n')
