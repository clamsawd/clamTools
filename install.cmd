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

echo Created!
echo Press ENTER to exit 
pause > nul