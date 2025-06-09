from operator import le
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data.prescriptions import *

# ------------------ Set operations


"""Sets are defined using {...}"""


def create_set():
    # Using literals
    num_set = {1, 2, 3, 4, 5}
    print(num_set)

    # Using constructor
    numbers = set("12345")
    print(numbers)

    range_set = set(range(0, 10, 2))
    print(range_set)

    # Creating empty set
    empty_set = {}
    print(type(empty_set))  # <class 'dict'> NOT set

    empty_set = {*""}
    empty_set = {*{}}
    print(type(empty_set))  # <class 'set'>

    # Unique element only
    colors = ["red", "blue", "green", "cyan", "yellow", "blue", "red"]
    unique_colors = set(colors)
    print(unique_colors)  # {'green', 'cyan', 'blue', 'red', 'yellow'}


def set_operations() -> None:
    farm_animals = {"hen", "cow", "sheep", "horse", "goat"}
    wild_animals = {"lion", "tiger", "elephant", "horse", "goat"}

    # Set membership
    if "hen" in farm_animals:
        print(f"hen is present in set {farm_animals} ")

    # ----- All set operations return a new set

    # Union set
    union = farm_animals.union(wild_animals)  # union
    union = farm_animals | wild_animals  # |
    print(f"Union: {union}")

    # Intersection set
    intersection = farm_animals.intersection(wild_animals)
    intersection = farm_animals & wild_animals
    print(f"Intersection: {intersection}")

    # Difference set
    difference = farm_animals.difference(wild_animals)
    difference = farm_animals - wild_animals
    print(f"Difference: {difference}")

    # Symmetric difference set
    symmetric_diff = farm_animals.symmetric_difference(wild_animals)
    symmetric_diff = farm_animals ^ wild_animals
    print(f"Symmetric difference: {symmetric_diff}")

    # Superset and Subset
    a = {1, 2, 3, 4, 5}
    b = {3, 4}

    print(a.issuperset(b))
    print(a >= b)  # a is superset of b

    print(b.issubset(a))
    print(b <= a)  # b is subset of a


def modify_set() -> None:
    numbers = {1, 2, 3}

    # ----- Add item
    numbers.add(4)
    print(numbers)

    # ----- Remove item
    # discard(): Does not throw Error, if the item being discard does not exist
    #            in the set. Use it when we not sure the item exist in the set.
    numbers.discard(100)
    print(numbers)

    # remove(): Throws Error, if the item being removed does not exist in the set.
    #           Use it only if we're sure that item exist
    # numbers.remove(100)  # throws ERROR!
    numbers.remove(4)
    print(numbers)

    # pop(): It removes arbitrary item from set
    print(numbers.pop())

    numbers.clear()
    print(numbers)


def prescription_trial():
    trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

    for patient in trial_patients:
        prescription = patients[patient]

        # In this case, remove is appropriate because we do not want
        # want to add the add the drug unless we can remove another
        # appropriate drug as below:
        # Only add `edoxaban` if `warfarin` exist and is removed.
        try:
            prescription.remove(warfarin)
            prescription.add(edoxaban)
        except KeyError:
            print(
                f"Patient {patient} is not taking {warfarin}. "
                f"Please remove {patient} from the trial."
            )

        print(patient, prescription)


def prescription_drug_interaction():
    drugs_to_watch = set()

    # Data structure:
    # - adverse_interaction => list of interactions
    # - interaction         => set of drugs
    for interaction in adverse_interactions:
        # Add elements from other sets to create a union but 'update'
        # is more efficient than 'union' because union returns new set
        # each time while update just updates the same set.
        drugs_to_watch.update(interaction)
    print(sorted(drugs_to_watch))  # list of all unique interactions


def set_to_list():
    colors = ["red", "blue", "green", "cyan", "yellow", "blue", "red"]

    # Create a set to remove duplicates
    unique_colors = sorted(set(colors))
    print(f"List of unique items sorted: {unique_colors}")

    # Create a set to remove duplicates and also preserve the original order
    unique_colors = list(dict.fromkeys(colors))
    print(f"List of unique sorted items with original order: {unique_colors}")


# ------------------ Tests

# create_set()
# set_operations()
# modify_set()

# prescription_trial()
# prescription_drug_interaction()

# set_to_list()
