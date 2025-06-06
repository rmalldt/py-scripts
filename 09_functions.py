# ------------------ Functions
"""Function definition starts with keyword 'def'"""


# ------------------ Function Annotations
from ast import arg
from logging.config import valid_ident


def add(a: float, b: float) -> float:
    return a + b


# ------------------ Docstring
def is_palindrome(string: str) -> bool:
    """
    Check if a string is palindrome. A palindrome is a string that reads the same forwards as backwards.

    Args:
        str (string): The string to check.

    Returns:
        bool: True if `string` is a palindrom, False otherwise
    """
    alnum = ""
    for char in string:
        if char.isalnum():
            alnum += char
    return alnum[::-1] == alnum


def test_palindrome() -> None:
    string = input("Enter a word: ")
    lowercase = string.casefold()
    if is_palindrome(lowercase):
        print(f"{string} is a palindrome")
    else:
        print(f"{string} is not a palindrome")


# ------------------ Default parameter value
# ------------------ Raising Error
def format_banner(text: str = " ", screen_width: int = 80) -> None:
    """
    Print a string centred, with ** either side.

    Args:
        text (str, optional): The string to print. An asterisk (*) will result
        in a row of asterisks. The default will print a blank line, with a **
        border at the left and right edges.  Defaults to " ".

        screen_width (int, optional): The overall width to print within
        (including the 4 spaces for the ** either side). Defaults to 80.

    Raises:
        ValueError: If the supplied string is too long to fit.
    """
    if len(text) > screen_width - 4:
        # Raise Error
        raise ValueError(f"String {text} is larger is larger than specified width")

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = f"**{text.center(screen_width - 4)}**"
        print(output_string)


# ------------------ Keyword argument
# Used to specify the value for specific parameter by providing paramter name
def create_banner() -> None:
    format_banner("*")
    format_banner("Always look on the bright side of life...")
    format_banner("If life seems jolly rotten")
    format_banner("There's something that you've forgotten")
    format_banner("And that's to laugh and simile and dance and sing,")
    format_banner(screen_width=80)  # keyword argument
    format_banner("When you're feeling in dumps,")
    format_banner("Don't be silly chumps,")
    format_banner("Just purse your lips and whistle - that's the thing!")
    format_banner("And... always look on the bright side of life...")
    format_banner("*")


def get_int(prompt: str) -> int:
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping and prompting
    the user until a valid `int` is entered.

    Args:
        prompt (str): The String that the user will see
        when they are prompted to enter the value.

    Returns:
        int: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print(f"{temp} is not a valid number")


def fibonacci(n: int) -> int | None:
    """
    Return the `n` th Fibinacci number, for positive n.

    Args:
        n (int): The index position of the the Fbonacci sequence.

    Returns:
        int: The Fibonacci number at the specified index.
    """
    if 0 <= n <= 1:
        return n

    zero, one = 0, 1
    result = None
    for f in range(n - 1):
        result = zero + one
        zero = one
        one = result
    return result


def fizzbuzz(num: int) -> str:
    """
    Play fizz buzz

    Args:
        num (int): The number to check

    Returns:
        str: 'fizz' if the number is divisible by 3
        'buzz' if the number is divisible by 5.
        'fizzbuzz' if the number is divisible by both 3 and 5.
        The number as a string otherwise.
    """
    if num % 15 == 0:
        return "fizz buzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return str(num)


def test_fizzbuzz() -> None:
    for i in range(1, 100):
        print(fizzbuzz(i))


# ------------------ Spread arguments (*args)
def spread_args() -> None:
    values = [1, 2, 3, 4, 5]

    print(values)  # [1, 2, 3, 4, 5]

    # Unpack the values
    print(*values)  # 1 2 3 4 5
    print(1, 2, 3, 4, 5)  # same as above


def variable_args(*args) -> None:
    print(args)  # pack the variable arguments

    for x in args:
        print(x)


def test_arguments(p1, p2, *args, k, **kwargs) -> None:
    print(f"positional arguments:........{p1}, {p2}")
    print(f"variable arguments:..........{args}")
    print(f"keyword:.....................{k}")
    print(f"variable arguments keyword:..{kwargs}")


# ------------------ Tests

# Calling function
# result = add(1.4, 2.1)
# print(f"Result: {result}")

# test_palindrome()

# print(f"Your number: {get_int("Please input a number: ")}")

# print(get_int.__doc__) # get Docstring of get_input function

# create_banner()

# print(fibonacci(12))
# test_fizzbuzz()

# spread_args()
# variable_args(1, 2, 3, 4, 5)

test_arguments(1, 2, 3, 4, 5, k=6, key1=7, key2=8)
