# Eli Robison, Movie Recommender

"""
Using the provided list of movies create a program that will read the list and give
top movie recommendations based on genre, directors, length, and/or actors. 

Program should be able to combine at least 2 search criteria to narrow down the list
of options. 

REQUIREMENTS:
Uses the provided Movies list
User is able to choose at least 2 filters for the program to search through
User can get recommendations based on genre, directors, length and/or actors 
User is able to print the whole list
"""

import csv

movies = {}
information = []

with open("Movie Recommender/Movies list.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        movies.update({row[0]:row[1]})
        information.append(row)

def display():
    amount = input("""1. Title and Director
    2. All information
    Enter the number of the amount of information you would like to be displayed: """)
    if amount == "1":
        for movie in movies:
            print(movie, "directed by", movies[movie])
    elif amount == "2":
        for rank in information:
            print(rank[0], "directed by", rank[1], "is a", rank[2], "movie. It is rated", rank[3], ",", rank[4], "minutes long and has", rank[5], "in it.")
    else:
        print("that is not an option")

def specific_search():
    for z in range(1):
        found = 0
        type = input("""do you want to search by 1. title, 2. author, 3. type of cover or 4. number of pages
                     enter the number of the category you want to search by: """)
        if type == "1":
            item = input("enter the title of the book you are searching for: ")
            for x in range(len(library)):
                if item == library[x]["Title"]:
                    print(library[x])
                    found += 1
        elif type == "2":
            item = input("enter the author of the book you are searching for: ")
            for x in range(len(library)):
                if item == library[x]["Author"]:
                    print(library[x])
                    found += 1
        elif type == "3":
            item = input("enter the type of cover of the book you are searching for: ")
            for x in range(len(library)):
                if item == library[x]["Cover"]:
                    print(library[x])
                    found += 1
        elif type == "4":
            item = input("enter the number of pages in the book you are searching for: ")
            for x in range(len(library)):
                if item == library[x]["Pages"]:
                    print(library[x])
                    found += 1
        else:
            print("that is not an option")
            pass
        if found == 0:
            print("there is not a book in the library that fits your search")

def general_search():
    for q in range(1):
        found = 0
        type = input("""do you want to search by 1. title, 2. author, 3. type of cover or 4. number of pages
                     enter the number of the category you want to search by: """)
        if type == "1":
            item = input("enter the title of the book you are searching for: ")
            for x in range(len(library)):
                if item == library[x]["Title"]:
                    print(library[x])
                    found += 1
        elif type == "2":
            item = input("enter the author of the book you are searching for: ")
            for x in range(len(library)):
                if item == library[x]["Author"]:
                    print(library[x])
                    found += 1
        elif type == "3":
            item = input("enter the type of cover of the book you are searching for: ")
            for x in range(len(library)):
                if item == library[x]["Cover"]:
                    print(library[x])
                    found += 1
        elif type == "4":
            item = input("enter the number of pages in the book you are searching for: ")
            for x in range(len(library)):
                if item == library[x]["Pages"]:
                    print(library[x])
                    found += 1
        else:
            print("that is not an option")
            pass
        if found == 0:
            print("there is not a book in the library that fits your search")

# function with the user interface
def main():
    choice = input("""1. display the list of movies
    2. Search for a specific movie
    3. search for a catagory of movie
    4. End
    Enter the number of the thing you would like to do: """)
    if choice == "1":
        display()
    elif choice == "2":
        specific_search()
    elif choice == "3":
        general_search()
    elif choice == "4":
        return "end"
    else:
        print("that is not an option")

# loop that makes sure the program continues until the user is done 
while True:
    end = main()
    if end == "end":
        print("thank you for using this program")
        break