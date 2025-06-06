# ------------------ Functions
# Function definition starts with keyword 'def'
def add(a, b):
    return a + b


def is_palindrome(str):
    return str[::-1] == str


def test_palindrome():
    str = input("Enter a word: ")
    lowercase = str.casefold()
    if is_palindrome(lowercase):
        print(f"{str} is a palindrome")
    else:
        print(f"{str} is not a palindrome")


# ------------------ Tests

# Calling function
# result = add(1, 2)
# print(f"Result: {result}")

test_palindrome()
