# Vivian Long
# CS 460
# Assignment 1
# 1/23/2018

# Program that takes a string and encrypts it with the Caesar, Playfair, and/or Vigenere ciphers


import sys

text = ""

# Checks if input is a string
while not text.isalpha():
    text = input("Enter text to encrypt/decrypt: ").lower()  # Ignore case
chars = list(text)  # Convert text string to list of chars


def caesar_encrypt():
    n = (input("Enter shift value: "))
    while not n.isdigit():
        n = (input("Enter shift value: "))

    secret = list()

    for i in range(len(chars)):
        # ASCII: a-z = 97-122
        # Converts plaintext char into its ASCII value and adds shift value
        asc = ord(chars[i]) + int(n)

        if asc > 122:
            asc = asc % 122 + 96  # Wraps back to a after z
        secret.append(chr(asc))  # Adds converted char into empty list

    print("Encrypted plaintext:")
    print(''.join(secret))  # Join list of chars into a single string


def caesar_decrypt():
    print("")


def playfair():
    keyword = list(input("Enter the keyword: "))
    key = list(keyword)  # Convert keyword to list of chars


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
        caesar_encrypt()

    elif ans == "2":
        playfair()

    elif ans == "3":
        vigenere()

    elif ans == "4":
        sys.exit(0)

    else:
        print("Not a valid choice, try again")