import random
min = 1
max = 100

target = random.randint(min, max)

pguess = []
cguess = []


def playerturn():
    while True:
        guess = int(input(f"Enter a guess between {min} and {max}: "))

        pguess.append(guess)

        if guess > target:
            print("To High")
        elif guess < target:
            print("To Low")
        else:
            break

def computureturn():
    print("my turn using binary search logic")

    guesses = 0
    lowv = min
    highv = max

    while True:
        computer_guess = random.randint(lowv, highv)
        cguess.append(computer_guess)
        guesses = guesses + 1

        print(f"computer guesses {computer_guess}")

        if computer_guess > target:
            highv = computer_guess - 1
        elif computer_guess < target:
            lowv = computer_guess + 1
        else:
            print("the computer guessed right")
            break


def finalresults():
    print(f"it took you {len(pguess)} guesses")
    print(f"it took the computure {len(cguess)} guesses")

    print("===== Final Results =====")
    print(f"The random number was: {target}")
    print(f"The Player Guessed {pguess}")
    print(f"The Player Guessed: {len(pguess)} amount of times")
    print(f"Computer Guesses: {cguess}")
    print(f"The Computer Guessed {len(cguess)} amount of times")

playerturn()
computureturn()
finalresults()