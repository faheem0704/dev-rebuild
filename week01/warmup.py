import math


def main():
    number = int(input("enter a number for fizzbuzz: "))
    print(fizzbuzz(number))
    num = int(input("enter a number to check prime: "))
    if is_prime(num):
        print("the number is prime!")
    else:
        print("not prime!")
    text = input("enter a string to compress: ")
    print(compress(text))


def fizzbuzz(x):
    results = []
    for i in range(1, x + 1):
        if i % 15 == 0:
            results.append("FizzBuzz")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(i))
    return results


def is_prime(x):
    if x < 2:
        return False
    for divisor in range(2, math.isqrt(x) + 1):
        if x % divisor == 0:
            return False
    return True


def compress(text):
    if text == "":
        return ""
    result = ""
    current = text[0]
    run_length = 0
    for char in text:
        if char == current:
            run_length += 1
        else:
            result += f"{current}{run_length}"
            current = char
            run_length = 1
    result += f"{current}{run_length}"
    return result

main()
