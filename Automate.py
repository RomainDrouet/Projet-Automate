class Automate:

    def __init__(self, auto):
        self.automate = []
        with open(auto, 'r') as fichier:
            lignes = fichier.readlines()
        self.nb_alphabet = int(lignes[0].strip())
        self.nb_etat = int(lignes[1].strip())
        self.etat = []
        for i in range(self.nb_etat):
            self.etat.append(str(i))
        self.alphabet = [" ", "Etat"]
        for i in range(self.nb_alphabet):
            self.alphabet.append(chr(97 + i))
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
            elif sortie[i] == "S":
                self.entsor[i] = "S"
            elif entree[i] == "E":
                self.entsor[i] = "E"
        self.transition = liste_transitions
        self.nb_transition = int(lignes[6].strip())
        self.ent = ent
        self.creer_liste()

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
        for i in range(len(self.automate[0]) + 1):
            print(hor * 7, end="")
            print(T, end="")
        print(hor * 7, end="")
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
        for i in range(len(self.automate) - 1):
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
                compteur += len(self.automate[i][j]) - 1
                for k in range(len(self.automate[i][j])):
                    compteur += len(self.automate[i][j][k])
                print(" " * (3 - compteur // 2), end="")
                for k in range(len(self.automate[i][j])):
                    if self.automate[i][j][k] == "-1":
                        print('--', end="")
                    else:
                        print(self.automate[i][j][k], end="")
                    if len(self.automate[i][j]) > 1 and k != len(self.automate[i][j]) - 1:
                        print(",", end="")
                if compteur % 2 != 0:
                    print(" " * (3 - compteur // 2), end="")
                else:
                    print(" " * (4 - compteur // 2), end="")
                print(ver, end="")
            print()

            """ligne de jonction"""
            print(t, end="")
            for k in range(len(self.automate[0]) + 1):
                print(hor * 7, end="")
                print(croix, end="")
            print(hor * 7, end="")
            print(l)
        print(ver, end="")

        """Derniere ligne de l'automate"""
        """Affichage E/S"""
        print(" " * 3, end="")
        print(self.entsor[len(self.entsor) - 1], end="")
        print(" " * 3, end="")
        print(ver, end="")

        """Affichage Etat"""
        print(" " * 2, end="")
        print(self.etat[len(self.etat) - 1], end="")
        print(" " * 4, end="")
        print(ver, end="")
        """Derniere ligne de l'automate"""
        for j in range(len(self.automate[len(self.automate) - 1])):
            compteur = 0
            for k in range(len(self.automate[len(self.automate) - 1][j])):
                compteur = len(self.automate[len(self.automate) - 1][j][k]) + len(
                    self.automate[len(self.automate) - 1][j]) - 1
            print(" " * (3 - compteur // 2), end="")
            for k in range(len(self.automate[len(self.automate) - 1][j])):
                if self.automate[len(self.automate) - 1][j][k] == "-1":
                    print('--', end="")
                else:
                    print(self.automate[len(self.automate) - 1][j][k], end="")
                if len(self.automate[len(self.automate) - 1][j]) > 1 and k != len(
                        self.automate[len(self.automate) - 1][j]) - 1:
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

    def est_standart(self):
        if len(self.ent) == 1:
            for i in range(len(self.automate)):
                for j in range(len(self.automate[i])):
                    for k in range(len(self.automate[i][j])):
                        for ent in self.ent:
                            if self.automate[i][j][k] == str(ent):
                                return False
            return True
        return False

    def est_deterministe(self):
        if len(self.ent) == 1:
            for i in range(len(self.automate)):
                for j in range(len(self.automate[i])):
                    if len(self.automate[i][j]) > 1:
                        return False
            return True
        return False

        def est_complet(self):
            for i in range(len(self.automate)):
                for j in range(len(self.automate[i])):
                    for k in range(len(self.automate[i][j])):
                        if self.automate[i][j][k] == '-1':
                            return False

        return True

    def completion(self):
        val = len(self.etat)
        self.etat.append(str(val))
        for i in range(len(self.automate)):
            for j in range(len(self.automate[i])):
                for k in range(len(self.automate[i][j])):
                    if self.automate[i][j][k] == '-1':
                        self.automate[i][j][k] = str(val)
        tmp = []
        for i in range(self.nb_alphabet):
            tmp.append([str(val)])
        self.automate.append(tmp)
        self.entsor.append(" ")

    def determinisation(self):
        deterministe = []
        tmp = []
        etat = []
        tmpprime = ''
        for i in range(len(self.entsor)):
            if self.entsor[i] == "E" or self.entsor[i] == "E/S":
                tmp.append(str(i))
        for i in range(len(tmp)):
            tmpprime += tmp[i]
        etat.append(tmpprime)
        liaison = []
        for i in range(self.nb_alphabet):
            temp = ''
            tempo = []
            for j in range(len(tmp)):
                if self.automate[int(tmp[j])][i] != ['-1']:
                    for k in range(len(self.automate[int(tmp[j])][i])):
                        double = 0
                        for z in range(len(temp)):
                            if self.automate[int(tmp[j])][i][k] == temp[z]:
                                double = 1
                        if double == 0:
                            temp += self.automate[int(tmp[j])][i][k]
            if temp == '':
                temp = '-1'
            tempo.append(temp)
            liaison.append(tempo)
        deterministe.append(liaison)
        repeat = 1
        while repeat == 1:
            repeat = 0
            for i in range(len(deterministe)):
                for j in range(len(deterministe[i])):
                    for k in range(len(deterministe[i][j])):
                        val = 0
                        tmpprime = ''
                        tmp = deterministe[i][j]
                        for l in range(len(tmp)):
                            tmpprime += tmp[l]
                        for h in range(len(etat)):
                            if deterministe[i][j][k] == etat[h] or deterministe[i][j][k] == '-1':
                                val = 1
                            elif tmpprime == etat[h]:
                                val = 1
                        if val == 0:
                            repeat = 1
                            etat.append(tmpprime)
                            liaison = []
                            for l in range(self.nb_alphabet):
                                vide = 0
                                temp = ''
                                tempo = []
                                for m in range(len(tmp)):
                                    if len(tmp[m]) != 1:
                                        for o in range(len(tmp[m])):
                                            if self.automate[int(tmp[m][o])][l] != ['-1']:
                                                for n in range(len(self.automate[int(tmp[m][o])][l])):
                                                    double = 0
                                                    for z in range(len(temp)):
                                                        if self.automate[int(tmp[m][o])][l][n] == temp[z]:
                                                            double = 1
                                                    if double == 0:
                                                        temp += self.automate[int(tmp[m][o])][l][n]
                                                vide = 1
                                    elif self.automate[int(tmp[m])][l] != ['-1']:
                                        for n in range(len(self.automate[int(tmp[m])][l])):
                                            double = 0
                                            for z in range(len(temp)):
                                                if self.automate[int(tmp[m])][l][n] == temp[z]:
                                                    double = 1
                                            if double == 0:
                                                temp += self.automate[int(tmp[m])][l][n]
                                        vide = 1
                                    if vide == 1:
                                        tempo.append(temp)
                                        liaison.append(tempo)
                                if vide == 0:
                                    liaison.append(['-1'])
                            deterministe.append(liaison)
        type_etat_L = []
        self.automate = deterministe
        for i in range(len(etat)):
            type_etat = ''
            for j in range(len(etat[i])):
                if type_etat == '':
                    if self.entsor[int(etat[i][j])] != " ":
                        type_etat += self.entsor[int(etat[i][j])]
                elif type_etat == 'E' and self.entsor[int(etat[i][j])] == 'S':
                    type_etat = 'E/S'
                elif type_etat == 'E' and self.entsor[int(etat[i][j])] == 'E/S':
                    type_etat = 'E/S'
                elif type_etat == 'S' and self.entsor[int(etat[i][j])] == 'E':
                    type_etat = 'E/S'
                elif type_etat == 'S' and self.entsor[int(etat[i][j])] == 'E/S':
                    type_etat = 'E/S'
            if type_etat == '':
                type_etat = " "
            if i != 0 and type_etat == 'E':
                type_etat = ''
            elif i != 0 and type_etat == 'E/S':
                type_etat = 'S'
            type_etat_L.append(type_etat)
        self.entsor = type_etat_L
        self.ent = [0]
        for i in range(len(self.automate)):
            for j in range(len(self.automate[i])):
                for k in range(len(self.automate[i][j])):
                    change = 0
                    for l in range(len(etat)):
                        if self.automate[i][j][k] == etat[l] and change == 0:
                            change = 1
                            self.automate[i][j][k] = str(l)
        self.etat = etat
        for l in range(len(etat)):
            self.etat[l] = str(l)

    def standardisation(self):
        """fait un etat inital et standardise"""
        self.etat.insert(0, "i")
        tmp = []
        for i in range(len(self.entsor)):
            if self.entsor[i] == "E" or self.entsor[i] == "E/S":
                tmp.append(str(i))
        self.automate.insert(0, [])
        for i in range(self.nb_alphabet):
            self.automate[0].append([])
            ajoute = []
            for j in range(len(tmp)):
                if self.automate[int(tmp[j]) + 1][i] != ["-1"]:
                    for k in range(len(self.automate[int(tmp[j]) + 1][i])):
                        ajoute.append(self.automate[int(tmp[j]) + 1][i][k])
            for j in range(len(ajoute)):
                self.automate[0][i].append(ajoute[j])

        """Met a jour les differentes listes"""
        for i in range(len(self.entsor)):
            if self.entsor[i] == "E":
                self.entsor[i] = " "
        self.entsor.insert(0, "E")
        self.ent = [0]
        self.retablir_etat()

    def test_mot(self, mot):
        for i in range(len(mot)):
            valide = 0
            for j in range(len(self.alphabet) - 2):
                if mot[i] == self.alphabet[j + 2]:
                    valide = 1
            if valide == 0:
                print("rater")
                return False
        path = 0
        while self.entsor[path] != 'E' and self.entsor[path] != 'E/S':
            path += 1
        next = 0
        for i in range(len(mot)):
            for j in range(len(self.alphabet) - 2):
                if mot[i] == self.alphabet[j + 2]:
                    next = j
            path = int(self.automate[path][next][0])
            print(path)
        if self.entsor[path] == 'S' or self.entsor[path] == 'E/S':
            return True
        else:
            return False

    def retablir_etat(self):
        self.automate = self.incrementer_liste(self.automate)
        for i in range(len(self.etat)):
            self.etat[i] = str(i)

    def incrementer_liste(self, liste):
        nouvelle_liste = []
        for sous_liste in liste:
            nouvelle_sous_liste = []
            for valeur in sous_liste:
                if valeur != ['-1']:
                    nouvelle_valeur = [str(int(i) + 1) for i in valeur]
                    nouvelle_sous_liste.append(nouvelle_valeur)
                else:
                    nouvelle_sous_liste.append(valeur)
            nouvelle_liste.append(nouvelle_sous_liste)
        return nouvelle_liste

    def creer_liste(self):
        tableau = []
        for i in range(self.nb_etat):
            tableau.append([])
            for j in range(self.nb_alphabet):
                tableau[i].append(['-1'])
        for i in range(len(self.transition)):
            x = 0
            deb = ""
            mil = ""
            fin = ""
            for j in range(len(self.transition[i])):
                if ord(self.transition[i][j]) >= 48 and ord(self.transition[i][j]) <= 57 and x == 0:
                    deb = self.transition[i][:j + 1]
                else:
                    x = 1
                if ord(self.transition[i][j]) >= 97 and ord(self.transition[i][j]) <= 122:
                    mil = self.transition[i][j]
                if ord(self.transition[i][j]) >= 48 and ord(self.transition[i][j]) <= 57 and x == 1:
                    fin = self.transition[i][j:]
                    x = 2
            mil = ord(mil) - 97
            if tableau[int(deb)][mil] == ['-1']:
                tableau[int(deb)][mil] = [fin]
            else:
                tableau[int(deb)][mil].append(fin)
        self.automate = tableau