@echo off
setlocal

echo SrujanaBuddy - AI Coaching Companion
echo ======================================
echo.

:: Move to the folder containing this bat file (repo root)
cd /d "%~dp0"

:: Check if GitHub Copilot CLI is already available
where copilot >nul 2>&1
if %errorlevel% == 0 goto :run

echo GitHub Copilot CLI not found. Attempting to install...
echo.

:: Try npm install (most direct path to 'copilot' binary)
where npm >nul 2>&1
if %errorlevel% == 0 (
    echo Installing GitHub Copilot CLI via npm...
    npm install -g @githubnext/github-copilot-cli
    where copilot >nul 2>&1
    if %errorlevel% == 0 (
        echo Installation complete.
        echo.
        goto :run
    )
)

:: Try winget to install GitHub CLI, then add the copilot extension
where winget >nul 2>&1
if %errorlevel% == 0 (
    echo Installing GitHub CLI via winget...
    winget install --id GitHub.cli -e --silent
    where gh >nul 2>&1
    if %errorlevel% == 0 (
        echo Installing GitHub Copilot extension for GitHub CLI...
        gh extension install github/gh-copilot
    )
)

:: Final availability check
where copilot >nul 2>&1
if %errorlevel% == 0 goto :run

echo.
echo Could not automatically install GitHub Copilot CLI.
echo Please install it manually using one of these options:
echo.
echo   Option 1 (npm):    npm install -g @githubnext/github-copilot-cli
echo   Option 2 (gh CLI): winget install GitHub.cli
echo                      gh extension install github/gh-copilot
echo.
echo After installation, re-run this file.
pause
exit /b 1

:run
echo Launching SrujanaBuddy...
echo.
powershell -NoExit -Command "copilot --silent --model claude-sonnet-4.6"