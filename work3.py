
import random
import string
import time
import os
import msvcrt


def clear_screen():
    """Clear the console screen."""
    os.system("cls")


def clear_keyboard_buffer():
    """Remove any pending keystrokes from the keyboard buffer."""
    while msvcrt.kbhit():
        msvcrt.getwch()



def generate_string(length):
    """Generate a random string of uppercase letters."""
    return "".join(
        random.choice(string.ascii_uppercase)
        for _ in range(length)
    )


def show_countdown():
    """Display five dots, one second apart."""
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(1)
    print()



def play_level(level):
    """Display a string and return it with the player's guess."""
    length = level + 3
    secret = generate_string(length)

    print(f"Level {level}")
    print(secret)
    show_countdown()

    clear_screen()
    clear_keyboard_buffer()
    guess = input(
        "Enter the string you just saw (case insensitive): "
    )

    return secret, guess


def show_results(level, secret, guess):
    """Display the failed answer and final game results."""
    completed = level - 1
    print("Incorrect!")
    print(f"Correct string: {secret}")
    print(f"Your answer:    {guess}")
    print(f"You successfully made it through Level {completed}.")

    if completed <= 2:
        print("Wow, did you understand the game?")
    elif completed <= 6:
        print("Not bad, keep working at it.")
    else:
        print("Nice Job! You're a memory master!")


def play_game():
    """Run levels until the player enters an incorrect answer."""
    level = 1

    while True:
        secret, guess = play_level(level)

        if guess.upper() != secret:
            show_results(level, secret, guess)
            break

        print("Good job!")
        time.sleep(3)
        clear_screen()
        level += 1


def replay_game():
    """Ask whether the player wants another game."""
    while True:
        answer = input(
            "Would you like to play again? (Y/N): "
        ).strip().upper()

        if answer == "Y":
            clear_screen()
            return True
        elif answer == "N":
            print("Have a good day")
            return False
        else:
            print("Please enter Y or N.")


def main():
    """Start the program and manage replaying games."""
    choice = input(
        "Press Q to quit or anything else to start the game: "
    )

    if choice.strip().upper() == "Q":
        print("Have a good day")
        return

    while True:
        clear_screen()
        play_game()

        if not replay_game():
            break


if __name__ == "__main__":
    main()
