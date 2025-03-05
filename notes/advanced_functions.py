# Eli Robison, Advanced Functions Notes

# What is a helper function?
    # A function writen to be called in another function.
def is_int(user_input):
    try:
        int(user_input)
    except:
        # What is recursion?
            # when you call a function inside itself.
        # How does recursion work?
        print("please give me a number.")
        user_input = is_int(input("enter your age: "))
    else:
        return int(user_input)
def age():
    old = is_int(input("enter your age: "))
    print(f"cool, you are {old}")
age()

# What is the purpose of a helper function?
    # to make other functions less large.
# What is an inner function?
    # A function that exists inside another function
def added(a):
    def addition(b):
        print(a + b)
    addition()
added(3)

# What is the scope of a variable in a function WITH an inner function?
    # the outer and inner function
# Why do we use inner functions?
    # to keep it safe from other code
# What is a closure function?
    # a function that lets you rmember values across multiple calls
# Why do we write closure functions?
def add(a):
    b = input("give me a number")
    def addition():
        return (a + b)
    return addition()
base = add(10)
print(base(5))