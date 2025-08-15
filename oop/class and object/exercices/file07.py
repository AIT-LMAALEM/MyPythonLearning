#  user management
users={}
class Users:
    def __init__(self,first_name,last_name,email,password,status="inactive"):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.status=status
    
    
def create_user():
    first_name=input("enter the first name:")
    last_name= input("enter the last name:")
    email=input("enter the email:")
    password=input("enter the password:")
    return Users(first_name,last_name,email,password)

print("Welcome to user management....\n")
print("choose an Action:\n")
print("1.Add user \n2.Display user \n3.Exit \n")

num=1
while True:
    choice=input("\nenter your choice:")
    if choice.isdigit():
        
        if int(choice)==1:
             user=create_user()
             users[num] = {
                "first name": user.first_name,
                "last name": user.last_name,
                "email": user.email,
                "password": user.password,
                "status": user.status
             }
             print("User added successfully!")
             num += 1
             
        elif int(choice)==2:
            print("Displaying all users....\n")
            for i ,info in users.items():
                for key,value in info.items():
                     print(f"{key}:{value}")
                print("----------------------------")
        elif int(choice)==3:
            print("Excting...")
            break
        else:
            print("Your choice is incorrect")

    else:
        print("Please enter a number (1, 2 or 3)")


    

