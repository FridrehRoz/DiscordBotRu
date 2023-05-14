#!venv/scripts python
# -*- coding: utf-8 -*-

"""
Main script
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⢛⠉⢛⠛⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣉⣤⡶⢃⣤⣾⠟⢠⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢛⣩⣤⣶⣶⣂⣬⣭⣬⣭⣀⣶⣤⣭⣙⠛⢿⣿⠟⢉⣴⣾⣿⡟⢠⣿⣿⣋⣠⣤⡌⢹
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢛⠉⢉⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡐⢿⣿⣿⡿⢰⢹⣿⣿⣿⡿⠃⠴⢺
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣋⣥⣶⠟⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣍⠻⠇⣾⣿⣿⣿⣿⣶⣿⠇⢸
⣿⣿⣿⣿⠿⠟⣋⣡⣴⣿⠿⢋⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠙⠻⣿⣿⣿⡿⠋⣰⣿
⠛⢋⣭⣤⣶⣿⣿⣯⣭⣤⠈⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⠟⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⠳⠤⠭⠛⣀⣠⠉⣹
⡆⠘⢿⣿⣿⣿⣿⣿⣿⠃⡞⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣰⣿⣿⣿⣿⣿⣿⣿⣿⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢻⣶⣿⣿⠏⣰⣿
⣿⡀⢈⠻⣿⣿⣿⣿⡏⢈⣴⣿⣿⣿⣿⣿⣿⣿⣿⠟⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣶⣤⠐⣿⣿
⣿⣷⡈⠷⣦⡉⠭⣤⣴⡟⣡⣿⣿⣿⣿⣿⢋⣿⡟⢰⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⠀⢙⠋⣠⣾⣿⣿
⣿⣿⣿⡆⢠⣽⣖⣤⡍⢰⣿⣿⣿⣿⣿⡏⢸⠿⠀⣿⡇⣿⣿⣿⣿⣿⣿⢻⣿⣯⡅⡈⣽⣏⢻⣿⡇⢿⣿⣿⣿⣿⣿⣿⣆⠠⢾⣿⣿⣿⣿
⣿⣿⣿⣷⣤⣍⡉⣿⢁⣿⣿⣿⣿⣿⡟⡇⢈⣔⡇⢹⡇⠹⣿⣿⣿⣿⣿⡌⣿⡿⢀⣧⡘⢿⡆⠻⣿⠘⣿⣿⣿⣿⣿⣿⣿⣷⣦⣍⡛⠛⢹
⣿⣿⣿⣿⣿⣿⣷⡆⣾⡏⣿⣿⣿⣿⡇⡇⢺⣿⣿⣄⠱⠀⡙⠿⣿⣿⣿⠇⢿⠃⠈⠁⠀⠀⠁⠀⡙⠀⣿⣿⣿⣿⣿⣿⣿⡈⣙⣋⣩⣴⣾
⣿⣿⣿⣿⣿⣿⣿⡇⣿⡇⢻⣿⣿⣿⠀⣇⠸⣿⣿⣿⣷⣦⣽⣦⣈⠻⠿⠀⣠⡀⠀⢰⠿⢿⡦⠀⠀⠰⢿⣿⣿⣿⣿⡇⢿⣇⢹⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡇⢿⣿⠀⢿⣿⣿⡇⢈⡀⠉⠉⠙⠲⢝⣿⣿⣿⣿⣦⣿⣿⡇⠠⣶⣂⣀⣲⠄⠀⣠⣿⣿⣿⣿⣿⠇⣾⡏⣸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣄⠻⠘⢀⡙⠻⢿⠈⣿⣿⣷⣶⣤⣄⡙⣿⣿⣿⣿⣿⣿⣟⣀⣛⣛⣛⡭⢀⣼⠟⢡⣿⣿⣿⠟⢰⡿⢡⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠓⣠⣾⣿⣶⡶⡄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡋⢐⣋⠅⠀⣿⣿⡿⢋⠀⢩⣴⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠟⢛⣉⣴⣾⣿⣿⣿⡿⢻⣷⡌⠻⣿⣿⣿⣿⣿⣟⠻⠟⠛⠿⢻⣿⣿⣿⣿⣿⡿⢋⣴⠐⠛⣩⣴⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿
⣿⠟⢉⣥⣶⡾⢹⣿⣿⣿⣿⣿⣿⢡⣿⣿⣿⣷⣬⠉⠻⠿⣿⣿⣷⣶⣶⣾⣿⣿⣿⠿⢛⣡⣴⣿⣿⣿⢿⣿⣿⣿⣇⠈⣿⣿⣿⣿⣿⣿⣿
⡇⣠⣿⣿⠋⢠⣿⣿⣿⣿⣿⣿⢃⣿⣿⣿⣿⠋⠀⠀⠛⢶⣤⡀⢩⣙⣛⣛⣩⡤⠀⣴⣿⣿⣿⣿⣿⣿⡌⣿⣿⣿⣿⣆⠈⠻⢿⣿⡿⢿⣿
⡇⣿⣿⡇⢀⣾⡟⢻⣿⣿⣿⣿⢸⣿⣿⡿⢃⣤⣄⠀⠑⠦⠙⢷⠀⠹⣿⣿⡿⢁⣤⡈⠛⢿⣿⣿⣿⣿⡇⣿⣿⣿⡏⢻⣦⠑⢶⣶⣶⣾⣿
⣧⠘⣿⢰⢸⣿⣇⢸⣿⣿⣿⣿⡄⣿⡿⢰⣿⣿⣿⣧⠀⠀⠀⠈⠂⠀⠙⠛⠃⢸⡿⢀⡇⣀⠹⣿⣿⣿⣷⠘⣿⣿⣿⡌⢻⣷⣄⠹⣿⣿⣿
⣿⣷⡈⠸⠘⢿⣿⡆⠻⣿⣿⣿⣷⠸⡇⣾⣿⣿⣿⣿⣗⠀⠀⠀⠀⠹⡆⠹⠇⡞⠀⠈⢠⠟⠀⢿⣿⣿⣿⠀⣿⣿⣿⣿⠀⡹⣿⣧⡈⢿⣿
⣿⣿⣿⣿⣷⣦⣍⡛⠆⠙⠿⣿⣿⣧⢠⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠁⣴⣷⡈⢻⣿⡿⢠⣿⣿⣿⣿⡆⢳⡈⢿⣷⡈⢿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣶⣤⣬⡉⢸⣿⣿⣿⣿⣿⣿⣿⣿⣆⠑⠀⠀⠀⠀⠀⠀⠂⣼⣿⣿⣿⣆⠙⣡⣾⣿⣿⣿⣿⡇⢸⣿⡌⣿⡇⢸
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⠀⣄⠰⣿⣿⣿⣿⣿⣿⣷⡌⠻⢿⣿⣿⠿⢁⣼⣿⡇⠸⢡⣾
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡅⣸⣿⣆⠹⣿⣿⣿⣿⣿⣿⣿⣶⣶⣦⣴⣶⣿⣿⣿⣃⣴⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⠀⠿⠿⠿⠂⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
@NekoRoom
"""

