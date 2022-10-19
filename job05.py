# n1 = int(input ("Valeur 1 : "))
# n2 = int(input ("Valeur 2 : "))

# for i in range(n1+1, n2) :
#    print (i , end="\n")
# for i in range(n2+1, n1) :
#    print (i , end="\n")
# if (n1 == n2) :
#    print ("Valeurs égales")n


Valeur1 = int(input ("Valeur 1 : "))
Valeur2 = int(input ("Valeur 2 : "))

if Valeur1 < Valeur2:
    for i in range(Valeur1, Valeur2 - 1 , 1):
     Valeur1 = Valeur1 + 1
     print (Valeur1)
elif Valeur1 > Valeur2:
    for i in range(Valeur1, Valeur2 - 1, -1):
     Valeur1 = Valeur1 - 1
     print (Valeur1)
else:
    print ("Valeurs égales")