"""Import"""
from utility import *
from Task import *
import datetime

class Main:

    Tache = Task()
    def __init__(self):
        pass

    # Message de Bienvenue
    Tache.messageBienvenue()

    # Affichage du menu
    Tache.afficherMenuPrincipal()

    # Initialiser une boucle inifinie avec while
    while True:
        # Initialiser une variable qui va contenir le choix de l'utilisateur
        choix = input(
            "\033[1m\033[4m\033[36mEntrer une commande à exécuter\033[0m \033[1m:\033[0m ")

        # Création de condition en fonction du choix
        if choix == "0" or choix.lower() == "menu":
            Tache.afficherMenuPrincipal()

        elif choix == "1" or choix.lower() == "add":
            # Afficher le sous-menu d'ajout de tâche
            Tache.afficherSousMenuAjout()

            # Permettre à l'utilisateur de faire un choix d"ajout de tâche
            choix_sous_menu_ajout = input(
                "\033[1m\033[4mTapez '1'\033[0m \033[1m:\033[0m ")

            # Créer des conditions en fonction du choix de l'utilisateur
            if choix_sous_menu_ajout == "1":
                print(Tache.ajouterTache())
            else:
                print("\n\033[41mEchec de l'ajout\033[0m\n")

        elif choix == "2" or choix.lower() == "list":
            print(Tache.listerTache())

        elif choix == "3" or choix.lower() == "update":
            print(Tache.modifierTache())

        elif choix == "4" or choix.lower() == "delete":

            # afficher le sous-menu de suppression
            Tache.afficherSousMenuSuppression()

            # Permettre à l'utilisateur de faire un choix de suppression
            choix_sous_menu_suppression = input(
                "\033[1m\033[4mTapez '1' ou '2'\033[0m \033[1m:\033[0m ")

            if choix_sous_menu_suppression == "1":
                print(Tache.supprimerTache())
            elif choix_sous_menu_suppression == "2":
                print(Tache.supprimerToutesLesTaches())
            else:
                print(f"\n\033[41mEchec de la suppression\033[0m\n")

        elif choix == "5" or choix.lower() == "quit":
            print(f"\n\033[32m\033[1mA très bientot \033[0m\n")

            # Appuyer sur ENTRER pour quitter
            input("\nTapez sur ENTRER pour quitter")

            # Arrêter la boucle
            break

        else:
            print(
                f"\n\033[31m\033[1m'{choix}'\033[0m\033[31m n'est pas une commande. "
                f"Tapez 'menu' ou '0' pour voir les commandes prises en charge\033[0m\n")

