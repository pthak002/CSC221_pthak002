from random import randint

def generate_star_pattern(num_stars):
    for _ in range(num_stars):
        x = randint(-100, 100)
        y = randint(-100, 100)
        print(f"Star at ({x}, {y})")

generate_star_pattern(10)