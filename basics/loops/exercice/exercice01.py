# names=input("Enter the first and the last name of your friends separated by a comma:").split(", ")
# abriv_list=[]
# for name in names:
#     name_p=name.split()
#     print(name_p)
#     first_name=name_p[0]
#     seconde_name=name_p[1]
#     abriv=first_name[0]+"."+seconde_name[0]+"."
#     abriv_list.append(abriv)

# for i in abriv_list:
#     print(i)




sentence=input("Eenter a sentence:")
print("h".join(sentence[::-1]))