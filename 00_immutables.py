# ------------------ Immutable
result = True
new_result = result
print(f"ID of result1: {id(result)}")  # 4318545392 (same)
print(f"ID of result2: {id(new_result)}")  # 4318545392 (same)

# Booleans are immutable, True can't be changed to False
# So, new object/value is created (different address) and is assigned to result variable
result = False
print(f"ID of result1: {id(result)}")  # 4320151056 (different)

# Booleans are immutable. True can't be changed to string
# So, new string object is created (different address) and is assigned to result variable
result = "Correct"
print(f"ID of result1: {id(result)}")  # 4309546304 (different)

# Strings are immutable. "Correct" can't be changed to new string
# So, new sting object is created (different address) and is assigned to result variable
result += "ish"
print(f"ID of result1: {id(result)}")  # 4313381424 (different)


# ------------------ Mutable
fruits = ["apple", "orange", "banana", "kiwi", "pears"]
print(f"ID of fruits: {id(fruits)}")  # 4305942976 (same)

# Lists are mutable, the contents of the list can be changed without creating
# new object
fruits += ["strawberry"]
print(f"ID of fruits: {id(fruits)}")  # 4305942976 (same)
