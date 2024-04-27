# You will be given key-value pairs of products and quantities (on a single line separated by space).
# On the following line, you will be given products to search for. Check for each product. You have 2 possibilities:
#     • If you have the product, print "We have {quantity} of {product} left".
#     • Otherwise, print "Sorry, we don't have {product}".

in_stock = input().split(" ")
wanted_items = input().split(" ")

keys = [in_stock[i] for i in range(len(in_stock)) if i % 2 == 0]
values = [int(in_stock[j]) for j in range(len(in_stock)) if j % 2 != 0]

bakery = dict(zip(keys, values))

for item in wanted_items:
    if item in bakery:
        print(f"We have {bakery[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
