
import matplotlib.pyplot as plt

def cube_numbers(n):
    return [x**3 for x in range(1, n+1)]

numbers_5 = cube_numbers(5)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(numbers_5, color='pink')
plt.title('First five Cubic Numbers')
plt.xlabel('Numbers')
plt.ylabel('Cube of numbers')
plt.grid(True)

numbers_5000 = cube_numbers(5000)
plt.subplot(1, 2, 2)
plt.plot(numbers_5000, color='black')
plt.title('First five thousands Cubic Numbers')
plt.xlabel('Numbers')
plt.ylabel('Cube of numbers')
plt.grid(True)

plt.tight_layout()
plt.show()