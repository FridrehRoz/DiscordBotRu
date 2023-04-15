"""
Используется для получения информации об объектах
"""

# Встроенные модули
from pprint import pprint
# Основные внешние модули
import typing
# Детальный импорт внешних модулей

# Вспомогательные со программные модули (с сопутствующим кодом)

# Модули отладки (вне работы программы)
import dev_scripts


async def get_info(obj,
                   key: str = 'show') -> typing.Union[typing.NoReturn, str]:
    """Выводит: Тип, атрибуты и словарь объекта

    key - show выводит информацию в консоль
    key - file выводит информацию в файл
    :param obj: передаваемый объект команды 
    :param key: ключ для вывода"""

    match key:
        case 'show':
            print(f'\nЗапрос на получение данных объекта: {obj}\n')

            print(f'Тип объекта: {type(obj)}\n')

            print('Атрибуты объекта:\n')
            pprint(dir(obj))
            print('Словарь реализации объекта:\n')
            pprint(obj.__dict__)

        case 'file':
            result_string = f'Тип объекта: {type(obj)}\n'
            result_string += f'Атрибуты объект:\n{dir(obj)}\n'
            result_string += f'Словарь реализации:\n{obj.__dict__}\n'
            return result_string
