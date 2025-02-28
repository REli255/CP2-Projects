# Eli Robison, page with the Word Counter

def counter(chosen_file):
    words = 0
    with open(chosen_file, "r") as text_file:
        data = text_file.read()
        lines = data.split()
        for word in lines:
            words += 1
    print(words)
    return (words)