@echo off

set PYTHONUNBUFFERED="1"
set "CMD_LINE=%~f0"
rem If no arguments were passed, add one for parser note for command line use
rem 300 seconds are used as no args means 5 minutes
if "%~1"=="" (
    "%~dp0main" 300
    exit /b
)

rem search

rem If arguments were provided, prepend or call
"%~dp0main" %*