import json

    
# Gestion de la persistance de données avec l'utilisation de JSON et d'exeption
try:
    # Essayer de charger le fichier "taches.json" (s'il existe)
    with open("taches.json", "r") as fichier:
        liste_Taches = json.load(fichier)

except FileNotFoundError:
    # S'il n'existe pas alors créer un dictionnaire qui va abriter l'ensemble des tâches
    liste_Taches = {}