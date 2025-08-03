import string
import random

print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.digits)
print(string.punctuation)
print(string.hexdigits)
print(string.octdigits)


sent=input("please type a sentence:")
new_sent=""
for i in sent:
    if i not in string.punctuation:
       new_sent+=i

print("\n\n Here is the same sentence without punctuation \n\n",new_sent)


#random.choices(sequence,K=num)
numbres=[0,1,2,3,4,5,6,7,8,9]
print(random.choice(numbres))
print(random.choices(numbres,k=2))
print(random.choices(numbres,k=6))
