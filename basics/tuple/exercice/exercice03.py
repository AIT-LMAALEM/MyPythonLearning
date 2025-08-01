# appartenir à un tuple
amis=("anouar","soufiane","rida","safae","rania")
note=(17,12,11,18,12)
if "mhamed" in amis:
    print("mhamed in tuple")
else:
    print("mhamed not in tuple")

#parcourir un tuple
t=tuple(range(1,100,10))
for num in t:
    print(num)

#methode 2
for i in range(len(t)):
    print("le nombre ",i+1,"est :",t[i])

#methode 3
for i,num in enumerate(t,1):
    print("le nombre ",i,"est:",num)

#methode 4
for nom,n in zip(amis,note):
    print("la note de ",nom,"est :",n)

