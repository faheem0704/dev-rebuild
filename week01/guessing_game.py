import random

secret = random.randint(1, 100)
print(secret)         #DEBUG: remove later
tries_left = 3
while tries_left:
    text = input("guess a number: ")
    if not text.strip().isdigit():
        print("please enter a whole number!")
        continue
    guess = int(text)
    if not 1 <= guess <= 100:
        print("number not between 1 and 100")
        continue
    tries_left -= 1
    if guess == secret:
        print("Correct!")
        break
    elif tries_left == 0:
        print(f"You lose! The number was {secret}")
    elif guess < secret:
        print(f"Too low, {tries_left} {'try' if tries_left == 1 else 'tries'} left")
    else:
        print(f"Too high, {tries_left} {'try' if tries_left == 1 else 'tries'} left")