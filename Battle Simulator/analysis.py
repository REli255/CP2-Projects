import pandas as pd

# function to do statistical analysis of character stats
def statistical_analysis(name, race, job, health, strength, speed, defense, xp):
    name
    data = {
            'Name' : name,
            'Health': health,
            'Strength': strength,
            'Speed': speed,
            'Defense': defense,
            'XP': xp
            }
    
    df = pd.DataFrame(data)
    print("Character Data:")
    print(df)
    
    print("\nStatistical Analysis:")
    print(f"Mean:\n{df.mean()}")
    print(f"\nMedian:\n{df.median()}")
    print(f"\nMax:\n{df.max()}")
    print(f"\nMin:\n{df.min()}")

    return  name, race, job, health, strength, speed, defense, xp