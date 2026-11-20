@echo off
rem Teleprompter launcher: double-click to start. Optional: drag a different script .txt onto this file.
cd /d "%~dp0"
where pyw >nul 2>nul && (start "" pyw "%~dp0teleprompter.py" %* & exit /b)
where pythonw >nul 2>nul && (start "" pythonw "%~dp0teleprompter.py" %* & exit /b)
where py >nul 2>nul && (start "" py "%~dp0teleprompter.py" %* & exit /b)
where python >nul 2>nul && (start "" python "%~dp0teleprompter.py" %* & exit /b)
echo Python 3 was not found.
echo Install it from https://www.python.org/downloads/ and tick "Add python.exe to PATH", then run this again.
pause
