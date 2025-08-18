# Getters & Setters

#private
class Member:
    def __init__(self,name):
        self.__name=name
    
    def say_hello(self):
        return f"hello {self.__name}"
    
    def get_name(self):
        return self.__name
    
    def set_name(self,new_name):
        self.__name=new_name
    
one=Member("ahmed")

print(one.get_name())
one.set_name("salim")
print(one.get_name())



# @property Decorator  
# @property in python lets you use methods like attributes so you can add validation or computes values while keeping clean

class Member:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def say_hello(self):
        print(f"hello {self.name}")
    
    @property
    def age_in_days(self):
        return self.age*365


member1=Member("samir",19)
print(member1.age_in_days)  #with @property



