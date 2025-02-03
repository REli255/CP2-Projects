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

# lists of letters as lowercase, uppercase and morse code
low_alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
up_alphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
morse_alphabet = (".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..")

# functon to Translate Morse Code to English
def morse_to_english():
    english_message = []
    morse_message = []
    length = int(input("enter how many characters long the message you want translated to English will be: "))
    for x in range(length):
        print("character #", x + 1)
        morse_part = input("Enter this character: ")
        morse_message.append(morse_part)
    for m in range(len(morse_message)):
        check = 0
        for n in range(26):
            if morse_message[m] == morse_alphabet[n]:
                english_message.append(low_alphabet[n])
                check += 1
                break
        if check == 0:
            english_message.append(morse_message[m])
    print(' '.join(english_message))

# function to translate English to Morse Code
def english_to_morse():
    morse_message = []
    english_message = input("Enter the message you want translated to Morse Code: ")
    for l in range(len(english_message)):
        check = 0
        for o in range(26):
            if english_message[l] == low_alphabet[o] or english_message[l] == up_alphabet[o]:
                morse_message.append(morse_alphabet[o])
                check += 1
                break
        if check == 0:
            morse_message.append(english_message[l])
    print(' '.join(morse_message))

# function with the user interface
def main():
    choice = input("""1. Translate Morse Code to English
    2. Translate English to Morse Code
    3. End
    Enter the number of the thing you would like to do: """)
    if choice == "1":
        morse_to_english()
    elif choice == "2":
        english_to_morse()
    elif choice == "3":
        return "end"
    else:
        print("that is not an option")

# loop that makes sure the program continues until the user is done 
while True:
    end = main()
    if end == "end":
        print("thank you for using this program")
        break