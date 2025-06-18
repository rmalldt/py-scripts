"""
Class:          Template for creating objects. All objects create using the same class will have the same characteristics.
Object:         An instance of a class.
Instantiate:    Create an instance of a class.
Attribute:       A variable bound to an instance of a class.
Method:         A function in a class.

self:           Reference to the instance of a class
"""


class Car:
    no_of_wheels = 4 # static field

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

    def start(self):
        self.on = True


# ------------------ Test

mercedes_s3 = Car("Mercedes", "S3", 1.4, 25000)
print(f"Make: {mercedes_s3.make}, Model: {mercedes_s3.model}, Price: {mercedes_s3.price}")
mercedes_s3.start()
print(f"Is ON: {mercedes_s3.on}")
print(mercedes_s3.__dict__)

audi_a3 = Car('Audi', "Q3", 2.0, 30000)

print('*' * 50)
print(f"No. of wheels Car: {Car.no_of_wheels}")
print(f"No. of wheels Mercedes: {mercedes_s3.no_of_wheels}")
print(f"No. of wheels Audi: {audi_a3.no_of_wheels}")

print('*' * 50)
Car.no_of_wheels = 8
print(f"No. of wheels Car: {Car.no_of_wheels}")
print(f"No. of wheels Mercedes: {mercedes_s3.no_of_wheels}")
print(f"No. of wheels Audi: {audi_a3.no_of_wheels}")





