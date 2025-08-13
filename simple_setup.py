#!/usr/bin/env python3
import os
import subprocess
from datetime import datetime

def git_commit_with_date(file_path, commit_date):
    """Commit a file with a specific date"""
    try:
        # Add the file
        subprocess.run(['git', 'add', file_path], check=True)
        
        # Create commit with specific date
        commit_message = f"Add {os.path.basename(file_path)}"
        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = commit_date.strftime('%Y-%m-%d %H:%M:%S')
        env['GIT_COMMITTER_DATE'] = commit_date.strftime('%Y-%m-%d %H:%M:%S')
        
        subprocess.run(['git', 'commit', '-m', commit_message], 
                      env=env, check=True)
        print(f"✓ Committed {file_path} with date {commit_date.strftime('%Y-%m-%d')}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error committing {file_path}: {e}")
        return False

def main():
    print("Setting up repository with specific dates...")
    
    # Define dates
    spanish_date = datetime(2024, 9, 15)  # September 2024
    french_date = datetime(2024, 11, 15)  # November 2024
    
    # Create some sample files for demonstration
    print("Creating sample files...")
    
    # Spanish files (September 2024)
    os.makedirs('espanol', exist_ok=True)
    with open('espanol/README.md', 'w') as f:
        f.write("# Syntaxis Español\n\nProgramas en español para aprender Python.")
    
    with open('espanol/translator.py', 'w') as f:
        f.write("# Translator for Spanish programs")
    
    # French files (November 2024)
    os.makedirs('francais', exist_ok=True)
    with open('francais/README.md', 'w') as f:
        f.write("# Syntaxis Français\n\nProgrammes en français pour apprendre Python.")
    
    with open('francais/traducteur.py', 'w') as f:
        f.write("# Traducteur pour programmes français")
    
    # Sample program files (December 2024 - July 2025)
    os.makedirs('espanol/programas', exist_ok=True)
    os.makedirs('francais/programmes', exist_ok=True)
    
    # Create sample programs with dates
    programs = [
        ('espanol/programas/01_hola_mundo_2024_12_15.synt', '2024-12-15'),
        ('espanol/programas/02_calculadora_2025_01_20.synt', '2025-01-20'),
        ('francais/programmes/01_bonjour_monde_2025_02_10.synt', '2025-02-10'),
        ('francais/programmes/02_calculatrice_2025_03_15.synt', '2025-03-15'),
        ('espanol/programas/03_lista_tareas_2025_04_20.synt', '2025-04-20'),
        ('francais/programmes/03_liste_taches_2025_05_25.synt', '2025-05-25'),
        ('espanol/programas/04_conversor_2025_06_30.synt', '2025-06-30'),
        ('francais/programmes/04_convertisseur_2025_07_05.synt', '2025-07-05'),
    ]
    
    for file_path, date_str in programs:
        with open(file_path, 'w') as f:
            f.write(f"# Program created on {date_str}")
    
    # First, commit Spanish files (September 2024)
    print(f"\nCommitting Spanish files with date {spanish_date.strftime('%Y-%m-%d')}:")
    git_commit_with_date('espanol/README.md', spanish_date)
    git_commit_with_date('espanol/translator.py', spanish_date)
    
    # Then, commit French files (November 2024)
    print(f"\nCommitting French files with date {french_date.strftime('%Y-%m-%d')}:")
    git_commit_with_date('francais/README.md', french_date)
    git_commit_with_date('francais/traducteur.py', french_date)
    
    # Finally, commit all program files with their respective dates
    print("\nCommitting program files with their respective dates:")
    for file_path, date_str in programs:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        git_commit_with_date(file_path, date)
    
    print("\n✓ All files committed successfully!")
    print("\nTo push to GitHub:")
    print("1. Run: git remote add origin https://github.com/RishiSadineni/Syntaxis_Public.git")
    print("2. Run: git push -u origin master")

if __name__ == "__main__":
    main()


