# Créer un programme job13.py qui demande à l’utilisateur de renseigner un nombre
# entier. Le programme devra alors parcourir le contenu du fichier “data.txt” compter le
# nombre de mots de la taille renseignée qui s’y trouvent.

# texte = input("quel est votre nombre ? : ")

# fichier = open("outpout.txt", "w")

nombre = int(input("entrer un nombre entier : "))

with open("data.txt", "r") as fichier:
    lines = fichier.read()

liste = lines.split() 
nb_words = 0

for element in liste:
    if len(element) == nombre:
        nb_words = nb_words + 1

print(nb_words)