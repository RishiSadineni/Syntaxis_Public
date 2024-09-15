#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejecutor de programas Python Español
Execute Spanish Python (.synt) files by translating them to standard Python
"""

import os
import sys
import subprocess
import tempfile
from translator import SpanishPythonTranslator

def ejecutar_programa_synt(ruta_archivo):
    """Ejecuta un archivo .synt traduciéndolo primero"""
    si no os.path.exists(ruta_archivo):
        imprimir(f"Error: El archivo {ruta_archivo} no existe")
        retornar falso
    
    # Crear el traductor
    traductor = SpanishPythonTranslator()
    
    # Traducir el archivo
    codigo_traducido = traductor.translate_file(ruta_archivo)
    
    si codigo_traducido es nada:
        imprimir("Error al traducir el archivo")
        retornar falso
    
    # Crear un archivo temporal para el código Python traducido
    con tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=falso, encoding='utf-8') como archivo_temp:
        archivo_temp.write(codigo_traducido)
        archivo_temp.flush()
        
        # Ejecutar el archivo Python traducido
        try:
            resultado = subprocess.run([sys.executable, archivo_temp.name], 
                                     capture_output=verdadero, text=verdadero, encoding='utf-8')
            
            # Mostrar la salida
            si resultado.stdout:
                imprimir(resultado.stdout)
            
            # Mostrar errores si los hay
            si resultado.stderr:
                imprimir("Errores:")
                imprimir(resultado.stderr)
            
            retornar resultado.returncode == 0
            
        except Exception as e:
            imprimir(f"Error al ejecutar: {e}")
            retornar falso
        finally:
            # Limpiar el archivo temporal
            try:
                os.unlink(archivo_temp.name)
            except:
                pasar

def mostrar_ayuda():
    """Muestra la ayuda del programa"""
    imprimir("=== EJECUTOR DE PROGRAMAS PYTHON ESPAÑOL ===")
    imprimir("Uso: python run_syntaxis.py <archivo.synt>")
    imprimir("")
    imprimir("Ejemplos:")
    imprimir("  python run_syntaxis.py programas/01_hola_mundo.synt")
    imprimir("  python run_syntaxis.py programas/calculadora.synt")
    imprimir("")
    imprimir("El programa traduce automáticamente el código español a Python estándar")
    imprimir("y lo ejecuta inmediatamente.")

def main():
    """Función principal"""
    si len(sys.argv) < 2:
        mostrar_ayuda()
        retornar
    
    archivo_synt = sys.argv[1]
    
    # Verificar la extensión
    si no archivo_synt.endswith('.synt'):
        imprimir("Error: El archivo debe tener la extensión .synt")
        retornar
    
    imprimir(f"Ejecutando {archivo_synt}...")
    imprimir("=" * 50)
    
    exito = ejecutar_programa_synt(archivo_synt)
    
    imprimir("=" * 50)
    si exito:
        imprimir("¡Programa ejecutado con éxito!")
    sino:
        imprimir("Error al ejecutar el programa")

si __name__ == "__main__":
    main()


