# Eli Robison, the actual calculations happen here

# statement to import a function
from two_D_calculator import *

class rectangular_prism:
    def __init__(self, width, height_rectangle, height_prism):
        self.width = width
        self.height_rectangle = height_rectangle
        self.height_prism = height_prism
    def surface_area(self):
        edge = (((self.width + self.height_rectangle) * 2) * self.height_prism) + ((self.width * self.height_rectangle) * 2)
        return f'the surface area of the rectangular prism is {edge}'
    def volume(self):
        space = (self.width * self.height_rectangle) * self.height_prism
        return f'the volume of the rectangular prism is {space}'

class cube(rectangular_prism):
    def __init__(self, width, height_rectangle, height_prism):
        super().__init__(width, height_rectangle, height_prism)
    def surface_area(self):
        edge = (self.width ** 2) * 6
        return f'the surface area of the cube is {edge}'
    def volume(self):
        space = self.width ** 3
        return f'the volume of the cube is {space}'

def rectangular_prisms(type_of_info):
    choice = input("is it 1. just a rectangular prism or 2. a cube (enter the number next to the option you want): ")
    if choice == "1":
        while True:
            try:
                width = float(input("enter the width of the rectangle: "))
                height_rectangle = float(input("enter the height of the rectangle: "))
                height_prism = float(input("enter the height of the prism: "))
            except:
                print("you must enter a number")
                continue
    
            shape = rectangular_prism(width, height_rectangle, height_prism)

            if type_of_info == "1":
                print(shape.surface_area())
            elif type_of_info == "2":
                print(shape.volume())
            break
    elif choice == "2":
        while True:
            try:
                sides = float(input("enter the length of sides the cube: "))
            except:
                print("you must enter a number")
                continue
    
            shape = cube(sides, sides, sides)

            if type_of_info == "1":
                print(shape.surface_area())
            elif type_of_info == "2":
                print(shape.volume())
            break
    else:
        print("that is not an option")
        rectangular_prisms(type_of_info)

class cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    def surface_area(self):
        edge = (((self.radius * 2) * 3.14) * self.height) + (((self.radius ** 2) * 3.14) * 2)
        return f'the surface area of the cylinder is {edge}'
    def volume(self):
        space = ((self.radius ** 2) * 3.14) * self.height
        return f'the volume of the cylinder is {space}'

def cylinders(type_of_info):
    try:
        radius = float(input("enter the radius of the base of the cylinder: "))
        height = float(input("enter the height of the cylinder: "))
    except:
        print("you must enter a number")
        cylinders(type_of_info)
    
    shape = cylinder(radius, height)

    if type_of_info == "1":
        print(shape.surface_area())
    elif type_of_info == "2":
        print(shape.volume())

class triangular_prism:
    def __init__(self, base, side_two, side_three, height_triangle, height_prism):
        self.base = base
        self.side_two = side_two
        self.side_three = side_three
        self.height_triangle = height_triangle
        self.height_prism = height_prism
    def surface_area(self):
        edge = ((self.base + self.side_two + self.side_three) * self.height_prism) + (((self.base * self.height_triangle) / 2) * 2)
        return f'the surface area of the triangular_prism is {edge}'
    def volume(self):
        space = ((self.base * self.height_triangle) / 2) * self.height_prism
        return f'the volume of the triangular_prism is {space}'

def triangular_prisms(type_of_info):
    try:
        base = float(input("enter the length of the base of the triangle: "))
        side_two = float(input("enter the length of the second side of the triangle: "))
        side_three = float(input("enter the length of the third side of the triangle: "))
        height_triangle = float(input("enter the height of the triangle: "))
        height_prism = float(input("enter the height of the prism: "))
    except:
        print("you must enter a number")
        triangles()
    
    shape = triangular_prism(base, side_two, side_three, height_triangle, height_prism)

    if type_of_info == "1":
        print(shape.surface_area())
    elif type_of_info == "2":
        print(shape.volume())