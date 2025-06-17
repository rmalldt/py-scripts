def area_of_square(length: float) -> float:
    return length**2


def area_of_rectangle(length: float, width: float) -> float:
    return length * width


# ------------------ Test

print(f"Area: {area_of_square(4)}")


if __name__ == "__main__":
    print(f"my_module __name__ is {__name__}")
