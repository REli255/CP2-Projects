# Eli Robison, the calculator menus


# statements to import functions
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
            type_of_info = input("do you want 1. the perimeter or 2. the area (enter the number next to the option you want): ")
            if type_of_info == "1" or type_of_info == "2":
                rectangles()
            else:
                print("that is not an option")
        elif choice == "2":
            type_of_info = input("do you want 1. the circumference or 2. the area (enter the number next to the option you want): ")
            if type_of_info == "1" or type_of_info == "2":
                rectangles()
            else:
                print("that is not an option")
        elif choice == "3":
            type_of_info = input("do you want 1. the perimeter or 2. the area (enter the number next to the option you want): ")
            if type_of_info == "1" or type_of_info == "2":
                rectangles()
            else:
                print("that is not an option")
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
        type_of_info = input("do you want 1. the surface area or 2. the volume (enter the number next to the option you want): ")
        if type_of_info != "1" and type_of_info != "2":
            print("that is not an option")
            continue
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