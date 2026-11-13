@echo off
setlocal EnableExtensions
cd /d "%~dp0" || exit /b 1

set "NGINX_DIR=%~dp0nginx"
set "PORT=8880"
set "API_PORT=8881"

echo ============================================
echo   SCEX DOCS startup - Windows
echo ============================================
echo   Project: %~dp0
echo   Web port: %PORT%
echo   API port: %API_PORT%
echo.

if not exist "%NGINX_DIR%\nginx.exe" (
    echo [ERROR] nginx.exe was not found in "%NGINX_DIR%".
    pause
    exit /b 1
)

netstat -ano -p tcp | findstr /R /C:":%PORT% .*LISTENING" >nul 2>&1
if not errorlevel 1 (
    echo [ERROR] Port %PORT% is already in use.
    pause
    exit /b 1
)

netstat -ano -p tcp | findstr /R /C:":%API_PORT% .*LISTENING" >nul 2>&1
if not errorlevel 1 (
    echo [ERROR] Port %API_PORT% is already in use.
    pause
    exit /b 1
)

set "PYTHON_EXE="
set "PYTHON_ARGS="
where.exe py >nul 2>&1
if not errorlevel 1 (
    set "PYTHON_EXE=py"
    set "PYTHON_ARGS=-3"
) else (
    where.exe python >nul 2>&1
    if not errorlevel 1 set "PYTHON_EXE=python"
)

if not defined PYTHON_EXE (
    echo [ERROR] Python 3 was not found in PATH.
    pause
    exit /b 1
)

%PYTHON_EXE% %PYTHON_ARGS% -c "import sys; raise SystemExit(sys.version_info.major != 3)" >nul 2>&1
if errorlevel 1 (
    echo [ERROR] The selected Python interpreter is not Python 3.
    pause
    exit /b 1
)

if exist "%~dp0bugreport\server.pid" del /Q "%~dp0bugreport\server.pid" >nul 2>&1
start "SCEX bug report API" /B %PYTHON_EXE% %PYTHON_ARGS% "%~dp0bugreport\server.py" --pid-file "%~dp0bugreport\server.pid"

pushd "%NGINX_DIR%"
start "SCEX DOCS nginx" /B nginx.exe -p . -c conf\nginx.conf
popd

echo.
echo Services started.
echo Site:       http://localhost:%PORT%/
echo Bug report: http://localhost:%PORT%/bugreport/
echo Run stop-server.bat to stop the services.
pause
exit /b 0
