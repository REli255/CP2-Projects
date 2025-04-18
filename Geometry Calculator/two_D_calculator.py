# Eli Robison, the actual calculations happen here

class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def perimeter(self):
        edge = (self.width + self.height) * 2
        return ("the perimeter of the rectangle is", edge)
    def area(self):
        space = self.width * self.height
        return ("the area of the rectangle is", space)

class square(rectangle):
    def __init__(self):
        super().__init__()
    def square_perimeter(self):
        edge = (self.width + self.height) * 2
        return ("the perimeter of the square is", edge)
    def square_area(self):
        space = self.width * self.height
        return ("the area of the rectangle is", space)

def rectangles():
    choice = input("is it 1. just a rectngle or 2. a square (enter the number next to the option you want): ")
    if choice == "1":
        while True:
            try:
                width = float(input("enter the width of the rectangle: "))
                height = float(input("enter the height of the rectangle: "))
            except:
                print("you must enter a number")
                continue
    
            shape = rectangle(width, height)
            break
    elif choice == "2":
        while True:
            try:
                sides = float(input("enter the length of sides the square: "))
            except:
                print("you must enter a number")
                continue
    
            shape = square(sides, sides)
            break
    else:
        print("that is not an option")
        rectangles()

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
        circles()
    
    shape = circle()

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
        triangles()
    
    shape = triangle()