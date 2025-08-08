# encrypted word
import string
alphabet=string.ascii_lowercase
word= input("Please type a word:").lower()
encrypted_word=""
for letter in word:
    original_position=alphabet.index(letter)
    new_position=original_position +3
    encrypted_word += alphabet[new_position]
print(" Here is the encrypted word :",encrypted_word)

