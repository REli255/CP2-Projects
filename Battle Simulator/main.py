# Eli Robison, Battle Simulator

"""
OVERVIEW:
Create a program that allows users to create, manage, and battle RPG characters.
The program should use inner and helper functions to organize the code
efficiently. Characters should be saved to and loaded from a CSV file.

REQUIREMENTS:
Character Creation and Management:
Create new characters with attributes (name, health, strength, defense,
speed)
Save characters to a CSV file
Load characters from a CSV file
Display character information

Battle System:
Implement a turn-based battle system between two characters
Calculate damage based on character attributes
Include a simple leveling system where characters gain experience after
battles

Program Structure:
Use inner functions for main features (character creation, battle system,
menu)
Implement helper functions for repetitive tasks (save/load, display
character info)
Create a main menu for user interaction

File Operations:
Save character data to a CSV file
Load character data from a CSV file

NOTES:
Focus on using inner and helper functions to organize your code
Ensure your program handles potential errors (e.g., file not found, invalid user
input)
Comment your code to explain the purpose of each function and any complex
logic
Test your program thoroughly to ensure all features work as expected
"""

races = ["human", "elf", "goblin", "orc"]
classes = ["berserker", "fighter", "ranger", "wizard"]

def character_creator():
    name = input("enter the name of your character: ")

    def race_selection():
        race = input("enter the race of your character (1=human, 2=elf, 3=goblin, 4=orc): ")
        if race == "1":
            race = races[0]
            health = 11
            strength = 11
            dexterity = 11
            intelligence = 11
        elif race == "2":
            race = races[1]
            health = 12
            strength = 10
            dexterity = 12
            intelligence = 11
        elif race == "3":
            race = races[2]
            health = 9
            strength = 11
            dexterity = 14
            intelligence = 10
        elif race == "4":
            race = races[3]
            health = 13
            strength = 14
            dexterity = 8
            intelligence = 9
        else:
            print("that is not an option")
            race_selection()
        return race, health, strength, dexterity, intelligence
    race, health, strength, dexterity, intelligence = race_selection()

    def class_selection(health, strength, dexterity, intelligence):
        job = input("enter the class of your character (1=berserker, 2=fighter, 3=ranger, 4=wizard): ")
        if job == "1":
            job = classes[0]
            health += 2
            strength += 4
            dexterity -= 1
            intelligence -= 1
        elif job == "2":
            job = classes[1]
            health += 1
            strength += 1
            dexterity += 1
            intelligence += 1
        elif job == "3":
            job = classes[2]
            health += 0
            strength -= 1
            dexterity += 4
            intelligence += 1
        elif job == "4":
            job = classes[3]
            health += 1
            strength -= 1
            dexterity -= 1
            intelligence += 5
        else:
            print("that is not an option")
            class_selection()
        return job, health, strength, dexterity, intelligence
    job, health, strength, dexterity, intelligence = race_selection(health, strength, dexterity, intelligence)
    
    print(name, "is a", race, job, "with", health, "health,", strength, "strength,", dexterity, "dexterity and", intelligence, "intelligence")

# function with the user interface
def main():
    choice = input("""1. Add to a file
    2. Display a file
    3. Check the word count of a file
    4. End
    Enter the number of the thing you would like to do: """)
    if choice == "1":
        character_creator()
    elif choice == "2":
        ()
    elif choice == "3":
        ()
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