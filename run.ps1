param([string]$wd="")

Write-Output "Sleeping"
Start-Sleep -Seconds 30.0
Write-Output "Done Sleep"
Set-Location $wd
.\.venv\Scripts\Activate.ps1
Write-Output "Init virtual enviroment"
python .\proxy_notif_bot.py