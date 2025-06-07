# ------------------ Dictionaries


emp = {
    "id": 100,
    "name": "Jim Page ",
    "address": "Uxbridge, London",
    "role": "DevOps",
}


# ------------------ Get key, values and items
def get_keys_values_items(data: dict) -> None:
    # Get keys
    print(f"Keys: {data.keys()}")
    print(f"Keys: {list(data)}")

    # Get values
    print(f"Values: {data.values()}")

    # Get items
    print(f"Items: {data.items()}")


# ------------------ Create new dictionary
def create_new_dict() -> None:

    # Create dictionary with dict literal
    a = {"one": 1, "two": 2, "three": 3}

    # Create dictionary using dict constructor
    b = dict(one=1, two=2, three=3)
    c = dict({"one": 1, "two": 2, "three": 3})
    d = dict([("one", 1), ("two", 2), ("three", 3)])
    e = dict(zip(["one", "two", "three"], [1, 2, 3]))
    print(f"All dictionaries are equal: {a == b == c == d == e} ")

    # Create dictionary fromkeys()
    keys = ("k1", "k2", "k3")
    new_dict = dict.fromkeys(keys, "default")
    print(f"New dict: {new_dict}")

    # Create a new shallow copy of the dictionary with copy()
    dict_copy = new_dict.copy()
    print(f"Dict copy: {dict_copy}")

    # Remove all elements from dictionary with clear()
    new_dict.clear()
    print(f"New dict: {new_dict}")
    print(f"Dict copy: {dict_copy}")


# ------------------ Access items
def access_value(info: dict) -> None:
    # Access value using indexing.
    # Raises KeyError if key doesn't exist however it is faster
    id = info["id"]

    # Access value get method. Returns None if key does not exist.
    # It is used if unsure about key
    name = info.get("name")

    print(f"Id: {id}, Name: {name} ")


# ------------------ Iterate dictionary
def iterate_dict(info: dict) -> None:
    # Approach 1: Iterate unpack key
    for key in info:
        print(key, info[key], sep=": ")

    # Approach 2:
    # Use dict.items() to iterate over dictionary that unpack key and value.
    # dict.items() is like using enumerate(sequence) that gives index and value.
    for key, value in info.items():
        print(key, value, sep=", ")

    # Note: enumerate() can also be used with dictionary to get index.
    # In fact enumerate can be used with any iterable type
    for index, key in info:
        print(index, key)


# ------------------ Modify dictionary items
def modify_dict(info: dict):
    # Add new items
    info["team"] = "Connection"
    info["lab"] = "Development Operations"

    # If the key does not exist, setdefault() creates new item with key and default value
    info["experience"] = info.setdefault("experience", 3)

    # If the key already exist, setdefault() returns the existing value to the key
    num_experience = info.setdefault("experience", 0)
    print(f"Experience: {num_experience}")
    print(info)

    # Update existing items
    info["role"] = "Cloud/DevOps"
    info["address"] = "Feltham, London"
    info.update({"experience": 5})
    print(info)

    # Remove item using del
    del info["address"]
    print(info)

    # Remove using pop(), if key does not exist, return None
    removed = info.pop("manager", None)
    print(f"Removed: {removed}")

    removed_lastitem = info.popitem()
    print(f"Removed last item: {removed_lastitem} ")


def dict_menu() -> None:
    available_parts = {
        "1": "computer",
        "2": "monitor",
        "3": "keyboard",
        "4": "mouse",
        "5": "hdmi cable",
    }

    current_choice = None
    computer_parts = []

    while current_choice != "0":
        print(current_choice)
        if current_choice in available_parts:
            chosen_part = available_parts[current_choice]

            if chosen_part in computer_parts:
                print(f"Removing {chosen_part}")
                computer_parts.remove(chosen_part)
            else:
                print(f"Adding {chosen_part}")
                computer_parts.append(chosen_part)
            print(f"Your current list contains: {computer_parts}")
        else:
            print("Please add options from the list")
            for key, value in available_parts.items():
                print(f"{key}: {value}")
            print("0: exit")

        current_choice = input("> ")


def nested_data() -> None:
    recipes_tuple = {
        "Chicken and chips": [
            ("chicken", 100),
            ("potatoes", 3),
            ("salt", 1),
            ("malt vinegar", 5),
        ]
    }

    recipes_dict = {
        "Chicken and chips": {
            "chicken": 100,
            "potatoes": 3,
            "salt": 1,
            "malt vinegar": 5,
        }
    }

    # using tuples
    for key, value in recipes_tuple.items():
        print(key, value, sep=": ")
        for ingredient, quantity in value:
            print(ingredient, quantity, sep=", ")

    # using dict
    for key, value in recipes_dict.items():
        print(key, value, sep=": ")

        for ingredient, quatity in value.items():
            print(ingredient, quantity, sep=", ")


# ------------------ Tests

# get_keys_values_items(emp)
# create_new_dict()
# access_value(emp)
# iterate_dict(emp)
# modify_dict(emp)
# dict_menu()
# nested_data()
