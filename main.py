# Application de gestion des tâches (console) - Partie 1

taches = []


def afficher_menu():
    print("\n=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche")
    print("2. Afficher")
    print("3. Rechercher")
    print("0. Quitter")





def afficher_taches():
    if len(taches) == 0:
        print("Aucune tâche pour le moment.")
    else:
        for i in range(len(taches)):
            print(f"{i + 1}. {taches[i]}")


def rechercher_tache():
    mot = input("Mot-clé : ").strip().lower()
    trouve = False
    for i in range(len(taches)):
        if mot in taches[i].lower():
            print(f"{i + 1}. {taches[i]}")
            trouve = True
    if not trouve:
        print("Aucune tâche trouvée.")


choix = ""
while choix != "0":
    afficher_menu()
    choix = input("Votre choix : ").strip()
    if choix == "1":
        ajouter_tache()
    elif choix == "2":
        afficher_taches()
    elif choix == "3":
        rechercher_tache()
    elif choix == "0":
        print("Au revoir !")
    else:
        print("Option invalide, veuillez réessayer.")