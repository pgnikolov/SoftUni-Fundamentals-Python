# On the first line, you receive n. On the second line, you will receive a word. On the following n lines,
# you will be given some strings. You should add them to a list and print them.
# After that, you should filter out only the strings that include the given word and print that list too.

number = int(input())
word = input()
all_strings = []
filtered_strings = []

for _ in range(1, number + 1):
    current_string = input()
    all_strings.append(current_string)
print(all_strings)

for i in range(len(all_strings)):
    if word in all_strings[i]:
        filtered_strings.append(all_strings[i])
print(filtered_strings)
