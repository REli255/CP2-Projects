# Eli Robison, the calculator menus


# statement to import a function
from two_D_calculator import *
from three_D_calculator import *


def two_d_menu():
    while True:
        choice = input("""1. Rectangle or Square
    2. Circle
    3. Triangle
    4. Exit
    Enter the number of the thing you would like to do: """)
        if choice == "1":
            rectangles()
        elif choice == "2":
            circles()
        elif choice == "3":
            triangles()
        elif choice == "4":
            break
        else:
            print("that is not an option")

def three_d_menu():
    while True:
        choice = input("""1. Rectangular Prism or Cube
    2. Cylinder
    3. Triangular Prism
    4. Exit
    Enter the number of the thing you would like to do: """)
        if choice == "1":
            rectangular_prisms()
        elif choice == "2":
            cylinders()
        elif choice == "3":
            triangular_prisms()
        elif choice == "4":
            break
        else:
            print("that is not an option")