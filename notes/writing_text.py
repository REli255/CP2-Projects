# Eli Robison, writing to text notes

import csv

"""
r = to read the filr
w = write on the file(replaces the old file)
w+ = 
a = 
x = 
a+ = append and read the file
"""

#with open("notes/test.txt", "w") as file:
#    file.write("fire is fun")

with open("notes/user_info.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows([["fire", "red"], ["air", "white"], ["water", "blue"], ["earth", "brown"], ["silly_username", "pink"]])

with open("notes/user_info.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print({row[0]:row[1]})