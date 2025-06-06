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
mcomplex = 1j
print(type(mcomplex))

# ------------------ Sequence types

# str
name = "Jim"
print(type(name))

# list
# - mutable (can add, remove, modify elements)
# - useful to store dynamic collections
# - slower than tuple
mstrs = ["apple", "ball", "cat"]  # list
print(type(mstrs))

# tuple
# - immutable (cannot add, remove, modify element after creation)
# - useful to store fixed-sized data
# - faster than list
# - duplicates allowed
# - ordered
# - hashable and indexable
mtuples = ("apple", "ball", "cat")
print(type(mtuples))

# range
mrange = range(5)
print(type(mrange))

# ------------------ Mapping types
# dict
mdict = {"name": "Jim", "id": 10}
print(type(mdict))

# ------------------ Set types
# set
# - mutable
# - duplicates not allowed
# - not ordered
# - not hashable and indexable
mset = {"apple", "ball", "cat"}
print(type(mset))

# forzenset
# - immutable
# - duplicates not allowed
# - not ordered
# - hashable but not indexable
mfrozenset = frozenset({"apple", "ball", "cat"})
print(type(mfrozenset))

# ------------------ Binary types
# bytes
mbyte = b"Hello"
print(type(mbyte))

# bytesarray
mbytearr = bytearray(5)
print(type(mbytearr))

# memoryview
mmemoryview = memoryview(bytes(5))
print(type(mmemoryview))


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
