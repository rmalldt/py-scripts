"""
After Python 3.12
"""

type IntOrStr = int | str

type ListOrSet[T] = list[T] | set[T]


# Generic class
class Box[T]:
    def __init__(self, item: T) -> None:
        self.item = item

    def get_item(self) -> T:
        return self.item

    def set_item(self, new_item: T) -> None:
        self.item = new_item


# Generic function
def get_first_item[T](items: list[T]) -> T:
    return items[0]


def main() -> None:
    # Integer
    int_box = Box(123)
    int_item = int_box.get_item()  # int_item => int
    print(int_item)

    # String
    str_box = Box("Hello there!")
    str_item = str_box.get_item()  # str_item => srt
    print(str_item)

    # List
    list_box = Box([1, 2, 3])
    list_item = list_box.item  # list_item => list[int]
    print(list_item)

    # Function
    first_item = get_first_item([1, 2, 3])  # first_item => int
    print(first_item)


if __name__ == "__main__":
    main()
