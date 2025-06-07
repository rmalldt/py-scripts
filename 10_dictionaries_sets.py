emp = {
    "id": 100,
    "name": "Jim Page ",
    "address": "Uxbridge, London",
    "role": "DevOps",
}


def access_value(info: dict) -> None:
    # Access value using indexing.
    # Raises KeyError if key doesn't exist however it is faster
    id = info["id"]

    # Access value get method. Returns None if key does not exist.
    # It is used if unsure about key
    name = info.get("name")

    print(f"Id: {id}, Name: {name} ")


def iterate_dict(info: dict) -> None:
    # Approach 1
    for key in info:
        print(key, info[key], sep=": ")

    # Approach 2
    # To iterate Sequence use enumerate, to iterate dictionary use .items()
    for key, value in info.items():
        print(key, value, sep=", ")


def modify_dict(info: dict):
    # Add new items
    info["team"] = "Connection"
    info["lab"] = "Development Operations"
    print(info)

    # Update existing items
    info["role"] = "Cloud/DevOps"
    info["address"] = "Feltham, London"
    print(info)

    # Remove item
    del info["address"]
    print(info)

    # Remove using pop(), if key does not exist, return None
    removed = info.pop("manager", None)
    print(f"Removed: {removed}")


# ------------------ Tests

# access_value(emp)

# iterate_dict(emp)

modify_dict(emp)
