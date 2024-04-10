# You receive 2 lines input. On first line, you receive a string of integers, separated by a comma and a space ", ".
# On second line, you will receive a count of beggars. Your job is to print a list with the
# sum of what each beggar brings home, assuming they all take regular turns, from the first to last number in the list.
# For example, [1, 2, 3, 4, 5] for 2 beggars will return a result of 9 and 6, as the first one takes [1, 3, 5],
# second one collects [2, 4]. same list with 3 beggars produce a  5, 7, and 3, they take [1, 4], [2, 5], and [3].
# Also, note that not all beggars have to take the same amount of "offers", meaning that the length of the list is
# not necessarily a multiple of n. The list length could be even shorter - i.e., the last beggars will take nothing (0).

sum_list = list()
beg_sum = 0

num_list = [int(num) for num in input().split(", ")]
beggars = int(input())


for beggar in range(1, beggars + 1):
    for i in range(beggar - 1, len(num_list), beggars):
        beg_sum += num_list[i]
    sum_list.append(beg_sum)
    beg_sum = 0

print(sum_list)
