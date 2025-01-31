# Eli Robison, Simple Morse Code Translator

"""
OVERVIEW:
    Write a program that will translate between English and Morse Code

REQUIREMENTS:
    Create two lists (one of the alphabet letters in English, and other for
    the corresponding Morse Code Symbols) 
    Create a function to translate English into Morse Code
    Create a function to translate Morse Code into English
    Create a main loop where users can choose to translate English to Morse Code,
    Morse Code to English, or Exit
    Project needs to:
        Use string manipulation to control the appearance of the output 
        Use basic error handling (for characters not in Morse Code)
        Use good naming for functions and variables
        Use pseudocode comments to explain what the program is doing
        Use white space to make sure code is easy to read
"""

low_alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
up_alphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
morse_alphabet = ("._", "_...", "_._.", "_..", ".", ".._.", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")