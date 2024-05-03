population = [int(num) for num in input().split(", ")]
min_money = int(input())

if sum(population) / len(population) < min_money:
    print("No equal distribution possible")
else:
    while min(population) != min_money:
        max_value = max(population)
        max_value_index = population.index(max_value)
        min_value = min(population)
        min_value_index = population.index(min_value)
        population[max_value_index] -= 1
        population[min_value_index] += 1
    print(population)
