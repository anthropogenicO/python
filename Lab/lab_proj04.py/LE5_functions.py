import random
random.randint(1,6)


MIN_DIE_VALUE = 1
MAX_DIE_VALUE = 6
POINTS_PER_WIN = 10


def roll_die():
    """Return a random die value between the minimum and maximum."""
    return random.randint(MIN_DIE_VALUE, MAX_DIE_VALUE)


def calculate_points(guess, actual):
    """Return the points earned for the player's guess."""
    if guess == actual:
        return POINTS_PER_WIN
    else:
        return 0
    


def show_result(guess, actual, points):
    """Display the die value, points earned, and whether the guess was correct."""
    print (f"Dice number: {actual}")
    print (f"Points Earned: {points}")
    if guess == actual:
        print(f"Correct Guess")
    else:
        print(f"Try again next time")
4