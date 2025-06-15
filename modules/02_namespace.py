# These modules are imported in this current module.
# The math and random functions can scope is the entire current module.
import math
import random

x = 10  # global namespace
print(f"Global: {x}")  # prints 10
print(f"Global modules: {dir()}")  # lists all names in current modules global namespace
print(f"Built-in modules: {dir(__builtins__)}")  # print built-in modules


def foo():
    x = 5  # local namespace
    print(f"Local: {x}")  # prints 5

    def bar():
        x = 0  # enclosing namespace
        print(f"Enclosing: {x}")  # prints 0

    bar()


def func():
    a = 100
    b = 50

    res = a + b
    print(
        f"Inside local function namespace is: {dir()}"
    )  # list names in local namespace
    print(f"Locals: {locals()}")


# ------------------ Test

# foo()

func()
print(f"Globals: {globals()}")
print(f"Global object item: {globals()['x']}")
