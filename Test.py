from Automate import *
def display_principal_menu():
    print("Menu Principal:")
    print("1. Choisir un automate :")
    print("2. Quitter")
    choice = input("Votre choix : ")
    if choice == "1":
        display_menu_choix_automate()
    elif choice == "2":
        print("Aurevoir !")
    else:
        print("Votre choix n'existe pas !")
        display_principal_menu()
def display_menu_choix_automate():
    print("Menu Choix de l'automate:")
    while True:
        choice = input("1. Quel automate voulez-vous choisir ? ")
        if choice.lower() < "1" or choice.lower() > "44":
            print("Votre choix n'existe pas !")
        else:
            break
        auto = 'F7-'+choice+'.txt'
        global var
        var = Automate(auto)
        display_menu_choix_option(i)

global i
i=0
def display_menu_choix_option(i):
    print("Menu des choix des options:")
    print("1. Affichage de l'automate")
    print("2. Standardisation de l'automate")
    print("3. Déterminisation et complétion")
    print("4. Minimisation")
    print("5. Reconnaissance de mots")
    print("6. Language complémentaire")
    print("0. Retour au menu principal")
    choice = input("Votre choix : ")
    if choice == "0":
        display_principal_menu()
    elif choice == "1":
        var.affichage()
        display_menu_choix_option(i)
    elif choice == "2":
        var.standardisation()
        display_menu_choix_option(i)
    elif choice == "3":
        var.determinisation()
        i=1
        display_menu_choix_option(i)
    elif choice == "4":
        if i==1:
            print("Choix indisponible pour le moment veuillez réessayer ultérieurement")
            display_menu_choix_option(i)
        else:
            print("Veuillez d'abord déterminiser l'automate avant de selectionner cette option")
            display_menu_choix_option(i)
    elif choice == "5":
        print("Choix indisponible pour le moment veuillez réessayer ultérieurement")
        display_menu_choix_option(i)
    elif choice == "6":
        if i==1:
            display_menu_language_compl()
        else:
            print("Veuillez d'abord déterminiser l'automate avant de selectionner cette option")
            display_menu_choix_option(i)
    else:
        print("Votre choix n'existe pas !")
        display_menu_choix_option()
def display_menu_language_compl():
    print("Menu du language complémentaire:")
    print("1. Utiliser l'automate déterminiser")
    print("2. Utiliser l'automate minimiser")
    print("0. Retour au menu principal")
    choice = input("Votre choix : ")
    if choice == "0":
        display_menu_choix_option(i)
    elif choice == "1":
        var.complement_language()
        display_menu_choix_option(i)
    elif choice == "2":
        print("Option indisponible pour le moment veuillez réessayer ultérieurement")
        display_menu_choix_option(i)
    else:
        print("Votre choix n'existe pas !")
        display_menu_language_compl()
