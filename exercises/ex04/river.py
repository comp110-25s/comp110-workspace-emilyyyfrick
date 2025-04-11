"""File to define River class."""

__author__ = "730566891"


from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove fish older than 3 and bears older than 5"""
        river_fish: list = []
        river_bear: list = []
        for idx in self.fish:
            if idx.age <= 3:
                river_fish.append(idx)
        self.fish = river_fish
        for i in self.bears:
            if i.age <= 5:
                river_bear.append(i)
        self.bears = river_bear
        return None

    def remove_fish(self, amount: int) -> None:
        """Remove amount many fish from river"""
        for i in range(0, amount):
            self.fish.pop(0)
        return None

    def bears_eating(self):
        """Bear eats 3 fish if there are at least 5 fish in the river"""
        for i in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                i.eat(3)
        return None

    def check_hunger(self):
        """Bear remvoed if hunger score is lower than 0"""
        river_bear: list[Bear] = []
        for i in self.bears:
            if i.hunger_score >= 0:
                river_bear.append(i)
        self.bears = river_bear
        return None

    def repopulate_fish(self):
        """For each pair of fish four offspring are produced"""
        offspring_fish: int = (len(self.fish) // 2) * 4
        for i in range(0, offspring_fish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """For each pair of bear's one offspring is produced"""
        offspring_bear: int = len(self.bears) // 2
        for i in range(0, offspring_bear):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Print status of bear and fish populations"""
        print(f"~~~ Day {self.day}: ~~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()


def one_river_week(self) -> None:
    """Calls one_river_day seven times"""
    for i in range(0, 7):
        self.one_river_day()
    return None
