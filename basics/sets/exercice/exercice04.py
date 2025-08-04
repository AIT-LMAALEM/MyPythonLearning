# pays={"maroc","egypt","algerie"}
# pays.add("souria")
# if "souria" in pays:
#     print("souria in pays")
# else:
#     print("souria not in pays")

# for pay in pays:
#     print(pay)

materiau={"bois","acier","béton","verre","plâte"}
choix=input("saisir un matériau :").lower()
if choix in materiau:
    print(choix," est disponible dans l'ensemble")
else:
    print(choix," n'est pas disponible dans l'ensemble")
materiau.update({"cuivre","aluminium","fer"})
print("Voici les elements de l'ensemble:")
for element in materiau:
    print(element)
supp=input("choisi un element de votre choix pour le supprimer:").lower()
materiau.remove(supp)

print("update:")
for element in materiau:
    print(element)
