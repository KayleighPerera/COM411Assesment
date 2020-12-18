import matplotlib.pyplot as plt

categories = {"Moon", "Europa", "Ganymede", "Titan", "Callisto", "Venus", "Earth", "Mars", "Saturn", "Jupiter"}
sizes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]


def pie_chart(categories):
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=categories, shadow=True, startangle=90)
    ax1.axis('equal')


    plt.show()
pie_chart(categories)


def entities_bar(categories):
    """
    Task 25: Display a single subplot that shows a bar chart for categories.

    The function should display a bar chart for the number of 'low', 'medium' and 'high' gravity entities.

    :param categories: A dictionary with entities categorised into 'low', 'medium' and 'high' gravity
    :return: Does not return anything
    """
    categories = {'Low', 'Medium', 'High'}
    values = [50, 80, 200]

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])

    ax.bar(categories, values)
    plt.show()


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


def gravity_animation(categories):
    """
    Task 27: Display an animation of "low", "medium" and "high" gravities.

    The function should display a suitable animation for the "low", "medium" and "high" gravity entities.
    E.g. an animated line plot

    :param categories: A dictionary containing "low", "medium" and "high" gravity entities
    :return: Does not return anything
    """
