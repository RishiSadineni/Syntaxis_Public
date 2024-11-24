#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Traducteur de Python Français vers Python standard
Translates French Python syntax to standard Python
"""

import re
import sys

class FrenchPythonTranslator:
    def __init__(self):
        # French to English keyword mappings
        self.keyword_map = {
            # Control flow
            'si': 'if',
            'sinon': 'else',
            'sinon_si': 'elif',
            'pour': 'for',
            'tant_que': 'while',
            'dans': 'in',
            'plage': 'range',
            
            # Functions
            'definir': 'def',
            'retourner': 'return',
            'afficher': 'print',
            
            # Data types
            'vrai': 'True',
            'faux': 'False',
            'rien': 'None',
            
            # Logic
            'et': 'and',
            'ou': 'or',
            'non': 'not',
            
            # Built-in functions
            'longueur': 'len',
            'type': 'type',
            'entree': 'input',
            'entier': 'int',
            'flottant': 'float',
            'chaine': 'str',
            'liste': 'list',
            'dictionnaire': 'dict',
            
            # Additional French keywords
            'demander': 'input',
            'calculer': 'eval',
            'ouvrir': 'open',
            'fermer': 'close',
            'lire': 'read',
            'ecrire': 'write',
        }
    
    def translate_line(self, line):
        """Translate a single line of French Python to English Python"""
        # Skip comments and empty lines
        if line.strip().startswith('#') or not line.strip():
            return line
        
        # Replace keywords
        translated_line = line
        for french, english in self.keyword_map.items():
            # Use word boundaries to avoid partial replacements
            pattern = r'\b' + re.escape(french) + r'\b'
            translated_line = re.sub(pattern, english, translated_line)
        
        return translated_line
    
    def translate_file(self, input_file, output_file=None):
        """Translate an entire file from French Python to English Python"""
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            translated_lines = []
            for line in lines:
                translated_line = self.translate_line(line)
                translated_lines.append(translated_line)
            
            if output_file:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.writelines(translated_lines)
                print(f"Fichier traduit sauvegardé comme: {output_file}")
            else:
                return ''.join(translated_lines)
                
        except FileNotFoundError:
            print(f"Erreur: Fichier {input_file} non trouvé")
            return None
        except Exception as e:
            print(f"Erreur lors de la traduction: {e}")
            return None
    
    def translate_string(self, code_string):
        """Translate a string of French Python code"""
        lines = code_string.split('\n')
        translated_lines = []
        
        for line in lines:
            translated_line = self.translate_line(line)
            translated_lines.append(translated_line)
        
        return '\n'.join(translated_lines)

def main():
    """Main function to run the translator"""
    translator = FrenchPythonTranslator()
    
    if len(sys.argv) < 2:
        print("Usage: python traducteur.py <fichier_entree> [fichier_sortie]")
        print("Exemple: python traducteur.py programme_francais.synt programme_python.py")
        return
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    result = translator.translate_file(input_file, output_file)
    if result and not output_file:
        print("Code traduit:")
        print(result)

if __name__ == "__main__":
    main()