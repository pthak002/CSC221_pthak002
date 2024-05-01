import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5_000)
    rw.fill_walk()

    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

    point_numbers = range(rw.num_points)

    ax.plot(rw.x_values, rw.y_values, c='lightgreen', linewidth=2, alpha=0.5, zorder=1)

    ax.scatter(0, 0, c='yellow', edgecolors='none', s=100, zorder=2)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100, zorder=2)

    ax.set_title("Random Walk Simulation", fontsize=18)
    ax.set_xlabel("X", fontsize=14)
    ax.set_ylabel("Y", fontsize=14)
    ax.grid(False)
    ax.set_axis_off()
    fig.patch.set_facecolor('black')

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
