# ------------------ Indentation and Code block
# A new code block starts below a line ending with colon ':'.

# ------------------ If-else
# If-else

name = "Jim"
age = int(input(f"Enter your age, {name}: "))
if age >= 18:
    print("You can apply for driving licence")
else:
    print("You are not eligible for driving licence")

# If-elif-else
gameOn = 1
num = 5
while gameOn == 1:
    guess = int(input("Guess number between 1 to 10: "))
    if guess > num:
        print("Go low")
    elif guess < num:
        print("Go high")
    else:
        print("You got it")
        gameOn = 0

# ------------------ If-else with and, or and not operators
gameOn = False
score = 5
losing = False
if gameOn and score >= 5:
    print("Game is active")
elif (gameOn and score >= 3) or not losing:  # and has higher precedence than or
    print("Game is active but score is low")
else:
    print("Game over")


# ------------------ Truthy and false values
mbool = False
mNone = None
num = 0
str = ""
mlist = []
mtuple = ()
mdict = {}

if mbool:
    print("True")
elif mNone:
    print("True")
elif num:
    print("True")
elif str:
    print("True")
elif mlist:
    print("True")
elif mtuple:
    print("True")
elif mdict:
    print("True")
else:
    print("False")

# ------------------ in and not in
word = "hello"
subStr = "Hel".casefold()  # lowercase
if subStr in word:
    print(f"{subStr} is in {word}")
else:
    print("N/A")

if subStr not in "there":
    subStr = "Changed"
    print(subStr)
