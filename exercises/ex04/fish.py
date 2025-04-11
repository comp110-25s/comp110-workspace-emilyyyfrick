"""File to define Fish class."""

__author__ = "730566891"


class Fish:
    age: int

    def __init__(self):
        self.age = 0
        return None

    def one_day(self):
        """Fish age after one day"""
        self.age += 1
        return None
