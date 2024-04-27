# You will be receiving key-value pairs on separate lines separated by ": " until you receive the command "statistics".
# Sometimes you may receive a product more than once. In that case, you have to add new quantity to the existing one.
# When you receive the "statistics" command, print the following:
# "Products in stock:
# - {product1}: {quantity1}
# - {product2}: {quantity2}
# …
# - {productN}: {quantityN}
# Total Products: {count_all_products}
# Total Quantity: {sum_all_quantities}"

command = input()

products = {}

while command != "statistics":
    product_kv = command.split(": ")
    if product_kv[0] not in products:
        products[product_kv[0]] = int(product_kv[1])
    else:
        products[product_kv[0]] += int(product_kv[1])

    command = input()


print("Products in stock:")

for (i, q) in products.items():
    print(f"- {i}: {q}")

print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")
