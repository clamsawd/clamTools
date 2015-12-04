@echo off

echo Creating desktop shortcut....

set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%.vbs"
echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = "%USERPROFILE%\Desktop\ClamAV.lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%
echo oLink.TargetPath = "%~d0%~p0\clamTools\clamTools.py" >> %SCRIPT%
echo oLink.WorkingDirectory = "%~d0%~p0" >> %SCRIPT%
echo oLink.IconLocation = "%~d0%~p0\icon\clamav.ico" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%
cscript /nologo %SCRIPT%
del %SCRIPT%

copy /Y "%~d0%~p0\regedit\clamTools-console.cmd" "%~d0%~p0"
set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%.vbs"
echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = "%USERPROFILE%\Desktop\ClamAV (tools).lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%
echo oLink.TargetPath = "%~d0%~p0\clamTools-console.cmd" >> %SCRIPT%
echo oLink.WorkingDirectory = "%~d0%~p0" >> %SCRIPT%
echo oLink.IconLocation = "%~d0%~p0\icon\clamav.ico" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%
cscript /nologo %SCRIPT%
del %SCRIPT%
echo Created!

echo Creating registry keys...
if "%~d0%~p0"=="C:\Program Files\clamTools\" (goto create_registry_keys) else (goto no_registry_keys)

:no_registry_keys
echo.
echo Warning: The current directory is different from 'C:\Program Files\clamTools\'
echo Warning: Registry keys aborted!
echo.
goto install_finished

:create_registry_keys
regedit\clamTools.reg
regedit\clamTools-dir.reg
goto install_finished

:install_finished
echo Press ENTER to exit 
pause > nul