# Eli Robison, Word Counter time handleing

from word_counter import counter

def clock():
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return (current_time)

def timestamp():
    chosen_file = input("Enter the relative path of the text file you want to check the word count of: ")
    number_of_words = counter(chosen_file)
    time = clock()
    with open(chosen_file, "a") as text_file:
        text_file.write(input("Enter what you want to add to the text file: "))