import pandas as pd
import random

# Step 1: Generate sample character data
data = {
    'Name': [f'Character {i}' for i in range(1, 11)],
    'Strength': [random.randint(50, 100) for _ in range(10)],
    'Agility': [random.randint(50, 100) for _ in range(10)],
    'Intelligence': [random.randint(50, 100) for _ in range(10)],
    'Endurance': [random.randint(50, 100) for _ in range(10)],
}

# Step 2: Create a DataFrame
df = pd.DataFrame(data)

# Step 3: Display the DataFrame
print("Character Data:")
print(df)

# Step 4: Perform basic statistical analysis
print("\nStatistical Analysis:")
print(f"Mean:\n{df.mean()}")
print(f"\nMedian:\n{df.median()}")
print(f"\nMax:\n{df.max()}")
print(f"\nMin:\n{df.min()}")