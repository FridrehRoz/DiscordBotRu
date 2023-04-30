@echo off

call %~dp0venv\scripts\activate
cd %~dp0

set BOT_TOKEN=
set MASTER_ID=
set GUILD_ID=
set WELCOME_CHANNEL_ID=
set GOOD_BY_CHANNEL_ID=
set GRAVEYARD_CHANNEL_ID=
set DEFAULT_PATH=%~dp0

python WakeUp.py

echo NekoBot Blueberry crash!

pause