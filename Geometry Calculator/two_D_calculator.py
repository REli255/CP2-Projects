# Eli Robison, the actual calculations happen here

class rectangle:
    def __init__(self):
        pass
    def perimeter(self):
        pass
    def area(self):
        pass

class square(rectangle):
    def __init__(self):
        super().__init__()
    def square_perimeter(self):
        pass
    def square_area(self):
        pass

def rectangles():
    choice = input("is it 1. just a rectngle or 2. a square (enter the number next to the option you want): ")
    if choice == "1":
        try:
            length = float(input("enter the length of the rectangle: "))
            height = float(input("enter the height of the rectangle: "))
        except:
            print("you must enter a number")
    
        shape = ()
    elif choice == "2":
        try:
            length = float(input("enter the length of the rectangle: "))
            height = float(input("enter the height of the rectangle: "))
        except:
            print("you must enter a number")
    
        shape = ()
    else:
        print("that is not an option")

class circle:
    def __init__(self):
        pass
    def circumference(self):
        pass
    def area(self):
        pass

def circles():
    try:
        radius = float(input("enter the radius of the triangle: "))
    except:
        print("you must enter a number")
    
    shape = ()

class triangle:
    def __init__(self):
        pass
    def perimeter(self):
        pass
    def area(self):
        pass
    
def triangles():
    try:
        base = float(input("enter the length of the base of the triangle: "))
        height = float(input("enter the height of the triangle: "))
    except:
        print("you must enter a number")
    
    shape = ()