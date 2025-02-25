# Eli Robison, my part of the highscore program

import csv

scores = []

with open("my part/scores.csv", "r") as file:
    for row in file:
        scores.append(row)

def display_top_ten():
    top = 10
    for score in scores:
        if top <= 0:
            break
        print(score)
        top -= 1

display_top_ten()