import random

secret = random.randint(1, 100)
print(secret)         #DEBUG: remove later
tries_left = 3
while tries_left:
    guess = int(input("guess a number: "))
    tries_left -= 1
    if guess == secret:
        print("Correct!")
        break
    elif tries_left == 0:
        print(f"You lose! The number was {secret}")
    elif guess < secret:
        print(f"Too low, {tries_left} tries left")
    else:
        print(f"Too high, {tries_left} tries left")