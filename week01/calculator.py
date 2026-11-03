def main():
    while True:
        choice = menu()
        if choice == "q":
            print("good bye!")
            break
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))
        if choice == "/" and second == 0:
            print("cant be divided by 0")
            continue
        elif choice == "+":
            answer = add(first, second)
        elif choice == "-":
            answer = subtract(first, second)
        elif choice == "*":
            answer = multiply(first, second)
        elif choice == "/":
            answer = divide(first, second)
        elif choice == "**":
            answer = power(first, second)
        print(f"{answer:.2f}")


def menu():
    while True:
        text = input("1) add  2) subtract  3) multiply  4) divide  5) power  q) quit: ").strip().lower()
        if text == "1":
            return "+"
        elif text == "2":
            return "-"
        elif text == "3":
            return "*"
        elif text == "4":
            return "/"
        elif text == "5":
            return "**"
        elif text == "q":
            return "q"
        else:
            print("please enter a valid menu choice!")

def add(first, second):
    return first + second

def subtract(first, second):
    return first - second

def multiply(first, second):
    return first * second

def divide(first, second):
    return first / second

def power(first, second):
    return first ** second

main()
