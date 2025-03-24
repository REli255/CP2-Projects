from faker import Faker
import random

# Step 1: Create a Faker instance
fake = Faker()

# Step 2: Define a function to generate a character with a backstory
def generate_character():
    name = fake.name()  # Generate a random name
    age = random.randint(18, 60)  # Generate a random age
    backstory = fake.paragraph(nb_sentences=3)  # Generate a random backstory
    return {
        'name': name,
        'age': age,
        'backstory': backstory
    }

# Step 3: Generate multiple characters
num_characters = 5  # Change this to generate more or fewer characters
characters = [generate_character() for _ in range(num_characters)]

# Step 4: Print the characters
for character in characters:
    print(f"Name: {character['name']}")
    print(f"Age: {character['age']}")
    print(f"Backstory: {character['backstory']}\n")