hauteur = int(input("hauteur : "))
largeur = int(input("largeur : "))

side = "|"
seperator = "-"

for i in range (hauteur):
    if i == 0 or i == hauteur -1:
        separator = "-"
    else:
        separator = " "
    print(side + separator * largeur + side)

