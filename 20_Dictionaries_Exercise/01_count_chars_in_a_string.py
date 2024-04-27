# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"
letter_list = [char for char in input() if char != ' ']

letters_dict = {}

for char in letter_list:
    if char not in letters_dict:
        letters_dict[char] = 0
    letters_dict[char] += 1

for k, v in letters_dict.items():
    print(f"{k} -> {v}")
