final_item_price = 0
number_of_items = int(input("How many items are you buying?: "))

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("How many items are you buying?: "))

for i in range(1, number_of_items + 1):
    item_price = float(input("What is the price of the item?: "))
    final_item_price += item_price

if final_item_price > 100:
    final_item_price = final_item_price - (final_item_price * 0.1)

print(f"You bought {number_of_items} and the total cost is ${final_item_price:.2f}")
