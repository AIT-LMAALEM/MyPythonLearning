import random
def welcome():
    print("Welcome to the guess number game!")
def guess_number(guess):
    while guess !=secret_number:
        if guess < secret_number:
            guess=int(input("too low Guess again:"))
        else:
            guess=int(input("too hight! Geuss again:"))
    print("congratulations! you guess the numbre! :",secret_number)

secret_number=random.randint(1,10)
welcome()
guess=int(input("enter a number between 1 and 10:"))
guess_number(guess)

