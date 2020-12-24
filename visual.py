import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Task 24
categories = {"Moon", "Europa", "Ganymede", "Titan", "Callisto", "Venus", "Earth", "Mars", "Saturn", "Jupiter"}
sizes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]


def entities_pie(categories):
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=categories, shadow=True, startangle=90)
    ax1.axis('equal')

    plt.show()


entities_pie(categories)

# Task 25
categories = {'High', 'Medium', 'Low'}
number_of_gravity_entities = [22, 17, 8]


def entities_bar(categories):
    x_pos = [i for i, _ in enumerate(categories)]
    plt.bar(x_pos, number_of_gravity_entities, color='blue')
    plt.xlabel("gravity entity")
    plt.ylabel("number_of_gravity_entities")
    plt.title("Gravity Entities")
    plt.xticks(x_pos, categories)

    plt.minorticks_on()

    plt.show()


entities_bar(categories)

# Task 26

summary = {"orbited planet": {"small": [3, 1, 2], "large": [3, 4]}}
entitys = [1, 2, 3, 4, 5, 6, 7, 8]


def orbits(summary):
    x_pos = [i for i, _ in enumerate(summary)]
    plt.bar(x_pos, number_of_gravity_entities, color='pink')
    plt.xlabel("gravity entity")
    plt.ylabel("number_of_gravity_entities")
    plt.title("Gravity Entities")
    plt.xticks(x_pos, summary)

    plt.minorticks_on()

    plt.show()


orbits(summary)

# Task 27
fig, ax = plt.subplots()
categories = {"low", "medium", "high"}


def gravity_animation(categories):
    categories = range(categories)
    ax.set_xlabel = "Low to Medium to High"
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.plot(categories, categories, 'b--x')


anim = animation.FuncAnimation(fig, gravity_animation, frames=10, interval=1000)
plt.show()
