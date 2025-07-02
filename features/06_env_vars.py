import os

# `os.getenv` return env var for the specific variable name.
#   - 1st arg: var name
#   - 2nd arg: default value to return
name = os.getenv("MNAME", "no name")
print(f"Hello {name}")
