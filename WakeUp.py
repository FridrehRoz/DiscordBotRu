# Встроенные модули

# Основные внешние модули
from bot_start import *

# Детальный импорт внешних модулей

# Вспомогательные со программные модули (с сопутствующим кодом)
from events import *
from slash_commands import *
from commands import *

# Модули отладки (вне работы программы)
import dev_scripts

__version__ = 0.1
__author__ = 'NekoMaster'

bot.run(TOKEN)
