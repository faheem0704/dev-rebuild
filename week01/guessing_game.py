import random
secret = random.randint(1, 100)
while True:
    guess = int(input("guess a number: "))
    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")




"""import random

def main():
    while True:
        difficulty = input("Pick a difficulty: easy (1–50, 10 tries), medium (1–100, 7 tries), hard (1–500, 9 tries)").lower()
        number_of_tries = 0
        upto = 0
        if difficulty == "easy":
            number_of_tries = 10
                upto = 50
        elif difficulty == "medium":
            number_of_tries = 7
                upto = 100
        elif difficulty == "hard":
            number_of_tries = 9
            upto = 500
        number = random.randint(1, upto)
        print(guess(number, number_of_tries))
        play_again = input("play again? (y/n)").lower()
        if play_again == "n":
            break


def guess(number, number_of_tries, guessed_number):
    while number_of_tries:
        guessed_number = int(input("guess a number: "))
        if guessed_number == number:
            print("Correct!")
        else:
            number_of_tries -= 1
            if guessed_number < number:
                print(f"Too low, {number_of_tries} tries left")
            else:
                print(f"Too high, {number_of_tries} tries left")


main()"""