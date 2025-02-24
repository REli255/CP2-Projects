# Eli Robison, Using Multiple Pages Notes

from calc import addition as add, subtraction as sub, num

print(add())
print(sub())
print(num)

def get_user_info():
    name = input("enter your name: ")
    age = input("enter your age: ")
    height = input("enter your height: ")
    return name, age, height

name, age, height = get_user_info()

print(age)