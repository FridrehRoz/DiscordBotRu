"""
Набор типов ошибок при работе бота
"""

from disnake.ext.commands.errors import \
    MissingAnyRole  # недостаточно прав/нет роли

from disnake.ext.commands.errors import \
    ExtensionFailed  # ошибка регистрации набора когов

from disnake.errors import LoginFailure  # ошибка доступа бота по токену
