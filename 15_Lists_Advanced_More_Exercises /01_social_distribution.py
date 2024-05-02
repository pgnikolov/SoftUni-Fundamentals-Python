# On the first line, you will be given the population (numbers separated by comma and space ", ").
# On the second line, you will be given the minimum wealth. You should distribute the wealth so that no part
# of the population has less than the minimum wealth. To do that, you should always take wealth
# from the wealthiest part of the population.
# There will be cases where the distribution will not be possible.
# In that case, print: "No equal distribution possible".

population = [int(char) for char in input().split(", ")]

min_wealth = int(input())

needed_wealth = 0
available_wealth = 0

for i in population:
    if i < min_wealth:
        needed_wealth += min_wealth - i
    elif i > min_wealth:
        available_wealth += i - min_wealth


if needed_wealth > available_wealth:
    print("No equal distribution possible")
else:
    max_index = population.index(max(population))
    for j in range(len(population)):
        max_index = population.index(max(population))
        if population[j] < min_wealth < population[max_index]:
            population[max_index] -= (min_wealth - population[j])
            population[j] += (min_wealth - population[j])
    print(population)
