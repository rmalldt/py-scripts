# These modules are imported in this current module.
# The math and random functions can scope is the entire current module.
import math
import random


print(dir())  # list current modules namespaces

x = 10  # global namespace


def foo():
    x = 5  # local namespace
    print(f"Local: {x}")  # prints 5

    def bar():
        x = 0
        print(f"Enclosing: {x}")

    bar()


def func():
    a = 100
    b = 50

    res = a + b
    print(f"Inside local function namespace is: {dir()}")
    print(f"Locals: {locals()}")


# ------------------ Test
# foo()
# print(f"Global: {x}")  # prints 10

func()
