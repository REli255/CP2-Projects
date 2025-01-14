# Eli Robison, Personal Library



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