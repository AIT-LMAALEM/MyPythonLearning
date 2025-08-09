import string

def dcrypt(message, shift):
    alphabet1 = string.ascii_lowercase
    alphabet2 = string.ascii_uppercase
    decrypted_message = ""
    for letter in message:
        if letter in alphabet1:
            original_position = alphabet1.index(letter)
            new_position = (original_position - shift) % 26
            decrypted_message += alphabet1[new_position]
        elif letter in alphabet2:
            original_position = alphabet2.index(letter)
            new_position = (original_position - shift) % 26
            decrypted_message += alphabet2[new_position]
        else:
            decrypted_message += letter
    print("Here is the decrypted_message:", decrypted_message)

message = input("Enter a message: ")
shift = int(input("Enter a shift number: "))
dcrypt(message, shift)
