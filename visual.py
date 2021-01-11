import matplotlib.pyplot as plt
import matplotlib.animation as animation


"""creates a pie chart with entities from the data given"""
# Task 24
categories = {"planets", "none-planets"}
sizes = [252, 13]


def entities_pie(categories):
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, colors=['yellow', 'green'], labels=categories, shadow=True, startangle=90)
    ax1.axis('equal')

    plt.legend()
    plt.show()


entities_pie(categories)

"""creates a bar chart with high, medium and low entities"""
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

"""creates a bar chart with small and large entities"""
# Task 26
entities_bar(categories)

summary = {'small': 15, 'large': 30}

plt.bar(range(len(summary)), list(summary.values()), align='center', color="red")
plt.xticks(range(len(summary)), list(summary.keys()))

plt.show()

"""task 27 creates an animation line graph that represents the low medium and high gravity levels"""
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
