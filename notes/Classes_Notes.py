# Eli Robison, Classes and Objects in Python

class subject:
    def __init__(self, content, period, teacher, room):
        self.content = content
        self.period = period
        self.teacher = teacher
        self.room = room

    def __str__(self):
        return f'Name: {self.content}\nPeriod: {self.period}\nTeacher: {self.teacher}\nRoom: {self.room}'

first = subject("CS Principles", 1, "LaRose", 200)
second = subject("CS2", 2, "LaRose", 200)

print(first)
print(second.content)

class pokemon:
    def __init__(self, name, species, hp, dmg):
        self.name = name
        self.species = species
        self.hp = hp
        self.dmg = dmg
    
    def __str__(self):
        return f'{self.name} is a {self.species} and have {self.hp} HP and do {self.dmg} amount of damage in battle.'
    
    def battle(self, opponent):
        while self.hp > 0 and opponent.hp > 0:
            opponent.hp -= self.dmg
            print(f'{self.name} attacked {opponent.name} for {self.dmg} and {opponent.name} now has {opponent.hp}')

            if opponent.hp <= 0:
                print(f'{opponent.name} is knocked out. {self.name} wins!')
            else:
                self.hp -= opponent.dmg
                print(f'{opponent.name} attacked {self.name} for {opponent.dmg} and {self.name} now has {self.hp}')
                if opponent.hp <= 0:
                    print(f'{self.name} is knocked out. {opponent.name} wins!')

fluffy = pokemon("Fluffy", "Arcanine", 280, 110)
slimy = pokemon("Slimy", "Ditto", 100, 70)
spikey = pokemon("Spikey", "Jolteon", 150, 100)

fluffy.battle(spikey)

# What is a class in python?
    # a blueprint for an object
# What is an object in python?
    # an instance of a class
# How do python classes relate to python objects?
    # the object is based of the class
# How do you create a python class?
    # 'class name:'
# What are methods?
    # a function that exists for a specific class 
# How do you create a python object?
    # 'name_of_object = name_of_class(object's information)'
# How to you call a method for an object?
    # 'name_of_object.name_of_method'
# Why do we use python classes?
    # Python classes help with object oriented programming