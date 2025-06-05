# ------------------ For loops
word = "Hello there"
for char in word:
    print(char)

# The start index is inclusive and the stop index is exclusive
for i in range(1, 5):
    print(f"{i}th index")

# Start value defaults to 0 if not provided
for i in range(5):
    print(f"{i}th index")

# Range with step value
for i in range(1, 5, 2):
    print(f"{i}th index")

# Nested for loops
for i in range(1, 5):
    for j in range(1, 3):
        print(i, j)

# ------------------  Continue and Breaks
vegetables = ["brocolli", "onion", "greens", "meat", "potato"]
for item in vegetables:
    if item == "meat":
        continue  # skip the execution below this line
    print("Buy: " + item)


item_to_find = "meat"
found_at = None  # constant represents nothing

for i in range(len(vegetables)):
    if vegetables[i] == item_to_find:
        found_at = i
        break  # break out of this loop immediately
    print(vegetables[i])
print(f"Item found at index {found_at}")

# ------------------ While loops
i = 0
while i < 10:
    print(f"{i}th index")
    i += 1

print("Please choose your option from the list below:")
print("1.\tLearn Python")
print("2.\tLearn Java")
print("3.\tLearn C++")
print("4.\tLearn JavaScript")
print("5.\tLearn Kotlin")
print("0.\tExit")
choice = "-"
while choice != "0":
    choice = input()
    if choice == "0":
        print("Goodbye!")
    elif choice in "12345":
        print(f"Your choice was {choice}")

# ------------------ Else with Loops
# In loops, break can be paired with else statement
# If loop finishes without break, else statement is executed
for i in range(1, 10):
    if i % 3 == 0:
        print("Found multiple of 3")
        break
# Else ONLY executes if no multiple of 3 is found
else:
    print("No multiple of 3 found")
