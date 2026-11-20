@echo off
rem Teleprompter launcher - double-click to start. Needs nothing installed (uses Windows PowerShell).
rem Optional: drag a different script .txt file onto this file.
start "" powershell.exe -NoProfile -ExecutionPolicy Bypass -STA -WindowStyle Hidden -File "%~dp0teleprompter.ps1" %*
