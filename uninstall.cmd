@echo off

echo Removing desktop shortcut....

del %USERPROFILE%\Desktop\ClamAV.lnk

echo Removed!
echo Press ENTER to exit 
pause > nul