import random
from typing import override


class Enemy:
    def __init__(
        self,
        name: str = "enemy",
        lives: int = 0,
        hit_points: int = 0,
    ):
        self.name = name
        self.lives = lives
        self.hit_points = hit_points
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print(f"{self.name} took {damage} points and have {self.hit_points} left")
        else:
            self.lives -= 1
            if self.lives > 0:
                print(f"{self.name} lost a life")
            else:
                print(f"{self.name} is dead")
                self.alive = False

    def __str__(self):
        return f"Name: {self.name}, Lives: {self.lives}, Hit points: {self.hit_points}"


# Class Troll extends Class Enemy
class Troll(Enemy):
    pass


# Class Nazgul extends Class Enemy
class Nazgul(Enemy):

    # Subclass constructor must call super class constructor first
    def __init__(self, name: str):
        super().__init__(name=name, lives=5, hit_points=20)

    def slash(self):
        print(f"{self.name} throwing the slash move")

    def defend(self):
        if random.randint(1, 3) == 3:
            print(f"***** {self.name} defends the attack *****")
            return True
        else:
            return False

    @override
    def take_damage(self, damage):
        if not self.defend():
            super().take_damage(damage=damage)


# Class NazgulKing extends Class Nazgul
class NazgulKing(Nazgul):

    def __init__(self, name: str):
        super().__init__(name)
        self.hit_points = 140

    @override
    def take_damage(self, damage):
        super().take_damage(damage // 4)
