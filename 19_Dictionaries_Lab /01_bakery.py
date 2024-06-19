# You will receive a single line containing some food (keys) and quantities (values).
# They will be separated by a single space (the first element is the key, the second – is the value, and so on).
# Create a dictionary with all the keys and values and print it on the console.gdfgdfgdf

food_values = input().split(" ")


keys = [food_values[i] for i in range(len(food_values)) if i % 2 == 0]
values = [int(food_values[j]) for j in range(len(food_values)) if j % 2 != 0]

bakery = dict(zip(keys, values))


print(bakery)
