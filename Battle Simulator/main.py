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

# statments to import the funtions from other pages
from Character_Management import character_selection
from Battle_System import battle_simulator

# function with the user interface
def main():
    chosen = 0
    if chosen == 0:
        health, strength, speed, defense, xp = character_selection()
        chosen += 76
    
    choice = input("""1. Select a diferent character
    2. Battle a monster
    3. End
    Enter the number of the thing you would like to do: """)
    if choice == "1":
        health, strength, speed, defense, xp = character_selection()
    elif choice == "2":
        health, strength, speed, defense, xp = battle_simulator(float(health), float(strength), float(speed), float(defense), float(xp))
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