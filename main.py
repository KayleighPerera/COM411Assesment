# Task 17
from abc import abstractmethod

import tui
import csv
import visual

# Task 18
records = []


# Task 19
def run():
    from tui import welcome


# Task 20
while True:
    from tui import menu

    # Task 21
    if menu() == 1:
        from tui import started
        from tui import source_data_path

        for line in source_data_path():
            records.append(records)
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
            from tui import completed

        if process_type() == 2:
            from tui import started
            from tui import entity_details

            index = records.index
            from tui import list_entity
            from tui import completed

        if process_type() == 3:
            from tui import started

            records.append(f"{list_categories}")
            from tui import list_categories
            from tui import completed

        if process_type() == 4:
            from tui import started
            from tui import gravity_range

            records.index = {{list_entity}}
            from tui import list_categories
            from tui import completed

        if process_type() == 5:
            from tui import started
            from tui import orbit

            records.index = {{orbit}}
            records.index = {{list_categories}}
        if list_categories() <= 100 or "high":
            from tui import list_categories
            from tui import completed

    # Task 23
    if menu() == 3:
        from tui import started
        from tui import visualise
        from tui import completed

        if visualise() == 1:
            from tui import started
            from tui import list_categories
            from visual import entities_pie
            from tui import completed

        if visualise() == 2:
            from tui import started
            from tui import gravity_range
            from visual import entities_bar
            from tui import completed

        if visualise() == 3:
            from tui import orbit
            from visual import orbits
            from tui import completed

        if visualise() == 4:
            from tui import started
            from tui import list_categories
            from visual import gravity_animation
            from tui import completed

    # Task 28
    if menu() == 4:
        from tui import started


        class planets:
            from abc import ABC, abstractmethod

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

        # Task 29
        if menu() == 5:
            exit()

        # Task 30:
        if menu() >= 6:
            from tui import error

        if __name__ == "__main__":
            run()
