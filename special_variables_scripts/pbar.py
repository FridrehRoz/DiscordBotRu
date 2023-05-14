"""
Progress bar для запуска бота
"""

# Встроенные модули
from time import sleep

# Основные внешние модули
import typing

# Детальный импорт внешних модулей
from tqdm import tqdm

# Вспомогательные со программные модули (с сопутствующим кодом)

# Модули отладки (вне работы программы)
import dev_scripts

__all__ = ['import_pbar',
           'is_imported']

import_pbar = tqdm(total=7,
                   desc='Imported packages',
                   colour='#004f84')


def is_imported() -> typing.NoReturn:
    """
    Обновляет progress bar импортированных модулей
    """
    if import_pbar.n != import_pbar.total:
        import_pbar.update()
        sleep(1)
    else:
        import_pbar.close()
    print()
