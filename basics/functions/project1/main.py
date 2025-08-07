# hangman game
import random 

words=["office","panda","bad","ginger"]
random_word=random.choice(words)
display=[]
for i in range(len(random_word)):
    display.append("_")
print(" ".join(display))

# en peut aussi faire : display=["_"]*len(random_word)   sans boucle for

lives=6
while "_" in display and lives >0:
    guessed=input("guess a letter:").lower()
    if guessed not in random_word:
        lives-=1

    for j in range(len(random_word)):
         if guessed==random_word[j]:
           display[j]=guessed

    print(" ".join(display))
    print("you have ",lives," more tries\n")
    

if lives==0:
    print("\n ** you lose** \n")
    print(   '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
     =========''')
else:
    print("\n** you Win **\n")

