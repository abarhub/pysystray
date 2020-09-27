rem @echo off
rem SET SHORTCUT_NAME="%AllUsersProfile%\desktop\NOTEPAD.url"
rem SET SHORTCUT_NAME=%APPDATA%\desktop\NOTEPAD.url
rem C:\Users\alain\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
SET SHORTCUT_NAME="%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\pysystray.url"
SET CMD_RUN="%CD%\run.bat"
echo SHORTCUT_NAME = %SHORTCUT_NAME%
echo CMD_RUN = %CMD_RUN%
echo [InternetShortcut] > %SHORTCUT_NAME%
echo URL=%CMD_RUN% >> %SHORTCUT_NAME%
echo IconFile=C:\WINDOWS\system32\SHELL32.dll >> %SHORTCUT_NAME%
echo IconIndex=20 >> %SHORTCUT_NAME%
rem more %SHORTCUT_NAME%