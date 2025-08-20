# Abstract base class
# class called abstract class if it has one or more abstract methode,
# a class that cannot be instantiated on its own
# requires children to use inherited abstract methods



from abc import  ABCMeta, abstractmethod

class Programming(metaclass=ABCMeta):
     
    @abstractmethod
    def has_oop(self):
        pass

class Python(Programming):

    def has_oop(self):
        return "yes"
    
class C(Programming):
     pass
    # def has_oop(self):
    #     return "no"
    
c=C()  #Can't instantiate abstract class C without an implementation for abstract method 'has_oop'
python=Python()
print(f"python has oop ? {python.has_oop()}")


class Vehicle(metaclass=ABCMeta):
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Car is moving")
    def stop(self):
        print("Car is stopping")
    
class Bike(Vehicle):
    def move(self):
        print("Bike is moving")
    def stop(self):
        print("Car is stopping")
    
car=Car()
print(car.move())




