import turtle  # import the whole module
from math import radians, cos  # import specific functions from the module

# ------------------ Square


def square(length: int) -> None:
    for side in range(4):
        turtle.forward(length)
        turtle.right(90)


# ------------------ Circle


def encircled_square(lenght: int) -> None:
    """Draws a square of length `length`,
    then encloses it in a circle
    """
    square(lenght)
    angle = radians(45)
    radius = lenght * cos(angle)
    turtle.right(135)
    turtle.circle(radius)


# ------------------ Tests


def squares():
    # Complete 360 deg [(left = 5 deg) * (range = 72)]
    for s in range(72):
        square(120)
        turtle.left(5)  # turn left by 5 deg
    turtle.done()


def encircled_squares():
    for s in range(72):
        encircled_square(120)
        turtle.left(5)  # turn left by 5 deg
    turtle.done()


# ------------------ Test
turtle.speed("fast")
# square(120)
# squares()

# encircled_square(300)
# encircled_squares()
