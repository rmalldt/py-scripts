# ------------------ Tests
"""Sets are defined using {...}"""

farm_animals = {"hen", "cow", "sheep", "horse", "goat"}
wild_animals = {"lion", "tiger", "elephant", "horse", "goat"}


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
    # Set membership
    if "hen" in farm_animals:
        print(f"hen is present in set {farm_animals} ")

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

    numbers.clear()
    print(numbers)


def set_to_list():
    colors = ["red", "blue", "green", "cyan", "yellow", "blue", "red"]

    # Create a set to remove duplicates
    unique_colors = sorted(set(colors))
    print(f"List of unique items sorted: {unique_colors}")

    # Create a set to remove duplicates and also preseve the original order
    unique_colors = list(dict.fromkeys(colors))
    print(f"List of unique sorted items with original order: {unique_colors}")


# ------------------ Tests

# create_set()
# set_operations()
modify_set()
# set_to_list()
