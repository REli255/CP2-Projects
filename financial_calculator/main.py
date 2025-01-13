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
    often = input("how often are you going to deposit (daily, weekly, montly or yearly): ")
    amount = int(input("how much are you going to deposit each time: "))
    time = goal / amount
    if often == "daily" or often == "Daily":
        print("It would take you", time, "days to save your goal of $", goal)
    elif often == "weekly" or often == "Weekly":
        print("It would take you", time, "weeks to save your goal of $", goal)
    elif often == "monthly" or often == "Monthly":
        print("It would take you", time, "months to save your goal of $", goal)
    elif often == "yearly" or often == "Yearly":
        print("It will take you", time, "years to save your goal of $", goal)
    else:
        print("that is not an option")

def interest():
    money_old = int(input("enter how much money is in the account: "))
    rate = float(input("enter the yearly intrest rate of the account: "))
    time = int(input("enter how long the account will accumulate intrest for (in years): "))
    rate = rate / 100
    money_new = money_old
    for t in range(time):
        money_new = (money_new + (money_new * rate))
    print("$", money_old, "became $", money_new, "over", time, "years!")

def budget():
    pass

def sale():
    price_old = int(input("enter the original price of the item: "))
    sale = int(input("enter what precent off the item is: "))
    sale = sale / 100
    price_new = price_old - (price_old * sale)
    print("the new price of the item on sale is $", price_new)

def tip():
    spent = int(input("enter the original price of the item: "))
    rate = int(input("enter what precent off the item is: "))
    rate = rate / 100
    your_tip = spent + (spent * rate)
    print("the new price of the item on sale is $", your_tip)

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
        print("thank you for using this program")
        break