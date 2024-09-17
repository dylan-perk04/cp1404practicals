"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Please input your sales here: $"))

while sales >= 0:
    if sales < 1000:
        bonus = 0.10

    if sales >= 1000:
        bonus = 0.15

    total_bonus = sales * bonus
    print(f"Your total bonus is ${total_bonus}")
    sales = float(input("Please input your sales here: $"))
else:
    print("Thank you for using this service")
