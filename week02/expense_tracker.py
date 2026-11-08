def main():
    expense = []
    while True:
        choice = menu()
        if choice == "q":
            print("good bye!")
            break
        if choice == "add":
            expense.append(add_expense())
            print("Added!")
        if choice == "list":
            print(expense)


def list_expense():
    pass

def add_expense():
    description = input("Description: ")
    amount = input("Amount: ")
    category = input("Category: ")
    return {"description": description, "amount": amount, "category": category}


def menu():
    while True:
        text = input("1) Add expense   2) List expenses   3) Totals by category   4) Biggest expense   q) Quit ").lower().strip()
        if text == "1":
            return "add"
        elif text == "2":
            return "list"
        elif text == "3":
            return "total"
        elif text == "4":
            return "biggest"
        elif text == "q":
            return "q"
        else:
            print("please enter a valid menu choice!")

main()