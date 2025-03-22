"""Exercise 01 Tea Party."""

__author__: str = "730566891"


def main_planner(guests: int) -> None:
    """Entry point to program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Number of teabags needed based on number of guests"""
    return people * 2


def treats(people: int) -> int:
    """Number of treats based on number of tea guests"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Costs of teabags and treats combined"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
