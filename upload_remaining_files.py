#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to upload remaining Spanish program files to GitHub with random dates
"""

import os
import subprocess
import random
from datetime import datetime, timedelta
import glob

def run_command(command, check=True):
    """Run a shell command and return the result"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=check)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(f"Error: {e.stderr}")
        return None

def git_commit_with_date(file_path, commit_date, commit_message):
    """Commit a file with a specific date"""
    # Add the file
    run_command(f'git add "{file_path}"')
    
    # Commit with specific date
    env = os.environ.copy()
    env['GIT_AUTHOR_DATE'] = commit_date
    env['GIT_COMMITTER_DATE'] = commit_date
    
    try:
        subprocess.run(
            f'git commit -m "{commit_message}"',
            shell=True,
            env=env,
            check=True
        )
        print(f"✓ Committed {file_path} with date {commit_date}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to commit {file_path}: {e}")
        return False

def generate_random_date(start_date, end_date):
    """Generate a random date between start_date and end_date"""
    time_between = end_date - start_date
    days_between = time_between.days
    random_days = random.randrange(days_between)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime("%Y-%m-%d %H:%M:%S")

def main():
    print("=== UPLOADING REMAINING SPANISH PROGRAMS ===")
    
    # Find all Spanish program files
    spanish_program_files = glob.glob('espanol/programas/*.synt')
    
    print(f"Found {len(spanish_program_files)} Spanish program files")
    
    # Commit each file with a random date
    successful_commits = 0
    
    for file_path in spanish_program_files:
        # Generate random date between Dec 1, 2024 and July 10, 2025
        start_date = datetime(2024, 12, 1)
        end_date = datetime(2025, 7, 10)
        commit_date = generate_random_date(start_date, end_date)
        
        # Create commit message
        filename = os.path.basename(file_path)
        program_name = filename.replace('.synt', '').replace('_', ' ').title()
        commit_message = f"Add {program_name} program"
        
        if git_commit_with_date(file_path, commit_date, commit_message):
            successful_commits += 1
    
    print(f"\nSuccessfully committed {successful_commits} Spanish program files")
    
    # Push to GitHub
    print("\nPushing to GitHub...")
    run_command('git push origin main')
    print("✓ Successfully pushed to GitHub!")
    
    print("\n=== UPLOAD COMPLETE ===")

if __name__ == "__main__":
    main()


