# Eli Robison, Battle System

from backstory import generate_backstory
from visualizations import pie_chart

# statments to make csv files usable and help make random chocies
import csv
import random

# function that choses a monster randomly and returns its information
def monster_selector(xp_c):
    xp_c
    available_monsters = []
    with open("Battle Simulator/monsters.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if float(row[5]) <= xp_c:
                available_monsters.append(row)
    chosen_monster = random.choice(available_monsters)

    name = chosen_monster[0]
    health = float(chosen_monster[1])
    strength = float(chosen_monster[2])
    speed = float(chosen_monster[3])
    defense = float(chosen_monster[4])

    backstory = generate_backstory(name)

    pie_chart(health, strength, speed, defense)

    return name, health, strength, speed, defense, backstory

# function that makes the battles happen
def battle_simulator(name_c, race_c, job_c, health_c, strength_c, speed_c, defense_c, xp_c):
    name_m, health_m, strength_m, speed_m, defense_m, backstory = monster_selector(xp_c)
    print("you will fight the", name_m)
    print(backstory)

    options = ["Attack", "Defend"]
    while health_c > 0.0 and health_m > 0.0:
        player_choice = input("do you want to 1. Attack or 2. Defend (enter the number of the thing you would like to do): ")
        monster_choice = random.choice(options)
        if player_choice == "1" and monster_choice == "Attack":
            print("you picked Attack and the", name_m, "picked", monster_choice)
            player_damage = strength_m
            monster_damage = strength_c
            print("you take", player_damage, "damage and the", name_m, "takes", monster_damage, "damage")
        elif player_choice == "1" and monster_choice == "Defend":
            print("you picked Attack and the", name_m, "picked", monster_choice)
            player_damage = 0
            monster_damage = strength_c - defense_m
            print("you take", player_damage, "damage and the", name_m, "takes", monster_damage, "damage")
        elif player_choice == "2" and monster_choice == "Attack":
            print("you picked Defend and the", name_m, "picked", monster_choice)
            player_damage = strength_m - (defense_c + speed_c - speed_m)
            monster_damage = 0
            print("you take", player_damage, "damage and the", name_m, "takes", monster_damage, "damage")
        elif player_choice == "2" and monster_choice == "Defend":
            print("you picked Defend and the", name_m, "picked", monster_choice)
            player_damage = 0
            monster_damage = 0
            print("you take", player_damage, "damage and the", name_m, "takes", monster_damage, "damage")
        else:
            print("that is not an option")
            continue
        health_c -= player_damage
        health_m -= monster_damage
    
    if health_m <= 0.0:
        xp_c += 10
        print("you won and gained 10 xp")
    elif health_c <= 0.0:
        xp_c -= 15
        ("the", name_m, "won and you lost 15 xp")
    with open("Battle Simulator/characters.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name_c, race_c, job_c, health_c, strength_c, speed_c, defense_c, xp_c])
    
    return name_c, race_c, job_c, health_c, strength_c, speed_c, defense_c, xp_c