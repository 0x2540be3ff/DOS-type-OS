:: it's not a virus.
@echo off
color c
:START
echo This action cannot be undone!
echo(
echo Before factory resetting, make sure the DOS is shut down.
echo(
echo(
set /p var=Are you sure you want to reset DOS to factory settings?[y/N]: 
if %var%== Y goto DELETE
if %var%== y goto DELETE
if %var%== N exit
if %var%== n exit
if not %var%== N goto OR_LO

:OR_LO
if not %var%== y goto INVALID_INT
if not %var%== Y goto INVALID_INT

:INVALID_INT
echo Not an option.
echo(
goto START


:DELETE
echo(
cd sys_files
echo Deleting files...
del users.txt /f /q
del *.u5r /f /q
goto CREATE_USER

:CREATE_USER
echo Creating guest user...
echo guest>guest.u5r
echo 1234>>guest.u5r
break>>guest.u5r
echo Resetting the user directory...
echo root>users.txt
echo guest>>users.txt
goto EXT_BAT


:EXT_BAT
echo(
echo Done!
pause
