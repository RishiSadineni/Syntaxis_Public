#!/usr/bin/env python3
import os
import subprocess
import re
from datetime import datetime, timezone, timedelta
import glob
import random

def extract_date_from_filename(filename):
    """Extract date from filename in format YYYY_MM_DD"""
    # Pattern to match YYYY_MM_DD at the end of filename
    pattern = r'(\d{4}_\d{2}_\d{2})\.synt$'
    match = re.search(pattern, filename)
    if match:
        date_str = match.group(1)
        # Convert YYYY_MM_DD to datetime object
        return datetime.strptime(date_str, '%Y_%m_%d')
    return None

def get_random_cdt_time(date):
    """Generate a random time in CDT timezone for the given date"""
    # CDT is UTC-5 (or UTC-6 during daylight saving, but we'll use UTC-5 for simplicity)
    cdt_offset = timedelta(hours=5)
    
    # Generate random hour (0-23), minute (0-59), second (0-59)
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)
    
    # Create datetime with random time
    random_time = date.replace(hour=random_hour, minute=random_minute, second=random_second)
    
    # Convert to UTC (add 5 hours to get UTC time)
    utc_time = random_time + cdt_offset
    
    return utc_time

def git_commit_with_date(file_path, commit_date):
    """Commit a file with a specific date"""
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"Warning: File {file_path} does not exist, skipping...")
            return False
            
        # Add the file
        result = subprocess.run(['git', 'add', file_path], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Warning: Could not add {file_path}: {result.stderr}")
            return False
        
        # Create commit with specific date
        commit_message = f"Add {os.path.basename(file_path)}"
        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = commit_date.strftime('%Y-%m-%d %H:%M:%S')
        env['GIT_COMMITTER_DATE'] = commit_date.strftime('%Y-%m-%d %H:%M:%S')
        
        result = subprocess.run(['git', 'commit', '-m', commit_message], 
                              env=env, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ Committed {file_path} with date {commit_date.strftime('%Y-%m-%d %H:%M:%S')} UTC (CDT time)")
            return True
        else:
            print(f"Warning: Could not commit {file_path}: {result.stderr}")
            return False
    except Exception as e:
        print(f"Error committing {file_path}: {e}")
        return False

def reset_git_repository():
    """Reset git repository to clean state"""
    try:
        # Try to reset to empty state
        subprocess.run(['git', 'update-ref', '-d', 'HEAD'], check=True, capture_output=True)
        print("✓ Reset repository to empty state")
        return True
    except:
        try:
            # If that fails, try to remove all commits
            subprocess.run(['git', 'reset', '--hard', 'HEAD~1'], capture_output=True)
            print("✓ Reset repository by removing last commit")
            return True
        except:
            try:
                # Last resort: remove all commits
                subprocess.run(['git', 'reset', '--hard', '--initial'], capture_output=True)
                print("✓ Reset repository to initial state")
                return True
            except:
                print("Warning: Could not reset repository, continuing with current state")
                return False

def main():
    print("Setting up repository with specific dates and random times...")
    
    # Reset to empty state (remove all commits but keep files)
    reset_git_repository()
    
    # Find all .synt files
    synt_files = []
    
    # Search in espanol/programas/
    espanol_files = glob.glob('espanol/programas/*.synt')
    synt_files.extend(espanol_files)
    
    # Search in francais/programmes/
    francais_files = glob.glob('francais/programmes/*.synt')
    synt_files.extend(francais_files)
    
    # Define dates for specific files
    spanish_date = datetime(2024, 9, 15)  # September 2024
    french_date = datetime(2024, 11, 15)  # November 2024
    
    # Spanish files (September 2024)
    spanish_files = [
        'espanol/README.md',
        'espanol/run_syntaxis.py',
        'espanol/translator.py'
    ]
    
    # French files (November 2024)
    french_files = [
        'francais/README.md',
        'francais/executeur_syntaxis.py',
        'francais/traducteur.py'
    ]
    
    # Filter out files that don't exist
    spanish_files = [f for f in spanish_files if os.path.exists(f)]
    french_files = [f for f in french_files if os.path.exists(f)]
    
    print(f"Found {len(synt_files)} .synt files")
    print(f"Spanish files: {len(spanish_files)}")
    print(f"French files: {len(french_files)}")
    
    # Sort synt files by date
    files_with_dates = []
    for file_path in synt_files:
        date = extract_date_from_filename(file_path)
        if date:
            files_with_dates.append((file_path, date))
        else:
            print(f"Warning: Could not extract date from {file_path}")
    
    # Sort by date (oldest first)
    files_with_dates.sort(key=lambda x: x[1])
    
    # First, commit Spanish files (September 2024) with random times
    print(f"\nCommitting Spanish files with date {spanish_date.strftime('%Y-%m-%d')} and random times:")
    for file_path in spanish_files:
        random_time = get_random_cdt_time(spanish_date)
        git_commit_with_date(file_path, random_time)
    
    # Then, commit French files (November 2024) with random times
    print(f"\nCommitting French files with date {french_date.strftime('%Y-%m-%d')} and random times:")
    for file_path in french_files:
        random_time = get_random_cdt_time(french_date)
        git_commit_with_date(file_path, random_time)
    
    # Finally, commit all .synt files with their respective dates and random times (Dec 2024 - Jul 2025)
    print("\nCommitting .synt files with their respective dates and random times:")
    for file_path, date in files_with_dates:
        random_time = get_random_cdt_time(date)
        git_commit_with_date(file_path, random_time)
    
    print("\n✓ All files processed!")
    print("\nTo push to GitHub:")
    print("1. Run: git remote add origin https://github.com/RishiSadineni/Syntaxis_Public.git")
    print("2. Run: git push -u origin master")

if __name__ == "__main__":
    main()

