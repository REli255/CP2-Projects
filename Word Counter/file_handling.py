# Eli Robison, Word Counter file handling

def add_to_file():
    chosen_file = input("Enter the relative path of the text file you want to add to: ")
    with open(chosen_file, "a") as text_file:
        text_file.write(input("Enter what you want to add to the text file: "))

def display_file():
    chosen_file = input("Enter the relative path of the text file you want to display: ")
    with open(chosen_file, "r") as text_file:
        text_read = text_file.read()
        print(text_read)