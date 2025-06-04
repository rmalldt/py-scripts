# ------------------ Lists Operations
fruits = ["apple", "orange", "banana", "kiwi", "pears"]

for part in fruits:
    print(part)

# Length
print("Length:", len(fruits))

# Index access
print(fruits[0])  # apple

# Slicing
print(fruits[0:3])  # ['apple', 'orange', 'banana']
print(fruits[-2])  # kiwi
print(fruits[0:4:2])  # ['apple', 'banana']


# Max Min
print(min(fruits))  # apple
print(max(fruits))  # pears

# Count
print("banana".count("na"))  # 2

# Append
fruits.append("strawberry")
fruits

# Enumerate function
for i, fruit in enumerate(fruits):
    print(i, fruit)
