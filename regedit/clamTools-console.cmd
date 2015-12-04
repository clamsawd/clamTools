@echo off

SET PATH=%PATH%;"%~d0%~p0\clamTools\
SET PATH=%PATH%;"%~d0%~p0\clamToolsdbd\
SET PATH=%PATH%;"%~d0%~p0\clamToolsd\

echo clamTools - Available commands:
echo.
echo * clamTools.py
echo.
echo * clamToolsdbd.py
echo * clamToolsdbd-log.py
echo.
echo * clamToolsd.py
echo * clamToolsd-config.py
echo * clamToolsd-log.py
echo.
PROMPT $G
CMD /Q /K