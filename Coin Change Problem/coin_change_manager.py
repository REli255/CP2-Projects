# Eli Robison, Coin Change Manager

# statment to let csv files work
import csv

# function that reads the csv file about the us dollar
def us_dollar():
    types = []

    with open("Coin Change Problem/US_Dollar_($).csv") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            types.append([row[0], float(row[1])])
    
    calculate_answer(types)

# function that reads the csv file about the canadian dollar
def ca_dollar():
    types = []

    with open("Coin Change Problem/Canadian_Dollar_(CA$).csv") as file:
        reader = csv.reader(file)
        for row in reader:
            types.append([row[0], float(row[1])])
    
    calculate_answer(types)

# function that reads the csv file about the british pound
def pound():
    types = []

    with open("Coin Change Problem/British_Pound_(£).csv") as file:
        reader = csv.reader(file)
        for row in reader:
            types.append([row[0], float(row[1])])
    
    calculate_answer(types)

# function that reads the csv file about the european euro
def euro():
    types = []

    with open("Coin Change Problem/Europian Euro (€).csv") as file:
        reader = csv.reader(file)
        for row in reader:
            types.append([row[0], float(row[1])])
    
    calculate_answer(types)

# function that does the calculations
def calculate_answer(types):
    try:
        target = float(input("enter the number you want used for the problem: "))
    except:
        print("you must to enter a number")
        coin_changer()
    
    target = round(target, 2)
    
    print("it will take: ")
    for item in types:
        value = float(item[1])
        if target >= value:
            amount = round(target/value)
            target -= value*amount
            print(amount, item[0])
    print("to reach the target.")

# function that lets the user choose a currency
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