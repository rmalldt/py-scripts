# ------------------ Functions
"""Function definition starts with keyword 'def'"""


# ------------------ Function Annotations
def add(a: float, b: float) -> float:
    return a + b


def is_palindrome(string: str) -> bool:
    """
    Check if a string is palindrome.

    A palindrome is a string that reads the same forwards as backwards.

    Args:
        str (string): The string to check,

    Returns:
        bool: True if `string` is a palindrom, False otherwise
    """
    alnum = ""
    for char in string:
        if char.isalnum():
            alnum += char
    return alnum[::-1] == alnum


def test_palindrome():
    string = input("Enter a word: ")
    lowercase = string.casefold()
    if is_palindrome(lowercase):
        print(f"{string} is a palindrome")
    else:
        print(f"{string} is not a palindrome")


# ----- Default parameter value
# ----- Raising Error
def format_banner(text: str = " ", screen_width: int = 80) -> None:
    """Print a string centred, with ** either side.

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


# ----- Keyword argument
# Used to specify the value for specific parameter by providing paramter name
def create_banner():
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


# ------------------ Docstring


def get_int(prompt):
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


# ------------------ Tests

# Calling function
# result = add(1.4, 2.1)
# print(f"Result: {result}")

# test_palindrome()

# print(f"Your number: {get_int("Please input a number: ")}")

# print(get_int.__doc__) # get Docstring of get_input function

create_banner()

# print(fibonacci(12))
