# Créer un programme job21.py. Reprenez l’exercice 19, mais modifiez le de façon à
# utiliser deux fonctions :
# - Une fonction mySort, qui prendra en paramètre une liste. Elle retourne une liste
# avec les valeurs de celle passée en paramètre, triés par ordre croissant.
# - Une fonction myDisplay qui prendra en paramètre une liste. Elle affichera dans le
# terminal le contenu de cette liste.


def mySort(liste):
    permutation = True
    passage = 0
    while permutation == True:
        permutation = False
        passage = passage + 1
        for en_cours in range(0, len(liste) - passage):
          if liste[en_cours] > liste[en_cours + 1]:
              permutation = True
              #On echange les deux éléments
              liste[en_cours], liste[en_cours + 1] = \
              liste[en_cours + 1], liste[en_cours]
              return liste


def myDisplay(liste2):
    print(liste2)

myDisplay(mySort([78,4,9,87,21]))
