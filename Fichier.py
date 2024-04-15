# Ouvrir le fichier en mode lecture
auto7 = 'D7-6.txt'
with open(auto7, 'r') as fichier:
    # Lire toutes les lignes du fichier
    lignes = fichier.readlines()

# Nombre de symboles
nombre_symboles = int(lignes[0].strip())

# Nombre d'états
nombre_etats = int(lignes[1].strip())
etat = []
for i in range(nombre_etats):
    etat.append(i)
print(etat)

ent = list(map(int, lignes[3].strip().split()))
sor = list(map(int, lignes[5].strip().split()))

nombre_transitions = int(lignes[6].strip())

liste_transitions = []

for i in range(7, len(lignes)):
    transition = lignes[i].strip()
    liste_transitions.append(transition)

print("Nombre de symboles:", nombre_symboles)
print("Nombre d'états:", nombre_etats)
print(ent)
print(sor)
print("Nombre de transitions:", nombre_transitions)
print("Liste des transitions:")
for transition in liste_transitions:
    print(transition)
