from my_module import area_of_square  # import only specific objects
from my_module import area_of_rectangle as rec  # import as alias

area_square = area_of_square(5)
print(f"Importing module 2, area of square: {area_square}")

area_rec = rec(10, 2)
print(f"Importing module 2, area of rectangle: {area_rec}")


def iterate_globals():
    for name, obj in globals().items():
        print(f"{name}: {obj}")


iterate_globals()
