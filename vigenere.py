import sys
import string

text = ""

# Checks if input is a string
while not text.isalpha():
    text = input("Enter text to encrypt/decrypt: ").lower()  # Ignore case
chars = list(text)  # Convert text string to list of chars
alpha = list(string.ascii_lowercase)  # Lower case letters

key = input("Enter the key: ")
if len(key) != len(text):
    key = key * (len(chars) // len(key))

secret = list()
choice = input("Would you like to \n1. Encrypt or 2. Decrypt? ")

if choice == "1":
    for i in range(len(key)):
        # ASCII: a-z = 97-122
        # Converts each key character into its ASCII value
        keyval = ord(key[i]) - 97

        for j in range(len(chars)):
            # Converts plaintext char into its ASCII value and adds key ASCII value
            asc = ord(chars[i]) + keyval

            if asc > 122:
                asc = asc % 122 + 96  # Wraps back to a after z

        secret.append(chr(asc))  # Adds converted char into empty list

    print("Encrypted plaintext:")
    print(''.join(secret))  # Join list of chars into a single string

elif choice == "2":
    for i in range(len(key)):
        keyval = ord(key[i]) - 97

        for j in range(len(chars)):
            asc = ord(chars[i]) - keyval

            if asc < 97:
                asc = asc - 96 + 122  # Wraps back to z after a

        secret.append(chr(asc))

    print("Decrypted ciphertext:")
    print(''.join(secret))

else:
    print("Invalid input")
