from Automate import *


auto7 = 'D7-6.txt'


a = Automate(auto7)

a.add_ligne([["0", "1"], ["0","3"]])
a.add_ligne([["-1"], ["-1"]])
a.add_ligne([["-1"], ["3"]])
a.add_ligne([["3"], ["-1"]])


"""a.affichage()"""



b = Automate(auto7)

b.add_ligne([["1"], ["2"]])
b.add_ligne([["0"], ["-1"]])
b.add_ligne([["-1"], ["2"]])
b.add_ligne([["3"], ["-1"]])

b.test1(["E"," "," ","S"])

b.affichage()

b.standardisation()

b.affichage()
