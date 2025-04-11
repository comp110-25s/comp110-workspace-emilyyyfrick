"""File to define Bear class."""

__author__ = "730566891"


class Bear:
    age: int
    hunger_score: int

    def __init__(self):
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Bear age after one day"""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Update bears hunger based on number of fish"""
        self.hunger_score += num_fish
        return None
