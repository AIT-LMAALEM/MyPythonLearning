# Gym Membership Management

import os
import time

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

class User:
    def __init__(self,first_name,last_name,ID,status="inactive"):
        self.first_name=first_name
        self.last_name=last_name
        self.ID=ID
        self.status=status
    
    def disaplay(self):
        print(f"Fist name :{self.first_name}")
        print(f"Last name:{self.last_name}")
        print(f"Email:{self.ID}")
        print(f"Membership status :{self.status}")
    
        print("_"*20)
    
def creat_member():
    first_name=input("enter the first name:")
    last_name=input("enter the last name:")
    ID=input("enter the membership ID:")
    status=input("enter the membership status, or click enter:")
    return User(first_name,last_name,ID,status)


new_members=[]
while True:
    print("\nWelcome to gym Membership management\n")
    print("\nchoose an actions\n")
    print("1.Add new user")
    print("2.Display all users")
    print("3.Search for a member:")
    print("4.Exit\n")
    choice=input("Enter your choice:")

    if choice=='1':
        clear_screen()
        new_members.append(creat_member())
        print("member added successfuly!")
        time.sleep(2)
    elif choice=='2':
        if new_members:
            clear_screen()
            print("Displayning all members....")
            time.sleep(1)
            for i in new_members:
                i.disaplay()
            time.sleep(1)
        else:
            print("Sorry, didn't find any user to disaplay")
            time.sleep(2)
    elif choice=='3':
        print("Searche by..\n")
        print("1.Membership ID")
        print("2.First name")
        print("3.Member ship status\n")
        choice2=input("enter your choice:")
        if choice2=="1":
            clear_screen()
            id=input("enter the membership id to search:")
            time.sleep(2)
            for member in new_members:
                if member.ID==id:
                    member.disaplay()
                else:
                    print("sorry, didn't find the membership with this id\n")
        elif choice2=="2":
            clear_screen()
            fname=input("enter the first name to search:")
            for member in new_members:
                if member.first_name==fname:
                    member.disaplay()
                else:
                    print("sorry, didn't find membership with this first name")
                
        elif choice2=="3":
            clear_screen()
            status_choice=input("enter the member ship status to search (active/inactive):")
            for member in new_members:
                if member.status==status_choice:
                    member.disaplay()
                else:
                    print("sorry, didn't find membership with this status")
        else:
            print("Invalid choice! Please try again.")
    elif choice=='4':
        print("Exiting...")
        break
    else:
        print("Envalid choice! Please try again.")




