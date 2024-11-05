@echo off
set URL=http://localhost:8081

:: Make a request to the website and check for "Welcome"
curl -s %URL% | findstr /I "Welcome" >nul
if %errorlevel% equ 0 (
    echo Homepage test passed.
    exit /b 0
) else (
    echo Homepage test failed.
    exit /b 1
)
