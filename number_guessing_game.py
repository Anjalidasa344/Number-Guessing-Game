
import random


def intro():
    print("\n" + "=" * 40)
    print("       NUMBER GUESSING GAME")
    print("=" * 40)

    name = input("May I know your name? ").strip()

    if not name:
        name = "Player"

    print(
        f"\nHello, {name}! I am thinking of a number "
        "between 1 and 200."
    )
    print("You have 6 attempts to guess it!")
    return name


def play_game(name):
    secret_number = random.randint(1, 200)
    max_attempts = 6

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"\nAttempt {attempt}/{max_attempts} - Guess: "))

            if guess < 1 or guess > 200:
                print("Please enter a number between 1 and 200.")
                continue

            if guess == secret_number:
                print(
                    f"\nCongratulations, {name}! "
                    f"You guessed the number in {attempt} attempts!"
                )
                return

            elif guess < secret_number:
                print("Too low! Try a higher number.")

            else:
                print("Too high! Try a lower number.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    print(f"\nGame over, {name}!")
    print(f"The correct number was {secret_number}.")


def main():
    name = intro()

    while True:
        play_game(name)

        play_again = input(
            "\nDo you want to play again? (yes/no): "
        ).strip().lower()

        if play_again not in ("yes", "y"):
            print(f"\nThanks for playing, {name}! Goodbye!")
            break


if __name__ == "__main__":
    main()
