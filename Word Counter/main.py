# Eli Robison, Word Counter main user interface

"""
OVERVIEW:
Write a program that look at a document that a user has written on and update it with
the word count and a timestamp for when that wordcount was last updated

REQUIREMENTS:
Uses at least 3 pages (main, file handling, and time handling) main is the
only file name I've given you
Reads and Writes to the file
Uses functional decomposition
Lets the user tell what file to use it on
Uses good naming practices
Has good white space
"""

from file_handling import *
from word_counter import counter

# function with the user interface
def main():
    choice = input("""1. make a new file
    2. add to anold file
    3. Chck the word count of a file
    4. End
    Enter the number of the thing you would like to do: """)
    if choice == "1":
        make_new()
    elif choice == "2":
        add_to_old()
    elif choice == "3":
        counter()
    elif choice == "4":
        return "end"
    else:
        print("that is not an option")

# loop that makes sure the program continues until the user is done 
while True:
    end = main()
    if end == "end":
        print("thank you for using this program")
        break