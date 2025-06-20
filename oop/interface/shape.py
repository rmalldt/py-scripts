from abc import ABC, abstractmethod


class ShapeInterface(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError


class Square(ShapeInterface):
    def __init__(self, length) -> None:
        self.length = length

    def area(self):
        return self.length * self.length


class Rectangle(ShapeInterface):
    def __init__(self, length, breadth) -> None:
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


# ------------------ Test

square = Square(2)
print(square.area())

rect = Rectangle(2, 6)
print(rect.area())
