# Eli Robison, To Do List

"""
OVERVIEW:
Create a program that allows the user to view, add, delete, and mark tasks on a to do list that is saved on a seperate text file. 

REQUIREMENTS:
    Create a to do list (Kept on a txt file)
    Add items to the to do list
    Mark item as complete
    Delete item from to do list
"""

def create():
    pass

def add():
    pass

def mark():
    pass

def delete():
    pass

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