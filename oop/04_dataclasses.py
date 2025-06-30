"""
Data class is a simple way to create classes that store data.
It comes with Python standard library.
"""

from dataclasses import dataclass


@dataclass
class Item:
    """
    Data class automatically implements the following methods behind the scene:
        - __init__
        - __repr__
        - __eq__
    """

    name: str
    unit_price: float
    quantity: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity


if __name__ == "__main__":
    item1 = Item("Monitor", 45.50, 1)

    # Auto implements __repr__
    print(item1)
    print(repr(item1))

    # Auto implements __eq__
    item2 = Item("Monitor", 45.50, 1)
    print(f"Are equal: {item1 == item2}")
