""" Importation des modules nécessaires """
from utility import *
import datetime


class Task():
    
    __etat = ['A faire', 'En cours', 'Terminée', 'Suspendu']
    
    @property
    def etat(self):
        return self.__etat

    @etat.setter
    def etat(self, new_etat):
        self.__etat = new_etat

    def __init__(self):
        pass 

    """ Fonction d'affichage du message de bienvenue """
    
    def messageBienvenue(self):
        print("""
                    ************************************************************************************
                    ********************* Bienvenue dans le gestionnaire de tâches *********************
                    ************************************************************************************

        PS : Choisissez une tâche en fonction de ce que vous voulez faire 
        \nVous pouvez insérer le numéro de la tâche ou écrire la tâche comme mentionné dans le menu ci dessous

        """)

    """Fonction d'affichage du menu de gestionnaire"""
    
    def afficherMenuPrincipal(self):
        print("""
                        *****************************************************************
                                                \033[36m\033[1m\033[4mMenu\033[0m 

                                    0- Tapez \033[32m'menu'\033[0m pour afficher le menu                                  

                                    1- Tapez \033[32m'add'\033[0m pour ajouter  une tâche     

                                    2- Tapez \033[32m'list'\033[0m pour afficher toutes les tâches 

                                    3- Tapez \033[32m'update'\033[0m pour modifier une tâche

                                    4- Tapez \033[32m'delete'\033[0m pour supprimer une tâche     

                                    5- Tapez \033[32m'quit'\033[0m pour quitter le gestionnaire      
                        *****************************************************************
        """)
        
    """ Fonction d'ajout d'une tâche """
    
    def ajouterTache(self):
        print(f"\n\033[36m\033[1m\033[4mAJOUTER UNE TACHE\033[0m\n")

        # Demander d'entrer le nom de la tâche à l'utilisateur
        nom_tache = input(
            "\033[4m\033[1mEntrer le nom de la tâche\033[0m \033[1m:\033[0m ")

        # Si le nom existe déjà, afficher un numéro de rang
        # Initialiser à 2 la variable i (qui va contenir, les numéros de rang)
        i = 2

        # Créer une variable qui va contenir initialement le nom de tâche original
        nom_tache_original = nom_tache

        # Variable qui va contenir le message d'alerte au doublon concernant les noms de tâches
        message_doublon_nom_tache = ""

        # Dès que la tâche existe déjà
        while nom_tache in liste_Taches:
            # Le nom de la tâche prend la valeur du nom de tâche initial et du numéro de rang
            nom_tache = f"{nom_tache_original} {i}"

            # Informer à l'utilisateur que le nom de tâche inséré est existant
            # et montrer comment la tâche sera enregistrée
            message_doublon_nom_tache = (f"\n\033[33mLe nom \033[1m{nom_tache_original}\033[0m\033[33m existe déjà. "
                                        f"Pour éviter les doublons de noms, "
                                        f"il sera enregistré comme tel : \033[1m{nom_tache_original} {i}\033[0m\n")

            # Définir les pas d'incrémentation
            i += 1
            # S'il n'y a pas de message, on passe à l'instruction suivante,
            # sinon on affiche le message à l'utilisateur
        if message_doublon_nom_tache == "":
            pass
        else:
            # Afficher le message de doublon à l'utilisateur
            print(message_doublon_nom_tache)

            # Demander d'entrer la description de la tâche
        description_tache = input(
            "\033[4m\033[1mEntrer la description de la tâche\033[0m \033[1m:\033[0m ")

            # Demander d'entrer la date limite de la tâche    
        print("\033[4m\033[1mEntrer la date limite de la tâche au format AAAA, MM, JJ\033[0m \033[1m:\033[0m ")
        while True:
            try:
                annee = int(input("Année:"))
                mois = int(input("Mois:"))  
                jours = int(input("Jour:"))
                new_date_tache = datetime.date(annee, mois, jours)
                break
            except ValueError:
                print(f"\n\033[31m\033[1mEntrez une date valide svp ! Les Mois sont compris entre 1-12 et les jours 1-28,29 30 ou 31\033[0m\n")
            # convertir la date en format str
        date_tache = new_date_tache.strftime("%Y-%m-%d")
        
            # Demander d'entrer l'état de la tâche
        print("")
        print("\033[4m\033[1mVeuillez saisir un état entre\033[0m \033[1m:\033[0m \033[32m1 Pour 'A faire', 2 'En cours', 3 'Terminée' ou 4 'Suspendu'\033[0m")
        print("")
        # Créer une boucle infinie jusqu'à ce que l'utilisateur insère nombre entier
        while True:
            try:
                inserer_tache = int(input(
            "\033[4m\033[1mEntrer l'état de la tâche\033[0m \033[1m:\033[0m "))
                break
            except ValueError:
                print(f"\n\033[31m\033[1mEntrer un nombre entier svp !\033[0m\n")
        if inserer_tache == 1:
            etat_tache = Task.__etat[0]
        elif inserer_tache == 2:
            etat_tache = Task.__etat[1]
        elif inserer_tache == 3:
            etat_tache = Task.__etat[2]
        elif inserer_tache == 4:
            etat_tache = Task.__etat[3]
        else:
            print(f"\n\033[31m\033[1mMerci d'entrer un état valide svp !\033[0m\n")
        
        # Insérer la tâche dans le dictionnaire
        liste_Taches[nom_tache] = description_tache, date_tache, etat_tache

        # Enregistrer le tout dans le fichier Json
        with open("taches.json", "w") as fichier:
            json.dump(liste_Taches, fichier, indent=4)

        # Retourner le message de confirmation à l'utilisateur
        return f"\n\033[32m\033[1mTâche enregistrée avec succès !\033[0m\n"
    
    """ Fonction d'affichage du sous-menu ajout de tâches """
        
    def afficherSousMenuAjout(self):
        print("""

    1- Ajouter une tâche 

    """)
        
    """"""""""""""" Fonction de listing d'une tâche """""""""""""""
    
    def listerTache(self):
        print("\n\033[1m\033[4mLISTE DES TACHES\033[0m")
        # Créer une liste qui va contenir l'ensemble des tâches parcourues avant de les afficher
        listeDeStockage = []
        # Parcourir le dictionnaire pour en lister les tâches enregistrées
        for compteur, (nom_tache_parcourue, others_tache_parcourue) in enumerate(liste_Taches.items(), 1):
            # Comportement de stockage des tâches dans la liste
            comportement = f"\n\033[37m\033[1m{compteur}.\033[4mNom \033[0m:\033[32m {nom_tache_parcourue} \n\033[0m \033[37m\033[1m.\033[4mDescription\033[0m :\033[32m {others_tache_parcourue[0]}\033[0m  \n\033[0m \033[37m\033[1m.\033[4mDate\033[0m :\033[32m {others_tache_parcourue[1]}\033[0m  \n\033[0m \033[37m\033[1m.\033[4mEtat\033[0m :\033[32m {others_tache_parcourue[2]}\033[0m\n\n"
            # Insérer chaque itération de tâche dans la liste de stockage
            listeDeStockage.append(comportement)
        # Conditions d'affichage final
        if listeDeStockage == []:
            return f"\033[33mAucune tâche disponible. Ajoutez une tâche en tapant 'add' ou '1'.\033[0m\n"
        else:
            # Retourner le résultat final en concaténant
            return "".join(listeDeStockage)
        
    """"""""" Fonction de suppression d'une tâche d'une tâche """""""""""""""
    
    def supprimerTache(self):
        print(f"\n\033[36m\033[1m\033[4mSUPPRIMER UNE TACHE\033[0m\n")

        # Créer une boucle infinie jusqu'à ce que l'utilisateur insère nombre entier
        while True:
            try:
                # Demander à l'utilisateur d'insérer un numéro avec lequel il fera la suppression
                numero_suppression = int(input(
                    "\033[4m\033[1mEntrer le numéro de la tâche à supprimer\033[0m \033[1m:\033[0m "))
                break

            except:
                print(f"\n\033[31m\033[1mEntrer un nombre entier svp !\033[0m\n")

                # Variable contenant le message final
        message_de_retour_final_de_suppression = ""

        # Créer une nouvelle liste contenant les élèments du dictionnaire afin de pouvoir les indexer plus facilement
        liste_suppression = list(liste_Taches)

        # Vérifier si le numéro inséré par l'utilisateur existe
        if numero_suppression <= len(liste_suppression) and numero_suppression != 0:
            # Récupérer la valeur correspondante pour la suppression
            index_correspondant = liste_suppression[numero_suppression - 1]

            try:
                # Message de confirmation
                confirmation_de_suppression = int(input(
                    f"\n\033[33m\033[4mVoulez-vous vraiment supprimer la tâche {numero_suppression} (tapez '1' (OUI) ou '2' (NON) \033[0m\033[33m :\033[0m"))

                # Supprimer ou pas en fonction de la réponse de l'utilisateur
                if confirmation_de_suppression == 1:

                    # Supprimer la valeur
                    del liste_Taches[index_correspondant]

                    # Enregistrer le tout dans le fichier Json
                    with open("taches.json", "w") as fichier:
                        json.dump(liste_Taches, fichier, indent=4)

                    message_de_retour_final_de_suppression = f"\n\033[32m\033[1mTâche {numero_suppression} supprimée avec succès !\033[0m\n"

                elif confirmation_de_suppression == 2:
                    message_de_retour_final_de_suppression = f"\n\033[41mSuppression annulée\033[0m\n"

                else:
                    print("\n\033[41mEchec de suppression\033[0m\n")

            # Générer une exception si l'utilisateur ne met pas d'entier
            except ValueError:
                print(f"\n\033[41m\033[1mTapez '1' ou '2' svp ! Echec de la suppression\033[0m")

            # Retourner le message de confirmation à l'utilisateur
            return message_de_retour_final_de_suppression
        else:
            # Retourner le message à l'utilisateur si l'index choisi est mauvais
            return (f"\n\033[31mLa tâche '{numero_suppression}' n'existe pas ! "
                    f"Tapez 'list' pour voir les tâches disponibles ainsi que leur numéro associé\033[0m\n\n\033[41mEchec de la suppression\n\033[0m")

    """ Fonction d'affichage du sous menu de suppression """
    
    def afficherSousMenuSuppression(self):
        print("""

    1- Supprimer une tâche     

    2- Supprimer toutes les tâches

    """)
        
    """ Fonction pour supprimer toutes les tâches """
    
    def supprimerToutesLesTaches(self):
        print(f"\n\033[36m\033[1m\033[4mSUPPRIMER TOUTES LES TÂCHES\033[0m\n")

        # Créer une liste qui va récupérer toutes les clé existantes du dictionnaire
        liste_recuperation_cle_suppression = []

        # Variable qui va contenir le message final
        message_de_confirmation_de_suppression_totale = ""

        # Variable qui va contenir le message final
        message_de_retour_final_de_suppression_totale = False

        try:
            # Message de confirmation
            confirmation_de_suppression = int(input(
                f"\n\033[33m\033[4mVoulez-vous vraiment supprimer toutes les tâches  (tapez '1' (OUI) ou '2' (NON) \033[0m\033[33m :\033[0m"))

            # Supprimer ou pas en fonction de la réponse de l'utilisateur
            if confirmation_de_suppression == 1:
                message_de_confirmation_de_suppression_totale = True

                # La variable reçoit un message de confirmation de suppression totale des tâches
                message_de_retour_final_de_suppression_totale = f"\n\033[42m\033[1m\033[1mToutes les tâches ont été supprimées avec succès !\033[0m\n"

            elif confirmation_de_suppression == 2:
                # La variable reçoit un message de confirmation d'annulation de suppression totale des tâches
                message_de_retour_final_de_suppression_totale = f"\n\033[41mSuppression annulée\033[0m\n"

            else:
                #  Si l'utilisateur entre un entier, mais qu'il est différent de '1' et '2'
                message_de_retour_final_de_suppression_totale = (f"\n\033[41m\033[1mEchec de la suppression !\033[0m\n")

        # Générer une exception si l'utilisateur ne met pas d'entier
        except ValueError:
            message_de_retour_final_de_suppression_totale = (f"\n\033[41m\033[1mEchec de la suppression !\033[0m\n")

        # Si la variable booléenne indiquant la confirmation ou pas de l'utilisateur prend la valeur True,
        # alors on peut démarrer la suppression
        if message_de_confirmation_de_suppression_totale == True:
            # Parcourir le dictionnaire
            for cle in liste_Taches:
                liste_recuperation_cle_suppression.append(cle)

            # Parcourir la liste contenant l'ensemble des clés
            for element in liste_recuperation_cle_suppression:

                # Supprimer les tâches
                del liste_Taches[element]

        # Enregistrer le tout dans le fichier Json
        with open("taches.json", "w") as fichier:
            json.dump(liste_Taches, fichier, indent=4)

        return message_de_retour_final_de_suppression_totale
    
    """ Fonction de modification de tâches """
    
    def modifierTache(self):
        print(f"\n\033[36m\033[1m\033[4mMODIFIER UNE TACHE\033[0m\n")

        # Demander à l'utilisateur d'entrer la tâche à modifier
        tache_modifier = input(
            "\033[4m\033[1mEntrer le nom de la tâche à modifier\033[0m \033[1m:\033[0m ")

        # Créer une liste qui va récupérer l'état de la demande faite
        liste_tache_modifier = []

        # Créer une liste qui va récupérer la clé correspondante
        liste_recuperation_cle_correspondante = []

        nom_tache_modifier = ""
        description_tache_modifier = []

        # Vérifier si la tâche est présente dans la liste des tâches afin de la modifier
        for cle, valeur in liste_Taches.items():
            if tache_modifier.lower() == cle.lower():
                # Demander le nouveau nom de la tâche
                nom_tache_modifier = input("\n\033[1m\033[4mEntrer le nouveau nom de la tâche\033[0m :")
                print("")

                # Demander la nouvelle description de la tâche  
                desc = input("\033[1m\033[4mEntrer la nouvelle description de la tâche\033[0m :")
                print("")
                # Demander la nouvelle date de la tâche au format date
                print("\033[1m\033[4mEntrer la nouvelle date de la tâche au format AAAA, MM, JJ\033[0m :")
                # Créer une boucle infinie jusqu'à ce que l'utilisateur insère nombre entier
                while True:
                    try:
                        annee = int(input("Année:"))
                        mois = int(input("Mois:"))  
                        jours = int(input("Jour:"))
                        date = datetime.date(annee, mois, jours)
                        break
                    except ValueError:
                        print(f"\n\033[31m\033[1mEntrez une date valide svp ! Les Mois sont compris entre 1-12 et les jours 1-28,29 30 ou 31\033[0m\n")
                print("")
                print("\033[4m\033[1mVeuillez saisir un état entre\033[0m \033[1m:\033[0m \033[32m1 Pour 'A faire', 2 'En cours', 3 'Terminée' ou 4 'Suspendu'\033[0m")
                while True:
                    try:
                        inserer_tache = int(input(
                    "\033[4m\033[1mEntrer l'état de la tâche\033[0m \033[1m:\033[0m "))
                        break
                    except ValueError:
                        print(f"\n\033[31m\033[1mEntrer un nombre entier svp !\033[0m\n")
                if inserer_tache == 1:
                    etat_tache = Task.__etat[0]
                elif inserer_tache == 2:
                    etat_tache = Task.__etat[1]
                elif inserer_tache == 3:
                    etat_tache = Task.__etat[2]
                elif inserer_tache == 4:
                    etat_tache = Task.__etat[3]
                else:
                    print(f"\n\033[31m\033[1mMerci d'entrer un état valide svp !\033[0m\n")
                # creer une boucle pour inserer les nouvelles données 
                while True:
                    try:
                        description_tache_modifier = [desc,
                        # convertir la date en format str
                        date.strftime("%Y-%m-%d"),
                        # Inserer le nouvel etat de la tâche
                        etat_tache]
                        break
                    except UnboundLocalError:
                        break
                # renvoyer un message d'erreur si le tableau description est vide
                if description_tache_modifier == []:
                    print(f"\n\033[31m\033[1mEchec de la modification !\033[0m\n")
                    break  
                else:
                    # Récupérer la clé correspondante à modifier ( le nom de la tâche )
                    liste_recuperation_cle_correspondante.append(cle)

                    # Initialiser une variable qui va enregistrer l'état de modification de la tâche
                    new_etat_tache = f"\n\033[32m\033[1mTâche modifiée avec succès !\033[0m\n"

                    # Ajout dans du message dans la liste
                    liste_tache_modifier.append(new_etat_tache)

        if liste_tache_modifier:
            # Supprimer la clé actuelle
            del liste_Taches["".join(liste_recuperation_cle_correspondante)]

            # Mettre à jour la tâche
            liste_Taches[nom_tache_modifier] = description_tache_modifier

            # Enregistrer le tout dans le fichier Json
            with open("taches.json", "w") as fichier:
                json.dump(liste_Taches, fichier, indent=4)

            # Retourner le message de confirmation de modification à l'utilisateur
            return "".join(liste_tache_modifier)
        else:
            return (f"\n\033[33mModification impossible. La tâche est introuvable !\033[0m\n")




   

