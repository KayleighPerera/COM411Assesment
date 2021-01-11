"""displays a title """


# Task 1
def welcome():
    title = 'Solar Record Management System'
    print(len(title) * '-', title, len(title) * '-')


welcome()

"""displays a menu of options for the user to choose from"""


def menu():
    data = ["[1] Load Data",
            "[2] Process Data",
            "[3] Visualise Data",
            "[4] save data",
            "[5] exit"]

    return data


def run():
    dat = menu()
    for index in range(len(dat)):
        print("{}".format(dat[index]))

    print("please select what you would like to do with your data")
    operation = int(input())

    if operation == 1:
        print(menu()[0])
        print("Loading data...")
    if operation == 2:
        print(menu()[1])
        print("Processing data...")
    if operation == 3:
        print(menu()[2])
        print("Visualising data...")
    if operation == 4:
        print(menu()[3])
        print("Saving data...")
    if operation == 5:
        print(menu()[4])
        print("Exiting...")
    elif operation == 0:
        print("invalid")
        exit()
    elif operation >= 6:
        print("invalid number")
        exit()


run()
menu()

"""gets information from task 2 and prints out the operation has started"""


# Task 3
def started(operation):
    operation = menu()
    print(f'{operation} has started')
    return started(operation)


"""gets information from task 2 and prints out the operation has been completed"""


# Task 4
def completed(operation):
    operation = menu()
    print(f'{operation} has completed')
    return completed(operation)


"""gets information from task 2 and prints out the operation has an error"""


# Task 5
def error(error_msg):
    error_msg = menu()
    print(f'Error! {error_msg}')
    return error


"""Asks user to input a csv file name"""


# Task 6
def source_data_path():
    print("please enter a file path for a data file")
    file_path_name = input()

    if file_path_name.endswith(".csv"):
        return file_path_name
    else:
        print("not a valid file path")
        exit()


def run():
    print(source_data_path())


run()

"""displays a menu of options for the user to choose from"""


# Task 7
def process_type():
    entities = ["[1] Retrieve entity",
                "[2] Retrieve entity details",
                "[3] categorize entities by type",
                "[4] categorize entities by gravity",
                "[5] summarise entities by orbit"]

    return entities


def run():
    type = process_type()
    for index in range(len(type)):
        print("{}".format(type[index]))

    print("what would you like to do with your entities")
    user_input = int(input())
    if user_input == 1:
        print(process_type()[0])
        print("Retrieving entities...")
    if user_input == 2:
        print(process_type()[1])
        print("retrieving entity details...")
    if user_input == 3:
        print(process_type()[2])
        print("categorizing entities by types...")
    if user_input == 4:
        print(process_type()[3])
        print("categorizing entities by gravity...")
    if user_input == 5:
        print(process_type()[4])
        print("summarising entities by orbit...")
    elif user_input == 0:
        print("invalid")
        exit()
    elif user_input > 6:
        print("invalid number")
        exit()


run()

"""asks user to input an entity name"""


# Task 8
def entity_name():
    print("What is the name of the entity?")
    name = input()
    print("...")
    return name


"""asks user to enter entity details"""


# Task 9:
def entity_details():
    print("What is the name of the entity?")

    name = input()
    print("...")

    print("enter a list of column indexes")

    index = [(input())]
    map_object = map(int, index)
    print("...")
    return name, index


def run():
    print(entity_details())


run()

"""gives user a list of entity options for the user to choose from"""
# Task 10
entity = [['Mercury', True, 3.7], ['Venus', True, 8.87], ['Earth', True, 9.8], ['Mars', True, 3.71]]


def list_entity(entity, cols=[]):
    ent = entity
    for index in range(len(ent)):
        print("{}".format(ent[index]))

    print("enter a list of column indexes")

    cols = [(input())]
    return cols


def run():
    print(list_entity(entity, cols=[]))

    index = (float(input("what is the index of the Planet\n")))
    print("please select the entity")
    user_input = int(input())

    if index == 3.7:
        print(entity[0])
        print("...")

    elif index == 8.87:
        print(entity[1])
        print("...")

    elif index == 9.8:
        print(entity[2])
        print("...")

    elif index == 3.71:
        print(entity[3])
        print("...")

    else:
        print(entity)
        print("...")


run()

"""gives user a list of entity options for the user to choose another entity"""
# Task 11
entity = [['Mercury', True, 3.7], ['Venus', True, 8.87], ['Earth', True, 9.8], ['Mars', True, 3.71]]


def list_entity(entity, cols):
    return entity


def run():
    list = entity
    for index in range(len(list)):
        print("{}".format(list[index]))

    cols = (float(input("enter another index for an entity\n")))
    print("please select the entity")
    user_input = int(input())

    if cols == 3.7:
        print(list_entity(entity, cols)[0])
        print("...")

    elif cols == 8.87:
        print(list_entity(entity, cols)[1])
        print("...")

    elif cols == 9.8:
        print(list_entity(entity, cols)[2])
        print("...")
    elif cols == 3.71:
        print(list_entity(entity, cols)[3])
        print("...")

    else:
        print(list_entity(entity, cols))
        print("...")


run()

"""prints a list for user, and the user should input a category to give another list of entitys for that category"""
# Task 12
categories = print({"Terrestrial Planets", "Gas Giants", "Ice Giants", "Dwarf Planets"})


def list_categories(categories):
    print(categories)


def run():
    select = input("Select the type of planet\n")

    if select == "Terrestrial Planets":
        print(["Mercury", "Venus", "Earth", "Mars"])

    if select == "Gas Giants":
        print(["Jupiter", "Saturn"])

    if select == "Ice Giants":
        print(["Uranus", "Neptune"])

    if select == "Dwarf Planets":
        print(["Pluto", "Eris"])


run()

"""asks user to input an upper and lower limit for the gravity range"""


# Task 13
def gravity_range():
    limit = [float(input("please enter the upper limit\n")), float(input("please enter the lower limit\n"))]
    print(tuple(limit))

    return limit


gravity_range()

"""asks user to input plant names and then print out a list of the planets"""


# Task 14:
def orbit():
    entities = input("enter a list of the planets names\n")
    planets = entities.split(",")

    print("\n")
    print("Printing all planet names....")
    for name in planets:
        print(name)

    return planets


orbit()

"""displays a menu of options for the user to choose from to visualise data"""


# Task 15:
def visualise():
    visualisations = ["[1] Entities by type",
                      "[2] Entities by gravity",
                      "[3] Summery of orbits"]

    return visualisations


def run():
    vis = visualise()
    for index in range(len(vis)):
        print("{}".format(vis[index]))

    print("please select what you would like to see")
    user_input = int(input())

    if user_input == 1:
        print(visualise()[0])
    if user_input == 2:
        print(visualise()[1])
    if user_input == 3:
        print(visualise()[2])
    elif user_input > 4:
        print("invalid number")
        exit()
    print("...")


run()

"""displays a menu of options for the user to choose from to save data"""


# Task 16
def save():
    saved = ["[1] export as JSON"]

    return saved


def run():
    sav = save()
    for index in range(len(sav)):
        print("{}".format(sav[index]))

    print("How should the data be saved")
    user_input = int(input())

    if user_input == 1:
        print(save())
        print("...")
        print("Saving as a JSON file...")
        print("done")
    elif user_input == 0:
        print("invalid number")
        exit()
    elif user_input > 2:
        print("invalid number")
        exit()


run()
