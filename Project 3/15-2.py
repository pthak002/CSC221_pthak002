import matplotlib.pyplot as plt
import numpy as np

def cube_numbers(n):
    return [x**3 for x in range(1, n+1)]

numbers_5 = cube_numbers(5)
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(numbers_5, marker='x', color='green', linestyle='--')
plt.title('First 5 Cubic Numbers', fontsize=14)
plt.xlabel('Numbers', fontsize=12)
plt.ylabel('Cube', fontsize=12)
plt.grid(True)

numbers_5000 = cube_numbers(5000)
cmap = plt.get_cmap('viridis')
colors = np.linspace(0, 1, len(numbers_5000))

plt.subplot(1, 2, 2)
plt.scatter(range(1, 5001), numbers_5000, c=colors, cmap=cmap, s=10) 
plt.title('First 5000 Cubic Numbers', fontsize=14)
plt.xlabel('Numbers', fontsize=12)
plt.ylabel('Cube', fontsize=12)
plt.grid(True)
plt.colorbar(label='Normalized Index', pad=0.15)

plt.tight_layout()
plt.show()