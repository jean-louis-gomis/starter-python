

# N = (input("> "))
# bonj = "Bonjour"
# aur = "Aurevoir"

# if N == bonj :
#    print("Bonjour à toi")
# else :
#    N == aur
#    print ("Fermerture du script") 
#    quit()

while True:
    entree = input(">")

    if entree == "Bonjour" :
        print("Bonjour à toi")
    elif entree == "Aurevoir":
        exit()
    else :
        print(entree)