# in / not in:  vérifier la presence d_une clé dans un dic 
A={
    "analyse":15,
    "algebre":16,
    "C":18,
    "thermo":19,
    "mecanique":17,
   }
if "thermo" in A:
    print("thermo in A")
else:
    print("thermo not in A")


for clé in A:
    print(clé)
for clé in A.keys():
    print(clé)
for valeur in A.values():
    print(valeur)

langages_pref={
    "mhamed":"c++",
    "adnane":"c#",
    "youssef":"python",
    "samir":"javascript"
}
for nom,langage in langages_pref.items():
    print(f"l'etudiat {nom} préfère le langage :{langage}")



#exemple:
resultats={}
number=int(input("Entrer le nombres des étudiant:"))
for i in range(number):
    nom=input(f"entrer le nom de l'etudiat {i+1}:" )
    note=float(input("entrer sa note:"))
    resultats[nom]=note
count=0
for nom,note in resultats.items():
    print(f"l'etudiant {nom} a obtenu une note de {note}")
    if note >=12:
        print(f" {nom} a réussi avec {note}")
        count +=1
print("le nombre totale des etudiant ayant réussi l'exam:",count)



