"""
Main script
@NekoRoom
"""

__version__ = 0.2
__author__ = 'NekoMaster'

# Встроенные модули
import os
import time

if __name__ == '__main__':
    from art import tprint

    tprint('NekoBotBlueberry')
    tprint(f'ver {__version__} ')
    os.system('title NekoBlueberry')
    from special_variables.bot_start_variables import \
        imported_modules_bar

    print('\n')

# Основные внешние модули
from bot_start import *

# Детальный импорт внешних модулей

# Вспомогательные со программные модули (с сопутствующим кодом)
from events import *
import _types

# Модули отладки (вне работы программы)
import dev_scripts

cogs_list: list = [cog for cog in os.listdir() if cog.startswith('cogs_')]

for cog in cogs_list:
    try:
        bot.load_extensions(cog)
        time.sleep(1)
    except _types.ExtensionFailed as error:
        print('Ошибка регистрации набора Cog-ов!\n', error)
    finally:
        print(f'Набор Cog-ов {cog} зарегистрирован!\n')

try:
    bot.run(TOKEN)
except _types.LoginFailure:
    print('Запуск не удался, проверьте действительность токена!')
except Exception as error:
    print('Ошибка запуска клиента бота!\n', error)
