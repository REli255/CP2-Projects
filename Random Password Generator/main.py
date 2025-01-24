# Eli Robison, Random Password Generator

"""
OVERVIEW:
Create a program that allows a user to specify password requirements (length,
upper/lowercase letters, numbers, and special characters) then gives them 4 possible
passwords they could use. 

PROJECT STEPS:
A main function that runs the code
Functions for the different password requirements
A function that assembles that password once it is the correct length
Users should be able to specify length and if they want to include:
    uppercase letters
    lowercase letters
    numbers
    special characters
HINT: You can make this by randomly selecting from different lists OR by randomly
generating the ASCII letters! 
"""

import random

upper_letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
lower_letters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
special_characters = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "`", "~", "[", "]", "{", "}", ";", ":", "'", ",", "<", ".", ">", "/", "?", "|")

def main():
    character_types = []
    print("Random Password Generator")
    length = int(input("How many characters long do you want the password to be: "))
    while True:
        lower_choice = input("Would you like lowercase letters to be included in the password: ")
        if lower_choice == "yes" or lower_choice == "Yes" or lower_choice == "YES":
            character_types.append(lower_letters)
        elif lower_choice == "no" or lower_choice == "No" or lower_choice == "NO":
            pass
        else:
            print("that is not an option")
            continue
        upper_choice = input("Would you like uppercase letters to be included in the password: ")
        if upper_choice == "yes" or upper_choice == "Yes" or upper_choice == "YES":
            character_types.append(upper_letters)
        elif upper_choice == "no" or upper_choice == "No" or upper_choice == "NO":
            pass
        else:
            print("that is not an option")
            continue
        numbers_choice = input("Would you like numbers to be included in the password: ")
        if numbers_choice == "yes" or numbers_choice == "Yes" or numbers_choice == "YES":
            character_types.append(numbers)
        elif numbers_choice == "no" or numbers_choice == "No" or numbers_choice == "NO":
            pass
        else:
            print("that is not an option")
            continue
        special_choice = input("Would you like special characters to be included in the password: ")
        if special_choice == "yes" or special_choice == "Yes" or special_choice == "YES":
            character_types.append(special_characters)
        elif special_choice == "no" or special_choice == "No" or special_choice == "NO":
            pass
        else:
            print("that is not an option")
            continue
        break
    for q in range(4):
        password = ""
        print("option", q + 1, ": ")
        for x in range(length):
            chosen_type = random.choice(character_types)
            chosen_character = random.choice(chosen_type)
            password += chosen_character
        print(password)

while True:
    main()
    end = input("do you want to make another password: ")
    if end == "yes" or end == "Yes" or end == "YES":
        pass
    elif end == "no" or end == "No" or end == "NO":
        break