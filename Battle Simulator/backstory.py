from faker import Faker
import random

fake = Faker()

# Lists of possible places, powers, and weaknesses
place_list = ["dark forest", "abandoned castle", "cave", "swamp", "mountain peak", "haunted village"]
powers_list = ["fire breath", "invisibility", "super strength", "mind control", "necromancy", "shape-shifting"]
weaknesses_list = ["silver", "holy water", "sunlight", "magic spells", "pure iron", "the sound of a bell"]

# Function to generate a backstory
def generate_backstory(species):
    name = fake.name()
    age = random.randint(1, 1000)
    habitat = random.choice(place_list)
    powers = random.sample(powers_list, 2)
    weaknesses = random.sample(weaknesses_list, 1)
    city = fake.city()
    event_date = fake.date_between(start_date='-1000d', end_date='-1d')

    backstory = (
        f"{name}, the {species}, has roamed the {habitat} for over {age} years. \n"
        f"Gifted with {', '.join(powers)}, they strike fear into the hearts of adventurers. \n"
        f"However, they are vulnerable to {', '.join(weaknesses)}. \n"
        f"Legends say that {name} was once a guardian of the realm of {city}, twisted by betrayal and dark magic \n"
        f"after the fateful event on {event_date}. \n"
        f"Now, they haunt the shadows, waiting for the day when they can reclaim their lost honor.\n"
    )
    return backstory