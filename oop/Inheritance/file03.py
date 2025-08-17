#multiple inheritance =inherit from more than one parent class
#multilevel inheritance=inherit from a parent which inherits from another parent
class Animal:
    def eat(self):
        print("this animal is eating")
    def sleep(self):
        print("this animal is sleeping")
    

class Prey(Animal):
    def flee(self):
        print("thid animal is fleeing")
    
class Predator(Animal):
    def hunt(self):
        print("this animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Predator,Prey):
    pass

rabbit=Rabbit()
rabbit.flee()
rabbit.eat()
rabbit.sleep()

fish=Fish()
fish.flee()
fish.hunt()
