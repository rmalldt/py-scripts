import sys


def range_list_diff():
    big_range = range(10000)
    print(f"big_range is {sys.getsizeof(big_range)} bytes")  # 48 bytes

    # Create a list containing all the values in big_range
    big_list = []
    for val in big_range:
        big_list.append(val)

    # big_list stores exact set of number but takes more space than big_range
    print(f"big_list is {sys.getsizeof(big_list)} bytes")  # 85176 bytes


# Generator function
def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print(f"my_range is returning {start}")
        # yield returns the value and goes to suspended state,
        # then wakes up and continues from where it left in the next iteration.
        yield start
        start += 1


def yield_example():
    big_range = my_range(5)

    big_list = []
    for val in big_range:
        big_list.append(val)

    print(f"big_range: {big_range}")
    print(f"big_list: {big_list}")


def consume_yield_value():
    big_range = my_range(5)

    # Consume the value yield by my_range
    # First value 0 won't be available for the for loop to consume
    print(f"Calling next(): {next(big_range)}")

    big_list = []
    for val in big_range:
        # generator will only yield when this line called (lazy evaluation)
        big_list.append(val)

    print(f"big_range: {big_range}")
    print(f"big_list: {big_list}")  # [1,2,3,4]


# ------------------ Generator Gotchas


def generator_loop():
    # This won't iterate through all the items
    # next() pull only the first value -> 0, then stops.
    # Only one iteration happens.
    res = next(i for i in range(5))
    print(res)  # 0

    """
    Equaivalent to above.
     for i in range(5):
        yield i 
    """

    # This iterates through the items until it finds the item

    res = next((i for i in range(5) if i == 3))
    print(res)  # 3

    """
    Equaivalent to above.
    for i in range(5):
        if i == 3:
            yield i
    """


# ------------------ Test

# range_list_diff()
# yield_example()
# consume_yield_value()

generator_loop()
