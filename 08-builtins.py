# ------------------ enumerate
def enumerate_items(items):
    for i, item in enumerate(items):
        print(f"{i} {item} ")


# ------------------ sorted()
# sorted(iter) takes any iterable and return alphabetically sorted lists of characters
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
for item in reversed(numbers):
    print(item)
