print(dir())
x = 10  # global namespace


def foo():
    x = 5  # local namespace
    print(f"Local: {x}")  # prints 5

    def bar():
        x = 0
        print(f"Enclosing: {x}")

    bar()


foo()
print(f"Global: {x}")  # prints 10
