# C'est qoui? :  les elements d'un dictionnaire sont des paires clé-valeur
# on peut ajouter, modifier ou supprimer des clé-valeur après la création d'un dictionnaire
# chaque key(clé) est unique et associe à une valeur. si nous stockons une valeur avec une clé qui existe deja la valeur la plus récente remplacera l'ancienne valeur
# chaque element est accessible via sa clé, un dictonnaire peut contenir differents types de valeurs
# les valeurs peuvent se repeter 


#création
user_info={
    "name":"Sam",
    "age":30,
    "taille":1.70,
    "email":"sam@gmail.com",
}

book={
    "title":"Red Queen",
    "auther":"Victoria Avryard",
    "year":2015,
    "pages":383,
    "is many": True,
    "rating":4.1,
}

D={

}
capitales=dict(france="paris" , japon="tokyo",canada="ottawa")

# Accés
user_info["taille"]=172
user_info["email"]="sam13@gmail.com"
print(user_info)
print(user_info["age"])
print(user_info.get("name"))
print(user_info.get("profession","inconnue"))
print(user_info.get("email","la clé n'existe pas"))

print(user_info.keys())
print(user_info.values())
print(user_info.items())


#exemple
informations={}
print("veuillez saisie les informations d'inscription:")
informations["nom"]=input("votre nom:")
informations["prenom"]=input("votre prénom:")
informations["age"]=int(input("votre âge:"))
informations["filiere"]=input("votre filière:")
print(informations)
print(informations.keys())
print(informations.values())

 

