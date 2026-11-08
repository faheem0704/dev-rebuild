def main():
    expenses = []

    while True:
        choice = menu()

        if choice == "q":
            print("Goodbye!")
            break

        elif choice == "add":
            expenses.append(add_expense())
            print("Added!")

        elif choice == "list":
            print(list_expenses(expenses))

        elif choice == "total":
            totals = total_by_category(expenses)
            print(show_totals(totals))

        elif choice == "biggest":
            print(show_biggest_expenses(expenses))


def show_totals(totals):
    if not totals:
        return "No expenses yet."

    result = ""
    total = 0

    for category, amount in totals.items():
        total += amount
        result += f"{category:<20}{amount:>10.2f}\n"

    result += "-" * 30 + "\n"
    result += f"{'Total':<20}{total:>10.2f}"

    return result


def show_biggest_expenses(expenses):
    biggest = biggest_expense(expenses)

    if biggest is None:
        return "No expenses yet."

    return (
        f"Biggest expense: {biggest['description']} "
        f"({biggest['amount']:.2f}, {biggest['category']})"
    )


def list_expenses(expenses):
    if not expenses:
        return "No expenses yet."

    result = f"{'Description':<20}{'Amount':>10}  Category\n"
    result += "-" * 45 + "\n"

    for expense in expenses:
        description = expense["description"]
        category = expense["category"]
        amount = expense["amount"]

        result += f"{description:<20}{amount:>10.2f}  {category}\n"

    return result


def biggest_expense(expenses):
    if not expenses:
        return None

    biggest = max(expenses, key=lambda expense: expense["amount"])

    return biggest


def total_by_category(expenses):
    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        totals[category] = totals.get(category, 0) + amount

    return totals


def get_amount():
    while True:
        try:
            amount = float(input("Amount: "))

        except ValueError:
            print("Please enter a valid number.")
            continue

        if amount <= 0:
            print("Please enter a positive number!")
            continue

        return amount


def get_text(prompt):
    while True:
        text = input(f"{prompt}: ").strip()

        if not text:
            print(f"Enter a {prompt}!")
            continue

        return text


def add_expense():
    description = get_text("Description")
    amount = get_amount()
    category = get_text("Category").lower()

    return {
        "description": description,
        "amount": amount,
        "category": category
    }


def menu():
    while True:
        text = input(
            "1) Add expense   "
            "2) List expenses   "
            "3) Totals by category   "
            "4) Biggest expense   "
            "q) Quit "
        ).lower().strip()

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
            print("Please enter a valid menu choice!")


main()