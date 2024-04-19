class Automate:

    def __init__(self):
        self.automate = []
        self.alphabet = [" ", "Etat"]
        self.entsor = ["E", " ", " ", "S", "S"]
        self.etat = [0, 1, 2, 3, 4]

    def affichage(self):
        supg = '┌'
        supd = '┐'
        infg = '└'
        infd = '┘'
        hor = '─'
        ver = '│'
        T = '┬'
        t = '├'
        croix = "┼"
        l = "┤"
        L = "┴"

        """Premiere ligne"""
        print(supg, end="")
        for i in range(len(self.automate[0])+1):
            print(hor*7, end="")
            print(T, end="")
        print(hor*7, end="")
        print(supd)
        print(ver, end="")

        """Alphabet"""
        for i in range(len(self.alphabet)):
            if len(self.alphabet[i]) > 1:
                print(" " * 1, end="")
                print(self.alphabet[i], end="")
                print(" " * 2, end="")
                print(ver, end="")
            else:
                print(" " * 3, end="")
                print(self.alphabet[i], end="")
                print(" " * 3, end="")
                print(ver, end="")
        print()

        """Affichage de l'automate sauf la derniere ligne"""
        print(t, end="")
        for i in range(len(self.automate[0]) + 1):
            print(hor * 7, end="")
            print(croix, end="")
        print(hor * 7, end="")
        print(l)
        for i in range(len(self.automate)-1):
            print(ver, end="")

            """Affichage E/S"""
            print(" " * 3, end="")
            print(self.entsor[i], end="")
            print(" " * 3, end="")
            print(ver, end="")

            """Affichage Etat"""
            print(" " * 2, end="")
            print(self.etat[i], end="")
            print(" " * 4, end="")
            print(ver, end="")

            for j in range(len(self.automate[i])):
                compteur = 0
                compteur +=  len(self.automate[i][j])-1
                for k in range(len(self.automate[i][j])):
                    compteur += len(self.automate[i][j][k])
                print(" " * (3-compteur//2), end="")
                for k in range(len(self.automate[i][j])):
                    if self.automate[i][j][k] == "-1":
                        print('--', end="")
                    else:
                        print(self.automate[i][j][k], end="")
                    if len(self.automate[i][j]) > 1 and k != len(self.automate[i][j])-1:
                        print(",", end="")
                if compteur % 2 != 0:
                    print(" " * (3-compteur//2), end="")
                else:
                    print(" " * (4 - compteur // 2), end="")
                print(ver, end="")
            print()

            """ligne de jonction"""
            print(t, end="")
            for k in range(len(self.automate[0])+1):
                print(hor*7, end="")
                print(croix, end="")
            print(hor * 7, end="")
            print(l)
        print(ver, end="")

        """Derniere ligne de l'automate"""
        """Affichage E/S"""
        print(" " * 3, end="")
        print(self.entsor[len(self.entsor)-1], end="")
        print(" " * 3, end="")
        print(ver, end="")

        """Affichage Etat"""
        print(" " * 2, end="")
        print(self.etat[len(self.etat)-1], end="")
        print(" " * 4, end="")
        print(ver, end="")
        """Derniere ligne de l'automate"""
        for j in range(len(self.automate[len(self.automate)-1])):
            compteur = 0
            for k in range(len(self.automate[len(self.automate)-1][j])):
                compteur = len(self.automate[len(self.automate)-1][j][k]) + len(self.automate[len(self.automate)-1][j]) - 1
            print(" " * (3 - compteur // 2), end="")
            for k in range(len(self.automate[len(self.automate)-1][j])):
                if self.automate[len(self.automate)-1][j][k] == "-1":
                    print('--', end="")
                else:
                    print(self.automate[len(self.automate)-1][j][k], end="")
                if len(self.automate[len(self.automate)-1][j]) > 1 and k != len(self.automate[len(self.automate)-1][j]) - 1:
                    print(",", end="")
            if compteur % 2 != 0:
                print(" " * (3 - compteur // 2), end="")
            else:
                print(" " * (4 - compteur // 2), end="")
            print(ver, end="")
        print()
        print(infg, end='')
        for k in range(len(self.automate[0]) + 1):
            print(hor * 7, end="")
            print(L, end="")
        print(hor * 7, end="")
        print(infd)

    def add_ligne(self, automate):
        self.automate.append(automate)

    def add_alphabet(self, alphabet):
        self.alphabet.append(alphabet)

    def created_tab(self, nb_etat, nb_alphabet):
        tableau = [[-1] * nb_etat for _ in range(nb_etat)]
        for i in range(len(self.automate)):
            for j in range(len(self.automate[i])):
                etat_depart = self.automate[i][j][0]
                symbole = self.automate[i][j][1]
                etat_arrivee = self.automate[i][j][2]
                index_etat = self.etat.index(etat_arrivee)
                index_symbole = self.alphabet.index(symbole)
                tableau[index_etat][index_symbole] = etat_depart[index_etat][index_symbole] = etat_arrivee
        return tableau

    def complement_language(self):
        #Création d'une nouvelle instance de l'automate pour stocler le complémentaire
        complement = Automate()
        #Copie des données de l'automate d'origine
        complement.automate = self.automate #Copie des transition
        complement.alphabet = self.alphabet #Copide de l'alphabet
        complement.etat = self.etat # Copie des états
        #Inversion des états terminaux et non terminaux
        for i in range(len(self.etat)):
            if self.sort[i]=="S": #test si l'état était terminal
                complement.sort[i] == " " #le rendre non terminal dans le complémentaire
            else:
                complement.sort[i] = "S" #le rendre complémentaire si il ne l'était pas avant

        return complement