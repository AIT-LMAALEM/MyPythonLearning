# hangman game
import random 

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


words=["office","panda","bad","ginger"]
random_word=random.choice(words)
display=["_"]*len(random_word)
print(" ".join(display))
lives=6
print(HANGMANPICS[0])

guessed_letter=[]
while "_" in display and lives >0:
    guessed=input("guess a letter:").lower()

    if guessed in guessed_letter:
        print("you already guessed that. Try again:")
        print(f"you have {lives} more tries")
        continue
    guessed_letter.append(guessed)



    if guessed not in random_word:
        lives-=1
        print(HANGMANPICS[6-lives])
    else:
        for j in range(len(random_word)):
            if guessed==random_word[j]:
               display[j]=guessed

    print(" ".join(display))
    print("\nyou have ",lives," more tries")
    

if lives==0:
    print("\n ** you lose** \n")
   
else:
    print("\n** you Win **\n")








