# Eli Robison, Coin Change Problem

"""
OVERVIEW:
Create a program that allows users to solve the Coin Change Problem by inputting a
target amount and the available coin denominations. The program should load the
coin denominations from a file based on the user's input of a country and then
calculate the minimum number of coins needed to make the target amount. The
program should also display the names of the coins used in the solution.

REQUIREMENTS:
Coin Denomination File:
Create a text or CSV file that contains the coin denominations for different
countries (minimum of 4).
Comma-separated list of coin names and values (e.g., "Penny-1,Nickel-5,Dime-
10,Quarter-25").

Coin Change Problem:
Implement the logic to solve the Coin Change Problem using the provided coin
denominations.
The program should handle various edge cases, such as negative or zero target
amounts, and invalid coin denominations.

User Interaction:
Prompt the user to enter the country for which they want to solve the Coin
Change Problem.
Prompt the user to enter the target amount.
Display the minimum number of coins needed to make the target amount, as
well as the names of the coins used.

Program Structure:
Use inner functions to implement the main features (loading coin
denominations, solving the Coin Change Problem).
Implement helper functions for repetitive tasks (e.g., reading and parsing the
coin denomination file).
Create a main function to handle user interaction and call the appropriate
functions.

Error Handling:
Ensure the program handles potential errors, such as the coin denomination
file not being found or the user providing invalid inputs.

NOTES:
Focus on using inner and helper functions to organize your code.
Ensure your program handles potential errors (e.g., file not found, invalid user
input).
Comment your code to explain the purpose of each function and any complex
logic.
Test your program thoroughly to ensure all features work as expected.
"""

from coin_change_manager import *

# function with the user interface
def main():
    currency = input("""1. US Dollar ($)
    2. Canadian Dollar (CA$)
    3. British Pound (£)
    4. Europian Euro (€)
    Enter the number of the type of money you would like to use: """)

    choice = input("""1. Get change for a amount of money
    2. End
    Enter the number of the thing you would like to do: """)
    if choice == "1" and currency == "1":
        ()
    elif choice == "1" and currency == "2":
        ()
    elif choice == "1" and currency == "3":
        ()
    elif choice == "1" and currency == "4":
        ()
    elif choice == "2":
        return "end"
    else:
        print("that is not an option")

# loop that makes sure the program continues until the user is done 
while True:
    end = main()
    if end == "end":
        print("thank you for using this program")
        break