import matplotlib.pyplot as plt

# Step 1: Define character stats
character_name = "Hero"
stats = {
    'Strength': 85,
    'Agility': 70,
    'Intelligence': 90,
    'Endurance': 75,
    'Charisma': 60
}

# Step 2: Prepare data for plotting
labels = list(stats.keys())
values = list(stats.values())

# Step 3: Create the bar graph
plt.figure(figsize=(10, 6))
plt.bar(labels, values, color='skyblue')

# Step 4: Customize the graph
plt.title(f'{character_name} Stats', fontsize=16)
plt.xlabel('Attributes', fontsize=14)
plt.ylabel('Values', fontsize=14)
plt.ylim(0, 100)  # Assuming the max stat value is 100

# Step 5: Display the graph
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()