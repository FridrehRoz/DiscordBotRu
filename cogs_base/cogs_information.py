"""
Набор когов для получения информация на сервере
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


class InfoCommands(_types.Cog, name='CogInfoCommands'):
    """
    Ког комманд для получения информации
    """

    def __init__(self, _bot: _types.Bot):
        self.bot = _bot

    @commands.slash_command(name='owner',
                            description="Информация об владельце сервера")
    async def owner_response(self,
                             cmd_inter: _types.CmdInter) -> typing.NoReturn:
        """
        Ответ на команду запроса /owner

        :param cmd_inter: объект слэш-команды
        """
        await cmd_inter.response.send_message(
            f'Хозяин этого борделя ฅ^•ﻌ•^ฅ {bot.get_user(MASTER_ID)}\n'
            f'https://github.com/FridrehRoz')

    @commands.slash_command(name='server',
                            description='Отображает информацию о сервере.')
    async def server_response(self,
                              cmd_inter: _types.CmdInter) -> typing.NoReturn:
        """
        Ответ на команду запроса /server

        :param cmd_inter: объект слэш-команды
        """
        await cmd_inter.response.send_message(
            f'Сервер: {cmd_inter.guild.name} ₍^ .ω. ^₎⟆\n'
            f'Участников на сервере: {cmd_inter.guild.member_count}\n'
            f'Хозяин сервера ฅ^•ﻌ•^ฅ: {cmd_inter.guild.owner.name}\n'
            'Github хозяина: https://github.com/FridrehRoz')

    @commands.slash_command(name='user',
                            description='Выводит тег и id пользователя.')
    async def user_response(self,
                            cmd_inter: _types.CmdInter) -> typing.NoReturn:
        """
        Ответ на команду запроса /user

        :param cmd_inter: объект слэш-команды
        """
        await cmd_inter.response.send_message(
            'Ваши данные  /ᐠ=ᆽ=ᐟ \\\n'
            f'Тег: {cmd_inter.user.name + "#" + cmd_inter.user.discriminator}'
            f'\nID: {cmd_inter.user.id}'
        )


def setup(_bot: _types.Bot):
    """
    Регистрация кога в боте

    :param _bot: объект бота
    """
    _bot.add_cog(InfoCommands(_bot))
    print(f'\n{__name__} ver {__version__} загружен!')
    is_imported()
