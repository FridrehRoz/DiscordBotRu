"""
Набор когов для команд бота для разработчика
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
from special_variables.bot_start_variables import is_imported


class CommandObject:
    """
    Отвечает за обрабатываемую команду в когах
    """

    def __init__(self, name):
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
        command: CommandObject = CommandObject(cmd_name)
        await command.set_command_obj()

        if command.command_obj is None:
            await cmd_inter.response.send_message(f'Команды {cmd_name} нет!')
        else:
            if command.command_obj.help is None:
                await cmd_inter.response.send_message(
                    'Документация отсутствует!')
            else:
                await cmd_inter.response.send_message(command.command_obj.help)

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
                    file.write(pprint.pformat(
                        await dev_scripts.get_object_data.get_info(cmd_inter)))
            case 'console':
                await dev_scripts.get_object_data.get_info(cmd_inter)

        await cmd_inter.response.send_message('Ответ на запрос был получен!')

    @help_response.error
    async def help_error(self,
                         cmd_inter: _types.CmdInter,
                         error: _types.MissingAnyRole) -> typing.NoReturn:
        """
        Обработчик ошибки команды help.

        Некорректная роль вызывающего команду

        :param cmd_inter: объект команды
        :param error: объект ошибки
        """
        await cmd_inter.response.send_message(
            'Проходи мимо котик, у тебя недостаточно прав! /ᐠᵕ ‸ᵕᐟ\\ﾉ')


def setup(_bot: _types.Bot) -> typing.NoReturn:
    """
    Регистрация кога в боте

    :param _bot: объект бота
    """
    _bot.add_cog(DevInfoCommands(_bot))
    print(f'\n{__name__} ver {__version__} загружен!')
    is_imported()
