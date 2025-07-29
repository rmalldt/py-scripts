from typing import Optional, Any

# --------------- Section: Typing Lists
hostnames: list[str] = ["web01.example.com", "db01.example.com"]
open_ports: list[int] = [80, 443, 22]


def process_hostnames(hosts: list[str]) -> None:
    for host in hosts:
        print(f"Processing host: {host.upper()}")


process_hostnames(hostnames)
# process_hostnames(open_ports) # will lead to type error


# --------------- Section: Typing Dictionaries
server_config: dict[str, str] = {
    "hostname": "app01.prod",
    "ip_address": "10.0.5.20",
    "os_type": "Linux",
}

user_roles: dict[str, list[str] | str] = {
    "user-123": ["admin", "editor"],
    "user-456": ["dev", "viewer"],
    "group": "common",
}

server_info: dict[str, int | str | bool | list[str]] = {
    "port": 80,
    "state": "running",
    "healthy": True,
    "region": ["us-east-1", "eu-west-2"],
}


# --------------- Section: Typing Tupless
server_status: tuple[str, int, bool] = (
    "api.example.com",
    443,
    True,
)

# variable length tuple
ip_parts: tuple[int, ...] = (192, 168, 1, 100)


# --------------- Section: Typing Sets
admin_users: set[str | int] = {"alice", "bob", "charlie"}


def is_admin(username: str, admins: set[str]) -> bool:
    return username in admins


# --------------- Section: Union[X, Y, ...] for Multiple Possible Types
identifier: str | int = "abcde-1234"
identifier = 1234


def process_mixed_data(data: list[int | str]) -> None:
    for item in data:
        if isinstance(item, str):
            print(f"Processing string: {item.upper()}")
        else:
            print(f"Processing int: {item * 2}")


# --------------- Section: Optional[X] for Values That Can Be None
def find_user(user_id: str) -> Optional[dict[str, str]]:
    if user_id == "123":
        return {
            "id": "123",
            "name": "Admin user",
            "email": "admin@example.com",
        }

    return None


# Same as above (RECOMMENDED)
def find_user_alt(user_id: str) -> dict[str, str] | None:
    if user_id == "123":
        return {
            "id": "123",
            "name": "Admin user",
            "email": "admin@example.com",
        }

    return None


found_user = find_user("123")
if found_user:  # need to check since it can be None too
    print(f"Found user: {found_user["name"]}")


def apply_config(settings: dict[str, str] | None) -> str:
    if settings:
        user = settings.get("user", "default")
        return f"User set to {user}"

    return "No settings provided"


print(apply_config(None))

user = {"user": "app-01", "ip": "192.168.0.1"}
print(apply_config(user))


# --------------- Section: Any for Unrestricted Types
def print_anything(item: Any) -> None:
    print(f"Item: {item}, type: {type(item)}")


print_anything(1)
print_anything("hello")


# --------------- Hands-on Exercise


# Ex 1:
def apply_config(settings: Optional[dict[str, str]]) -> str:
    if settings:
        user = settings.get("USER", "default")
        return f"User set to {user}"

    return "No settings provided."


config_data = {"USER": "admin", "HOST": "prod.server"}
print(apply_config(config_data))


print(apply_config(None))


# Ex 2:
def format_ports(ports: int | list[int]) -> str:
    if isinstance(ports, int):
        return f"Port: {ports}"
    else:
        # return f"Ports:{','.join(ports)}"  # raises ERROR str.join expects list[str]
        return f"Ports: {",".join(str(p) for p in ports)}"


print(format_ports([1, 2, 3]))


# Ex 3:
def get_user_id(raw_id: str | int) -> int | None:
    if isinstance(raw_id, str):
        try:
            parsed_int = int(raw_id)
            return parsed_int
        except ValueError as e:
            print(f"Error: {e}")
            return
    return raw_id


print(get_user_id(123))
print(get_user_id("456b"))
