from typing import TypedDict, NotRequired


# TypeDict is a better choice for annotating dict type than dict[str, Ant] because
# TypeDict specifies "shape" for a dictionary which allows static type checker to
# verify expected keys (all defined keys must be present unless 'NotRequired') and
# their corresponding values type such as:
#       - id: int
#       - name: str
#
# dict[str, Any] provides no information about which keys must be present and their
# corresponding values.


# ` NotRequired` means the key itself does not have to exist in the dictionary at all.
# It is different from `str | None`` becuase `str | None` means the key must exist but
# its value can be either `str` or `None`.

# --------------- Ex 1:


class User(TypedDict):
    id: int
    name: str
    email: str
    phone: NotRequired[str]


user1: User = {
    "id": 123,
    "name": "Alice",
    "email": "alice@example.com",
    "phone": "+123456789",
}

user2: User = {
    "id": 456,
    "name": "Bob",
    "email": "bob@example.com",
}

print(f"User data: {user1.get("email")}")


# --------------- Ex 2:


class UserProfile(TypedDict):
    user_id: int
    display_name: str
    email: str


def greet_user(profile: UserProfile) -> None:
    # print(f"Hello, {profile['username']}!")  # static ERROR, 'username' is not defined
    print(f"Hello, {profile['user_id']}!")


user_data: UserProfile = {
    "user_id": 101,
    "display_name": "jdoe",
    "email": "j.doe@example.com",
}

greet_user(user_data)


# --------------- Ex 3:


class ServiceConfig(TypedDict):
    service_name: str
    port: int
    timeout: NotRequired[int]
    retries: NotRequired[int]


def configure_service(config: ServiceConfig) -> None:
    timeout = config.get("timeout", 10)
    retries = config.get("retries", 3)

    print(
        f"Configuring {config['service_name']} on port {config['port']}. "
        f"Timeout: {timeout}, Retries: {retries}"
    )


base_config: ServiceConfig = {"service_name": "auth-service", "port": 8080}
configure_service(base_config)
