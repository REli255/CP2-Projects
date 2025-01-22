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

upper_letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
lower_letters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
special_characters = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "`", "~", "[", "]", "{", "}", ";", ":", "'", ",", "<", ".", ">", "/", "?", "|")

def main():
    print("Random Password Generator")
    length = int(input("enter how many characters do you want to be in the password: "))