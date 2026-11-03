import random


def main():
    best_score = None
    while True:
        highest, maximum_tries = choose_difficulty()
        tries_used = play_round(highest, maximum_tries)
        if tries_used is not None:
            if best_score is None or tries_used < best_score:
                best_score = tries_used
            print(f"Best score = {best_score}")
        else:
            print("No best score yet!")
        if not ask_play_again():
            print("Good bye! see you again")
            break


def ask_play_again():
    while True:
        answer = input("want to play again? (y/n) ").strip().lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        print("please type y/n.")


def choose_difficulty():
    while True:
        text = input("choose difficulty easy/medium/hard: ").strip().lower()
        if text == "easy":
            return 50, 10
        elif text == "medium":
            return 100, 7
        elif text == "hard":
            return 500, 9
        else:
            print("please enter a valid difficulty!")


def get_guess(highest):
    while True:
        text = input("guess a number: ")
        if not text.strip().isdigit():
            print("please enter a whole number!")
            continue
        guess = int(text)
        if not 1 <= guess <= highest:
            print(f"number not between 1 and {highest}")
            continue
        return guess


def play_round(highest, maximum_tries):
    tries_left = maximum_tries
    secret = random.randint(1, highest)
    while tries_left:
        tries_left -= 1
        guess = get_guess(highest)
        if guess == secret:
            print("Correct!")
            return maximum_tries - tries_left
        elif tries_left == 0:
            print(f"You lose! The number was {secret}")
            return None
        elif guess < secret:
            print(f"Too low, {tries_left} {'try' if tries_left == 1 else 'tries'} left")
        else:
            print(f"Too high, {tries_left} {'try' if tries_left == 1 else 'tries'} left")

main()

