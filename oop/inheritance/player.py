class Player:

    def __init__(self, name) -> None:
        self.name = name
        self._lives = 3
        self._level = 0
        self._score = 0

    # Python does not need getters and setters to read and change attribute value
    # however, getters and setters can be used to validate the return and input
    # values as in this case.
    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives can't be negative value")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print("Level can't be less than 1")

    # The attribute lives can be accessed and changed via specified methods below.
    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    # Using decorators
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self) -> str:
        return f"Name: {self.name}, Lives: {self.lives}, Level: {self.level}, Score: {self.score}"
