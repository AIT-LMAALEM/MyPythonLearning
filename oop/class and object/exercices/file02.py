class Book:

    def __init__(self,title,auther,pages):                     #magic method
        self.title=title
        self.auther=auther
        self.pages=pages
        
new_book= Book("Origin","San Brown", 564)

print(new_book.title)

seconde_book= Book("the 142","Rayan sallin",100)

print(f"the seconde book title is {seconde_book.title}")


class Profile:
    def __init__(self,name,email,language):
        self.name=name
        self.email=email
        self.languge=language


user1= Profile("mhamed","mhamed@gmail.com","Python")

name2=input("enter your name:")
email2=input("enter your email:")
language2=input(" enter your language :")

user2=Profile(name2,email2,language2)


import datetime

class Message:
    def __init__(self, sender, receiver, text, timestamp):
        self.sender = sender
        self.receiver = receiver
        self.text = text
        self.timestamp = timestamp

# Saisie des données
sender = input("Entrez votre nom : ")
receiver = input("Entrez son nom : ")
text = input("Entrez le message : ")

# Création du message avec horodatage
timestamp = datetime.datetime.now()  # date + heure actuelle
message1 = Message(sender, receiver, text, timestamp)

# Affichage
print(f"Message de {message1.sender} à {message1.receiver} le {message1.timestamp} : {message1.text}")
print(f"Message de {message2.sender} à {message2.receiver} le {message2.timestamp} : {message2.text}")

