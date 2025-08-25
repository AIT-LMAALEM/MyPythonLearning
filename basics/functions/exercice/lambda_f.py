# fuction => Lambda 
# Anonymous function
# 1 it has no name 
# 2 lambda is one single expression not block of code

def say_hello(name):
    return f" hello {name}"

hello= lambda name:f"hello {name}"

print(hello("ahmed"))
print(say_hello("ahmed"))

# 1. Addition simple
add = lambda x, y: x + y
print("1:", add(5, 3))

# 2. Carré d'un nombre
square = lambda x: x ** 2
print("2:", square(4))

# 3. Nombre pair ou impair
is_even = lambda x: x % 2 == 0
print("3:", is_even(10))

# 4. Plus grand de deux nombres
max_of_two = lambda x, y: x if x > y else y
print("4:", max_of_two(5, 9))




