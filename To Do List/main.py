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

with open("notes/test.txt", "w") as file:
    file.write("")

def add():
    with open("notes/user_info.csv", "w", newline="") as file:
        file.write(input("enter the item you wnt to add to the to do list: "))

def mark():
    pass

def delete():
    pass

# function with the user interface
def main():
    with open("notes/test.txt") as file:
        content = file.read()
        print("your to do list is: \n", content)
    choice = input("""1. Add items to the to do list
    2. Mark item as complete
    3. Delete item from to do list
    4. End
    Enter the number of the thing you would like to do: """)
    if choice == "1":
        add()
    elif choice == "2":
        mark()
    elif choice == "3":
        delete()
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