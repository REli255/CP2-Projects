# Eli Robison, Personal Library

"""
OVERVIEW:
Update your personal library so each item in the library is a dictionary. (Yes library
itself should still be a list or a tuple) 

REQUIREMENTS:
Each item in the dictionary should have AT LEAST 4 different details about it
You should be able to update the different items in your dictionary
There should be the option to print a simple list (Names and
authors/artists/director) OR print a detailed list (Contains all the information)
"""

library = []

# function for adding a book (including title, author, type of cover and number of pages)
def add():
    title = input("enter the title of the book you want to add: ")
    author = input("enter the author of the book you want to add: ")
    cover = input("enter the type of cover of the book you want to add: ")
    pages = input("enter the number of pages in the book you want to add: ")
    book = {"Title": title, "Author": author, "Cover": cover, "Pages": pages}
    library.append(book)
    print(book["Title"], "by", book["Author"], "has been removed")

# function for searching the library by title, author, type of cover or number of pages
def search():
    for z in range(1):
        found = 0
        type = input("""do you want to search by 1. title, 2. author, 3. type of cover or 4. number of pages
                     enter the number of the category you want to search by: """)
        if type == "1":
            item = input("enter the title of the book you are searching for: ")
            for x in range(len(library)):
                if item == library[x]["Title"]:
                    print(library[x])
                    found += 1
        elif type == "2":
            item = input("enter the author of the book you are searching for: ")
            for x in range(len(library)):
                if item == library[x]["Author"]:
                    print(library[x])
                    found += 1
        elif type == "3":
            item = input("enter the type of cover of the book you are searching for: ")
            for x in range(len(library)):
                if item == library[x]["Cover"]:
                    print(library[x])
                    found += 1
        elif type == "4":
            item = input("enter the number of pages in the book you are searching for: ")
            for x in range(len(library)):
                if item == library[x]["Pages"]:
                    print(library[x])
                    found += 1
        else:
            print("that is not an option")
            pass
        if found == 0:
            print("there is not a book in the library that fits your search")

# function for editing a book's title, author, type of cover and/or number of pages
def edit():
    title = input("enter the title of the book you want to edit: ")
    author = input("enter the author of the book you want to edit: ")
    cover = input("enter the type of cover of the book you want to edit: ")
    pages = input("enter the number of pages in the book you want to edit: ")
    book_search = {"Title": title, "Author": author, "Cover": cover, "Pages": pages}
    found = 0
    for x in range(len(library)):
        if book_search == library[x]:
            title_edited = input("enter what you want to change the title to: ")
            author_edited = input("enter what you want to change the author to: ")
            cover_edited = input("enter what you want to change the type of cover to: ")
            pages_edited = input("enter what you want to change the number of pages to: ")
            book_edited = {"Title": title_edited, "Author": author_edited, "Cover": cover_edited, "Pages": pages_edited}
            library[x] = book_edited
            found += 1
            break
    if found == 0:
            print("there is not a book in the library that fits your search")

# function for removing a book by the title and author
def remove():
    title = input("enter the title of the book you want to remove: ")
    author = input("enter the author of the book you want to remove: ")
    cover = input("enter the type of cover of the book you want to remove: ")
    pages = input("enter the number of pages in the book you want to remove: ")
    book = {"Title": title, "Author": author, "Cover": cover, "Pages": pages}
    found = 0
    for x in range(len(library)):
        if book == library[x]:
            print(library[x]["Title"], "by", library[x]["Author"], "has been removed")
            library.remove(book)
            found += 1
            break
    if found == 0:
            print("there is not a book in the library that fits your search")

# function to display the books in the library
def display():
    amount = input("""1. Title and Author
    2. All information
    Enter the number of the thing you would like to do: """)
    if amount == "1":
        for b in range(len(library)):
            print(library[b]["Title"], "by", library[b]["Author"])
    elif amount == "2":
        for d in range(len(library)):
            print(library[d]["Title"], "by", library[d]["Author"], "is", library[d]["Cover"], "and has", library[d]["Pages"], "pages.")
    else:
        print("that is not an option")

# function with the user interface
def main():
    choice = input("""1. Add a book
    2. Search the library
    3. Edit a book
    4. Remove a book
    5. Display the library
    6. End
    Enter the number of the thing you would like to do: """)
    if choice == "1":
        add()
    elif choice == "2":
        search()
    elif choice == "3":
        edit()
    elif choice == "4":
        remove()
    elif choice == "5":
        display()
    elif choice == "6":
        return "end"
    else:
        print("that is not an option")

# loop that makes sure the program continues until the user is done 
while True:
    end = main()
    if end == "end":
        print("thank you for using this program")
        break