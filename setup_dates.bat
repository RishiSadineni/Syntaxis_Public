@echo off
echo Setting up repository with specific dates...
echo.
echo This will:
echo - Spanish files (README, translator): September 2024
echo - French files (README, translator): November 2024
echo - All programs: December 2024 - July 2025 (from filenames)
echo.
python setup_dates.py
echo.
echo Done! Now you can push to GitHub.
pause



