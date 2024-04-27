food_values = input().split(" ")


keys = [food_values[i] for i in range(len(food_values)) if i % 2 == 0]
values = [int(food_values[j]) for j in range(len(food_values)) if j % 2 != 0]

bakery = dict(zip(keys, values))


print(bakery)
