# Task 17
from abc import abstractmethod
from abc import ABC
import csv
import tui
import visual

"""creates a list called records"""
# Task 18
records = []

"""imports the title from tui"""


# Task 19
def run():
    print(tui.welcome())


"""imports menu from tui"""
# Task 20
while True:
    from tui import menu

    """imports menu if the input is a certain value then it prints out valid information from that input(tasks21,22,
    23) """
    # Task 21
    if menu() == 1:
        print(started)
        from tui import started
        from tui import source_data_path

        with open("sol_data.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            for row in csv_reader:
                records.append(records)
        print(completed)
        from tui import completed

    # Task 22:
    if menu() == 2:
        from tui import started
        from tui import process_type
        from tui import completed

        if process_type() == 1:
            from tui import started
            from tui import entity_name
            from tui import entity_details
            index = records.index
            from tui import list_entity
            from tui import completed

        if process_type() == 2:
            from tui import started
            from tui import entity_details
            index = records.index
            from tui import list_entity
            from tui import completed

        if process_type() == 3:
            from tui import started
            planets = {
                "types_of_planets": {
                    "planets": ["Pluto", "Earth", "Venus"],
                    "none-planets": ["Moon", "Europa"]
                }
            }
            records.append(f"{planets}")
            from tui import list_categories
            from tui import completed

        if process_type() == 4:
            from tui import started
            from tui import gravity_range

            category_limits = {
                "limits": {
                    "lower_limit": ["1"],
                    "medium_limit": ["250"],
                    "upper_limit": ["500"]
                }
            }
            records.append({category_limits})
            from tui import list_categories
            from tui import completed

        if process_type() == 5:
            from tui import started
            from tui import orbit

            orbited_planets = {
                "output": {
                    "limits": ["1-500"],
                    "planets": ["Pluto", "Earth", "Venus", "Moon", "Europa"]
                }
            }
            records.index = {{orbit}}
            records.index = {{list_categories}}
        if gravity_range() <= 100 or "high":
            from tui import list_categories
            from tui import completed

    # Task 23
    if menu() == 3:
        from tui import started
        from tui import visualise
        from tui import completed

        if visualise() == 1:
            from tui import started
            planets = {
                "types_of_planets": {
                    "planets": ["Pluto", "Earth", "Venus"],
                    "none-planets": ["Moon", "Europa"]
                }
            }
            from visual import entities_pie
            from tui import completed

        if visualise() == 2:
            from tui import started
            limits = {
                "limits": {
                    "lower_limit": ["1"],
                    "medium_limit": ["250"],
                    "upper_limit": ["500"]
                }
            }
            from visual import entities_bar
            from tui import completed

        if visualise() == 3:
            from tui import orbit
            output = {
                "output": {
                    "limits": ["1-500"],
                    "planets": ["Pluto", "Earth", "Venus", "Moon", "Europa"]
                }
            }
            from visual import entities_bar
            from tui import completed

        if visualise() == 4:
            from tui import started
            category_limits = {
                "limits": {
                    "lower_limit": ["1"],
                    "medium_limit": ["250"],
                    "upper_limit": ["500"]
                }
            }
            from visual import gravity_animation
            from tui import completed

    """creates an abstract class with none planets and planets and then creates a class that inherits from the 
        abstract class """
    # Task 28
    if menu() == 4:
        from tui import started


        class planets:

            class Abstract(ABC):
                @abstractmethod
                def none(self):
                    print(sorted(["Moon", "Titan", "Callisto", "Europa"]))

                @abstractmethod
                def plan(self):
                    print(sorted(["Uranus", "Pluto", "Earth", "Venus"]))

            class Planets(Abstract):
                def none(self):
                    print("none planets")
                    super().none()

                def plan(self):
                    print("Planets")
                    super().plan()

                def __repr__(self):
                    return f"{self.none}, {self.plan}"

                def __str__(self):
                    return f"The none planets are {self.none} and the planets are {self.plan}"

            Abstract = Planets()
            Abstract.none()
            Abstract = Planets()
            Abstract.plan()


        from tui import completed

        """if user chooses the option exit the program will exit"""
        # Task 29
        if menu() == 5:
            exit()

        """if an invalid number is chosen then an error message should appear"""
        # Task 30:
        if menu() >= 6:
            print(error)
            from tui import error

        if __name__ == "__main__":
            run()
