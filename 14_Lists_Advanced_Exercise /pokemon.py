sequence = [int(number) for number in input().split()]
removed_num_total = 0
while len(sequence) != 0:
    index = len(sequence) - 1
    command = int(input())
    if command < 0:
        removed_num = sequence.pop(0)
        sequence.insert(0, sequence[-1])
    elif command > index:
        removed_num = sequence.pop(-1)
        sequence.insert(index+1, sequence[0])
    else:
        removed_num = sequence.pop(command)
    for index_place, value in enumerate(sequence):
        if value <= removed_num:
            sequence[index_place] += removed_num
        else:
            sequence[index_place] -= removed_num
    removed_num_total += removed_num

print(removed_num_total)
