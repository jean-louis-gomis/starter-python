# Créer un programme job11.py qui parcourt le contenu du fichier “domains.xml” et qui
# compte le nombre d’extension de domaines qui s’y trouvent (.com, .net, etc ...).

# file = open("domains.xml", "r")
# read_data = file.read()
# per_word = read_data.split()

# print('domain', len(per_word))


from xml.dom import minidom

doc = minidom.parse('domains.xml')
elements = doc.getElementsByTagName("column")
newlist = []

for element in elements:
    if element.getAttribute("name") == "domain":
        newlist.append(element.childNodes[0].data)

print(len(newlist))
