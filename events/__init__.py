"""
Пакет отвечает за наборы event-ов сервера.
"""

__version__ = 0.2

if __name__ != '__main__':
    print(f'\nИнициализация пакета {__name__} ver-{__version__}',
          '*' * 30, sep='\n')

from events import events_bot
from events import events_member
from special_variables.bot_start_variables import is_imported

is_imported()
print('\n')
