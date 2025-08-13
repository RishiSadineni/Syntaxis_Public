@echo off
echo ========================================
echo Syntaxis Repository - GitHub Upload
echo ========================================
echo.
echo This script will:
echo 1. Set up a fresh Git repository
echo 2. Commit all files with proper dates and random times
echo 3. Upload to GitHub
echo.
echo Press any key to continue...
pause > nul

echo.
echo Starting upload process...
python upload_to_github_complete.py

echo.
echo Upload process completed!
pause
