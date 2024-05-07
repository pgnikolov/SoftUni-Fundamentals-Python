# You are now to create a program that prints a Josephus permutation, receiving two lines of code:
#     • the list itself - numbers separated by a single space representing the people in the circle
#     • a number k
# People are standing in circle waiting to be executed. Counting begins from the first one
# in the circle and proceeds from left to right. After a specified number of people are skipped,
# the k person is executed. The procedure is repeated with the remaining people, starting with the next person,
# going in the same direction, and skipping the same number of people until no one remains.
# Print the people by order of executions in the format: "[{executed1},{executed2}, … {executedN}]"


people = [int(char) for char in input().split()]
k = int(input())
result = []
people_worklist = people.copy()

for _ in range(len(people)):
    k_to_use = k
    while k_to_use > len(people_worklist):
        k_to_use -= len(people_worklist)
    else:
        result.append(people_worklist[k_to_use - 1])
        people_worklist.pop(k_to_use - 1)
        right = people_worklist[:k_to_use - 1]
        left = people_worklist[k_to_use - 1:]
        people_worklist = left + right

result = [str(el) for el in result]
print(f"[{','.join(result)}]")
