# Vivian Long
# CS 460
# Assignment 1
# 1/25/2018


import sys
import string

text = ""

# Checks if input is a string
while not text.isalpha():
    text = input("Enter text to encrypt/decrypt: ").lower()  # Ignore case
chars = list(text)  # Convert text string to list of chars
alpha = list(string.ascii_lowercase)  # Lower case letters


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
                asc = asc - 96 + 122  # Wraps back to z after a

            secret.append(chr(asc))

        print("Decrypted ciphertext:")
        print(''.join(secret))  # Join list of chars into a single string

    else:
        print("Please enter a valid choice")

'''
def playfair():
    keyword = list(input("Enter the keyword: "))
    key = list(keyword)  # Convert keyword to list of chars

    matrix = list()  # Empty list
    alpha.remove("j")  # Remove j

    # Populates key into empty list
    for i in range(len(key)):
        for char in key:
            if char not in matrix and char in alpha:
                matrix += char

    # Fills rest of the list with unused letters
    for letter in alpha:
        if letter not in matrix:
            matrix += letter

    matrix2 = []
    for j in range(5):
        matrix2.append('')

    # Split list into 5x5 matrix
    matrix2[0] = matrix[0:5]
    matrix2[1] = matrix[5:10]
    matrix2[2] = matrix[10:15]
    matrix2[3] = matrix[15:20]
    matrix2[4] = matrix[20:25]

    # Checks for repeated letters in digrams, adding x if necessary
    a = 0
    for k in range(len(chars) - 2):
        if chars[a] == chars[a + 1]:
            chars.insert(a + 1, 'x')
        a = a + 2

    # Adds x to end of an odd length string
    if len(chars) % 2 == 1:
        chars.append('x')

    # Split into digrams
    i = 0
    digram = []
    for x in range(len(chars) // 2):
        digram.append(chars[i: i + 2])
        i = i + 2

    # Encrypt
    new = list()
    x = y = 0
    for b in range(len(chars)):
        for m in range(5):
            for n in range(5):
                if matrix2[m][n] == chars[b]:
                    x = m  # Row of chars[b]
                    y = n  # Col of chars[b]

                    row = chars[b]  # row is x of chars[b]
                    col = chars[b + 1]  # col is y or chars[b+1]

    print(digram)
    print(new)
    print(matrix2)
    print(chars)
'''

caesar()
