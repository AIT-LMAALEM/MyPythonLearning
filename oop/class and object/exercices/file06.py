# challenge -Esay
class Recipe:
    def __init__(self,name,ingredients,time,instructions):
        self.name=name
        self.ingredients=ingredients
        self.time=time
        self.instructions=instructions
    def display(self):
        print(f"name :{self.name}")
        print(f"ingredients :{self.ingredients}")
        print(f"cooking time:{self.time}")
        print(f"instructions :{self.instructions}")
    
def creat_recipe():
    name=input("enter recipe name:")
    ingredients=input("enter ingredients (comme_separated)")
    time=input("enter time:")
    instructions=input("enter cooking instructions:")
    return Recipe(name,ingredients,time,instructions)

        

print(" Welcome to Recipe Collection ...\n")
recipe1=creat_recipe()

print("displaying recipe ...\n")
recipe1.display()
