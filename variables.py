# Boolean Type:
isActive = True  # bool
print(type(isActive))

# Numeric Types:
num = 12  # int
print(type(num))

myFloat = 12.45  # float
print(type(myFloat))

myComplex = 1j  # complex
print(type(myComplex))

# Text type:
name = "Jim"  # str
print(type(name))

# Sequence types:
# list
# - mutable (can add, remove, modify elements)
# - useful to store dynamic collections
# - slower than tuple
myStrs = ["apple", "ball", "cat"]  # list
print(type(myStrs))

# tuple
# - immutable (cannot add, remove, modify element after creation)
# - usefult to store fixed-sized data
# - faster than list
myTuples = ("apple", "ball", "cat")
print(type(myTuples))
