# Function Packing unpacking arguments *Args
numbrs=[1,2,3,4,5,6]
print(*numbrs) #=> 1 2 3 4 5 6 

def say_hello(n1,n2,n3,n4):
    peoples=[n1,n2,n3,n4]
    for name in peoples:
        print(f"hello {name}")
say_hello("osama","mhamed","rachid","alaa")


def say_hello(*peoples): #n1,n2,n3,...
    for name in peoples:
        print(f"hello {name}")
say_hello("osama","mhamed","rachid","alaa","hamza")




def show_details(name,*skills):
    print(f"hello {name} your skills is:")
    for skill in skills:
        print(skill)

show_details("mhamed","python","latex","js","git")


