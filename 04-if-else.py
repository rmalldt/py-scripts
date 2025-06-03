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
game_on = 1
answer = 5
while game_on == 1:
    guess = int(input("Guess number between 1 to 10: "))
    if guess > answer:
        print("Go low")
    elif guess < answer:
        print("Go high")
    else:
        print("You got it")
        game_on = 0

# ------------------ If-else with and, or and not operators
game_on = False
score = 5
losing = False
if game_on and score >= 5:
    print("Game is active")
elif (game_on and score >= 3) or not losing:  # and has higher precedence than or
    print("Game is active but score is low")
else:
    print("Game over")


# ------------------ Truthy and false values
mbool = False
mNone = None
answer = 0
str = ""
mlist = []
mtuple = ()
mdict = {}

if mbool:
    print("True")
elif mNone:
    print("True")
elif answer:
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
sub_str = "Hel".casefold()  # lowercase
if sub_str in word:
    print(f"{sub_str} is in {word}")
else:
    print("N/A")

if sub_str not in "there":
    sub_str = "Changed"
    print(sub_str)
