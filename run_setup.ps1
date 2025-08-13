Write-Host "Setting up repository with correct dates..." -ForegroundColor Green

# Kill any existing git processes
Get-Process -Name "git" -ErrorAction SilentlyContinue | Stop-Process -Force

Write-Host "Resetting repository..." -ForegroundColor Yellow
git reset --hard --empty

Write-Host "Running setup script..." -ForegroundColor Yellow
python setup_dates.py

Write-Host "Adding remote origin..." -ForegroundColor Yellow
git remote add origin https://github.com/RishiSadineni/Syntaxis_Public.git

Write-Host "Pushing to GitHub..." -ForegroundColor Yellow
git push -u origin master

Write-Host "Done! Check your repository at: https://github.com/RishiSadineni/Syntaxis_Public.git" -ForegroundColor Green
Read-Host "Press Enter to continue"



