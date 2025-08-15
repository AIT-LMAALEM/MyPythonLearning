# les dict imbriqués
D={
    "matières":{
                "salle 1":"math",
                "salle 2":"info",
                },
    "maroc":{
            "capitale":"rabat",
            "population":"37.67M",
             },
    "langage":{ 
                1:"python",
               "web":{
                      1:"html",
                      2:"css",
                      3:"js",
                      },
                2:"C++",
              },
                
  }

etudinats={
    "yassine":{"age":19, "filière":"informatique","note":16,},
    "asmaa":{"age":18, "filière":"math", "note":17,},
    "lina":{"age":20, "filière":"gestion","note":15},
}


print(etudinats["yassine"])
print(etudinats["yassine"]["age"])
print(D["langage"]["web"][3])


# ajouter des éléments dans un dict imbriqué
etudinats["yassine"]["adresse"]="rabat"
etudinats["asmaa"]["note"]=19
del etudinats["lina"]["note"]
# print(etudinats)


# with loops

for etudiant, sous_dic in etudinats.items():
    print(f"l'etudiant {etudiant}:")
    for key,value in sous_dic.items():
        print(f" {key} :{value}")
    print("\n")


print(etudinats["asmaa"].get("filière","inconnue"))
etudinats.update({"radi":{"age":19, "filière":"pc", "note":17}})

print(etudinats)