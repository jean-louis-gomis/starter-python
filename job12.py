# Créer un programme job12.py qui parcourt le contenu du fichier “data.txt” et qui compte
# le nombre nombre de mots (sans caractère spéciaux) qui s’y trouvent.


# file = open("data.txt", "r")
# read_data = file.read()
# per_word = read_data.split()
# Total = '\w'
# print("Total" " de mots sans caractère spéciaux =", len(per_word))




import re

fichier = open("data.txt", "r")
text = fichier.read()
pattern = '[a-zA-Z]+'
matches = re.findall(pattern, text)

print(len(matches))