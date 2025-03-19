# eli robison, Character Creation and Management

# statment to make csv files usable
import csv

# lists of posible classes and races
races = ["human", "elf", "goblin", "orc"]
classes = ["berserker", "fighter", "ranger", "wizard"]

# function that lets the user make a new character
def character_creator():
    name = input("enter the name of your character: ")
    xp = 0

    # function that controls the traits of the selected race
    def race_selection():
        race = input("enter the race of your character (1=human, 2=elf, 3=goblin, 4=orc): ")
        if race == "1":
            race = races[0]
            health = 22
            strength = 11
            speed = 11
            defense = 5.5
        elif race == "2":
            race = races[1]
            health = 24
            strength = 10
            speed = 12
            defense = 5.5
        elif race == "3":
            race = races[2]
            health = 28
            strength = 11
            speed = 14
            defense = 5
        elif race == "4":
            race = races[3]
            health = 26
            strength = 14
            speed = 8
            defense = 4.5
        else:
            print("that is not an option")
            race_selection()
        return race, health, strength, speed, defense
    race, health, strength, speed, defense = race_selection()

    # function that controls the traits of the selected class
    def class_selection(health, strength, speed, defense):
        job = input("enter the class of your character (1=berserker, 2=fighter, 3=ranger, 4=wizard): ")
        if job == "1":
            job = classes[0]
            health += 4
            strength += 4
            speed -= 1
            defense -= 1
        elif job == "2":
            job = classes[1]
            health += 2
            strength += 1
            speed += 1
            defense += 1
        elif job == "3":
            job = classes[2]
            health += 0
            strength -= 1
            speed += 4
            defense += 1
        elif job == "4":
            job = classes[3]
            health += 2
            strength -= 1
            speed -= 1
            defense += 5
        else:
            print("that is not an option")
            class_selection()
        return job, health, strength, speed, defense
    job, health, strength, speed, defense = class_selection(health, strength, speed, defense)
    
    print(name, "is a", race, job, "with", health, "health,", strength, "strength,", speed, "speed and", defense, "defense")
    with open("Battle Simulator/characters.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, race, job, health, strength, speed, defense, xp])
    return health, strength, speed, defense, xp

# function that lets the user choose what character they want to use
def existing_character():
    while True:
        chosen_name = input("enter the name of the character you want to use: ")

        found = 0
        if found == 0:
            with open("Battle Simulator/characters.csv", "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == chosen_name:
                        chosen_character = row
                        found += 1

        if found == 0:
            print("no character with that name was found.")
            continue
        else:
            name = chosen_character[0]
            race = chosen_character[1]
            job = chosen_character[2]
            health = chosen_character[3]
            strength = chosen_character[4]
            speed = chosen_character[5]
            defense = chosen_character[6]
            xp = chosen_character[7]

        print(name, "is a", race, job, "with", health, "health,", strength, "strength,", speed, "speed,", defense, "defense and", xp, "xp")
        return health, strength, speed, defense, xp

# function that lets the user chose what type of character they want
def character_selection():
    choice = input("""1. Make a new character
    2. Choose an existing character
    Enter the number of the thing you would like to do: """)
    if choice == "1":
        health, strength, speed, defense, xp = character_creator()
        return health, strength, speed, defense, xp
    elif choice == "2":
        health, strength, speed, defense, xp = existing_character()
        return health, strength, speed, defense, xp
    else:
        print("that is not an option")
        character_selection()