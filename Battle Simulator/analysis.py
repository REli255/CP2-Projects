import pandas as pd

# function to do statistical analysis of character stats
def statistical_analysis(name, race, job, health, strength, speed, defense, xp):
    stats = [health, strength, speed, defense, xp]
    data = {  
        'Stats': stats
        }
    
    df = pd.DataFrame(data)
    print("Character Data:")
    print(df)
    
    print("\nStatistical Analysis:")
    print(f"Mean:\n{df.mean()}")
    print(f"\nMedian:\n{df.median()}")
    print(f"\nMax:\n{df.max()}")
    print(f"\nMin:\n{df.min()}")

    return  str(name), str(race), str(job), float(health), int(strength), int(speed), float(defense), int(xp)