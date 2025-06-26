from typing import TypeVar, Any

T = TypeVar("T")  # T is a generic type variable


def process_any(elems: list[Any]) -> list[Any]:
    return [elem for index, elem in enumerate(elems) if index % 2 == 1]


def process_numbers(numbers: list[int]) -> list[int]:
    return [number**2 for number in numbers]


# Works for any list with any type
def process_elements(elems: list[T]) -> list[T]:
    return [elem for index, elem in enumerate(elems) if index % 2 == 1]


def main():

    # anys => list[Any]
    anys = process_any(["a", "b", "c"])
    print(anys)

    # numbers => list[int]
    numbers = process_numbers([1, 2])
    print(numbers)

    # res1 => list[str]
    res1 = process_elements(["apple", "ball", "cat", "dog", "fox"])
    print(res1)

    # res2 => list[int]
    res2 = process_elements([0, 1, 2, 3, 4, 5])
    print(res2)


if __name__ == "__main__":
    main()
