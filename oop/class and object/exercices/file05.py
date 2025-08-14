class User:
    def __init__(self,first_name,last_name,email,password,status="inactive"):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.status=status

# user1=User("Ahmed","Ali","ahmedali@gmail.com","ali123","active")
# print(f"this user {user1.first_name} and his email is {user1.status}")

def create_user():
    first_name=input("enter your first name:")
    last_name=input("enter your last name:")
    email=input("enter your email:")
    password=input("enter your password:")
    
    return User(first_name,last_name,email,password)
    

user1= create_user()

print(user1.first_name)



