# Write a program that takes a single string and prints a list of all the capital letters indices.
string_input = input()

string_list = list(string_input)
capital_indices = []

# if the current character (char) is an uppercase letter
# its index (i) is added to the capital_indices list.
for i, char in enumerate(string_list):
    if char.isupper():
        capital_indices.append(i)

print(capital_indices)
