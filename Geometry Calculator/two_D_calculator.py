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
    def __init__(self, width, height):
        super().__init__(width, height)
    def perimeter(self):
        edge = (self.width) * 4
        return ("the perimeter of the square is", edge)
    def area(self):
        space = self.width ** 2
        return ("the area of the square is", space)

def rectangles(type_of_info):
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
            print(shape.area())
            break
    else:
        print("that is not an option")
        rectangles()

class circle:
    def __init__(self, radius):
        self.radius = radius
    def circumference(self):
        pass
    def area(self):
        pass

def circles(type_of_info):
    try:
        radius = float(input("enter the radius of the triangle: "))
    except:
        print("you must enter a number")
        circles()
    
    shape = circle()

class triangle:
    def __init__(self, base, side_two, side_three, height):
        self.base = base
        self.side_two = side_two
        self.side_three = side_three
        self.height = height
    def perimeter(self):
        edge = (self.base + self.height)
        return ("the perimeter of the rectangle is", edge)
    def area(self):
        space = self.width * self.height
        return ("the area of the rectangle is", space)
    
def triangles(type_of_info):
    try:
        base = float(input("enter the length of the base of the triangle: "))
        side_two = float(input("enter the length of the second side of the triangle: "))
        side_three = float(input("enter the length of the third side of the triangle: "))
        height = float(input("enter the height of the triangle: "))
    except:
        print("you must enter a number")
        triangles()
    
    shape = triangle(base, side_two, side_three, height)