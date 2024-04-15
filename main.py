from Automate import *

a = Automate()

a.add_ligne([["0", "1"], ["0","4"], ["0"]])
a.add_ligne([["-1"], ["-1"], ["2"]])
a.add_ligne([["-1"], ["3"], ["-1"]])
a.add_ligne([["3"], ["-1"], ["-1"]])
a.add_ligne([["-1"], ["-1"], ["2"]])

a.add_alphabet("a")
a.add_alphabet("b")
a.add_alphabet("c")

a.affichage()


