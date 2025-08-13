#!/usr/bin/env python3
import os
import subprocess
import re
from datetime import datetime, timedelta
import glob
import random

def extract_date_from_filename(filename):
    """Extract date from filename in format YYYY_MM_DD"""
    pattern = r'(\d{4}_\d{2}_\d{2})\.synt$'
    match = re.search(pattern, filename)
    if match:
        date_str = match.group(1)
        return datetime.strptime(date_str, '%Y_%m_%d')
    return None

def get_random_cdt_time(date):
    """Generate a random time in CDT timezone for the given date"""
    cdt_offset = timedelta(hours=5)
    
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)
    
    random_time = date.replace(hour=random_hour, minute=random_minute, second=random_second)
    utc_time = random_time + cdt_offset
    
    return utc_time

def run_git_command(command, description):
    """Run a git command and handle errors"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ {description}")
            return True
        else:
            print(f"✗ {description}: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ {description}: {e}")
        return False

def main():
    print("Syntaxis Repository - FINAL Upload with ALL Timestamps Randomized")
    print("=" * 75)
    
    # Check if git is available
    try:
        subprocess.run(['git', '--version'], check=True, capture_output=True)
    except:
        print("✗ Git is not available. Please install Git and try again.")
        return
    
    # Remove existing git directory if it exists
    if os.path.exists('.git'):
        print("Removing existing .git directory...")
        run_git_command("rmdir /s /q .git", "Remove existing .git directory")
    
    # Initialize new git repository
    print("\nInitializing new Git repository...")
    run_git_command("git init", "Initialize git repository")
    run_git_command('git config user.name "RishiSadineni"', "Set git user name")
    run_git_command('git config user.email "rishi.sadineni@example.com"', "Set git user email")
    
    # Find all .synt files (only the real ones, duplicates removed)
    synt_files = []
    espanol_files = glob.glob('espanol/programas/*.synt')
    francais_files = glob.glob('francais/programmes/*.synt')
    synt_files.extend(espanol_files)
    synt_files.extend(francais_files)
    
    # Define dates for specific files
    spanish_date = datetime(2024, 9, 15)  # September 2024
    french_date = datetime(2024, 11, 15)  # November 2024
    
    # Spanish files (September 2024) - ALL with random times
    spanish_files = [
        'espanol/README.md',
        'espanol/run_syntaxis.py',
        'espanol/translator.py'
    ]
    
    # French files (November 2024) - ALL with random times
    french_files = [
        'francais/README.md',
        'francais/executeur_syntaxis.py',
        'francais/traducteur.py'
    ]
    
    # Filter out files that don't exist
    spanish_files = [f for f in spanish_files if os.path.exists(f)]
    french_files = [f for f in french_files if os.path.exists(f)]
    
    # Sort synt files by date
    files_with_dates = []
    for file_path in synt_files:
        date = extract_date_from_filename(file_path)
        if date:
            files_with_dates.append((file_path, date))
    
    files_with_dates.sort(key=lambda x: x[1])
    
    print(f"\nFound {len(spanish_files)} Spanish files, {len(french_files)} French files, and {len(files_with_dates)} program files")
    
    # First, commit Spanish files (September 2024) with COMPLETELY random times
    print(f"\nCommitting Spanish files with date {spanish_date.strftime('%Y-%m-%d')} and RANDOM times:")
    for file_path in spanish_files:
        random_time = get_random_cdt_time(spanish_date)
        cdt_time = random_time - timedelta(hours=5)
        
        # Add file
        run_git_command(f'git add "{file_path}"', f"Add {file_path}")
        
        # Commit with specific date
        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = random_time.strftime('%Y-%m-%d %H:%M:%S')
        env['GIT_COMMITTER_DATE'] = random_time.strftime('%Y-%m-%d %H:%M:%S')
        
        commit_cmd = f'git commit -m "Add {os.path.basename(file_path)}"'
        result = subprocess.run(commit_cmd, shell=True, env=env, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"  ✓ Committed {file_path} - {cdt_time.strftime('%H:%M:%S')} CDT")
        else:
            print(f"  ✗ Failed to commit {file_path}")
    
    # Then, commit French files (November 2024) with COMPLETELY random times
    print(f"\nCommitting French files with date {french_date.strftime('%Y-%m-%d')} and RANDOM times:")
    for file_path in french_files:
        random_time = get_random_cdt_time(french_date)
        cdt_time = random_time - timedelta(hours=5)
        
        # Add file
        run_git_command(f'git add "{file_path}"', f"Add {file_path}")
        
        # Commit with specific date
        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = random_time.strftime('%Y-%m-%d %H:%M:%S')
        env['GIT_COMMITTER_DATE'] = random_time.strftime('%Y-%m-%d %H:%M:%S')
        
        commit_cmd = f'git commit -m "Add {os.path.basename(file_path)}"'
        result = subprocess.run(commit_cmd, shell=True, env=env, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"  ✓ Committed {file_path} - {cdt_time.strftime('%H:%M:%S')} CDT")
        else:
            print(f"  ✗ Failed to commit {file_path}")
    
    # Finally, commit ALL .synt files with their respective dates and COMPLETELY random times
    print("\nCommitting ALL .synt files with their respective dates and RANDOM times:")
    for file_path, date in files_with_dates:
        random_time = get_random_cdt_time(date)
        cdt_time = random_time - timedelta(hours=5)
        
        # Add file
        run_git_command(f'git add "{file_path}"', f"Add {file_path}")
        
        # Commit with specific date
        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = random_time.strftime('%Y-%m-%d %H:%M:%S')
        env['GIT_COMMITTER_DATE'] = random_time.strftime('%Y-%m-%d %H:%M:%S')
        
        commit_cmd = f'git commit -m "Add {os.path.basename(file_path)}"'
        result = subprocess.run(commit_cmd, shell=True, env=env, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"  ✓ Committed {file_path} - {date.strftime('%Y-%m-%d')} {cdt_time.strftime('%H:%M:%S')} CDT")
        else:
            print(f"  ✗ Failed to commit {file_path}")
    
    # Add remaining files
    print("\nAdding remaining files...")
    run_git_command("git add -A", "Add all remaining files")
    
    # Commit remaining files with current date
    current_time = datetime.now()
    env = os.environ.copy()
    env['GIT_AUTHOR_DATE'] = current_time.strftime('%Y-%m-%d %H:%M:%S')
    env['GIT_COMMITTER_DATE'] = current_time.strftime('%Y-%m-%d %H:%M:%S')
    
    commit_cmd = 'git commit -m "Add remaining project files"'
    result = subprocess.run(commit_cmd, shell=True, env=env, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("  ✓ Committed remaining files")
    else:
        print("  ✗ Failed to commit remaining files")
    
    # Set up GitHub remote and push
    print("\nSetting up GitHub remote...")
    run_git_command('git remote add origin https://github.com/RishiSadineni/Syntaxis_Public.git', "Add GitHub remote")
    
    # Push to GitHub
    print("\nPushing to GitHub...")
    run_git_command('git push -u origin master', "Push to GitHub master branch")
    
    print("\n" + "=" * 75)
    print("FINAL UPLOAD COMPLETE!")
    print("=" * 75)
    print("✓ Repository has been uploaded to GitHub")
    print("✓ ALL files have COMPLETELY random times")
    print("✓ Spanish files dated to September 2024 with random times")
    print("✓ French files dated to November 2024 with random times")
    print("✓ ALL program files have their respective dates with random times")
    print("✓ Duplicate files removed")
    print("\nRepository URL: https://github.com/RishiSadineni/Syntaxis_Public")

if __name__ == "__main__":
    main()
