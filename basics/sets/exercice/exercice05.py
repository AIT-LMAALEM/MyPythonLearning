#programme qui supprime tous les nombres entiers d'un ensemble
# K={11 , 1.5 , 4 , 3.14 , 16 , 1.42}
# for i in list(K):
#     if type(i)==int:
#         K.remove(i)
# print(K)



#programme qui compte le nombre de voyelles dans un texte
# voyelles={"a","e","i","o","u","y"}
# texte=input("entrer un texte:").lower()
# count=0
# for x in texte:
#     if x in voyelles:
#         count+=1
# print("le nombre de voyelles dans le texte est:",count)


#programme qui affiche les mots qui composent un texte saisi par l'utilisateur
# texte1=input("entrer un texte:").split(" ")
# print("les mots qui composent le texte sont:")
# print(set(texte1))

#programme qui affiche les mots qui composent un texte saisi par l'utilisateur
texte2=input("entrer un texte:")
list_texte2=texte2.split()
sans_espace=""
for i in list_texte2:
    sans_espace+=i
print("les caractères qui composent le texte est:",set(sans_espace))


#methode 2
texte = "  Bonjour le  monde  !  "
texte_sans_espaces = ""

for caractere in texte:
    if caractere != " ":  # Si le caractère n'est pas un espace
        texte_sans_espaces += caractere  # On l'ajoute à la nouvelle chaîne

print(set(texte_sans_espaces) ) 

#methode 3
texte = "  Bonjour le  monde  !  "
texte_sans_espaces = texte.replace(" ", "")
print(set(texte_sans_espaces) ) 

#methode 4
texte = "  Bonjour le  monde  !  "
texte_sans_espaces = "".join(texte.split())
print(set(texte_sans_espaces) )     


