"""
Пакет отвечает за наборы event-ов сервера.
"""

__version__ = 0.3

from checkout_scripts.initialized import is_initialized
from checkout_scripts.pbar import is_imported

from events_res.events_bot import *
from events_res.events_member import *
from events_res.events_command import *

is_initialized(__name__, __version__)
is_imported()
print('\n')
