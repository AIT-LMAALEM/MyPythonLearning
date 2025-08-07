# hangman game
import random 

words=["office","panda","bad","ginger"]
random_word=random.choice(words)
display=[]
for i in range(len(random_word)):
    display.append("_")
    print("_",end=" ")

lives=6
while "_" in display and lives >0:
    guessed=input("\nguess a letter:").lower()
    if guessed not in random_word:
        lives-=1

    for j in range(len(random_word)):
         if guessed==random_word[j]:
           display[j]=guessed

    for i in display:
        print(i,end=" ")

    print("\nyou have ",lives," more tries")
    

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

