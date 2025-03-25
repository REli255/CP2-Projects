# Eli Robison, visualizations

import matplotlib.pyplot as plt

# function to display character stats on a bar graph
def bar_graph(name, race, job, health, strength, speed, defense, xp):
    name
    stats = {
            'Health': health,
            'Strength': strength,
            'Speed': speed,
            'Defense': defense,
            'XP': xp
            }
    
    labels = list(stats.keys())
    values = list(stats.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color='skyblue')
    
    plt.title(f'{name} Stats', fontsize=16)
    plt.xlabel('Attributes', fontsize=14)
    plt.ylabel('Values', fontsize=14)
    if int(float(xp)) > 50:
        plt.ylim(0, xp)
    else:
        plt.ylim(0, 50)
    
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    return  name, race, job, health, strength, speed, defense, xp