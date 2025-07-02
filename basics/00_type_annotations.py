# ------------------ Auto-completion


# Without type hints – editor is NOT able to provide auto-completion
from typing import Annotated, Union


def get_fullname(firstname, lastname):
    fullname = firstname + " " + lastname
    return fullname


# With type hints – editor is able to provide the auto-completion
def get_fullname_with_type(firstname: str, lastname: str):
    fullname = firstname.title() + " " + lastname.title()
    return fullname


# ------------------ Error checks


# Editor is able able to check the type of variables and perform error checks
def get_name_with_age(name: str, age: int):
    name_with_age = name.title() + " is this old " + str(age)
    return name_with_age


# ------------------ Generic types


# ----- List
def process_items_list(items: list[str]):
    for item in items:
        print(item.upper())


# ----- Tuples
def process_items_tuples(items: tuple[int, str, int]):
    id, name, age = items
    print(id, name)


# ----- Set
def process_items_set(items: set[str]):
    for item in items:
        print(item)


# ----- Dict
def process_items_dict(items: dict[str, int]):
    for key, value in items.items():
        print(key, value)


# ------------------ Union, Possibly None (Optional)


# ----- Union
# In this case, item could of either int or str
def process_item_union(item: int | str):
    print(item)


# Same as above
def process_item_union_alt(item: Union[int, str]):
    print(item)


# ----- Possibly None
# In this case, item could either be str or None with default value None
def process_item_optional(item: str | None = None):
    print(item)


# Same as above
def process_item_optional_alt(item: Union[str, None]):
    print(item)


# ------------------ Classes


class Person:
    def __init__(self, name: str) -> None:
        self.name = name


def get_person(person: Person) -> str:
    return person.name


# ------------------ Type Hints with Metadata Annotations


# Annotated is a part of standard library imported from `typing`
# Annotated parameters:
#   - first param: actual type
#   - second: metadata
def greet(name: Annotated[str, "This is just a metadat"]):
    print(f"Hello {name}")


if __name__ == "__main__":
    # print(get_fullname("jim", "doe"))
    # print(get_fullname_with_type("jim", "doe"))

    # print(get_name_with_age("jim", 30))

    # process_items_list(["app", "ball", "cat"])
    # process_items_tuples((80, "Jim", 30))
    # process_items_set({"app", "ball", "cat"})
    # process_items_dict({"id": 10})

    # process_item_union(10)
    # process_item_union("app")

    # process_item_optional()
    # process_item_optional("Jim")

    greet("Jim")

    pass
