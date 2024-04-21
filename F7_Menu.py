from F7_Automate import *

global i
i = 0

def display_principal_menu():
    print("Menu Principal:")
    print("1. Choisir un automate :")
    print("2. Quitter")
    choice = input("Votre choix : ")
    print()
    if choice == "1":
        display_menu_choix_automate()
    elif choice == "2":
        print("Aurevoir !")
        return False
    else:
        print("Votre choix n'existe pas !")
        display_principal_menu()

def display_menu_choix_automate():
    print("Menu Choix de l'automate:")
    while True:
        choice = input("1. Quel automate voulez-vous choisir ? \nAutomate n°")
        if int(choice) < 1 or int(choice) > 44:
            print("Votre choix n'existe pas !")
        else:
            break
    auto = 'F7-'+choice+'.txt'
    global var
    var = Automate(auto)
    display_menu_choix_option(i)

def display_menu_choix_option(i):
    print()
    print("Menu des choix des options:")
    print("1. Affichage de l'automate")
    print("2. Standardisation de l'automate")
    print("3. Déterminisation et complétion")
    print("4. Reconnaissance de mots")
    print("5. Language complémentaire")
    print("0. Retour au menu principal")
    choice = input("Votre choix : ")
    print()
    if choice == "0":
        display_principal_menu()
    elif choice == "1":
        var.affichage()
        display_menu_choix_option(i)
    elif choice == "2":
        if not var.est_standart():
            var.standardisation()
        else:
            print("Automate est déjà standart")
        display_menu_choix_option(i)
    elif choice == "3":
        if not var.est_deterministe():
            var.determinisation()
        else:
            if var.est_complet():
                print("Automate est déjà deterministe et complet")
            else:
                print("Automate est déjà deterministe mais pas complet")
                a = input("voulez vous le completer ?\n1. oui\n2. non\n")
                if a == "1":
                    var.completion()
        if not var.est_complet():
            var.completion()
        i = 1
        display_menu_choix_option(i)
    elif choice == "4":
        if i == 1:
            mot = input("Quels mot voulez-vous trouver : ")
            resultat = var.test_mot(mot)
            if resultat:
                print("Le mot", mot, "existe dans cette automate")
            else:
                print("Le mot", mot, "n'existe pas dans cette automate")
        else:
            print("Veuillez d'abord déterminiser l'automate avant de selectionner cette option")
        display_menu_choix_option(i)
    elif choice == "5":
        if i == 1:
            display_menu_language_compl()
        else:
            print("Veuillez d'abord déterminiser l'automate avant de selectionner cette option")
            display_menu_choix_option(i)
    else:
        print("Votre choix n'existe pas !")
        display_menu_choix_option(i)

def display_menu_language_compl():
    print("Menu du language complémentaire:")
    print("1. Utiliser l'automate déterminiser")
    print("0. Retour au menu principal")
    choice = input("Votre choix : ")
    print()
    if choice == "0":
        display_menu_choix_option(i)
    elif choice == "1":
        complement = var.complement_language()
        complement.affichage()
        display_menu_choix_option(i)
    else:
        print("Votre choix n'existe pas !")
        display_menu_language_compl()
