# -------------- polymorphism --------------------#
# that means to "have many forms or faces"
           # poly =many
           # morphe=form


print(len("mahmoud"))
print(len([1,3,5,7,9]))
print(len({1:"helle",2:"bonjour"}))

print(3+1)
print("hello"+"world")


# exemple 3
class Dog:
    def sound(self):
        return "woof!"

class Cat:
    def sound(self):
        return "meow!"
    
for animal in (Dog(),Cat()):
    print(animal.sound())

#exemple 4

class French:
    def greet(self):
        return "Bonjour"

class English:
    def greet(self):
        return "Hello"

def introduce(lang):
    print(lang.greet())

introduce(French())
introduce(English())




