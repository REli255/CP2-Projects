# Eli Robison, Coin Change Manager

import csv

def us_dollar():
    types = {}

    with open("Coin Change Problem/US_Dollar_($).csv") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            types.update({row[0]:row[1]})
    
    calculate_answer(types)

def ca_dollar():
    types = {}

    with open("Coin Change Problem/Canadian_Dollar_(CA$).csv") as file:
        reader = csv.reader(file)
        for row in reader:
            types.update({row[0]:row[1]})
    
    calculate_answer(types)

def pound():
    types = {}

    with open("Coin Change Problem/British_Pound_(£).csv") as file:
        reader = csv.reader(file)
        for row in reader:
            types.update({row[0]:row[1]})
    
    calculate_answer(types)

def euro():
    types = {}

    with open("Coin Change Problem/Europian Euro (€).csv") as file:
        reader = csv.reader(file)
        for row in reader:
            types.update({row[0]:int(row[1])})
    
    calculate_answer(types)

def calculate_answer(types):
    try:
        target = float(input())
    except:
        print("you must to enter a number")
        coin_changer()
    
    target = round(target, 2)
    
    for item in types:
        if target >= item[2]:
            amount = round(target/item[2])
            target -= item[2]*amount
            print(amount, item[1])

def coin_changer():
    currency = input("""1. US Dollar ($)us dollar
    2. Canadian Dollar (CA$)
    3. British Pound (£)
    4. Europian Euro (€)
    Enter the number of the type of money you would like to use: """)
 
    if currency == "1":
        us_dollar()
    elif currency == "2":
        ca_dollar()
    elif currency == "3":
        pound()
    elif currency == "4":
        euro()
    else:
        print("that is not an option")
        coin_changer()