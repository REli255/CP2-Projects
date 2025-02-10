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

with open("Movie Recommender/Movies list.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)
        movies.update({row[0]:row[1]})

print(movies)