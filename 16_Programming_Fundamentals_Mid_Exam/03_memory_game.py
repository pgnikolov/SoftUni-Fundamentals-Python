# On the first line, you will receive a sequence of elements. Each element in the sequence will have a twin.
# Until the player receives "end" from the console, you will receive strings with two integers separated by a space,
# representing the indexes of elements in the sequence.

elements = input().split(" ")
moves = 0

while True:
    command = input()
    if command == "end":
        break

    first_index, second_index = [int(x) for x in command.split()]
    moves += 1

    if first_index == second_index or not 0 <= first_index < len(elements) or not 0 <= second_index < len(elements):
        half_len = int(len(elements)/2)
        el_insert = f"-{moves}a"
        elements = elements[:half_len] + [el_insert, el_insert] + elements[half_len:]
        print("Invalid input! Adding additional elements to the board")
    elif elements[first_index] == elements[second_index]:
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")
        if second_index > first_index:
            elements.pop(second_index)
            elements.pop(first_index)
        else:
            elements.pop(first_index)
            elements.pop(second_index)
    else:
        print("Try again!")

    if not elements:
        break

if command == "end":
    final = " ".join(elements)
    print(f"Sorry you lose :(\n{final}")

if len(elements) == 0:
    print(f"You have won in {moves} turns!")
