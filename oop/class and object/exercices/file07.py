#  user management -v2
import os
import time

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

class User:
    def __init__(self,first_name,last_name,email,password,status="inactive"):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.status=status
    
    def disaplay(self):
        print(f"Fist name :{self.first_name}")
        print(f"Last name:{self.last_name}")
        print(f"Email:{self.email}")
        print(f"Password:{self.password}")
        print("_"*20)
    
def creat_user():
    first_name=input("enter the first name:")
    last_name=input("enter the last name:")
    email=input("enter the Email:")
    password=input("enter tha Password:")
    return User(first_name,last_name,email,password)


new_users=[]
while True:
    print("\nWelcome to user management\n")
    print("\nchoose an actions\n")
    print("1.Add new user")
    print("2.Display all users")
    print("3.Exit\n")
    choice=input("Enter your choice:")

    if choice=='1':
        new_users.append(creat_user())
        print("User added successfuly!")
        time.sleep(2)
    elif choice=='2':
        if new_users:
            clear_screen()
            print("Displayning all new_users....")
            time.sleep(1)
            for i in new_users:
                i.disaplay()
            time.sleep(1)
        else:
            print("Sorry, didn't find any user to disaplay")
            time.sleep(2)
    elif choice=='3':
        print("Exiting...")
        break
    else:
        print("Envalid choice! Please try again.")




