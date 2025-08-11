# contact management
contact={}
def ajouter(nom,num_tele):
    if nom in contact:
        print("Ce contact existe déja!")
    else:
        contact.update({nom:num_tele})
        print("Contact ajouté avec succés!")
def Recherche(nom):
    if nom in contact:
        print(f"Numero de téléphone de {nom.capitalize()} : {contact[nom]} ")
    else:
        print("Contact non trouvé")
def Supprimer(nom):
    if nom in contact:
        del contact[nom]
        print(f" {nom.capitalize()} est supprimer avec succès!")
    else:
        print("Contact non trouvé")
def Afficher():
    if contact:
        print("contact:")
        for nom, num_tele in contact.items():
            print(f"{nom.capitalize()}:{num_tele}")
    else:
        print("Aucun Contact à Afficher")


number_choice=[1,2,3,4,5]
print("********contact management*********")
print("""
      1. Ajouter un contact
      2. Rechercher un contact
      3. Supprimer un contact
      4. Afficher tous les contacts
      5. Quitter      """)
while True:
    choix=input("Entrer votre choix:")
    if choix.isdigit():
        choix= int(choix)
        if choix ==1:
           nom=input("Entrer le nom:").lower()
           num_tele=input("Entrer le téléphone:")
           ajouter(nom,num_tele)
        elif choix ==2:
           nom=input("Entrer le nom à Rechercher :").lower()
           Recherche(nom)
        elif choix==3:
           nom=input("Entrer le nom à Supprimer :").lower()
           Supprimer(nom)
        elif choix ==4:
           Afficher()
        else:
           print("Au revoir!")
           break
    else:
        print(" choix incorrect! ")



