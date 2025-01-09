# Eli Robison, Financial Calculator

"""
OVERVIEW:
Create a program that completes the following basic financial calculations:
How long it will take to save for a goal based on a weekly or monthly deposit
Compound Interest Calculator 
Budget Allocator (use set percentages to divide an income into spending categories like savings, entertainment, and food)
Sale Price Calculator (apply discounts to prices)
Tip Calculator
PROJECT STEPS:
Create a main function that will run the user interface
Using project decomposition to figure out what other functions you need and how they interact with each other
Create your functions
"""

def saving():
    pass

def interest():
    money = input("enter how much money is in the account: ")
    rate = input("enter the intrest rate of the account: ")
    time = input("enter how long the account will accumulate intrest for: ")

def budget():
    pass

def sale():
    pass

def tip():
    pass

def main():
    choice = int(input("""1. Calculate how long it will take to Save for a Goal
    2. Compound Interest Calculator
    3. Budget Allocator
    4. Sale Price Calculator
    5. Tip Calculator
    6. End
    Enter the number of the thing you would like to do: """))
    if choice == 1:
        saving()
    elif choice == 2:
        interest()
    elif choice == 3:
        budget()
    elif choice == 4:
        sale()
    elif choice == 5:
        tip()
    elif choice == 6:
        return "end"
    else:
        print("that is not an option")

while True:
    end = main()
    if end == "end":
        break