# Eli Robison, my part of the personal finance program

# Limits

import csv

def set_limits():
    try:
        num_limits = int(input("enter the number of limits you want to set: "))
        for x in range(num_limits):
            limit_for = input("enter what expence this limit is for: ")
            limit_is = float(input("enter what you want the limit to be: "))
            limit = [limit_for,limit_is]
            with open("my_part/limits.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(limit)
    except:
        print("you must enter a number")
        set_limits()

def compare_limits():
    limits = []

    with open("my_part/limits.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            limits.append([row[0],float(row[1])])
    
    expenses = []

    with open("my_part/expenses.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            expenses.append([row[0],float(row[1])])
    
    for limit in limits:
        found = 0
        for item in expenses:
            if limit[0] == item[0]:
                gap = limit[1] - item[1]
                print("you have $", gap, "left before you reach the", limit[0], "limit.")
                found += 1
                break
        if found == 0:
            print("no expense was associated with the", limit, "limit.")

def limit_managment():
    choice = input("1. set budget limit or 2. compare expenses? (enter a number): ")
    if choice == "1":
        set_limits()
    elif choice == "2":
        compare_limits()
    else:
        print("that is not an option")
        limit_managment()

# Goals

def set_goals():
    try:
        goal_for = input("enter what what you want the name of this goal to be: ")
        goal_is = float(input("enter how much you want the goal to be: "))
        goal = [goal_for, goal_is, 0]
        with open("my_part/goals.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(goal)
    except:
        print("you must enter a number")
        set_goals()

def advance_goals():
    goals = []

    with open("my_part/goals.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            goals.append([row[0],row[1],row[2]])

    try:
        wanted_goal_name = input("enter what the name of the goal you want to put money towards: ")
        amount = float(input("enter the amount you want to put towards the goal: "))

        amount = round(amount, 2)
    
        found = 0
        for x in range(len(goals)):
            if wanted_goal_name == goals[x][0]:
                goals[x][2] = float(goals[x][2]) + amount
                print("you have put $", amount, "towards the", goals[x][0], "goal.")
                found += 1
        if found == 0:
            print("no goal was found with the name", wanted_goal_name)
        
        count = 0

        for item in goals:
            if count == 0:
                with open("my_part/goals.csv", "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(item)
                    count += 1
            else:
                with open("my_part/goals.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(item)
    except:
        print("you must enter a number")
        advance_goals()

def track_goals():
    goals = []

    with open("my_part/goals.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            goals.append([row[0],float(row[1]),float(row[2])])
    
    for item in goals:
        gap = item[1] - item[2]
        print("you have $", gap, "left before you reach the", item[0], "goal of $", item[1])

def goal_managment():
    choice = input("1. set a savings goal, 2. put money towards a goal or 3. track progress towards a goal? (enter a number): ")
    if choice == "1":
        set_goals()
    elif choice == "2":
        advance_goals()
    elif choice == "3":
        track_goals()
    else:
        print("that is not an option")
        goal_managment()

def expense_managment():
    try:
        expense_for = input("enter what this expense is for: ")
        expense_is = float(input("enter how much the expense is: "))
        expense = [expense_for, expense_is]
        with open("my_part/expenses.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(expense)
    except:
        print("you must enter a number")
        set_goals()

# function with the user interface
def main():
    choice = input("""1. Manage Limits
    2. Manage Goals
    3. Add an Expense
    4. End
    Enter the number of the thing you would like to do: """)
    if choice == "1":
        limit_managment()
    elif choice == "2":
        goal_managment()
    elif choice == "3":
        expense_managment()
    elif choice == "4":
        return "end"
    else:
        print("that is not an option")

# loop that makes sure the program continues until the user is done 
while True:
    end = main()
    if end == "end":
        print("thank you for using this program")
        break