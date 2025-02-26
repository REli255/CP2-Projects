# Eli Robison, page with the Word Counter

def counter(chosen_file):
    words = 0
    with open(chosen_file, "r") as text_file:
        for word in text_file:
            words += 1
    print(words)