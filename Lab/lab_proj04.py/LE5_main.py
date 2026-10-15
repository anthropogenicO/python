import LE5_functions as functions

ROUNDS =3 
player_name = input("Enter your name: ")

def welcome():
    print(f"Welcome, {player_name}")
    print("Guess the dice number from 1 to 6!")
    print("Each correct guess earns 10 points.")


def main():
    welcome()
    total_score = 0

    for round in range(1, ROUNDS +1):
        print(f"\nRound {round}")
        guess = int(input("Your guess: "))
        actual = functions.roll_die()
        points = functions.calculate_points(guess, actual)
        functions.show_result(guess, actual, points)

        total_score += points

    

    # TODO: Display the final score and maximum possible score.
    print(f"\nGame Over! {player_name}")
    print(f"Final Score: {total_score}/{ROUNDS * functions.POINTS_PER_WIN}")



main()
