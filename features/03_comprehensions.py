# ------------------ For loop


def squares(nums):
    squares = []
    for n in nums:
        squares.append(n**2)
    print(squares)


# ------------------ Comprehension


def squares_comp(nums):
    # List comprehension: note the brackets used.
    squares = [number**2 for number in nums]
    print(squares)

    # Set comprehension: note the curly brackets used.
    squares = {number**2 for number in nums}
    print(squares)


# ------------------ Comprehension and String


def text_comp(text):
    uppers = [char.upper() for char in text]
    print(uppers)

    words = [word.upper() for word in text.split(" ")]
    print(words)

    # Only use comprehension when required.
    # In this case, result is achieved without comprehension.
    lowers = text.split(" ")
    print(lowers)


def center_text(*args):
    text = " ".join(args)  # throws Error, can't join string and numbers
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


def center_text_comp(*args):
    text = " ".join([str(arg) for arg in args])  # ok numbers converted to strings
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# ------------------ Test

numbers = range(1, 6)
# squares(numbers)
# squares_comp(numbers)

# text = "hello there! how are you?"
# text_comp(text)

# center_text("bread, egg, bread and egg ")
center_text_comp("bread", "egg", "bread and egg", 1, 2, 3, "eggs")
