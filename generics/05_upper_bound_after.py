"""
After Python 3.12
"""

from typing import TypeVar, Generic
from dataclasses import dataclass


# Base class Vehicle
@dataclass
class Vehicle:
    model: str

    def display(self) -> None:
        print(f"Vehicle model: {self.model}")


# Subclasses of class Vehicle
class Car(Vehicle):
    def display(self) -> None:
        print(f"Car mode: {self.model}")


class Boat(Vehicle):
    def display(self) -> None:
        print(f"Boat mode: {self.model}")


class Plane(Vehicle):
    def display(self) -> None:
        print(f"Plane mode: {self.model}")


# Create a TypeVar with an upper bound of Vehicle
class VehicleRegistry[V: Vehicle]:
    def __init__(self) -> None:
        self.vehicles: list[V] = []

    def add_vehicles(self, vehicle: V) -> None:
        self.vehicles.append(vehicle)

    def display_all(self) -> None:
        for vehicle in self.vehicles:
            vehicle.display()


class SubRegistry[V: Car](VehicleRegistry):
    def __init__(self) -> None:
        super().__init__()


def main() -> None:
    generic_registry = VehicleRegistry[Vehicle]()
    generic_registry.add_vehicles(Car("Sedan"))
    generic_registry.add_vehicles(Boat("Cruiser"))
    generic_registry.add_vehicles(Plane("ABus"))
    generic_registry.display_all()

    car_registry = VehicleRegistry[Car]()
    car_registry.add_vehicles(Car("Hatchback"))  # OK
    car_registry.add_vehicles(Car("SUV"))  # OK
    car_registry.display_all()
    # car_registry.add_vehicles(Boat("Yatch"))  # Type Error


if __name__ == "__main__":
    main()
