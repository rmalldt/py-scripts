# --------------- Section: Basic Type Hint Syntax - Variable Annotations
config_path: str = "/etc/app.conf"
retry_count: int = 3
is_enabled: bool = bool(1)
servers: list[str] = ["web01", "web02"]
settings: dict[str, int | str] = {"port": 8080, "user": "admin"}


# --------------- Section: Basic Type Hint Syntax - Function Argument and Return Type Annotations
def get_server_status(hostname: str, port: int) -> str:
    print(f"Checking {hostname}:{port}")
    if port == 80:
        return "Online"
    else:
        return "Unknown"


# --------------- Section: Python Remains Dynamically Typed
def process_id(user_id: int) -> None:
    print(f"Processing user ID: {user_id} (type: {type(user_id)})")


# --------------- Demonstration of dynamic typing
process_id(1234)

"""
- Below line will compile and run fine at runtime.
- But it will raise ERROR when run with `mypy` which is a tool/ a Python linter that performs
  the static type checking for Python.
- If we include `mypy` as a part of our CI/CD pipeline, below line would raise ERROR and the
  execution of our pipeline would not continue.
"""
# process_id("user-1234")
