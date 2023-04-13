from pprint import pprint


async def get_info(command) -> None:
    """Выводит: Тип и словарь объекта,
    а так же информацию касательно значений из дискорд

    :param command: передаваемый объект команды """
    print(f'Запрос на получение данных объекта: {command}\n')

    print(f'Тип объекта: {type(command)}\n')

    print('Атрибуты объекта: ')
    pprint(dir(command))
    try:
        print('Словарь реализации объекта: ')
        pprint(command.__dict__)
    except AttributeError:
        print('Объект не имеет атрибута __doc__.')
