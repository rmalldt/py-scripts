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
    greeting = "hello"

    def bar():
        x = 0  # local scope (it is also a free variable since it is already defined in enclosing scope)
        print(f"Nested local: {x}")  # prints 0
        # inner function can access variables of enclosing function
        print(f"Greeting: {greeting}")

    bar()


def func():
    a = 100
    b = 50
    res = a + b

    # list names in local namespace
    print(f"Inside local function namespace is: {dir()}")
    print(f"Locals: {locals()}")


# ------------------ Test

foo()

# func()
# print(f"Globals: {globals()}")
# print(f"Global object item: {globals()['x']}")
