param(
    [switch]$SkipInstall
)

$ErrorActionPreference = "Stop"

function Write-Step {
    param([string]$Message)
    Write-Host "`n==> $Message" -ForegroundColor Cyan
}

function Assert-Preflight {
    if ($PSVersionTable.PSVersion.Major -lt 6) {
        throw "PowerShell 6 or higher is required to run this bootstrap script."
    }
}

function Test-CommandAvailable {
    param([string]$CommandName)
    return [bool](Get-Command $CommandName -ErrorAction SilentlyContinue)
}

function Refresh-Path {
    $machinePath = [Environment]::GetEnvironmentVariable("Path", "Machine")
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    $paths = @($machinePath, $userPath) | Where-Object { $_ }
    $env:Path = $paths -join ";"
}

function Ensure-CopilotCli {
    if (Test-CommandAvailable "copilot") {
        Write-Host "GitHub Copilot CLI is already available."
        return
    }

    if ($SkipInstall) {
        throw "GitHub Copilot CLI is missing. Re-run without -SkipInstall to install it."
    }

    Write-Step "Installing GitHub Copilot CLI"

    if (Test-CommandAvailable "winget") {
        winget install --id GitHub.Copilot -e --accept-package-agreements --accept-source-agreements --silent
    }
    elseif (Test-CommandAvailable "npm") {
        npm install -g @github/copilot
    }
    else {
        throw "Neither winget nor npm was found. Install one of them, then run this script again."
    }

    Refresh-Path

    if (-not (Test-CommandAvailable "copilot")) {
        throw "Copilot installed, but the command is still unavailable on PATH. Open a new terminal and try again."
    }
}

function Get-StartupPrompt {
    param([string]$SkillPath)

    $skillText = Get-Content -Raw -Path $SkillPath
    if ($skillText.Length -le 12000) {
        return @"
You are in the SrujanaBuddy repository.

Use the following SKILL.md content as the master orchestration file:

---
$skillText
---

Begin by identifying yourself according to SKILL.md and ask what the user needs most right now.
"@
    }

    return @"
You are in the SrujanaBuddy repository.

Open and use SKILL.md in the current folder as the master orchestration file.
Follow its identity and first-response rules, then ask the user what they need most right now.
"@
}

Assert-Preflight

Write-Step "Preparing SrujanaBuddy core coaching setup"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$skillPath = Join-Path $repoRoot "SKILL.md"

if (-not (Test-Path $skillPath)) {
    throw "SKILL.md was not found next to this script. Run the script from the extracted release folder."
}

Ensure-CopilotCli

Write-Step "Launching GitHub Copilot CLI"
Set-Location $repoRoot

$startupPrompt = Get-StartupPrompt -SkillPath $skillPath

try {
    & copilot -p $startupPrompt
}
catch {
    Write-Warning "Programmatic launch failed. Starting interactive Copilot CLI instead."
    & copilot
}
