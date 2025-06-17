# These modules are imported in this current module
# The math and random functions scope is the entire current module
import math
import random

x = 10  # global scope

# print() is in builtin scope
print(f"Global: {x}")  # prints 10
print(f"Global modules: {dir()}")  # lists all names in current modules global namespace
print(f"Built-in modules: {dir(__builtins__)}")  # print builtin modules


def foo():
    x = 5  # local enclosing scope
    print(f"Enclosing local: {x}")  # prints 5

    def bar():
        x = 0  # local scope
        print(f"Nested local: {x}")  # prints 0

    bar()
    print(f"Enclosing local: {x}")


def func():
    a = 100
    b = 50
    res = a + b

    # list names in local namespace
    print(f"Inside local function namespace is: {dir()}")
    print(f"Locals: {locals()}")


# ------------------ Free variable


def free_variable():
    greeting = "hello"

    def innerfun():
        # free variable, same name as enclosing variable but bound to new value
        greeting = "Hi"
        print(f"Inner greeting: {greeting}")  # prints Hi

    innerfun()
    print(f"Enclosing greeting: {greeting}")  # prints Hello


def nonlocal_modify_enclosing_variable():
    greeting = "hello"

    def innerfun():
        nonlocal greeting
        greeting = "Hi"
        print(f"Inner greeting: {greeting}")  # prints Hi

    innerfun()
    print(f"Enclosing greeting: {greeting}")  # prints Hi


# ------------------ Global variable


result = 0


def add(a, b):
    result = a + b  # local scope


add(1, 1)
print(f"Result: {result}")  # prints 0


def add_global(a, b):
    global result  # using global keyword will update global variable here
    result = a + b


add_global(1, 1)
print(f"Result: {result}")  # prints 2


def add_better(a: int, b: int) -> int:
    return a + b


sum = add_better
print(f"Sum: {sum}")

# ------------------ Test

# foo()
# func()

# free_variable()
# nonlocal_modify_enclosing_variable()

# print(f"Globals: {globals()}")
# print(f"Global object item: {globals()['x']}")
