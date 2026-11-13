$ErrorActionPreference = 'Stop'
$root = 'E:\Minecarft\.F2_scexdocs'
$log = Join-Path $root 'recovery.log'
function Write-RecoveryLog([string]$message) {
    Add-Content -LiteralPath $log -Encoding UTF8 -Value ("{0} {1}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $message)
}
function ListeningPid([int]$port) {
    $line = netstat -ano -p tcp | Select-String (":$port\s+.*LISTENING") | Select-Object -First 1
    if ($line) { return [int](($line.Line -split '\s+')[-1]) }
    return $null
}
$webPid = ListeningPid 8880
if (-not $webPid) {
    Start-Process -FilePath (Join-Path $root 'nginx\nginx.exe') -ArgumentList @('-p', (Join-Path $root 'nginx\'), '-c', 'conf\nginx.conf') -WorkingDirectory (Join-Path $root 'nginx') -WindowStyle Hidden
    Start-Sleep -Seconds 2
    $webPid = ListeningPid 8880
    if (-not $webPid) { throw 'F2 nginx failed to listen on 8880' }
    Write-RecoveryLog "nginx restored pid=$webPid"
}
$apiPid = ListeningPid 8881
if (-not $apiPid) {
    Start-Process -FilePath 'py.exe' -ArgumentList @('-3', (Join-Path $root 'bugreport\server.py'), '--pid-file', (Join-Path $root 'bugreport\server.pid')) -WorkingDirectory $root -WindowStyle Hidden
    Start-Sleep -Seconds 2
    $apiPid = ListeningPid 8881
    if (-not $apiPid) { throw 'F2 bugreport API failed to listen on 8881' }
    Write-RecoveryLog "bugreport API restored pid=$apiPid"
}
try {
    $response = Invoke-WebRequest -UseBasicParsing 'http://127.0.0.1:8880/' -TimeoutSec 5
    if ($response.StatusCode -ne 200) { throw "unexpected HTTP $($response.StatusCode)" }
} catch {
    Write-RecoveryLog "health check failed: $($_.Exception.Message)"
    throw
}
