import string

def encrypt(message, shift):
    alphabet1 = string.ascii_lowercase
    alphabet2 = string.ascii_uppercase
    encrypted_message = ""
    for letter in message:
        if letter in alphabet1:
            original_position = alphabet1.index(letter)
            new_position = (original_position + shift) % 26
            encrypted_message += alphabet1[new_position]
        elif letter in alphabet2:
            original_position = alphabet2.index(letter)
            new_position = (original_position + shift) % 26
            encrypted_message += alphabet2[new_position]
        else:
            encrypted_message += letter
    print("Here is the encrypted message:", encrypted_message)

message = input("Enter a message: ")
shift = int(input("Enter a shift number: "))
encrypt(message, shift)
