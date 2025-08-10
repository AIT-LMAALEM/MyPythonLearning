import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

secret_number = random.randint(1, 10)

while True:
    clear_screen()
    guess = input("Guess the number between 1 and 10: ")
    if guess.isdigit():
        guess = int(guess)
        if guess == secret_number:
            print("✅ Correct! You guessed the number.")
            break
        else:
            print("❌ Wrong guess. Try again.")
    else:
        print("⚠ Please enter a valid number.")
    
    input("\nPress Enter to try again...")

    