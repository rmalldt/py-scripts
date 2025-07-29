from typing import Optional, TypeVar, Generic

# --------------- Section: Defining a generic function

# Create Type Variable
T = TypeVar("T")


def get_first_item(input_list: list[T]) -> T | None:
    if input_list:
        return input_list[0]

    return None


first_number = get_first_item([1, 2, 3])
first_str = get_first_item(["abc", "def"])
first_mixed_list = get_first_item(["abc", "def", 1, 2, 3])


# --------------- Section: Constrained TypeVar for numeric addition

# Create Type Variable with constraints
NumberType = TypeVar("NumberType", int, float)


def add_generic_numbers(x: NumberType, y: NumberType) -> NumberType:
    return x + y


sum = add_generic_numbers(3, 5.0)


# --------------- Section: Bounded TypeVar


# Superclass
class CloudResource:
    def __init__(self, name: str, cpu_usage: float) -> None:
        self.name: str = name
        self.cpu_usage: float = cpu_usage
        self.deployed: bool = False

    def deploy(self) -> None:
        print(f"Deploying {self.name}")
        self.deployed = True


# Subclass
class VirtualMachine(CloudResource):
    # Only need to explicity call super().__init__ inside this class's `__init__` method
    # of we need to override the default __init__() method in  this class.
    # __init__ method is inherited from SuperClass.

    def reboot(self) -> None:
        print(f"Rebooting VM {self.name}")


# Subclass
class DockerContainer(CloudResource):
    def restart(self) -> None:
        print(f"Restarting container {self.name}")


# Create Type Variable with upper bound
# NOTE: ResourceType will work with both Subclasses since the bound is set to SuperClass CloudResource
ResourceType = TypeVar("ResourceType", bound=CloudResource)


def filter_deployed(
    resources: list[ResourceType],  # TypeVar with upperbound
) -> list[ResourceType]:
    return [resource for resource in resources if resource.deployed]


vm1 = VirtualMachine("vm-01", cpu_usage=65.0)
vm2 = VirtualMachine("vm-02", cpu_usage=45.0)
container1 = DockerContainer("api-service", cpu_usage=85.0)
container2 = DockerContainer("worker", cpu_usage=55.0)

vm1.deploy()
container1.deploy()

all_resources = [vm1, vm2, container1, container2]
deployed_resources = filter_deployed(all_resources)

# print([resource.name for resource in deployed_resources])


# --------------- Section: Generic class

G = TypeVar("G")


class SimpleStack(Generic[G]):
    def __init__(self) -> None:
        self._items: list[G] = []

    def push(self, item: G) -> None:
        self._items.append(item)

    def pop(self) -> G:
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self._items.pop()

    def peek(self) -> Optional[G]:
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        # return len(self._items) == 0
        return not self._items


str_stack = SimpleStack[str]()
str_stack.push("str")

int_stack = SimpleStack[int]()
int_stack.push(12)

print(int_stack.pop())
print(int_stack.pop())
