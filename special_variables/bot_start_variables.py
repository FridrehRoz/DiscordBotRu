"""
Специальные переменные на этапе старта бота.
"""
# Встроенные модули
from time import sleep
# Основные внешние модули

# Детальный импорт внешних модулей
from tqdm import tqdm

# Вспомогательные со программные модули (с сопутствующим кодом)

# Модули отладки (вне работы программы)

imported_modules_bar = tqdm(total=6)
imported_modules_bar.set_description('Imported packages')


def is_imported():
    """
    Обновляет progress bar импортированных модулей
    """
    if imported_modules_bar.n != imported_modules_bar.total:
        imported_modules_bar.update()
        sleep(1)
    else:
        imported_modules_bar.close()
    print()
