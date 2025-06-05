# ------------------ enumerate()
# Used when we need count of the items we need to iterate. It returns a tuple
# containing a count (from start which default to 0) and the value obtained from
# iterating over the iterable.
def enumerate_items(items):
    for i, item in enumerate(items):
        print(f"{i} {item} ")


# ------------------ sorted()
# sorted(iter) takes any iterable and return alphabetically sorted lists of characters


def sorted_items():
    words = "Hello there, how are you?"
    sorted_words = sorted(words)
    print(f"Sorted words case sensitive: {sorted_words}")

    # Case-insensitive sorting
    sorted_words = sorted(words, key=str.casefold)
    print(f"Sorted words case insensitive: {sorted_words}")

    # Numbers are sorted in ascending order
    numbers = [1.3, 5.1, 1.1, 5.3, 3.3, 5.5, 9.0]
    sorted_numbers = sorted(numbers)
    print(f"Sorted numbers: {sorted_numbers}")


# ------------------ reversed()
# It returns the reveresed iterator that associate with the sequence
# in reverse order i.e.:
#   - last element          = index 0
#   - second last element   = index 1
#   - first element         = index (length - 1)
def reversed_items():
    numbers = [1, 2, 3, 4, 5]
    for i, item in enumerate(reversed(numbers)):
        print(i, item)


# ------------------ print()
def print_items():
    print()
    print("Hello there Jim")
    print("Hello", "there", "Jim")
    print("Hello", "there", "Jim", sep=", ")  # default sep = " "
    print("Hello", "there", "Jim", sep=", ", end=" ")  # default sep = " ", end="\n"


# ------------------ list() and tuple()


# list() is used to convert sequence to list
# tuple() is used to convert sequence to tuple
def list_tuples():
    album = ["Altered State", "Tesseract", 2013]
    print(album)  # ['Tesseract', 'Altered State', 2013]

    copy = tuple(album)
    print(copy)  # ('Tesseract', 'Altered State', 2013)


# ------------------ Tests

# enumerate_items()
# sorted_items()
# reversed_items()
# print_items()
list_tuples()
