categories = ({"Terrestrial Planets", "Gas Giants", "Ice Giants", "Dwarf Planets"})

def list_categories(categories):
   print(categories)


def run():
    select = input("write down the type of planet\n")

    if select == "Terrestrial Planets":
        print(["Mercury", "Venus", "Earth", "Mars"])

    if select == "Gas Giants":
        print(["Jupiter", "Saturn"])

    if select == "Ice Giants":
        print(["Uranus", "Neptune"])

    if select == "Dwarf Planets":
        print(["Pluto", "Eris"])


run()
