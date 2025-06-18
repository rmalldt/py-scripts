"""
Class:          Template for creating objects. All objects create using the same class will have the same characteristics.
Object:         An instance of a class.
Instantiate:    Create an instance of a class.
Atribute:       A variable bound to an instance of a class.
Method:         A function in a class.
"""


class Car:

    def __init__(self, make: str, model: str, price: float) -> None:
        self.make = make
        self.model = model
        self.price = price
        self.on = False


# ------------------ Test

mercedes_s3 = Car("mercedes", "S3", 25000)

print(
    f"Make: {mercedes_s3.make}, Model: {mercedes_s3.model}, Price: {mercedes_s3.price}"
)
print(mercedes_s3.__dict__)
