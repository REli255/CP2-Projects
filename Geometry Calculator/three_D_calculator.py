# Eli Robison, the actual calculations happen here

# statement to import a function
from two_D_calculator import *

class rectangular_prism:
    def __init__(self):
        pass
    def surface_area(self):
        pass
    def volume(self):
        pass
    def cube_surface_area(self):
        pass
    def cube_volume(self):
        pass

def rectangular_prisms():
    choice = input("is it 1. just a rectngle or 2. a square (enter the number next to the option you want): ")
    if choice == "1":
        while True:
            try:
                width = float(input("enter the width of the rectangle: "))
                height = float(input("enter the height of the rectangle: "))
            except:
                print("you must enter a number")
                continue
    
            shape = ()
            break
    elif choice == "2":
        while True:
            try:
                sides = float(input("enter the length of sides the square: "))
            except:
                print("you must enter a number")
                continue
    
            shape = ()
            break
    else:
        print("that is not an option")
        rectangular_prisms

class cylinder:
    def __init__(self):
        pass
    def surface_area(self):
        pass
    def volume(self):
        pass

def cylinders():
    try:
        radius = float(input("enter the radius of the base of the cylinder: "))
        height = float(input("enter the height of the cylinder: "))
    except:
        print("you must enter a number")
        cylinders()
    
    shape = ()

class triangular_prism:
    def __init__(self):
        pass
    def surface_area(self):
        pass
    def volume(self):
        pass

def triangular_prisms():
    pass