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

information = []

with open("To Do List/to_do_list_1.text", "w") as file:
    file.write("")

def add():
    with open("To Do List/to_do_list_1.text", "a") as file:
        file.write(input("enter the item you want to add to the to do list: "))
    with open("To Do List/to_do_list_1.text", "a") as file:
        file.write("\n")

def mark():
    found = 0
    item  = input("enter the item you want to mark as done: ")
    # loop that check every item in the list to see if it matches
    for q in range(len(information)):
        if item in information[q]:
            information[q] = information[q] + " -- completed \n"
            found += 1
    if found == 0:
        print("there is not an item in the list that fits your search")
    with open("To Do List/to_do_list_1.text", "w") as file:
        for rank in information:
            file.write(rank)

def delete():
    found = 0
    item  = input("enter the item you want to delete: ")
    # loop that check every item in the list to see if it matches
    for rank in information:
        if item in rank:
            information.remove(rank)
            found += 1
    if found == 0:
        print("there is not an item in the list that fits your search")
    with open("To Do List/to_do_list_1.text", "w") as file:
        for rank in information:
            file.write(rank)

# function with the user interface
def main():
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
    # opens the file and prints the to do list
    information = []
    with open("To Do List/to_do_list_1.text") as file:
        for row in file:
            information.append(row)
    print("your to do list is: ")
    for rank in information:
        print(rank)
    if end == "end":
        print("thank you for using this program")
        break