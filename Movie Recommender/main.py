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

# lets the program use CSV files
import csv

# lists to store information about the movies
movies = {}
information = []

# opens the CSV file and adds information to the lists
with open("Movie Recommender/Movies list.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        movies.update({row[0]:row[1]})
        information.append(row)

# function that displays the list of movies
def display():
    while True:
        amount = input("""1. Title and Director
    2. All information
    Enter the number of the amount of information you would like to be displayed: """)
        # conditional that makes only the selected amount of information be displayed
        if amount == "1":
            for movie in movies:
                print(movie, "directed by", movies[movie])
        elif amount == "2":
            for rank in information:
                print(rank[0], "directed by", rank[1], "is a", rank[2], "movie. It is rated", rank[3], ",", rank[4], "minutes long and has", rank[5], "in it.")
        else:
            print("that is not an option")
            continue
        break


# function that searches for a specific movie
def specific_search():
    found = 0
    title  = input("enter the title of the movie you are searching for: ")
    # loop that check every item in the list to see if it matches
    for rank in information:
        if title == rank[0]:
            print(rank[0], "directed by", rank[1], "is a", rank[2], "movie. It is rated", rank[3], ",", rank[4], "minutes long and has", rank[5], "in it.")
            found += 1
    if found == 0:
        print("there is not a movie in the list that fits your search")

# function that searches for a catagory of movie
def general_search():
    while True:
        found = 0
        type = input("""do you want to search by 1. title, 2. director, 3. genre, 4. rating, 5. length or 6. notable actors
                     enter the number of the category you want to search by: """)
        # conditional that searches the list for movies that fit in the selected catagory
        if type == "1":
            item = input("enter the title of the movies you are searching for: ")
            for rank in information:
                if item in rank[0]:
                    print(rank[0], "directed by", rank[1], "is a", rank[2], "movie. It is rated", rank[3], ",", rank[4], "minutes long and has", rank[5], "in it.")
                    found += 1
        elif type == "2":
            item = input("enter the director of the movies you are searching for: ")
            for rank in information:
                if item in rank[1]:
                    print(rank[0], "directed by", rank[1], "is a", rank[2], "movie. It is rated", rank[3], ",", rank[4], "minutes long and has", rank[5], "in it.")
                    found += 1
        elif type == "3":
            item = input("enter the genre of the movies you are searching for: ")
            for rank in information:
                if item in rank[2]:
                    print(rank[0], "directed by", rank[1], "is a", rank[2], "movie. It is rated", rank[3], ",", rank[4], "minutes long and has", rank[5], "in it.")
                    found += 1
        elif type == "4":
            item = input("enter the rating of the movies you are searching for: ")
            for rank in information:
                if item == rank[3]:
                    print(rank[0], "directed by", rank[1], "is a", rank[2], "movie. It is rated", rank[3], ",", rank[4], "minutes long and has", rank[5], "in it.")
                    found += 1
        elif type == "5":
            item = input("enter the length (in minutes) of the movies you are searching for: ")
            for rank in information:
                if item == rank[4]:
                    print(rank[0], "directed by", rank[1], "is a", rank[2], "movie. It is rated", rank[3], ",", rank[4], "minutes long and has", rank[5], "in it.")
                    found += 1
        elif type == "6":
            item = input("enter the name of a notable actor in the movies you are searching for: ")
            for rank in information:
                if item in rank[5]:
                    print(rank[0], "directed by", rank[1], "is a", rank[2], "movie. It is rated", rank[3], ",", rank[4], "minutes long and has", rank[5], "in it.")
                    found += 1
        else:
            print("that is not an option")
            continue
        if found == 0:
            print("there is not a movie in the list that fits your search")
        break

# function with the user interface
def main():
    choice = input("""1. display the list of movies
    2. Search for a specific movie
    3. search for a catagory of movie
    4. End
    Enter the number of the thing you would like to do: """)
    # conditional that makes the function the user selects activate
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