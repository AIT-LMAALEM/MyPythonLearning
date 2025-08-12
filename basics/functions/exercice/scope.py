# ---------------
# scope function
#----------------

x=1 # global scope
print(f"print variable from global scope {x}")

def one():
    print(f" print variable from global scope {x}")


def two():
    y=2 # local scope
    print(f" print variable from function scope {y}")

# print(f"print variable from function {y}") # => y is not define


a=10 
def add():
    global a
    a= a+ 10
add()
print(a)



