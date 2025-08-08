# function with parameters
def hi(name): # parameter
    print("hello",name)
name=input("enter your name:")
hi(name) # argument

def information(name,age,nationality):
    print(f"Your name is {name}, and you are {age} years old, you are {nationality}")
information("mhamed",19,"marocaine")


def multiply(num):
    for i in range(1,11):
        print(f"{num} * {i} ={num * i}")

num=int(input("enter a number:"))
multiply(num)



#positional arguments
def greet(name,age):
    print("your name is :",name)
    print("your age is ",age," years old")
greet(age=19,name="ahmed")
