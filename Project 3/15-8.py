import matplotlib.pyplot as plt
import numpy as np

rolls_1 = np.random.randint(1, 7, size=1000)
rolls_2 = np.random.randint(1, 7, size=1000)

products = rolls_1 * rolls_2

plt.figure(figsize=(10, 6))
plt.hist(products, bins=np.arange(0.5, 37.5, 1), color='skyblue', edgecolor='black', align='mid', density=True)
plt.title('Multiplying Two Six-Sided Dice 1000 Times')
plt.xlabel('Product of Two Dice')
plt.ylabel('Frequency')
plt.xticks(np.arange(1, 37, 1), rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
