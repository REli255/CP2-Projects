# Eli Robison, Battle Simulator

"""
OVERVIEW:
Enhance your existing RPG Character Creator and Battle Simulator by incorporating
data visualization, statistical analysis, and random data generation using Python
libraries. This project will focus on reading and implementing features from library
documentation.

REQUIREMENTS:

Library Integration:
Use Matplotlib for character stat visualizations
Use Pandas for data manipulation and basic statistical analysis
Use Faker for generating random character names and descriptions

Character Visualization:
Create a radar chart or bar graph to display a character's stats using Matplotlib

Data Analysis:
Use Pandas to load character data into a DataFrame
Implement basic statistical analysis on character attributes (e.g., mean, median,
max, min)

Random Generation:
Use Faker to generate random character names and backstories

Enhanced User Interface:
Create a menu system that allows users to access new visualization and
analysis features

Documentation Reading:
Demonstrate understanding of library documentation by implementing at least
one additional feature from each library not explicitly required above

NOTES:
Focus on reading and understanding the documentation for each library
Ensure your program handles potential errors (e.g., file not found, invalid user input)
Comment your code to explain the purpose of each function and any complex logic
Test your program thoroughly to ensure all features work as expected
"""

# statments to import the funtions from other pages
from Character_Management import character_selection
from Battle_System import battle_simulator
from visualizations import *
from analysis import *
from backstory import *

chosen = 0
name =  ""
race =  ""
job =  ""
health =  ""
strength =  ""
speed =  ""
defense =  ""
xp =  ""

# function with the user interface
def main(chosen, name, race, job, health, strength, speed, defense, xp):
    if chosen == 0:
        name, race, job, health, strength, speed, defense, xp = character_selection()
        chosen += 76

    choice = input("""1. Select a diferent character
    2. Battle a monster
    3. Show a bar graph of your characters stats
    4. Do statistical analysis of character stats
    5. Generate a back story
    6. End
    Enter the number of the thing you would like to do: """)
    if choice == "1":
        name, race, job, health, strength, speed, defense, xp = character_selection()
    elif choice == "2":
        name, race, job, health, strength, speed, defense, xp = battle_simulator(name, race, job, float(health), float(strength), float(speed), float(defense), float(xp))
    elif choice == "3":
        name, race, job, health, strength, speed, defense, xp = bar_graph(name, race, job, health, strength, speed, defense, xp)
    elif choice == "4":
        name, race, job, health, strength, speed, defense, xp = statistical_analysis(name, race, job, health, strength, speed, defense, xp)
    elif choice == "5":
        generated_backstory = generate_backstory(race)
        print(generated_backstory)
    elif choice == "6":
        return ("end"), str(name), str(race), str(job), int(health), int(strength), int(speed), int(defense), str(xp)
    else:
        print("that is not an option")
    
    return ("not yet"), str(name), str(race), str(job), int(health), int(strength), int(speed), int(defense), str(xp)

# loop that makes sure the program continues until the user is done 
while True:
    end, name, race, job, health, strength, speed, defense, xp = main(chosen, name, race, job, health, strength, speed, defense, xp)
    chosen = 56
    if end == "end":
        print("thank you for using this program")
        break