def get_amount():
    while True:
        try:
            amount = float(input("Amount: ").strip())
            if amount < 0:
                raise ValueError("please enter a positive amount!")
            return amount
        except ValueError:
            print("please enter a valid number")

a = get_amount()
print(a)