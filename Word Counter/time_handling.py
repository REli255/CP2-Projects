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
        text_file.write("word count equaled ")
        text_file.write(number_of_words)
        text_file.write(" at ")
        text_file.write(time)
        text_file.write("\n")