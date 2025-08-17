# super()= function used in a child class to call methods from a parent class(superclass)


class Shape:
    def __init__(self,color,filled):
        self.color=color
        self.filled=filled

class Circle:
    def __init__(self,color,filled,radius):
        self.color=color
        self.filled=filled
        self.radius=radius
   
class Square:
    def __init__(self,color,filled,width):
        self.color=color
        self.filled=filled
        self.width=width
    
class Triangle:
     def __init__(self,color,filled,width,height):
        self.color=color
        self.filled=filled
        self.width=width
        self.height=height

##############################################################################
class Shape:
    def __init__(self,color,filled):
        self.color=color
        self.filled=filled
    
    def describe(self):
        print(f" it's {self.color} and {"filled" if self.filled else "not filled"}")

class Circle(Shape):
    def __init__(self,color,filled,radius):
        super().__init__(color,filled)
        self.radius=radius
    
    def describe(self):
        print(f"it's a circle with an area of {46.2} cm^2")
        super().describe()
   
class Square(Shape):
    def __init__(self,color,filled,width):
        super().__init__(color,filled)
        self.width=width
    
class Triangle(Square):
     def __init__(self,color,filled,width,height):
        super().__init__(color,filled,width)
        self.height=height


circle= Circle(color="red",filled=True,radius=5)
triangle=Triangle(color="blue",filled=False,width=10,height=5)
print(circle.color)    
print(circle.filled)

print(triangle.filled)
print(triangle.width)

triangle.describe()
circle.describe()

