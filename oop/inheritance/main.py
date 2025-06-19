from linecache import clearcache

from player import Player
from enemy import Enemy, Troll

# ------------------ Test

# ----- Player instances
jim = Player("Jim")
print(f"Name: {jim.name}, Lives: {jim.lives}, Level: {jim.level}")

jim.level = 10
jim.lives = 10
print(f"Name: {jim.name}, Lives: {jim.lives}, Level: {jim.level}")

basic_enemy = Enemy("Basic enemy", 12, 1)
basic_enemy.take_damage(5)
print(basic_enemy)


# ----- Enemy instances
troll1 = Troll()  # default values provided in the class constructor used to instantiate
print(troll1)

troll2 = Troll("Big Troll", 20)  # overloaded constructor with default values
print(troll2)

troll3 = Troll("Super Big Troll", 20, 10)
print(troll3)
