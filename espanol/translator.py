#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Traductor de Python Español a Python estándar
Translates Spanish Python syntax to standard Python
"""

import re
import sys

class SpanishPythonTranslator:
    def __init__(self):
        # Spanish to English keyword mappings
        self.keyword_map = {
            # Control flow
            'si': 'if',
            'sino': 'else',
            'sino_si': 'elif',
            'para': 'for',
            'mientras': 'while',
            'en': 'in',
            'range': 'range',
            
            # Functions
            'definir': 'def',
            'retornar': 'return',
            'imprimir': 'print',
            
            # Data types
            'verdadero': 'True',
            'falso': 'False',
            'nada': 'None',
            
            # Logic
            'y': 'and',
            'o': 'or',
            'no': 'not',
            
            # Built-in functions
            'longitud': 'len',
            'tipo': 'type',
            'entrada': 'input',
            'entero': 'int',
            'flotante': 'float',
            'cadena': 'str',
            'lista': 'list',
            'diccionario': 'dict',
        }
    
    def translate_line(self, line):
        """Translate a single line of Spanish Python to English Python"""
        # Skip comments and empty lines
        if line.strip().startswith('#') or not line.strip():
            return line
        
        # Replace keywords
        translated_line = line
        for spanish, english in self.keyword_map.items():
            # Use word boundaries to avoid partial replacements
            pattern = r'\b' + re.escape(spanish) + r'\b'
            translated_line = re.sub(pattern, english, translated_line)
        
        return translated_line
    
    def translate_file(self, input_file, output_file=None):
        """Translate an entire file from Spanish Python to English Python"""
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
                print(f"Archivo traducido guardado como: {output_file}")
            else:
                return ''.join(translated_lines)
                
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {input_file}")
            return None
        except Exception as e:
            print(f"Error al traducir: {e}")
            return None
    
    def translate_string(self, code_string):
        """Translate a string of Spanish Python code"""
        lines = code_string.split('\n')
        translated_lines = []
        
        for line in lines:
            translated_line = self.translate_line(line)
            translated_lines.append(translated_line)
        
        return '\n'.join(translated_lines)

def main():
    """Main function to run the translator"""
    translator = SpanishPythonTranslator()
    
    if len(sys.argv) < 2:
        print("Uso: python translator.py <archivo_entrada> [archivo_salida]")
        print("Ejemplo: python translator.py programa_espanol.synt programa_python.py")
        return
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    result = translator.translate_file(input_file, output_file)
    if result and not output_file:
        print("Código traducido:")
        print(result)

if __name__ == "__main__":
    main()