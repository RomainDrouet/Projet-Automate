class Automate:

    def __init__(self, auto):
        self.automate = []
        with open(auto, 'r') as fichier:
            lignes = fichier.readlines()
        self.nb_alphabet = int(lignes[0].strip())
        self.nb_etat = int(lignes[1].strip())
        self.etat = []
        for i in range(self.nb_etat):
            self.etat.append(i)
        self.alphabet = [" ", "Etat"]
        for i in range(self.nb_alphabet):
            self.alphabet.append(chr(97+i))
        liste_transitions = []
        for i in range(7, len(lignes)):
            transition = lignes[i].strip()
            liste_transitions.append(transition)
        ent = list(map(int, lignes[3].strip().split()))
        sor = list(map(int, lignes[5].strip().split()))
        entree = []
        sortie = []
        self.entsor = []
        for i in range(len(self.etat)):
            self.entsor.append(" ")
        for i in range(len(self.etat)):
            entree.append(" ")
        for i in range(len(self.etat)):
            sortie.append(" ")
        for i in range(len(ent)):
            entree[ent[i]] = "E"
        for i in range(len(sor)):
            sortie[sor[i]] = "S"
        for i in range(len(self.etat)):
            if sortie[i] == "S" and entree[i] == "E":
                self.entsor[i] = "E/S"
            elif sortie[i] == "S" :
                self.entsor[i] = "S"
            elif entree[i] == "E" :
                self.entsor[i] = "E"
        self.transition = liste_transitions
        self.nb_transition = int(lignes[6].strip())


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
