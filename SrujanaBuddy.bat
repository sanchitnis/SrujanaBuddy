@echo off
setlocal enabledelayedexpansion

set "CURRENT_VERSION=V0.1.6"

echo SrujanaBuddy - AI Mentoring Companion (%CURRENT_VERSION%)
echo ==================================================

:: Move to the folder containing this bat file (repo root)
cd /d "%~dp0"

:: Check for updates from GitHub Releases
echo Checking for updates...
set "LATEST_VERSION="
for /f "tokens=2 delims= " %%A in ('curl.exe -sI https://github.com/sanchitnis/SrujanaBuddy/releases/latest ^| findstr "Location:"') do (
    set "URL_LINE=%%A"
)
if defined URL_LINE (
    set "URL_LINE=!URL_LINE:/= !"
    for %%B in (!URL_LINE!) do set "LATEST_VERSION=%%B"
    for /f "delims=" %%C in ("!LATEST_VERSION!") do set "LATEST_VERSION=%%C"
)

if defined LATEST_VERSION (
    if not "!LATEST_VERSION!" == "%CURRENT_VERSION%" (
        echo.
        echo ====================================================
        echo A new version of SrujanaBuddy is available!
        echo Current Version: %CURRENT_VERSION%
        echo Latest Version:  !LATEST_VERSION!
        echo ====================================================
        echo.
        set /p "UPDATE_CHOICE=Would you like to automatically download and install the update? (Y/N): "
        if /i "!UPDATE_CHOICE!" == "Y" (
            goto :do_update
        )
    )
)

goto :check_agy

:do_update
echo.
echo Downloading and preparing update (!LATEST_VERSION!)...
powershell -Command "Invoke-WebRequest -Uri 'https://github.com/sanchitnis/SrujanaBuddy/archive/refs/tags/!LATEST_VERSION!.zip' -OutFile '%temp%\update.zip'"
if %errorlevel% neq 0 (
    echo Failed to download the update. Continuing with current version...
    pause
    goto :check_agy
)

echo Extracting update files...
powershell -Command "Expand-Archive -Path '%temp%\update.zip' -DestinationPath '%temp%\SrujanaBuddyUpdate' -Force"
if %errorlevel% neq 0 (
    echo Failed to extract the update. Continuing with current version...
    pause
    goto :check_agy
)

echo Installing update and restarting SrujanaBuddy...
(
echo @echo off
echo timeout /t 2 /nobreak ^>nul
echo xcopy /s /y /e "%temp%\SrujanaBuddyUpdate\SrujanaBuddy-*\*" "%~dp0"
echo rd /s /q "%temp%\SrujanaBuddyUpdate"
echo del "%temp%\update.zip"
echo start "" /d "%~dp0" SrujanaBuddy.bat
echo del "%%~f0"
) > "%temp%\srujana_updater.bat"

start "" "%temp%\srujana_updater.bat"
exit /b 0

:check_agy
:: Prompt user to login to Google account for authentication
echo Please ensure you are logged in to your Google account in your default browser before continuing.
pause

:: Check if Google Antigravity CLI (agy) is already available
where agy >nul 2>&1
if %errorlevel% == 0 goto :runagy

:: Check if agy exists in default installation paths
if exist "%LOCALAPPDATA%\Antigravity\agy.exe" (
    set "PATH=%PATH%;%LOCALAPPDATA%\Antigravity"
    goto :runagy
)
if exist "%USERPROFILE%\.local\bin\agy.exe" (
    set "PATH=%PATH%;%USERPROFILE%\.local\bin"
    goto :runagy
)

echo Google Antigravity CLI (agy) not found. Attempting to install...
echo.

:: Try official installation script via curl
where curl >nul 2>&1
if %errorlevel% == 0 (
    echo Installing agy via official installation script...
    curl -fsSL https://antigravity.google/cli/install.cmd -o "%temp%\install.cmd"
    if %errorlevel% == 0 (
        call "%temp%\install.cmd"
        del "%temp%\install.cmd"
        
        :: Re-check after installation
        where agy >nul 2>&1
        if %errorlevel% == 0 goto :runagy
        
        if exist "%LOCALAPPDATA%\Antigravity\agy.exe" (
            set "PATH=%PATH%;%LOCALAPPDATA%\Antigravity"
            goto :runagy
        )
        if exist "%USERPROFILE%\.local\bin\agy.exe" (
            set "PATH=%PATH%;%USERPROFILE%\.local\bin"
            goto :runagy
        )
    )
)

:: Try winget as fallback
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
    if exist "%LOCALAPPDATA%\Antigravity\agy.exe" (
        set "PATH=%PATH%;%LOCALAPPDATA%\Antigravity"
        goto :runagy
    )
)

echo.
echo Please install Google Antigravity CLI (agy) manually and re-run this script.
echo Run this in PowerShell: irm https://antigravity.google/cli/install.ps1 ^| iex
echo.
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