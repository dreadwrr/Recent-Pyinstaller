

@echo off

rem rnt

rem If no arguments were passed, add one for parser note for command line use
if "%~1"=="" (
	"%~dp0main" run
    exit /b
)

rem search

rem If arguments were provided, prepend or call
"%~dp0main" %*
