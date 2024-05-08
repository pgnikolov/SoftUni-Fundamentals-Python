# You are given an array with integers. Write a program to modify the elements after receiving the following commands:
#     • "swap {index1} {index2}" takes two elements and swap their places.
#     • "multiply {index1} {index2}" takes element at the 1st index and multiply it with the element at 2nd index.
#     Save the product at the 1st index.
#     • "decrease" decreases all elements in the array with 1.

array_ints = [int(char) for char in input().split()]

command = input()

while command != "end":
    command_components = command.split()
    action = command_components[0]
    if action == "decrease":
        array_ints = [int(char) - 1 for char in array_ints]
    elif action == "swap":
        indx1 = int(command_components[1])
        indx2 = int(command_components[2])
        array_ints[indx1], array_ints[indx2] = array_ints[indx2], array_ints[indx1]
    elif action == "multiply":
        indx1 = int(command_components[1])
        indx2 = int(command_components[2])
        array_ints[indx1] = array_ints[indx1] * array_ints[indx2]
    command = input()

result = [str(char) for char in array_ints]
print(", ".join(result))
