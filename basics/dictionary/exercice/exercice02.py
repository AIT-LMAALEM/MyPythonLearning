#operation sur les dictionnaire
#égalité == : True ssi les dic A et B ont exactement les même clé et valeurs
# !=    : True ssi les dic A et B contiennet des clés ou des valeurs différents
A={
    "math":15,
    "pc":16,
    "info":18,
   }
B={
    "pc":16,
    "math":14,
    "info":20
}
print(A!=B)
B["info"]=18
B["math"]=15
print(A==B)

# | :permet de fusionner deux dic
dict1={"nom":"lina","prenom":"radi","age":18}
dict2={"age":20,"filière":"gestion"}
print(dict1|dict2)

# =|: mettre à jour un dictionnaire en fusionnant un autre dic avec lui





