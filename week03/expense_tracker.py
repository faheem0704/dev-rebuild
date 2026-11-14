from storage import EXPENSES_FILE, load_expenses, save_expenses, HERE
from expenses import total_by_category, biggest_expense
import logging

def main():
    logging.basicConfig(filename=HERE / "tracker.log", level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s")
    logging.info("Program started")
    expenses = load_expenses(EXPENSES_FILE)

    while True:
        choice = menu()

        if choice == "q":
            print("Goodbye!")
            break

        elif choice == "add":
            expenses.append(add_expense())
            save_expenses(EXPENSES_FILE, expenses)
            print(f"Saved. You have {len(expenses)} expenses.")

        elif choice == "list":
            print(list_expenses(expenses))

        elif choice == "total":
            totals = total_by_category(expenses)
            print(show_totals(totals))

        elif choice == "biggest":
            print(show_biggest_expenses(expenses))
        elif choice == "delete":
            delete_expense(expenses)
            save_expenses(EXPENSES_FILE, expenses)
            print(f"Saved. You have {len(expenses)} expenses.")


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
    return f"Biggest expense: {biggest['description']} ({biggest['amount']:.2f}, {biggest['category']})"


def delete_expense(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    print(list_expenses(expenses))
    while True:
        try:
            number = int(input("enter the number of the list you want to delete: "))
        except ValueError:
            print("please enter a number, e.g. 3")
            continue
        if not 0 < number <= len(expenses):
            print(f"Please enter a number from 1 to {len(expenses)}")
            continue
        break
    index = number - 1
    removed = expenses.pop(index)
    print(f"Deleted: {removed['description']} ({removed['amount']:.2f})")
    logging.info("Deleted expense: %s", removed["description"])
    print(list_expenses(expenses))

def list_expenses(expenses):
    if not expenses:
        return "No expenses yet."

    result = f"{'#':>3}  {'Description':<20}{'Amount':>10}  Category\n"
    result += "-" * 45 + "\n"

    for number, expense in enumerate(expenses, start=1 ):
        description = expense["description"]
        category = expense["category"]
        amount = expense["amount"]

        result += f"{number:>3}  {description:<20}{amount:>10.2f}  {category}\n"

    return result


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
            "5) Delete expense   "
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

        elif text == "5":
            return "delete"

        elif text == "q":
            return "q"

        else:
            print("Please enter a valid menu choice!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")