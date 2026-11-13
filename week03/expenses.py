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