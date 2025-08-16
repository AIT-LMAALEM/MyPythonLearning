import os
import time

def clear_screen():
    # Vide le terminal (compatible Windows et Unix)
    os.system("cls" if os.name == "nt" else "clear")

class Member:
    def __init__(self, first_name, last_name, ID, status="inactive"):
        # Initialise un membre avec prénom, nom, ID et statut (par défaut inactif)
        self.first_name = first_name
        self.last_name = last_name
        self.ID = ID
        self.status = status

    def display(self):
        # Affiche les informations du membre
        print(f"First name           : {self.first_name}")
        print(f"Last name            : {self.last_name}")
        print(f"Membership ID        : {self.ID}")
        print(f"Membership status    : {self.status}")
        print("_" * 30)  # ligne de séparation

def create_member():
    # Demande des informations à l'utilisateur pour créer un nouveau membre
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    ID = input("Enter the membership ID: ")
    status = input("Enter the membership status (active/inactive), or press Enter for default: ")
    if not status:
        # Si l'utilisateur ne renseigne rien, on met le statut à "inactive"
        status = "inactive"
    return Member(first_name, last_name, ID, status)

def search_member(new_members):
    clear_screen()
    print("Search by:")
    print("1. Membership ID")
    print("2. First name")
    print("3. Membership status\n")
    choice = input("Enter your choice: ")

    found_members = []

    if choice == "1":
        clear_screen()
        id_query = input("Enter the membership ID to search: ")
        time.sleep(1)
        # On cherche le premier membre dont l'ID correspond exactement
        for member in new_members:
            if member.ID == id_query:
                found_members.append(member)
                break

    elif choice == "2":
        clear_screen()
        fname_query = input("Enter the first name to search: ")
        # Ajoute tous les membres avec prénom identique (sensible à la casse)
        for member in new_members:
            if member.first_name == fname_query:
                found_members.append(member)

    elif choice == "3":
        clear_screen()
        status_query = input("Enter the membership status to search (active/inactive): ")
        # Ajoute les membres dont le statut correspond
        for member in new_members:
            if member.status == status_query:
                found_members.append(member)

    else:
        print("Invalid choice!")
        time.sleep(1)
        return  # retourne à la boucle principale en cas de choix invalide

    clear_screen()
    if found_members:
        print("Members found:\n")
        # Affiche tous les membres trouvés
        for m in found_members:
            m.display()
    else:
        print("Member not found.")
    time.sleep(2)

new_members = []

while True:
    clear_screen()
    print("Welcome to Gym Membership Management\n")
    print("Choose an action:")
    print("1. Add new user")
    print("2. Display all users")
    print("3. Search for a member")
    print("4. Exit\n")
    choice = input("Enter your choice: ")

    if choice == '1':
        clear_screen()
        new_members.append(create_member())
        print("Member added successfully!")
        time.sleep(1)
    elif choice == '2':
        clear_screen()
        if new_members:
            print("Displaying all members:\n")
            for m in new_members:
                m.display()
        else:
            print("No members to display.")
        time.sleep(2)
    elif choice == '3':
        clear_screen()
        search_member(new_members)
    elif choice == '4':
        print("Exiting...")
        break  # Sort de la boucle principale
    else:
        print("Invalid choice! Please try again.")
        time.sleep(1)
