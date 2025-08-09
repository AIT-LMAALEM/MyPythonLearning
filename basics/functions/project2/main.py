# encrypted sentence
import string
alphabet=string.ascii_lowercase
sentence= input("Please type a sentence:").lower()
step=int(input("enter the step:"))
encrypted_sentence=""
for letter in sentence:
    if letter in alphabet:
        original_position=alphabet.index(letter)
        new_position= (original_position +step)%26
        encrypted_sentence+=alphabet[new_position]
    else:
        encrypted_sentence+=" "
print("Here is the encrypted sentence: ",encrypted_sentence)

        




