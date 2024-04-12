# Write a function that calculates the total price of an order and returns it.
# The function receive one of the products: "coffee", "coke", "water", or "snacks", and a quantity of the product.
# The prices for a single piece of each product are:
#     • coffee - 1.50
#     • water - 1.00
#     • coke - 1.40
#     • snacks - 2.00
# Print the result formatted to the second decimal place.

def order_sum(quantity, price):
    return quantity * price


prices = {
    "coffee": 1.50,
    "water": 1.00,
    "coke": 1.40,
    "snacks": 2.00
}

product = input()
quantity = int(input())

print(f"{order_sum(quantity, prices[product]):.2f}")
