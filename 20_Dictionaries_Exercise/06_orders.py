# Write a program that keeps the information about products and their prices.
# Each product has a name, a price, and a quantity:
#     • If the product doesn't exist yet, add it with its starting quantity.
#     • If you receive a product, that already exists, increase its quantity by the
#     input quantity and if its price is different, replace the price as well.
# You will receive products' names, prices, and quantities on new lines.
# Until you receive the command "buy", keep adding items.
# Finally, print all items with their names and the total price of each product.

products = {}

command = input()

while command != "buy":
    order = command.split(' ')
    product = order[0]
    price = float(order[1])
    qnt = int(order[2])
    if product not in products:
        products[product] = {"Price": 0.0, "Quantity": 0}
    products[product]["Price"] = price
    products[product]["Quantity"] += qnt
    command = input()

for k, v in products.items():
    print(f"{k} -> {v['Price'] * v['Quantity'] :.2f}")