__version__ = 0.26
__author__ = 'NekoMaster'

# Встроенные модули
import os
import time

# Вывод информации о боте и запуск progressbar-а для импорта модулей
if __name__ == '__main__':
    from art import tprint

    tprint('NekoBotBlueberry')
    tprint(f'ver {__version__} ')
    os.system('title NekoBlueberry')
    print('\n')

# Основные внешние модули
from bot_start import *

# Детальный импорт внешних модулей
from termcolor import colored

# Вспомогательные со программные модули (с сопутствующим кодом)
import _types
import special_bot_scripts
import events_res

# Модули отладки (вне работы программы)
import dev_scripts

# Сбор папок с когами команд бота
cogs_list: list = [cog for cog in os.listdir() if cog.startswith('cogs_')]

# Инициализация когов
for cog in cogs_list:
    try:
        bot.load_extensions(cog)
        time.sleep(1)
    except _types.ExtensionFailed as error:
        print(colored(text='Ошибка регистрации набора Cog-ов!\n',
                      color='red'), error)
    finally:
        print(colored(text=f'Набор Cog-ов {cog} зарегистрирован!\n',
                      color='green'))

try:
    bot.run(TOKEN)
except _types.LoginFailure:
    print(colored(text='Запуск не удался, проверьте действительность токена!',
                  color='red'))
except Exception as error:
    print(colored(text='Ошибка запуска клиента бота!\n',
                  color='red'), error)
