@echo off

echo Removing desktop shortcut....
del "%USERPROFILE%\Desktop\ClamAV.lnk"
del "%USERPROFILE%\Desktop\ClamAV (tools).lnk"
del clamTools-console.cmd

echo Removing registry keys...
reg delete HKCR\*\shell\OpenWithClamav /f
reg delete HKCR\Directory\shell\OpenWithClamav /f

echo Removed!
echo Press ENTER to exit 
pause > nul