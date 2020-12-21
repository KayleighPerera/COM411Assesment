import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Q24
categories = {"Moon", "Europa", "Ganymede", "Titan", "Callisto", "Venus", "Earth", "Mars", "Saturn", "Jupiter"}
sizes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]


def entities_pie(categories):
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=categories, shadow=True, startangle=90)
    ax1.axis('equal')

    plt.show()


entities_pie(categories)

# Q25

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


def orbits(summary):
    """
    Task 26: Display subplots where each subplot shows the "small" and "large" entities that orbit the planet.

    Summary is a nested dictionary of the form:
    summary = {
        "orbited planet": {
            "small": [entity, entity, entity],
            "large": [entity, entity]
        }
    }

    The function should display for each orbited planet in summary. Each subplot should show a bar chart with the
    number of "small" and "large" orbiting entities.

    :param summary: A dictionary containing the "small" and "large" entities for each orbited planet.
    :return: Does not return anything
    """



    """
    Task 27: Display an animation of "low", "medium" and "high" gravities.

    The function should display a suitable animation for the "low", "medium" and "high" gravity entities.
    E.g. an animated line plot

    :param categories: A dictionary containing "low", "medium" and "high" gravity entities
    :return: Does not return anything
    """


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