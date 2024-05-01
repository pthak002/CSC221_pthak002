import matplotlib.pyplot as plt
import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)

num_rolls = 1000

results = [roll_dice() for _ in range(num_rolls)]

frequency = [results.count(i) for i in range(3, 19)]

plt.figure(figsize=(12, 6))
plt.bar(range(3, 19), frequency, color='skyblue')
plt.xlabel('Sum of Three Dice')
plt.ylabel('Frequency')
plt.title(f'Frequency of Sum of Three D6 Dice ({num_rolls} Rolls)')
plt.grid(axis='y', alpha=0.5)
plt.show()
