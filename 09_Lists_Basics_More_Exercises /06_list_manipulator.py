# The list may be manipulated by one of the following commands:
#     • "exchange {index}" – splits the list after the given index and exchanges the places of the
#     two resulting sub-lists. E.g., [1, 2, 3, 4, 5] -> "exchange 2" -> result: [4, 5, 1, 2, 3]
#         ◦ If the index is outside the boundaries of the list, print "Invalid index"
#         ◦ A negative index is considered invalid
#     • "max even/odd"– returns the INDEX of the max even/odd element. E.g., [1, 4, 8, 2, 3] -> "max odd" -> print: 4
#     • "min even/odd" – returns the INDEX of the min even/odd element. E.g. [1, 4, 8, 2, 3] -> "min even" -> print: 3
#         ◦ If there are two or more equal min/max elements, return the index of the rightmost one
#         ◦ If a min/max even/odd element cannot be found, print "No matches"
#     • "first {count} even/odd"–returns  first count even/odd elements.[1, 8, 2, 3] -> "first 2 even" -> print [8, 2]
#     • "last {count} even/odd"–returns the last count even/odd elements.[1, 8, 2, 3] -> "last 2 odd" -> print [1, 3]
#         ◦ If the count is greater than the list length, print "Invalid count"
#         ◦ If there are not enough elements to satisfy the count, print as many as you can.
#         If there are zero even/odd elements, print an empty list "[]"
#     • "end" - stop taking input and print the final state of the list

list_of_numbers = list(input().split())

while True:
    command = input().split()

    if command[0] == "end":
        break

    elif command[0] == "exchange":
        if int(command[1]) >= len(list_of_numbers) or int(command[1]) < 0:
            print("Invalid index")
        else:
            working_list_a = list_of_numbers[:int(command[1]) + 1]
            working_list_b = list_of_numbers[int(command[1]) + 1:]
            list_of_numbers = working_list_b + working_list_a

    elif command[0] == "max":
        working_list_a = sorted(list_of_numbers, key=int)
        working_value_a = "No matches"
        if command[1] == "even":
            for number in list(reversed(working_list_a)):
                if int(number) % 2 == 0:
                    working_value_a = number
                    break
        elif command[1] == "odd":
            for number in list(reversed(working_list_a)):
                if int(number) % 2 == 1 :
                    working_value_a = number
                    break

        if working_value_a != "No matches":
            counter = int(len(list_of_numbers))
            for min_max_even_number in list(reversed(list_of_numbers)):
                counter -= 1
                if min_max_even_number == working_value_a:
                    print(counter)
                    break
        else:
            print(working_value_a)

    elif command[0] == "min":
        working_list_a = sorted(list_of_numbers, key=int)
        working_value_a = "No matches"
        if len(list_of_numbers) < 1:
            print(working_value_a)
            continue
        elif command[1] == "even":
            for number in working_list_a:
                if int(number) % 2 == 0:
                    working_value_a = number
                    break
        elif command[1] == "odd":
            for number in working_list_a:
                if int(number) % 2 == 1 :
                    working_value_a = number
                    break
        if working_value_a != "No matches":
            counter = int(len(list_of_numbers))
            for min_max_even_number in list(reversed(list_of_numbers)):
                counter -= 1
                if min_max_even_number == working_value_a:
                    print(counter)
                    break
        else:
            print(working_value_a)
            working_value_a = 0

    elif command[0] == "first":
        working_list_a = []
        if len(list_of_numbers) < 1 or int(command[1]) > len(list_of_numbers):
            print("Invalid count")
            continue
        elif command[2] == "even":
            for number in list_of_numbers:
                if int(number) % 2 == 0:
                    if len(working_list_a) == int(command[1]):
                        break
                    else:
                        working_list_a.append(number)
        elif command[2] == "odd":
            for number in list_of_numbers:
                if int(number) % 2 == 1:
                    if len(working_list_a) == int(command[1]):
                        break
                    else:
                        working_list_a.append(number)
        print("[", end="")
        print(*working_list_a, sep=", ", end="")
        print("]")

    elif command[0] == "last":
        working_list_a = []
        if len(list_of_numbers) < 1 or int(command[1]) > len(list_of_numbers):
            print("Invalid count")
            continue
        elif command[2] == "even":
            for number in list(reversed(list_of_numbers)):
                if int(number) % 2 == 0:
                    if len(working_list_a) == int(command[1]):
                        break
                    else:
                        working_list_a.append(number)
        elif command[2] == "odd":
            for number in list(reversed(list_of_numbers)):
                if int(number) % 2 == 1:
                    if len(working_list_a) == int(command[1]):
                        break
                    else:
                        working_list_a.append(number)
        working_list_b = list(reversed(working_list_a))
        print("[", end="")
        print(*working_list_b, sep=", ", end="")
        print("]")

print("[", end="")
print(*list_of_numbers, sep=", ", end="")
print("]")