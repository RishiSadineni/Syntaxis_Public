#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to upload all files to GitHub with specific commit dates
- Spanish files (non-programs): September 6, 2024
- French files (non-programs): November 24, 2024
- Program files: Random dates between Dec 1, 2024 and July 10, 2025
"""

import os
import subprocess
import random
from datetime import datetime, timedelta
import re

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

def get_file_date(file_path):
    """Determine the commit date for a file based on its type and location"""
    # Spanish non-program files: September 6, 2024
    if file_path.startswith('espanol/') and not file_path.startswith('espanol/programas/'):
        return "2024-09-06 10:00:00"
    
    # French non-program files: November 24, 2024
    if file_path.startswith('francais/') and not file_path.startswith('francais/programmes/'):
        return "2024-11-24 14:30:00"
    
    # Program files: Random date between Dec 1, 2024 and July 10, 2025
    if file_path.endswith('.synt'):
        start_date = datetime(2024, 12, 1)
        end_date = datetime(2025, 7, 10)
        return generate_random_date(start_date, end_date)
    
    # Default date for any other files
    return "2024-12-01 09:00:00"

def main():
    print("=== UPLOADING TO GITHUB WITH SPECIFIC DATES ===")
    
    # Initialize git repository if not already done
    if not os.path.exists('.git'):
        print("Initializing git repository...")
        run_command('git init')
    
    # Add remote origin if not already added
    remote_url = "https://github.com/RishiSadineni/Syntaxis_Public.git"
    run_command(f'git remote add origin "{remote_url}"')
    
    # Get all files to commit
    files_to_commit = []
    
    # Spanish files
    spanish_files = [
        'espanol/README.md',
        'espanol/translator.py',
        'espanol/run_syntaxis.py'
    ]
    
    # French files
    french_files = [
        'francais/README.md',
        'francais/traducteur.py',
        'francais/executeur_syntaxis.py'
    ]
    
    # Program files
    spanish_programs = [
        'espanol/programas/01_hola_mundo_maria_gonzalez_2024_07_15.synt',
        'espanol/programas/02_calculadora_carlos_rodriguez_2024_08_03.synt',
        'espanol/programas/03_lista_tareas_ana_martinez_2024_09_12.synt',
        'espanol/programas/04_conversor_monedas_luis_hernandez_2024_10_05.synt',
        'espanol/programas/05_juego_adivinanza_sofia_lopez_2024_11_20.synt',
        'espanol/programas/06_gestor_contactos_diego_ramirez_2024_12_08.synt',
        'espanol/programas/07_conversor_temperatura_jimena_sanchez_2025_01_10.synt',
        'espanol/programas/08_gestor_notas_soraya_morales_2025_02_14.synt'
    ]
    
    french_programs = [
        'francais/programmes/01_bonjour_monde_marie_dupont_2025_02_10.synt',
        'francais/programmes/02_calculatrice_pierre_martin_2025_03_15.synt',
        'francais/programmes/03_liste_taches_sophie_bernard_2025_04_20.synt',
        'francais/programmes/04_convertisseur_devises_lucas_dubois_2025_05_25.synt',
        'francais/programmes/05_jeu_devinettes_emma_leroy_2025_06_30.synt'
    ]
    
    # Add all files to the list
    files_to_commit.extend(spanish_files)
    files_to_commit.extend(french_files)
    files_to_commit.extend(spanish_programs)
    files_to_commit.extend(french_programs)
    
    # Filter out files that don't exist
    existing_files = [f for f in files_to_commit if os.path.exists(f)]
    
    print(f"Found {len(existing_files)} files to commit")
    
    # Commit each file with its specific date
    successful_commits = 0
    
    for file_path in existing_files:
        commit_date = get_file_date(file_path)
        
        # Create commit message based on file type
        if file_path.endswith('.synt'):
            # Extract program name from filename
            filename = os.path.basename(file_path)
            program_name = filename.replace('.synt', '').replace('_', ' ').title()
            commit_message = f"Add {program_name} program"
        elif 'README' in file_path:
            commit_message = f"Add README for {os.path.dirname(file_path)}"
        elif 'translator' in file_path or 'traducteur' in file_path:
            commit_message = f"Add Python translator for {os.path.dirname(file_path)}"
        elif 'run_syntaxis' in file_path or 'executeur' in file_path:
            commit_message = f"Add program executor for {os.path.dirname(file_path)}"
        else:
            commit_message = f"Add {os.path.basename(file_path)}"
        
        if git_commit_with_date(file_path, commit_date, commit_message):
            successful_commits += 1
    
    print(f"\nSuccessfully committed {successful_commits} files")
    
    # Push to GitHub
    print("\nPushing to GitHub...")
    
    # Check if we need to force push (in case of history rewrite)
    try:
        run_command('git push -u origin main')
        print("✓ Successfully pushed to GitHub!")
    except:
        print("Attempting force push...")
        run_command('git push --force origin main')
        print("✓ Successfully force pushed to GitHub!")
    
    print("\n=== UPLOAD COMPLETE ===")
    print("All files have been uploaded with their specified dates:")
    print("- Spanish files (non-programs): September 6, 2024")
    print("- French files (non-programs): November 24, 2024")
    print("- Program files: Random dates between Dec 1, 2024 and July 10, 2025")

if __name__ == "__main__":
    main()


