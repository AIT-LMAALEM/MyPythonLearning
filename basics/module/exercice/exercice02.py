#Password Generator
import random
import string


print("Welcome to the Password Generator!")
length=int(input("Enter the total number of characters in the password:"))
num_letters=int(input("Enter the number of letters in the password:"))
num_numb=int(input("Enter the number of numbers in the password:"))
num_sym=int(input("Enter the number of symbols in the password:"))
if (num_letters + num_numb +num_sym)!=length:
    print("Invalid input. The sum of letters, numbers and symbols dosen't match the pasword!")
else:
    p1=random.choices(string.ascii_letters,k=num_letters)
    p2=random.choices(string.punctuation,k=num_sym)
    p3=random.choices(string.digits,k=num_numb)
    random.shuffle(p1+p2+p3)
    print("Generated Password:","".join(p1+p2+p3))
