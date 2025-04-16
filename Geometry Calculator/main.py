# Eli Robison, Classes Project Option 2: Geometry Calculator

"""
OVERVIEW:
Create a Geometry Calculator using Python classes. This project will focus on object-oriented programming concepts, implementing mathematical formulas, and creating a simple text-based user interface. Students will design a system to calculate and compare properties of different geometric shapes.

REQUIRED ELEMENTS:
Class Implementation:
    - Create separate classes for different shapes: Circle, Rectangle, and Triangle
    - Implement a Square class as a subclass of Rectangle Include appropriate attributes for each shape (e.g., radius, length, width, base, height)

Shape Calculations:
    - Implement methods to calculate area and perimeter for each shape
    - Create a method to display all information about a shape Include a static method in each class to explain the formulas used

User Interface:
    - Design a text-based menu for interacting with the calculator
    - Allow users to create multiple shapes and switch between them
    - Include options to perform various calculations on the selected shape

Validation and Error Handling:
    - Implement input validation to ensure positive values for dimensions Handle potential errors (e.g., division by zero, invalid input types)

Shape Comparisons:
    - Create methods to compare two shapes (e.g., has_larger_area(), has_longer_perimeter())
    - Implement a feature to sort multiple shapes based on a chosen property (area or perimeter)

BONUS: (Bonuses are only available to projects submitted on time that meet ALL of the minimum requirements.)
3D Shape Extension: (rectangular prism, cylinder, and triangular prism)
    - Design and implement classes for 3D shapes (3 points)
    - Create methods for volume and surface area calculations (4 points)
    - Extend the user interface to incorporate 3D shape options (5 points)

NOTES:
    - Ensure your program uses proper mathematical formulas for all calculations
    - Comment your code to explain the purpose of each method and any complex logic
    - Use appropriate naming conventions for classes, methods, and variables
    - Round results to a reasonable number of decimal places for readability
    - Consider the user experience when designing your text-based interface
    - Test your program thoroughly to ensure all calculations are accurate
"""

# statement to import a function
from calculator_menu import *

# function with the user interface
def main():
    choice = input("""1. 2D Shapes
    2. 3D Shapes
    3. End
    Enter the number of the thing you would like to do: """)
    if choice == "1":
        two_d_menu()
    elif choice == "2":
        three_d_menu()
    elif choice == "3":
        return "end"
    else:
        print("that is not an option")

# loop that makes sure the program continues until the user is done 
while True:
    end = main()
    if end == "end":
        print("thank you for using this program")
        break