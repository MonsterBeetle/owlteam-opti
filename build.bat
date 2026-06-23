@echo off
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Building EXE...
python build.py
echo.
echo Build complete! Check dist/ folder for OwlTeam-Opti.exe
pause
