# hangman game
import random 

words=["office","panda","bad","ginger"]
random_word=random.choice(words)
display=[]


for i in range(len(random_word)):
    display.append("_")
    print("_",end=" ")
guessed=input("\nguess a letter:").lower()

for j in random_word:
    if guessed==j:
        display[random_word.index(j)]=guessed

for i in display:
    print(i,end=" ")
