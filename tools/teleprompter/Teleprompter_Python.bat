@echo off
rem Python version of the teleprompter (only if Python 3 is installed). Teleprompter.bat needs nothing installed.
cd /d "%~dp0"
where pyw >nul 2>nul && (start "" pyw "%~dp0teleprompter.py" %* & exit /b)
where pythonw >nul 2>nul && (start "" pythonw "%~dp0teleprompter.py" %* & exit /b)
where py >nul 2>nul && (start "" py "%~dp0teleprompter.py" %* & exit /b)
where python >nul 2>nul && (start "" python "%~dp0teleprompter.py" %* & exit /b)
echo Python 3 was not found. Use Teleprompter.bat instead - it needs nothing installed.
pause
