
menu = {
    "pizza": 50,
    "salad": 30,
    "burger": 100,
    "pop corn": 150,
    "chicken puff": 100
}

print("Welcome to Coders Cafe!")
print("\n----- MENU -----")

for item, price in menu.items():
    print(f"{item.title()}: Rs.{price}")

order_total = 0

while True:
    order_item = input("\nEnter your item: ").strip().lower()

    if order_item not in menu:
        print("Sorry, wrong item! Please choose from the menu.")
        continue

    order_total += menu[order_item]
    print(f"{order_item.title()} added to your order.")

    another_order = input(
        "Do you want anything else? (Yes/No): "
    ).strip().lower()

    if another_order in ("no", "n"):
        break
    elif another_order not in ("yes", "y"):
        print("Please enter Yes or No.")
        break

print("\n----- BILL -----")
print(f"Your total order value is: Rs.{order_total}")
print("Thank you for visiting Coders Cafe!")
