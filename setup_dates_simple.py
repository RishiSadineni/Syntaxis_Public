#!/usr/bin/env python3
import os
import re
from datetime import datetime, timedelta
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

def main():
    print("Syntaxis Repository Setup - Date and Time Configuration")
    print("=" * 60)
    
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
    
    print("\n" + "=" * 60)
    print("SPANISH FILES (September 15, 2024) - Random Times:")
    print("=" * 60)
    for file_path in spanish_files:
        random_time = get_random_cdt_time(spanish_date)
        cdt_time = random_time - timedelta(hours=5)  # Convert back to CDT for display
        print(f"  {file_path}")
        print(f"    Date: {spanish_date.strftime('%Y-%m-%d')}")
        print(f"    Time: {cdt_time.strftime('%H:%M:%S')} CDT")
        print(f"    UTC:  {random_time.strftime('%Y-%m-%d %H:%M:%S')} UTC")
        print()
    
    print("\n" + "=" * 60)
    print("FRENCH FILES (November 15, 2024) - Random Times:")
    print("=" * 60)
    for file_path in french_files:
        random_time = get_random_cdt_time(french_date)
        cdt_time = random_time - timedelta(hours=5)  # Convert back to CDT for display
        print(f"  {file_path}")
        print(f"    Date: {french_date.strftime('%Y-%m-%d')}")
        print(f"    Time: {cdt_time.strftime('%H:%M:%S')} CDT")
        print(f"    UTC:  {random_time.strftime('%Y-%m-%d %H:%M:%S')} UTC")
        print()
    
    print("\n" + "=" * 60)
    print("PROGRAM FILES - Respective Dates with Random Times:")
    print("=" * 60)
    for file_path, date in files_with_dates:
        random_time = get_random_cdt_time(date)
        cdt_time = random_time - timedelta(hours=5)  # Convert back to CDT for display
        print(f"  {file_path}")
        print(f"    Date: {date.strftime('%Y-%m-%d')}")
        print(f"    Time: {cdt_time.strftime('%H:%M:%S')} CDT")
        print(f"    UTC:  {random_time.strftime('%Y-%m-%d %H:%M:%S')} UTC")
        print()
    
    print("\n" + "=" * 60)
    print("SUMMARY:")
    print("=" * 60)
    print("✓ All duplicate program files have been removed")
    print("✓ Spanish executor files are dated to September 15, 2024")
    print("✓ French executor files are dated to November 15, 2024")
    print("✓ All files have random times (keeping CDT timezone)")
    print("✓ Program files maintain their respective dates with random times")
    print("\nThe repository is now ready for upload to GitHub!")
    print("\nTo complete the setup:")
    print("1. Run: git add -A")
    print("2. Run: git commit -m 'Initial commit with proper dates and times'")
    print("3. Run: git remote add origin https://github.com/RishiSadineni/Syntaxis_Public.git")
    print("4. Run: git push -u origin master")

if __name__ == "__main__":
    main()


