import sys
import os
import functools

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data import medals_dict


# ------------------ Map


def text_comp(text):
    uppers = [char.upper() for char in text]
    print(uppers)

    words = [word.upper() for word in text.split(" ")]
    print(words)


def text_map(text):
    uppers = list(map(str.upper, text))
    print(uppers)

    words = list(map(str.upper, text.split(" ")))
    print(words)


# ------------------ Filter

menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["chicken", "chips"],
]


def conditional_comp():
    filtered_meals = [
        meal for meal in menu if "spam" not in meal and "chicken" not in meal
    ]
    return filtered_meals


def not_spam(meal_list):
    return "spam" not in meal_list and "chicken" not in meal_list


def filter_meal():
    filtered_meals = list(filter(not_spam, menu))
    return filtered_meals


# ------------------ Reduce


def add(x, y):
    return x + y


# NOT RECOMMENDED
def reduce_sum(nums):
    reduced = functools.reduce(add, nums)
    print(f"Reduced sum: {reduced}")


# This is recommended by Zen
def sum(nums):
    result = 0
    for n in nums:
        result += n
    print(f"Sum: {result}")


# ------------------ Any and All


def any_all():
    entries = [1, 2, 3, 4, 5]
    print(f"all: {all(entries)} ")  # True since all values are truthy
    print(f"any: {any(entries)} ")  # True since at least one value is truthy

    entries = [0, 1, 2, 3, 4]
    print(f"all: {all(entries)} ")  # False since 0 is falsy value
    print(f"any: {any(entries)} ")  # True since at least one value is truthy


people = [
    ("Jim Doe", "jim@in.com"),
    ("Kale Yang", "kale@in.com"),
    ("Tim Copper", "tim@in.com"),
    ("John Dale", "john@in.com"),
    ("Kiara Jam", ""),
]


def all_comp():
    if all(person[1] for person in people):
        print("All people have email address")
    else:
        print("Some people do not have email address")


def any_comp(name):
    if any(False if person[1].find(name) == -1 else True for person in people):
        print(f"There is an email containing {name} ")
    else:
        print(f"There is no email containing {name}")


def edge_case():
    people = []

    # Always check the edge case
    if bool(people) and all(person[1] for person in people):
        print("All people have email address")
    else:
        print("Some people do not have email address")


def truthy_falsy():
    print("Values interpreted as False in Python:")
    print(
        f"""False: {False} 
None: {bool(None)}
0: {bool(0)}
0.0: {bool(0.0)}
Empty string: {bool("")}
Empty list: {bool([])}
Empty tuple: {bool(())}
Empty dict: {bool({})}
"""
    )


def gotchas():
    entries = []
    result = entries and all(entries)
    print(result)  # []

    result = bool(entries) and all(entries)
    print(result)  # False

# ------------------ Lambdas


# ------------------ Test

# text = "hello there! how are you?"
# text_comp(text)
# text_map(text)

# print(f"Comprehension filter: {timeit.timeit(conditional_comp, number=10000):.6f} sec")
# print(f"Filter: {timeit.timeit(filter_meal, number=10000):.6f} sec")


# numbers = [1, 2, 3, 4, 5]
# reduce_sum(numbers)
# sum(numbers)

# any_all()
# all_comp()
# any_comp('jim')
# edge_case()
# truthy_falsy()
# gotchas()
