# On the first line, you will receive a sequence of numbers separated by a single space.
# On the second line, you will receive a string.
# Each char the program adds to the message should be found by its index.
# The index you are looking for is the sum of a number('s digits from the first sequence.
# If the index is greater than the length of the text, continue counting from the beginning
# (so that you always have a valid index). When you find a char, you should add it to the message and remove it
# from the string. It means that for the following index, the text will contain one character less.)

nums_list = [int(char) for char in input().split()]
text = input()
indexes_list = []
result = []

for num in nums_list:
    small_list = list(str(num))
    index = sum([int(el) for el in small_list])
    # print(current_index)
    indexes_list.append(index)

for ind in indexes_list:
    index_to_use = ind % len(text)
    letter = text[index_to_use]
    result.append(letter)
    text = text[:index_to_use] + text[index_to_use + 1:]

print("".join(result))
