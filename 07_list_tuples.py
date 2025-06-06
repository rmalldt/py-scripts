import sys
import os

# Add the parent directory to the path so Python can find folder data
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data.albums_data import albums

# ------------------ Lists Operations


def list_operations():
    fruits = ["apple", "orange", "banana"]

    # Length
    print(f"Len: {len(fruits)}")

    # Index access and Slicing
    print(fruits[0])  # apple
    print(fruits[0:2])  # ['apple', 'orange']
    print(fruits[0:3:2])  # ['apple', 'banana']
    print(fruits[-2])  # orange
    fruits[0] = "Guava"
    del fruits[0]
    del fruits[0:2]
    print(f"Updated list: {fruits}")

    # Append and Extend
    fruits.append("strawberry")  # add item to the end of the list
    fruits.extend(["apple", "orange"])  # add lists

    # Insert, Remove and Pop
    fruits.insert(0, "grapes")  # insert at given index
    fruits.remove("apple")  # remove first item whose value match
    fruits.pop()  # remove last item

    # Count: Count the number occurences of given item in the list
    print(f"Orange count: {fruits.count("orange")}")

    # Min and Max
    print(f"Min: {min(fruits)}")
    print(f"Max: {max(fruits)}")

    # Sort: Sort elements in place
    fruits.sort()
    print(fruits)

    # Reverse: Reverse elements in place
    fruits.reverse()
    print(fruits)

    # Copy: Return a shallow copy of the list
    new_list = fruits.copy()

    # Clear: Remove all items from the list
    fruits.clear()
    print(f"Original list: {fruits}")
    print(f"New list: {new_list}")


def create_list():
    odd = [1, 3, 5, 7, 9]
    even = [2, 4, 6, 8]
    numbers = odd + even  # append list
    print(numbers)


# ----- enumerate


def enumerate_items(items):
    for i, item in enumerate(items):
        print(f"{i} {item} ")


# ----- Sort reverse


def sort_items(items):
    items.sort(reverse=True)
    print(items)


# ----- Caveats


# This function does not delete the right elements.
# It prints [5, 100, 200, 220] instead of [100,200]
# The problem is the list is mutated within the for loop and the
# size of the list changes,so, the elements are skipped since the
# indexes are already processed.
def delete_unsafe():
    min_limit = 100
    max_limit = 200
    data = [4, 5, 100, 200, 210, 220]  # sorted data
    for index, value in enumerate(data):
        if (value < min_limit) or (value > max_limit):
            del data[index]
    print(data)


# ----- Solution for Sorted Sequence
def delete_safe_ordered():
    min_limit = 100
    max_limit = 200
    data = [4, 5, 100, 200, 210, 220]  # sorted data

    stop = 0
    # Range:
    #   - start: 0
    #   - stop: len(data) (last index is exclusive)
    for index in range(0, len(data)):
        if data[index] >= min_limit:
            stop = index
            break

    print(f"Min limit index: {stop}")
    del data[:stop]  # delete upto stop exclusive
    print(data)

    start = 0
    # Range:
    #   - start: len(data) - 1 (inclusive)
    #   - stop: -1 (need to include the at 0 index)
    #   - step: -1 (iterate backward where start is greater than stop)
    for index in range(len(data) - 1, -1, -1):
        if data[index] <= max_limit:
            start = index + 1
            break

    print(f"Max limit index: {stop}")
    del data[start:]  # delete from start+1 to end of list
    print(data)


# ----- Solution 1 for Unsorted Sequence
def delete_safe_unordered():
    min_limit = 100
    max_limit = 200
    data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106]  # unsorted data

    for index in range(len(data) - 1, -1, -1):
        if data[index] < min_limit or data[index] > max_limit:
            print(index, data[index])
            del data[index]

    print(data)


# ----- Solution 2 for Unsorted Sequence using reversed()
# Using builtin reversed(sequence) returns a reverse iterator
# but the caveat is the index returned by reverse iterator
# associate with the sequence in reverse order as follows:
#   - last element       = index 0
#   - second last elemet = index 1
#   - so on...
#   - first element      = index (length-1)
#
# BUT the sequence elements are still the 0 indexed i.e.
#   - first element = index 0
#   - second element = index 1
#   - so on...
#
# To access the right element from sequence, we need to adjust the index
# when accessing the element:
#   - last index = len(sequence) - 1
#   - correct index = last index - reversed index
#
# Using reversed() is tricky so, ONLY use it when absolutely necessary with CAUTION.
# This approach is faster than using range().
def delete_safe_unordered_reversed():
    min_limit = 100
    max_limit = 200
    data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106]  # unsorted data

    last_index = len(data) - 1
    for index, value in enumerate(reversed(data)):
        if value < min_limit or value > max_limit:
            print(last_index - index, data)
            del data[last_index - index]

    print(data)


