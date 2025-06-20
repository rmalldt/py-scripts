"""
Class:          Template for creating objects. All objects create using the same class will have the same characteristics.
Object:         An instance of a class.
Instantiate:    Create an instance of a class.
Attribute:       A variable bound to an instance of a class.
Method:         A function in a class.

self:           Reference to the instance of a class
"""


class Car:

    # Static field
    no_of_wheels = 4

    # Constructor
    def __init__(
        self,
        make: str,
        model: str,
        engine_size: float,
        price: float,
    ) -> None:
        self.make = make
        self.model = model
        self.engine_size = engine_size
        self.price = price
        self.on = False

    # Methods
    def start(self):
        self.on = True

    # Override object string method
    def __str__(self) -> str:
        return f"Make: {mercedes_s3.make}, Model: {mercedes_s3.model}, Engine Size: {self.engine_size}, Price: {mercedes_s3.price}"


# ------------------ Test

mercedes_s3 = Car("Mercedes", "S3", 1.4, 25000)
print(mercedes_s3)

mercedes_s3.start()
print(f"Is ON: {mercedes_s3.on}")

print(mercedes_s3.__dict__)
