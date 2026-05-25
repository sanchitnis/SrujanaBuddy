@echo off
setlocal

echo SrujanaBuddy - AI Coaching Companion
echo ======================================
cd /d "%~dp0"

:: Check if GitHub Copilot CLI is already available
if %errorlevel% == 0 (
    echo Installing GitHub Copilot CLI via npm...
@echo off
setlocal


echo ======================================
echo.

:: Move to the folder containing this bat file (repo root)
cd /d "%~dp0"

:: Prompt user to login to Google account for authentication
echo Please ensure you are logged in to your Google account in your default browser before continuing.
pause

:: Check if Google Antigravity CLI (agy) is already available
where agy >nul 2>&1
if %errorlevel% == 0 goto :runagy

echo Google Antigravity CLI (agy) not found. Attempting to install...
echo.

:: Try winget to install agy
where winget >nul 2>&1
if %errorlevel% == 0 (
    echo Installing agy via winget...
    winget install --id Google.AntigravityCLI -e --silent
    where agy >nul 2>&1
    if %errorlevel% == 0 (
        echo Installation complete.
        echo.
        goto :runagy
    )
)

echo Please install Google Antigravity CLI (agy) manually and re-run this script.
pause
exit /b 1

:runagy
echo Launching SrujanaBuddy with agy...
:: Continue from previous session if available
agy coach --resume
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

:runagy
echo Launching SrujanaBuddy with agy...
:: Continue from previous session if available, will prompt for Google login if needed
agy --continue
if %errorlevel% neq 0 (
    echo.
    echo If this is your first time, a browser window should open for Google authentication.
    echo If you see an error, please login to your Google account and try again.
    pause
)