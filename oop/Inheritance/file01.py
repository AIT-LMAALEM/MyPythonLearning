# inheritance

class Food: #base class
    def __init__(self,name):
        self.name=name
        print(f"{self.name} is created from base class")

    def eat(self):
        print("Eat method from base class")



class Apple(Food): #Derived class
    def __init__(self,name,price):
        #Food.__init__(self, name) #create instance from base class

        super().__init__(name)
        self.price=price

        print(f" {self.name} is created from derived class and price is {self.price}")
    
    def catch(self):
        print("get from tree from derived class")
    

    
food_zero= Food("pizza")
food_one=Apple("apple",15)
food_one.eat()
food_one.catch()

food_zero.eat()



#multiple inheritance

class BaseOne:
    def __init__(self):
        print("base one")
    
    def fun_one(self):
        print("one")

class BaseTwo:
    def __init__(self):
        print("base two")
    
    def fun_two(self):
        print("two")

class Derived(BaseOne,BaseTwo):
    pass

object1= Derived() # base one
# if class Drived(BaseTwo,BaseOne) =>  object1=Drived() # base two

object1.fun_one()
object1.fun_two()










    
