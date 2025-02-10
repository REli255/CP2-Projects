# Eli Robison, Reading Files notes

import csv

with open("notes/test.txt") as file:
    content = file.read()
    #print(content)

users = {}

with open("notes/Class CSV sample - Sheet1.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        users.update({row[0]:row[1]})

print(users)