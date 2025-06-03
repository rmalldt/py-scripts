# ------------------ Boolean type
isActive = True  # bool
print(type(isActive))

# ------------------ Numeric types
# int
num = 12
print(type(num))

# float
myFloat = 12.45
print(type(myFloat))

# complex
myComplex = 1j
print(type(myComplex))

# ------------------ Sequence types

# str
name = "Jim"
print(type(name))

# list
# - mutable (can add, remove, modify elements)
# - useful to store dynamic collections
# - slower than tuple
myStrs = ["apple", "ball", "cat"]  # list
print(type(myStrs))

# tuple
# - immutable (cannot add, remove, modify element after creation)
# - useful to store fixed-sized data
# - faster than list
# - duplicates allowed
# - ordered
# - hashable and indexable
myTuples = ("apple", "ball", "cat")
print(type(myTuples))

# range
myRange = range(5)
print(type(myRange))

# ------------------ Mapping types
# dict
myDict = {"name": "Jim", "id": 10}
print(type(myDict))

# ------------------ Set types
# set
# - mutable
# - duplicates not allowed
# - not ordered
# - not hashable and indexable
mySet = {"apple", "ball", "cat"}
print(type(mySet))

# forzenset
# - immutable
# - duplicates not allowed
# - not ordered
# - hashable but not indexable
myFrozenSet = frozenset({"apple", "ball", "cat"})
print(type(myFrozenSet))

# ------------------ Binary types
# bytes
myByte = b"Hello"
print(type(myByte))

# bytesarray
myByteArr = bytearray(5)
print(type(myByteArr))

# memoryview
myMemoryView = memoryview(bytes(5))
print(type(myMemoryView))


# ------------------ None type
none = None
print(type(none))


# ------------------ Python has
# - strong typing
# - dynamic typing (no need to declare types)
# - type safety (enforced at runtime)
# - type inference (implicit at runtime)

# Strongly typed language
x = 10
y = "5"
# print(x + y) # TypeError: can't concatenate int and str
print(x + int(y))  # 15

# Dynamically typed language
a = 10  # a is an int
a = "hello"  # a is a str
print(a)
