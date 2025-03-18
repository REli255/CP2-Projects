# Eli Robison, Battle System

# statments to make csv files usable and help make random chocies
import csv
import random

# function that choses a monster randomly and returns its information
def monster_selector(xp_c):
    int(xp_c)
    available_monsters = []
    with open("Battle Simulator/monsters.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[5] <= xp_c:
                available_monsters.append(row)
    chosen_monster = random.choice(available_monsters)

    name = chosen_monster[0]
    health = chosen_monster[1]
    strength = chosen_monster[2]
    speed = chosen_monster[3]
    defense = chosen_monster[4]

    return name, health, strength, speed, defense

# function that makes the battles happen
def battle_simulator(health_c, strength_c, speed_c, defense_c, xp_c):
    name_m, health_m, strength_m, speed_m, defense_m = monster_selector(xp_c)
    print("you will fight the", name_m)

    options = ["Attack", "Defend"]
    while health_c < 0 and health_m < 0:
        player_choice = input("do you want to 1. Attack or 2. Defend (enter the number of the thing you would like to do): ")
        monster_choice = random.choice(options)
        if player_choice == "1" and monster_choice == "Attack":
            print("you picked", player_choice, "and the", name_m, "picked", monster_choice)
            player_damage = strength_m
            monster_damage = strength_c
            print("you take", player_damage, "damage and the", name_m, "takes", monster_damage, "damage")
        elif player_choice == "1" and monster_choice == "Defend":
            print("you picked", player_choice, "and the", name_m, "picked", monster_choice)
            player_damage = 0
            monster_damage = strength_c - defense_m
            print("you take", player_damage, "damage and the", name_m, "takes", monster_damage, "damage")
        elif player_choice == "2" and monster_choice == "Attack":
            print("you picked", player_choice, "and the", name_m, "picked", monster_choice)
            player_damage = strength_m - (defense_c + speed_c - speed_m)
            monster_damage = 0
            print("you take", player_damage, "damage and the", name_m, "takes", monster_damage, "damage")
        elif player_choice == "2" and monster_choice == "Defend":
            print("you picked", player_choice, "and the", name_m, "picked", monster_choice)
            player_damage = 0
            monster_damage = 0
            print("you take", player_damage, "damage and the", name_m, "takes", monster_damage, "damage")
        else:
            print("that is not an option")
    
    if health_m <= 0:
        xp_c += 10
    elif health_c <= 0:
        xp_c -= 15
    
    return health_c, strength_c, speed_c, defense_c, xp_c