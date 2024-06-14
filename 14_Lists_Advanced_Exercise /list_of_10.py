list_of_numbers = input().split(", ")
all_lists = []
working_group = 0
working_list = list_of_numbers.copy()

while len(list_of_numbers) >= 1:
    working_group += 10
    all_lists.append([])
    for index_number in range(len(list_of_numbers)):
        int_number = int(list_of_numbers[index_number])
        if working_group - 10 < int_number <= working_group:
            all_lists[-1].append(int_number)
            working_list.remove(list_of_numbers[index_number])
    list_of_numbers = working_list.copy()

for group in range(len(all_lists)):
    print(f"Group of {(group+1) * 10}'s: {all_lists[group]}")
