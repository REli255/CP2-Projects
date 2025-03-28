# Eli Robison, Coin Change Manager

import csv

def us_dollar():
    types = {}

    with open("Coin Change Problem/US_Dollar_($).csv") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            types.update({row[0]:row[1]})

def ca_dollar():
    types = {}

    with open("Coin Change Problem/Canadian_Dollar_(CA$).csv") as file:
        reader = csv.reader(file)
        for row in reader:
            types.update({row[0]:row[1]})

def pound():
    types = {}

    with open("Coin Change Problem/British_Pound_(£).csv") as file:
        reader = csv.reader(file)
        for row in reader:
            types.update({row[0]:row[1]})

def euro():
    types = {}

    with open("Coin Change Problem/Europian Euro (€).csv") as file:
        reader = csv.reader(file)
        for row in reader:
            types.update({row[0]:row[1]})

def coin_changer():
    try:
        target = float(input())
    except:
        print("you must to enter a number")
        coin_changer()
    
    target = round(target, 2)

    if currency == "1":
        us_dollar(target)
    elif currency == "2":
        ca_dollar(target)
    elif currency == "3":
        pound(target)
    elif currency == "4":
        euro(target)