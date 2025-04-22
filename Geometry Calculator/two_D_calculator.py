# Eli Robison, the actual calculations happen here

class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def perimeter(self):
        edge = (self.width + self.height) * 2
        return f'the perimeter of the rectangle is {edge}'
    def area(self):
        space = self.width * self.height
        return f'the area of the rectangle is {space}'
    def diplay_all_info(self):
        print("the width of the rectangle is", self.width)
        print("the height of the rectangle is", self.height)
        print("the perimeter of the rectangle is", (self.width + self.height) * 2)
        print("the area of the rectangle is", self.width * self.height)
    @staticmethod
    def formulas():
        print("the formula for the perimeter is adding the lengths of the sides together")
        print("the formula for the area is base times height")

class square(rectangle):
    def __init__(self, width, height):
        super().__init__(width, height)
    def perimeter(self):
        edge = self.width * 4
        return f'the perimeter of the square is {edge}'
    def area(self):
        space = self.width ** 2
        return f'the area of the square is {space}'
    def diplay_all_info(self):
        print("the sides of the square are", self.width)
        print("the perimeter of the square is", self.width * 4)
        print("the area of the square is", self.width ** 2)
    @staticmethod
    def formulas():
        print("the formula for the perimeter is adding the lengths of the sides together")
        print("the formula for the area is the lenght of a side squared")

def rectangles(type_of_info):
    choice = input("is it 1. just a rectangle or 2. a square (enter the number next to the option you want): ")
    if choice == "1":
        while True:
            try:
                width = float(input("enter the width of the rectangle: "))
                height = float(input("enter the height of the rectangle: "))
            except:
                print("you must enter a number")
                continue
    
            shape = rectangle(width, height)

            if type_of_info == "1":
                print(shape.perimeter())
            elif type_of_info == "2":
                print(shape.area())
            elif type_of_info == "3":
                shape.diplay_all_info()
            elif type_of_info == "4":
                shape.formulas()
            break
    elif choice == "2":
        while True:
            try:
                sides = float(input("enter the length of sides the square: "))
            except:
                print("you must enter a number")
                continue
    
            shape = square(sides, sides)

            if type_of_info == "1":
                print(shape.perimeter())
            elif type_of_info == "2":
                print(shape.area())
            elif type_of_info == "3":
                shape.diplay_all_info()
            elif type_of_info == "4":
                shape.formulas()
            break
    else:
        print("that is not an option")
        rectangles()

class circle:
    def __init__(self, radius):
        self.radius = radius
    def circumference(self):
        edge = (self.radius * 2) * 3.14
        return f'the circumference of the circle is {edge}'
    def area(self):
        space = (self.radius ** 2) * 3.14
        return f'the area of the circle is {space}'
    def diplay_all_info(self):
        print("the radius of the circle is", self.radius)
        print("the circumference of the circle is", (self.radius * 2) * 3.14)
        print("the area of the circle is", (self.radius ** 2) * 3.14)
    @staticmethod
    def formulas():
        print("the formula for the circumference is the radius dubled times 3.14")
        print("the formula for the area is the radius squared times 3.14")

def circles(type_of_info):
    try:
        radius = float(input("enter the radius of the circle: "))
    except:
        print("you must enter a number")
        circles()
    
    shape = circle(radius)

    if type_of_info == "1":
        print(shape.circumference())
    elif type_of_info == "2":
        print(shape.area())
    elif type_of_info == "3":
        shape.diplay_all_info()
    elif type_of_info == "4":
        shape.formulas()

class triangle:
    def __init__(self, base, side_two, side_three, height):
        self.base = base
        self.side_two = side_two
        self.side_three = side_three
        self.height = height
    def perimeter(self):
        edge = self.base + self.side_two + self.side_three
        return f'the perimeter of the triangle is {edge}'
    def area(self):
        space = (self.base * self.height) / 2
        return f'the area of the triangle is {space}'
    def diplay_all_info(self):
        print("the base of the triangle is", self.base)
        print("the second side of the triangle is", self.side_two)
        print("the third side of the triangle is", self.side_three)
        print("the height of the triangle is", self.height)
        print("the perimeter of the triangle is", self.base + self.side_two + self.side_three)
        print("the area of the triangle is", (self.base * self.height) / 2)
    @staticmethod
    def formulas():
        print("the formula for the perimeter is adding the lengths of the sides together")
        print("the formula for the area is base times height divided by 2")
    
    
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

    if type_of_info == "1":
        print(shape.perimeter())
    elif type_of_info == "2":
        print(shape.area())
    elif type_of_info == "3":
        shape.diplay_all_info()
    elif type_of_info == "4":
        shape.formulas()