# ----- Nested Lists


def nested_lists():
    even = [2, 4, 6, 8]
    odd = [1, 3, 5, 7]
    lists = [even, odd]
    print(f"Nested List: {lists}")  # [[2, 4, 6, 8], [1, 3, 5, 7]]

    for list in lists:
        print(list)

        for value in list:
            print(value)


def nested_lists1():
    menu = [
        ["tea", "toast"],
        ["tea", "bacon", "toast"],
        ["tea", "bacon", "beans", "toast"],
        ["tea", "bacon", "beans", "sausage", "toast"],
        ["coffee", "toast"],
        ["coffee", "bacon", "toast"],
        ["coffee", "bacon", "beans", "toast"],
        ["coffee", "bacon", "beans", "sausage", "toast"],
    ]

    for breakfast in menu:
        if "sausage" in breakfast:
            print(breakfast)

            for item in breakfast:
                print(item)


# ----- Join list items


def join_items():
    guitars = ["Fender", "Gibson", "PRS", "Charvel", "Ibanez"]

    # Using join
    seperator = ", "
    print(seperator.join(guitars))  # returns single string

    # Using * operator
    print(*guitars, sep=", ")

    # Using for loop
    for guitar in guitars:
        print(guitar, end=", ")


# ------------------ Tuples Operations
"Always enclose tuples with parenthesis"


# ----- Unpacking tuple
# Sequences can be unpacked
# Unpacking tuples makes the code more readeable as we can provide name for each elements
def unpacking_tuples():
    # Unpack tuple
    album = ("One", "Tesseract", 2013)

    name, artist, year = album
    print(f"Album: {name}")
    print(f"Band: {artist}")
    print(f"Release date: {year}")

    for item in enumerate(album):
        index, value = item
        print(index, value)

    # Unpack nested tuples
    albums = [
        ("One", "Tesseract", 2013),
        ("Periphery", "Periphery", 2010),
        ("Silhouettes", "Textures", 2008),
        ("Animals as Leaders", "Animals as Leaders", 2009),
        ("Language", "The Contortionists", 2014),
    ]

    # Unpack tupes approach 1
    for name, artist, year in albums:
        print(f"Album: {name:<30} Artist: {artist:<30} Release date: {year:<10} ")

    # Unpack tupes approach 2
    for album in albums:
        name, artist, year = album
        print(f"Album: {name:<30} Artist: {artist:<30} Release date: {year:<10} ")


# ----- Nested Tuples


def nested_tuples():
    for name, artist, year, songs in albums:
        print()
        print(f"Album: {name}")
        print(f"Artist: {artist}")
        print(f"Release year: {year}")
        print("Songs:")
        for index, song in songs:
            track_no = f"{index}."
            print(f"{track_no:<3}{song}")


def juke_box():
    SONG_LIST_INDEX = 3  # song_list is 3rd item in the album tuple starting index 0
    SONG_TITLE_INDEX = 1  # song_title is 1st index in the song tuple starting index 0
    on = True

    while on:
        print("Choose album or press 0 to exit: ")
        for index, (name, artist, year, songs) in enumerate(albums):
            album_index = f"{index + 1}."  # display album index from 1
            print(f"{album_index:<3}{name}")

        choice = int(input())
        print()
        if 1 <= choice <= len(albums):
            # Album index displayed from index 1, therefore albums[choice-1]
            songs_list = albums[choice - 1][SONG_LIST_INDEX]

            print("Choose song or press 0 to go back to main menu: ")
            for index, song in songs_list:
                print(f"{index:<3}{song}")

            song_choice = int(input())
            if 1 <= song_choice <= len(songs_list):
                song_title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
                print(f"Playing: {song_title}\n")
            print("=" * 40)

        else:
            on = False
            print("Goodbye")


# ------------------ Tests

# list_operations()
# create_list()
# enumerate_items(["apple", "ball", "cat"])
# sort_items([1, 5, 9, 2, 5, 6])
# delete_unsafe()
# delete_safe_ordered()
# delete_safe_unordered()
# delete_safe_unordered_reversed()
# nested_lists()
# nested_lists1()
# join_items()
# unpacking_tuples()
# nested_tuples()

juke_box()
