# fonction et méthodes
# création
# zip(): crée in dic en combinant deux sequences l'une contenant les clés et l'autre contenant les valeurs
# nom_dict=dict(zip(clés,valuer))
clés=["nom","prix","quantit_stock"]
valeurs=["iphone 14",999,25]
print(dict(zip(clés,valeurs)))

#fromkeys() :crée in dic à partir d'une séquence de clés en associant à chaque clé une valeur par défaut
voyelles=['a','e','i','o','u']
valeur="voyelle"
voyelles_dic=dict.fromkeys(voyelles,valeur)
print(voyelles_dic)


#Accés
#get() : acces à une valeur sans générer d'erreur si la clé n'existe pas
print(voyelles_dic.get('y',"la valeur n'existe pas"))



#ajout
#update() 
book={
    "title":"Red Queen",
    "auther":"Victoria Avryard",
    "year":2015,
    "pages":383,
    "is many": True,
    "rating":4.1,
}
book.update({"chapters":12})
print(book)
# book.update(voyelles_dic)
# print(book)


# remove:
# pop(): peut supprimer une clé et de retourner la valeur associée à cette clé
print(book.pop("is many"))

#popitem(): supprimer et renvoie la dernière paire clé-valeur
print(book.popitem())

# clear(): suppimer toutes les paires clé-valeur 
print(voyelles_dic.clear())

# del :permet de supprimer  une clé et sa valeur 
del book["rating"]
print(book)



# len(): le nombre de paires dans un dic

