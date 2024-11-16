# Traducteur de Python Français

## Description

Ce projet contient un traducteur qui convertit du code Python écrit avec des mots-clés français en Python standard. Il permet aux programmeurs francophones d'écrire du code Python en utilisant des mots-clés dans leur langue maternelle.

## Caractéristiques

- **Traduction automatique** : Convertit les mots-clés français en anglais
- **Préserve les commentaires** : Les commentaires et la structure du code restent intacts
- **Facile à utiliser** : Interface simple en ligne de commande
- **Compatible** : Génère du code Python standard exécutable

## Mots-clés Supportés

### Contrôle de Flux
- `si` → `if`
- `sinon` → `else`
- `sinon_si` → `elif`
- `pour` → `for`
- `tant_que` → `while`
- `dans` → `in`
- `plage` → `range`

### Fonctions
- `definir` → `def`
- `retourner` → `return`
- `afficher` → `print`

### Types de Données
- `vrai` → `True`
- `faux` → `False`
- `rien` → `None`

### Logique
- `et` → `and`
- `ou` → `or`
- `non` → `not`

### Fonctions Intégrées
- `longueur` → `len`
- `type` → `type`
- `entree` → `input`
- `entier` → `int`
- `flottant` → `float`
- `chaine` → `str`
- `liste` → `list`
- `dictionnaire` → `dict`

### Fonctions Supplémentaires
- `demander` → `input`
- `calculer` → `eval`
- `ouvrir` → `open`
- `fermer` → `close`
- `lire` → `read`
- `ecrire` → `write`

## Installation

1. Assurez-vous d'avoir Python 3.6+ installé
2. Clonez ou téléchargez ce dépôt
3. Naviguez vers le répertoire `francais/`

## Utilisation

### Utilisation de Base

```bash
python traducteur.py fichier_entree.synt fichier_sortie.py
```

### Exemples

**Entrée** (`programme_francais.synt`):
```python
definir saluer(nom):
    si nom:
        afficher(f"Bonjour {nom}!")
    sinon:
        afficher("Bonjour inconnu!")

pour i dans plage(5):
    afficher(f"Nombre: {i}")

liste_nombres = [1, 2, 3, 4, 5]
longueur_liste = longueur(liste_nombres)
afficher(f"La liste a {longueur_liste} éléments")
```

**Sortie** (`programme_python.py`):
```python
def saluer(nom):
    if nom:
        print(f"Bonjour {nom}!")
    else:
        print("Bonjour inconnu!")

for i in range(5):
    print(f"Nombre: {i}")

liste_nombres = [1, 2, 3, 4, 5]
longueur_liste = len(liste_nombres)
print(f"La liste a {longueur_liste} éléments")
```

### Utilisation Interactive

```bash
python traducteur.py fichier_entree.synt
```

Cela affichera le code traduit dans la console sans créer de fichier de sortie.

## Programmes d'Exemple

Le répertoire `programmes/` contient plusieurs exemples de code Python en français :

1. **01_bonjour_monde_marie_dupont_2025_02_10.synt** - Programme de salutation interactif avancé
2. **02_calculatrice_pierre_martin_2025_03_15.synt** - Calculatrice avancée avec fonctions mathématiques
3. **03_liste_taches_sophie_bernard_2025_04_20.synt** - Gestionnaire de recettes de cuisine
4. **04_convertisseur_devises_lucas_dubois_2025_05_25.synt** - Système de gestion de bibliothèque
5. **05_jeu_devinettes_emma_leroy_2025_06_30.synt** - Gestionnaire de playlist musicale

## Comment Ça Fonctionne

Le traducteur utilise des expressions régulières pour identifier et remplacer les mots-clés français par leurs équivalents anglais. Le processus est :

1. **Lecture** : Lit le fichier `.synt` ligne par ligne
2. **Analyse** : Identifie les mots-clés français en utilisant des limites de mots
3. **Traduction** : Remplace chaque mot-clé par son équivalent anglais
4. **Préservation** : Maintient les commentaires, espaces et structure originale
5. **Sortie** : Génère du code Python standard exécutable

## Structure du Projet

```
francais/
├── README.md              # Ce fichier
├── traducteur.py          # Traducteur principal
├── executeur_syntaxis.py  # Exécuteur de programmes .synt
└── programmes/            # Programmes d'exemple
    ├── 01_bonjour_monde_marie_dupont_2025_02_10.synt
    ├── 02_calculatrice_pierre_martin_2025_03_15.synt
    └── ...
```

## Fonctionnalités Avancées

### Gestionnaire de Recettes
- Ajout et gestion de recettes de cuisine
- Recherche par ingrédients
- Filtrage par difficulté
- Système de favoris

### Système de Gestion de Bibliothèque
- Gestion des livres et membres
- Système d'emprunt et retour
- Recherche de livres
- Statistiques d'utilisation

### Gestionnaire de Playlist Musicale
- Gestion de bibliothèque musicale
- Création et gestion de playlists
- Recherche par artiste, titre, genre
- Calcul de durée totale

### Programme de Salutation Interactif
- Calcul d'âge et génération
- Nombre magique personnalisé
- Horoscope quotidien
- Statistiques d'utilisation

## Limitations

- Ne traduit que les mots-clés, pas la syntaxe complète
- Ne gère pas les traductions de bibliothèques personnalisées
- Les variables et noms de fonctions doivent suivre les conventions Python
- Ne traduit pas les chaînes littérales (texte entre guillemets)

## Contribuer

Pour ajouter de nouveaux mots-clés :

1. Ouvrez `traducteur.py`
2. Ajoutez la nouvelle entrée au dictionnaire `keyword_map`
3. Testez avec un programme d'exemple
4. Mettez à jour cette documentation

## Licence

Ce projet est open source et disponible sous licence MIT.

## Auteur

Développé pour faciliter l'apprentissage de Python pour les francophones.

---

**Note** : Ce traducteur est un outil éducatif conçu pour aider les programmeurs francophones à apprendre Python en utilisant leur langue maternelle comme pont vers l'anglais.