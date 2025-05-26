# Single and double quote strings
print("Single quote string")
print("Double quote string")
print('There is no difference between "single" and "double" quote strings in Python')

# String concatenation
print("Hello" + " " + "there")
greeting = "Hello"

# Input from console
name = input("Please enter your name: ")
print(greeting + " " + name)

# Escape Character: Newline, tab and Quote
# Newlines
splitString = "First line\nSecond line\nThird line"
print(splitString)

# Tabs
tabbedString = "1\t2\t3"
print(tabbedString)

# Quotes
anotherString = (
    """Hello, my name is "Jim" and I'm going to walk you through the project."""
)

print(anotherString)
anotherString = """This is first line
The second line
The third line"""
print(anotherString)

# Escape the escape characters
print("C:\\Users\\tim\\notes.txt") # use double backslash to escape the escape chars
print(r"C:\Users\tim\notes.txt") # use "r" raw string to escape the escape chars



