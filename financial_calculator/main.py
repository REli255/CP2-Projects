# Eli Robison, Financial Calculator

"""
OVERVIEW:
Create a program that completes the following basic financial calculations:
How long it will take to save for a goal based on a weekly or monthly deposit
Budget Allocator (use set percentages to divide an income into spending categories like savings, entertainment, and food)
Sale Price Calculator (apply discounts to prices)
Tip Calculator
PROJECT STEPS:
Create a main function that will run the user interface
Using project decomposition to figure out what other functions you need and how they interact with each other
Create your functions
"""

def saving():
    goal = int(input("what is the goal you are saving for: "))
    often = input("how often are you going to deposit: ")
    amount = int(input("how much are you going to deposit each time: "))
    time = goal / amount
    if often == "daily" or often == "Daily":
        print("")
    elif often == "weekly" or often == "Weekly":
        pass
    elif often == "monthly" or often == "Monthly":
        pass
    elif often == "yearly" or often == "Yearly":
        pass
    else:
        print("that is not an option")

def interest():
    money_old = int(input("enter how much money is in the account: "))
    rate = int(input("enter the yearly intrest rate of the account: "))
    time = int(input("enter how long the account will accumulate intrest for (in years): "))
    rate = rate / 100
    money_new = (money_old + (money_old * rate)) * time
    print("$", money_old, "became $", money_new, "over", time, "years!")

def budget():
    pass

def sale():
    pass

def tip():
    pass

def main():
    choice = input("""1. Calculate how long it will take to Save for a Goal
    2. Compound Interest Calculator
    3. Budget Allocator
    4. Sale Price Calculator
    5. Tip Calculator
    6. End
    Enter the number of the thing you would like to do: """)
    if choice == "1":
        saving()
    elif choice == "2":
        interest()
    elif choice == "3":
        budget()
    elif choice == "4":
        sale()
    elif choice == "5":
        tip()
    elif choice == "6":
        return "end"
    else:
        print("that is not an option")

while True:
    end = main()
    if end == "end":
        break