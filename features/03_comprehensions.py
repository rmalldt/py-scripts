# ------------------ For loop


def squares(nums):
    squares = []
    for n in nums:
        squares.append(n**2)
    print(squares)


# ------------------ Comprehension Intro


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


# ------------------ Comprehension vs Loops: Side Effects


def get_squareof():
    numbers = [1, 2, 3, 4, 5]
    number = int(input("Enter a number whose square you want to find: "))

    squares = []
    for number in numbers:
        print(number)
        squares.append(number**2)

    # Side-effect: variable number is used for both:
    #               - storing user input
    #               - loop control variable
    # So, when the loop terminates, variable number has value last item in the loop,
    # so, the result is always last item in the squares list.
    index_pos = numbers.index(number)
    print(squares[index_pos])


def get_squareof_comp():
    numbers = [1, 2, 3, 4, 5]
    number = int(input("Enter a number whose square you want to find: "))

    # Using comprehension eliminates this side effect.
    squares = [number**2 for number in numbers]

    index_pos = numbers.index(number)
    print(squares[index_pos])


# ------------------ Conditional comprehensions


menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["chicken", "chips"],
]


def conditional():
    meals = []
    for meal in menu:
        if "spam" not in meal and "chicken" not in meal:
            meals.append(meal)
    print(meals)


def conditional_comp():
    meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
    print(meals)


def if_else():
    meals = []
    for meal in menu:
        if "spam" not in meal:
            meals.append(meal)
        else:
            meals.append("skipped")
    print(meals)


def if_else_comp():
    meals = [meal if "spam" not in meal else "skipped" for meal in menu]
    print(meals)


def fizzbuzz():
    for x in range(1, 20):
        fizzbuzz = (
            "fizz buzz"
            if x % 15 == 0
            else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
        )
        print(fizzbuzz)


def fizzbuzz_comp():
    fizzbuzz = [
        (
            "fizz buzz"
            if x % 15 == 0
            else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
        )
        for x in range(1, 20)
    ]

    print(fizzbuzz)


# ------------------ Nested Comprehension

burgers = ["beef", "chicken", "spicy beans"]
toppings = ["cheese", "egg", "beans", "spam"]


def nestedfor():
    meals = []
    for burger in burgers:
        for topping in toppings:
            meals.append((burger, topping))
    print(meals)


def nested_comp():
    meals = [(burger, topping) for burger in burgers for topping in toppings]
    print(meals)


def compare_nested_comps():
    for meals in [(burger, topping) for burger in burgers for topping in toppings]:
        print(meals)

    print("*" * 80)

    for meals in [[(burger, topping) for burger in burgers] for topping in toppings]:
        print(meals)

    print("*" * 80)

    for meals in [[(burger, topping) for topping in toppings] for burger in burgers]:
        print(meals)


# ------------------ Converting Loops to Comprehension


def to_words():
    text = input("Enter your text: ")

    output = []
    for word in text.split():
        output.append((word, len(word)))  # tuple of word and word length
    print(output)  # list of tuples


def to_words_comp():
    text = input("Enter your text: ")
    output = {(word, len(word)) for word in text.split()}  # set of tuples
    print(output)


def nested_loop():
    multiples = []
    for i in range(1, 6):
        for j in range(1, 6):
            multiples.append((i, i * j))
    print(multiples)


def nested_loop_comp():
    multiples = [(i, i * j) for i in range(1, 6) for j in range(1, 6)]
    print(multiples)


def nested_loop_comp1():
    for multiples in [[(i, i * j) for i in range(1, 6)] for j in range(1, 6)]:
        print(multiples)


# ------------------ Test

# numbers = range(1, 6)
# squares(numbers)
# squares_comp(numbers)

# text = "hello there! how are you?"
# text_comp(text)

# center_text("bread, egg, bread and egg ")
# center_text_comp("bread", "egg", "bread and egg", 1, 2, 3, "eggs")

# get_squareof()
# get_squareof_comp()

# conditional()
# conditional_comp()
# if_else()
# if_else_comp()
# fizzbuzz()
# fizzbuzz_comp()

# nestedfor()
# nested_comp()
# compare_nested_comps()


# to_words()
# to_words_comp()
# nested_loop()
# nested_loop_comp()
# nested_loop_comp1()
