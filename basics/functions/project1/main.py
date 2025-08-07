import random 

words=["office","panda","cabin","ginger"]
random_word=random.choice(words)
letter=input("please guess a letter:")
for i in random_word:
    if i==letter:
        print("Right")
    else:
        print("Wrong")
