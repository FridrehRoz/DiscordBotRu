"""
Пакет отвечает за наборы event-ов сервера.
"""

__version__ = 0.1

if __name__ != '__main__':
    print(f'\nИнициализация пакета {__name__} ver-{__version__}',
          '*' * 30, sep='\n')

from events import events_on
from special_variables.bot_start_variables import is_imported

is_imported()
print('\n')
