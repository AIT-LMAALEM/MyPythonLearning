 #magic methods
# everything in python is an object
import file02
class Skill:
    def __init__(self):
        self.skills=["html","css","js"]
    
    # __str__ gives a human readable output of the object
    def __str__(self):
        return f"this is my skills => {self.skills}"
    
    def __len__(self):
        return len(self.skills)
    
profile=Skill()

#Si le fichier est lancé directement, __name__ vaut "__main__".
#Si le fichier est importé comme module, __name__ prend le nom du module.

print(__name__)
print(file02.__name__)

print(profile) # this is my skills => .... not __main__.Skill .......
print(profile.__class__)  #→ p.__class__ renvoie la classe de l'objet p.

my_string= "mhamed"
print(type(my_string))
print(my_string.__class__)

my_int=11
print(my_int.__class__)
print(type(my_int))


print(str.upper(my_string))# =>
print(my_string.upper())  # <=


profile.skills.append("php")
profile.skills.append("mysql")

print(len(profile))

