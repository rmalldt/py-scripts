from typing import Any


class Wing:
    def __init__(self, ratio) -> None:
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Flying easy")
        elif self.ratio == 1:
            print("Flying ok")
        else:
            print("Can't fly")


class Duck:
    ratio = 1.8

    def __init__(self) -> None:
        # Composition: Each instance of duck will have its own wing.
        self.wing = Wing(self.ratio)

    def walk(self):
        print("Duck Walking...")

    def swim(self):
        print("Duck Swimming...")

    def quack(self):
        print("Duck Quacking...")

    def fly(self):
        self.wing.fly()


class Penguin:
    def walk(self):
        print("Penguin Walking...")

    def swim(self):
        print("Penguin Swimming...")

    def quack(self):
        print("Penguin Quacking...")


# ------------------ Test


def testduck(duck: Any):
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == "__main__":
    # ----- Duck testing
    donald = Duck()
    testduck(donald)

    # Even though Penguin is not Duck, but it passes the Duck testing
    # since it has all similar methods
    jim = Penguin()
    testduck(jim)
