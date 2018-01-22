# Vivian Long
# CS 460
# Assignment 1
# 1/25/2018

# Program that takes a string and encrypts/decrypts it with the Caesar, Playfair, and/or Vigenere ciphers


import sys
import string

text = ""

# Checks if input is a string
while not text.isalpha():
    text = input("Enter text to encrypt/decrypt: ").lower()  # Ignore case
chars = list(text)  # Convert text string to list of chars


def caesar():
    n = (input("Enter shift value: "))
    while not n.isdigit():
        n = (input("Enter shift value: "))
    
    secret = list()
    choice = input("Would you like to \n1. Encrypt or 2. Decrypt? ")

if choice == "1":  # Caesar encrypt
    for i in range(len(chars)):
        # ASCII: a-z = 97-122
        # Converts plaintext char into its ASCII value and adds shift value
        asc = ord(chars[i]) + int(n)
        
        if asc > 122:
            asc = asc % 122 + 96  # Wraps back to a after z
            secret.append(chr(asc))  # Adds converted char into empty list
        
        print("Encrypted plaintext:")
        print(''.join(secret))  # Join list of chars into a single string

    elif choice == "2":  # Caesar decrypt
        for i in range(len(chars)):
            asc = ord(chars[i]) - int(n)  # Convert ciphertext to ASCII value and subtract shift
            
            if asc < 97:
                asc = asc % 97 + 121  # Wraps back to z after a
            secret.append(chr(asc))

print("Decrypted ciphertext:")
print(''.join(secret))  # Join list of chars into a single string

else:
    print("Please enter a valid choice")


def playfair():
    keyword = list(input("Enter the keyword: "))
    key = list(keyword)  # Convert keyword to list of chars
    
    matrix = list()  # Empty list
    alpha = list(string.ascii_lowercase)
    
    for i in range(len(key)):
        for char in key:
            if char not in matrix and char in alpha:
                matrix += char

for letter in alpha:
    if letter not in matrix:
        matrix += letter
    
    matrix2 = []
    for j in range(5):
        matrix2.append('')

    matrix2[0] = matrix[0:5]
    matrix2[1] = matrix[5:10]
    matrix2[2] = matrix[10:15]
    matrix2[3] = matrix[15:20]
    matrix2[4] = matrix[20:25]

print(matrix2)


def vigenere():
    print("")


ans = True
while ans:
    print("""
        1. Caesar cipher
        2. Playfair cipher
        3. Vigenere cipher
        4. Exit/Quit
        """)
    ans = input("What would you like to do? ")
    
    if ans == "1":
        caesar()
    
    elif ans == "2":
        playfair()
    
    elif ans == "3":
        vigenere()
    
    elif ans == "4":
        sys.exit(0)
    
    else:
        print("Not a valid choice, try again")
