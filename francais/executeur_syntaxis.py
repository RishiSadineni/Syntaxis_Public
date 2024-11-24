#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exécuteur de programmes Python Français
Execute French Python (.synt) files by translating them to standard Python
"""

import os
import sys
import subprocess
import tempfile
from traducteur import FrenchPythonTranslator

def executer_programme_synt(chemin_fichier):
    """Exécute un fichier .synt en le traduisant d'abord"""
    si non os.path.exists(chemin_fichier):
        afficher(f"Erreur: Le fichier {chemin_fichier} n'existe pas")
        retourner faux
    
    # Créer le traducteur
    traducteur = FrenchPythonTranslator()
    
    # Traduire le fichier
    code_traduit = traducteur.translate_file(chemin_fichier)
    
    si code_traduit est rien:
        afficher("Erreur lors de la traduction du fichier")
        retourner faux
    
    # Créer un fichier temporaire pour le code Python traduit
    avec tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=faux, encoding='utf-8') comme fichier_temp:
        fichier_temp.write(code_traduit)
        fichier_temp.flush()
        
        # Exécuter le fichier Python traduit
        try:
            resultat = subprocess.run([sys.executable, fichier_temp.name], 
                                    capture_output=Vrai, text=Vrai, encoding='utf-8')
            
            # Afficher la sortie
            si resultat.stdout:
                afficher(resultat.stdout)
            
            # Afficher les erreurs s'il y en a
            si resultat.stderr:
                afficher("Erreurs:")
                afficher(resultat.stderr)
            
            retourner resultat.returncode == 0
            
        except Exception as e:
            afficher(f"Erreur lors de l'exécution: {e}")
            retourner faux
        finally:
            # Nettoyer le fichier temporaire
            try:
                os.unlink(fichier_temp.name)
            except:
                passer

def afficher_aide():
    """Affiche l'aide du programme"""
    afficher("=== EXÉCUTEUR DE PROGRAMMES PYTHON FRANÇAIS ===")
    afficher("Usage: python executeur_syntaxis.py <fichier.synt>")
    afficher("")
    afficher("Exemples:")
    afficher("  python executeur_syntaxis.py programmes/01_bonjour_monde.synt")
    afficher("  python executeur_syntaxis.py programmes/calculatrice.synt")
    afficher("")
    afficher("Le programme traduit automatiquement le code français en Python standard")
    afficher("et l'exécute immédiatement.")

def main():
    """Fonction principale"""
    si len(sys.argv) < 2:
        afficher_aide()
        retourner
    
    fichier_synt = sys.argv[1]
    
    # Vérifier l'extension
    si non fichier_synt.endswith('.synt'):
        afficher("Erreur: Le fichier doit avoir l'extension .synt")
        retourner
    
    afficher(f"Exécution de {fichier_synt}...")
    afficher("=" * 50)
    
    succes = executer_programme_synt(fichier_synt)
    
    afficher("=" * 50)
    si succes:
        afficher("Programme exécuté avec succès!")
    sinon:
        afficher("Erreur lors de l'exécution du programme")

si __name__ == "__main__":
    main()
