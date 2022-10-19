# Créer un programme job19.py. Le programme devra contenir une seule fonction qui
# prend en paramètres un nombre de paramètres indéfini (uniquement des nombres).
# La fonction devra :
# - Remplir une liste myList contenant tous ces paramètres.
# - Trier par ordre croissant la liste à l’aide de la fonction sort
# - Afficher la liste dans un terminal


permutation = True
passage = 0
# myList = []

while permutation == True:

    permutation = False
    passage = passage + 1

    for en_cours in range(0, len(myList) - passage):
        if myList[en_cours] > myList[en_cours + 1]:
            permutation = True
            # On echange les deux éléments
            myList[en_cours], myList[en_cours + 1] = \
            myList[en_cours +1], myList[en_cours]

print (myList)