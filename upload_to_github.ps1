Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Syntaxis Repository - GitHub Upload" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "This script will:" -ForegroundColor Yellow
Write-Host "1. Set up a fresh Git repository" -ForegroundColor Yellow
Write-Host "2. Commit all files with proper dates and random times" -ForegroundColor Yellow
Write-Host "3. Upload to GitHub" -ForegroundColor Yellow
Write-Host ""
Write-Host "Press Enter to continue..." -ForegroundColor Green
Read-Host

Write-Host ""
Write-Host "Starting upload process..." -ForegroundColor Green
python upload_to_github_complete.py

Write-Host ""
Write-Host "Upload process completed!" -ForegroundColor Green
Read-Host "Press Enter to continue"


