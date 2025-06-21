# ------------------ Indentation and Code block
"A new code block starts below a line ending with colon ':'."


# ------------------ If-else
def eligible_to_vote():
    name = input("Enter your name: ")
    age = int(input(f"Enter your age, {name}: "))
    if age >= 18:
        print("You can apply for driving licence")
    else:
        print("You are not eligible for driving licence")


# ------------------ If-elif-else
def guess_number():
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
def game_active():
    game_on = False
    score = 5
    losing = False
    if game_on and score >= 5:
        print("Game is active")
    elif (game_on and score >= 3) or not losing:  # and has higher precedence than or
        print("Game is active but score is low")
    else:
        print("Game over")


# ------------------ Truthy and falsy values
def truthy_falsy():

    print("Values interpreted as False in Python:")
    print(
        f"""Flase: {False} 
None: {bool(None)}
0: {bool(0)}
0.0: {bool(0.0)}
Empty string: {bool("")}
Empty list: {bool([])}
Empty tuple: {bool(())}
Empty dict: {bool({})}
"""
    )


# in and not in
def in_notin():
    word = "hello"
    sub_str = "Hel".casefold()  # lowercase
    if sub_str in word:
        print(f"{sub_str} is in {word}")
    else:
        print("N/A")

    if sub_str not in "there":
        sub_str = "Changed"
        print(sub_str)


# ------------------ Pass statement
# Pass statement is used when statement is required syntactically
# but the program requires no action.
def pass_statement():
    x = 10
    if x == 10:
        pass


# ------------------ Match statements
# Match statement is similar to Switch statements in C and Java
def match_statement():
    choice = int(input("Please enter a number between 1-3: "))
    match choice:
        case 1:
            print("Your choice is one")
        case 2:
            print("Your choice is two")
        case 3:
            print("Your choice is three")
        case _:
            print("Invalid option")


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403 | 404:  # multiple cases
            return "Not allowed"
        case 405:
            return "Method not allowed"
        case 408:
            return "Request timeout"
        case _:  # default match if no case matches
            return "Server error"


# ------------------ Test
# eligible_to_vote()
# guess_number()
# game_active()
truthy_falsy()
# in_notin()
# pass_statement()
# match_statement()
# print(f"Error message: {http_error(404)}")
