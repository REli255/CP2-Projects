# Eli Robison, Personal Library

"""
Create a program that allows user to manage a personal library catalog for any ONE
type (books, movies, music, etc). The project needs to allow users to add new items,
display ALL contents, search for a specific item (by title, author/artist/director),
remove a book from the library, exit the program. 

PROJECT STEPS:
Stores all items in a list
Function to add a new item
Function to search the items
Function to remove an item
Function that runs the code (displays the menu options inside and calls the, functions inside of a while True loop)
Project must include
easy to understand variable and function names
Pseudocode comments explaining what the code is doing
Good use of white space to keep items separate and easy to read/find
Have at least 2 people test your code before submission!
"""

library = []

# function for adding a book (including title and author)
def add():
    title = input("enter the title of the book you want to add: ")
    author = input("enter the author of the book you want to add: ")
    book = (title, author)
    library.append(book)

# function for searching the library by title or author
def search():
    for z in range(1):
        found = 0
        type = input("do you want to search by title or author: ")
        if type == "title" or type == "Title" or type == "TITLE":
            item = input("enter the title of the book you are searching for: ")
            for x in range(len(library)):
                if item in library[x][0]:
                    print(library[x][0], "by", library[x][1])
                    found += 1
        elif type == "author" or type == "Author" or type == "AUTHOR":
            item = input("enter the author of the book you are searching for: ")
            for x in range(len(library)):
                if item in library[x][1]:
                    print(library[x][0], "by", library[x][1])
                    found += 1
        else:
            print("that is not an option")
            pass
        if found == 0:
            print("there is not a book in the library that fits your search")

# function for removing a book by the title and author
def remove():
    title = input("enter the title of the book you want to remove: ")
    author = input("enter the author of the book you want to remove: ")
    book = (title, author)
    found = 0
    for x in range(len(library)):
        if book == library[x]:
            print(library[x][0], "by", library[x][1], "has been removed")
            library.remove(book)
            found += 1
    if found == 0:
            print("there is not a book in the library that fits your search")

# function with the user interface
def main():
    choice = input("""1. Add a new book
    2. Search the library
    3. Remove a book
    4. Display library
    5. End
    Enter the number of the thing you would like to do: """)
    if choice == "1":
        add()
    elif choice == "2":
        search()
    elif choice == "3":
        remove()
    elif choice == "4":
        for b in range(len(library)):
            print(library[b][0], "by", library[b][1])
    elif choice == "5":
        return "end"
    else:
        print("that is not an option")

# loop that makes sure the program continues until the user is done 
while True:
    end = main()
    if end == "end":
        print("thank you for using this program")
        break