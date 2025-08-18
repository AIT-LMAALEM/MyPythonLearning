#------------Encapsulation---------------
# Restrict access to the data stored in attributes and methods
#public
#every attributes and method that we use so far is public
#attributes and methods can be modified and run from everywhere

class Member:
    def __init__(self,name):
        self.name=name
    
one=Member("ahmed")
print(one.name)
one.name="imad"
print(one.name)

#Protected
# attributes and methods can be accessed from within the class and subclass
#attributes and methode prefixed with one underscore _


class Member:
    def __init__(self,name):
        self._name=name
    


#Privete
# attributes and methods can be accessed from within the class or object only
#attributes cannot be modified from outside the class
# attributes and methods prefixed with two undescores __

# attributes=variables= properties

class Member:
    def __init__(self,name):
        self.__name=name
    
    def say_hello(self):
        return f"hello {self.__name}"
    
one=Member("ahmed")
print(one.say_hello())
# print(one.__name) #  'Member' object has no attribute '__name'






