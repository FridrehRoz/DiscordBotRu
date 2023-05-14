"""
Визуализация инициализаций в коде
"""

# Встроенные модули

# Основные внешние модули
import typing

# Детальный импорт внешних модулей
from termcolor import colored

# Вспомогательные со программные модули (с сопутствующим кодом)

# Модули отладки (вне работы программы)
import dev_scripts

__all__ = ['is_initialized', 'is_reg']


def is_initialized(module_name: str, module_ver: float) -> typing.NoReturn:
    """
    Используется при инициализации модуля/пакета

    :param module_name: имя модуля
    :param module_ver: версия модуля
    """

    print(colored(text=f'\nИнициализирован {module_name} ver-{module_ver}',
                  color='green'))
    print('*' * 30, sep='\n')


def is_reg(cog_name: str, cog_ver: float) -> typing.NoReturn:
    """
    Используется при регистрации кога

    :param cog_name: название кога
    :param cog_ver: версия кога
    """

    print(colored(
        text=f'\n{cog_name[cog_name.index(".")+1:]} ver {cog_ver} загружен!',
        color='yellow'))
