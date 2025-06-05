# ------------------ String Concepts


def string_concepts():
    # ----- Single and double quote strings
    print("Double quote string")
    print(
        'There is no difference between "single" and "double" quote strings in Python'
    )

    # ----- String concatenation
    print("Hello" + " " + "there")

    # ----- Input from console
    greeting = "Hello"
    name = input("Please enter your name: ")
    print(greeting + " " + name)

    # ----- Escape Character: Newline, tab and Quote
    # Newlines
    splitString = "First line\nSecond line\nThird line"
    print(splitString)

    # Tabs
    tabbedstring = "1\t2\t3"
    print(tabbedstring)

    # Quotes
    anotherstring = (
        """Hello, my name is "Jim" and I'm going to walk you through the project."""
    )

    print(anotherstring)
    anotherstring = """This is first line
    The second line
    The third line"""
    print(anotherstring)

    # ----- Escape the escape characters
    print(
        "C:\\Users\\tim\\notes.txt"
    )  # use double backslash to escape the escape chars
    print(r"C:\Users\tim\notes.txt")  # use "r" raw string to escape the escape chars


# ------------------ String Operations


def string_operations():

    parrot = "Norwegian Blue"

    # ----- Access element via index
    print(parrot[3])  # w

    # Access element from back via negative index
    print(parrot[-1])  # e
    print(parrot[-2])  # u

    # ----- String length
    print(len(parrot))  # 14

    # ----- Slice (Subtrings)
    print(parrot[0:6])  # Norweg, start index is inclusive and end index is exclusive
    print(parrot[3:9])  # wegian
    print(parrot[10:])  # Blue
    print(parrot[:9])  # Norwegian
    print(parrot[:])  # Norwegian Blue

    # Slice with negative index
    print(parrot[-4:-2])  # Bl
    print(parrot[-4:12])  # Bl
    print(parrot[-4:])  # Blue

    # Slice with steps
    print(parrot[0:6:2])  # Nre, 0: start index, 6: end index, 2: step
    print(parrot[0:6:3])  # Nw, 0: start index, 6: end index, 3: step
    print(parrot[0::2])  # NreinBu, 0: start index, 2: step

    # Slice backwards
    strLen = len(parrot)
    print(parrot[13::-1])  # eulB naigewroN
    print(parrot[::-1])  # eulB naigewroN

    # ----- Concatenation
    str1 = "hello "
    str2 = "there "
    str3 = "Jim "
    print(str1 + str2 + str3)  # hello there Jim
    print("hello " "there " "Jim")  # hello there Jim

    # Concatenate using multiply
    print("Hello " * 5)  # Hello Hello Hello Hello Hello

    # Check substring using 'in'
    today = "friday"
    print("day" in today)  # True
    print("fri" in today)  # True
    print("wed" in today)  # False
    print("thur" in today)  # False

    # ----- Convert number to string
    # Number and string can't be concatenated because in the presence of number
    # '+' operator tries to add instead of concatenate

    # Convert number to string using str function
    id = 1003
    print("ID: " + str(id))
    print("ID: {0} ".format(id))

    # ----- String format replacement field (OLD APPROACH)
    name = "Jim"
    print("ID: {0}, Name: {1}".format(id, name))

    print(
        """ID: {0}
    Name: {1}
    Status: ID {0} is active            
    """.format(
            id, name
        )
    )

    # String format field width, alignment and precision
    # String replacement part {1:<6.2f} breakdown:
    #   1 second parameter
    #   :<6 field width, left aligned
    #   .2f precision
    for i in range(1, 5):
        print(
            "Number {0:2} squared is {1:<6.2f} and cubed is {2:<8.2f}".format(
                i, i**2, i**3
            )
        )


# ------------------ f string (MODERN APPROACH and RECOMMENDED)


def string_format():
    id = 1005
    name = "Jim"
    print(f"Id: {id}, Name: {name}")

    for i in range(1, 5):
        print(f"Number {i} squared is {i**2:<6.2f} and cubed is {i**3:<8.2f}")


# ------------------ split() and join()


# split() returns a list
def split_items():
    sentence = "Hello there, how are you?"
    words = sentence.split(sep=" ")

    for word in words:
        print(word)


# join() returns a single string
def join_items():
    guitars = ["Fender", "Ibanez", "Gibson", "PRS", "Kiesel"]
    separator = ", "

    result_str = separator.join(guitars)
    print(result_str)  # Fender, Ibanez, Gibson, PRS, Kiesel


# ------------------ Tests

# string_concepts()
# string_operations()
# string_format()
# split_items()
join_items()
