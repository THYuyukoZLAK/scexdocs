@echo off
setlocal EnableExtensions EnableDelayedExpansion
cd /d "%~dp0" || exit /b 1

set "NGINX_DIR=%~dp0nginx"
set "API_PID_FILE=%~dp0bugreport\server.pid"
set "STOP_FAILED=0"

echo Stopping SCEX DOCS services...

if exist "%NGINX_DIR%\nginx.exe" (
    pushd "%NGINX_DIR%"
    nginx.exe -p . -c conf\nginx.conf -s stop >nul 2>&1
    if errorlevel 1 set "STOP_FAILED=1"
    popd
)

if exist "%API_PID_FILE%" (
    set "API_PID="
    set /p API_PID=<"%API_PID_FILE%"
    if defined API_PID (
        powershell.exe -NoProfile -NonInteractive -Command "Stop-Process -Id !API_PID! -Force -ErrorAction SilentlyContinue" >nul 2>&1
        if errorlevel 1 set "STOP_FAILED=1"
    )
    del /Q "%API_PID_FILE%" >nul 2>&1
)

if not "!STOP_FAILED!"=="0" (
    echo [WARNING] One or more services could not be stopped.
    pause
    exit /b 1
)

echo Stop commands completed.
pause
exit /b 0
