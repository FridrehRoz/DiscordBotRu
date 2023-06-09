"""
Набор когов для команд бота в интересах разработчика
"""

__version__ = 1.0

# Встроенные модули

# Основные внешние модули
import typing

# Детальный импорт внешних модулей
from disnake.ext import commands

# Вспомогательные со программные модули (с сопутствующим кодом)
from bot_start import *
import _types

# Модули отладки (вне работы программы)
import dev_scripts


class CommandObject:
    """
    Отвечает за обрабатываемую команду в когах
    """

    def __init__(self, name: str):
        self.name = name
        self.command_obj: typing.Union[_types.Cmd, None] = None

    async def set_command_obj(self):
        """Делает асинхронный запрос для получения объекта команды"""
        self.command_obj = await dev_scripts.get_command.request_cmd(self.name)


class DevInfoCommands(_types.Cog,
                      name='CogDevInfoCommands'):
    """
    Набор команд для получения информации разработчику
    """

    def __init__(self, _bot: _types.Bot):
        self.bot = _bot

    @commands.has_any_role(1095625852735213608, 1095630062528766053)
    @commands.slash_command(
        name='help',
        description='При имении docstring у запрашиваемой '
                    'команды отправляет её.')
    async def help_response(self,
                            cmd_inter: _types.CmdInter,
                            cmd_name: str = commands.Param(
                                description='команда')) -> typing.NoReturn:
        """
        Обработчик команды help

        :param cmd_inter: объект сообщения
        :param cmd_name: название команды для запроса help
        """
        command: CommandObject = CommandObject(cmd_name.strip().lower())
        await command.set_command_obj()

        if command.command_obj is None:
            await cmd_inter.send(f'Команды {cmd_name} нет!')
        else:
            if command.command_obj.help is None:
                await cmd_inter.send(
                    'Документация отсутствует!')
            else:
                await cmd_inter.send(command.command_obj.help)

    @commands.has_any_role(1095625852735213608, 1095630062528766053)
    @commands.slash_command(name='request_info',
                            description='Даёт информацию не лезь!')
    async def request_info_response(
            self,
            cmd_inter: _types.CmdInter,
            key: str = commands.Param(
                description='ключ вывода file/console')) -> typing.NoReturn:
        """
        Обработчик для команды request_info

        Разработчик сам вводит что ему требуется
        :param cmd_inter: объект команды
        :param key: file/console
        """
        import pprint

        match key:
            case 'file':
                with open('request_info.txt', 'w') as file:
                    file.write(pprint.pformat(None))
            case 'console':
                print(None)

        await cmd_inter.send('Ответ на запрос был получен!')


def setup(_bot: _types.Bot) -> typing.NoReturn:
    """
    Регистрация кога в боте

    :param _bot: объект бота
    """
    from checkout_scripts.initialized import is_reg
    from checkout_scripts.pbar import is_imported

    _bot.add_cog(DevInfoCommands(_bot))
    is_reg(__name__, __version__)
    is_imported()
