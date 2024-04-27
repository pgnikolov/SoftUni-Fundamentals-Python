# Write a program that prints all elements from a given sequence of words that occur
# an odd number of times (case-insensitive) in it.
#     • Words are given on a single line, space-separated.
#     • Print the result elements in lowercase, in their order of appearance.

words = [word.lower() for word in input().split(" ")]
words_dict = {}

for word in words:
    if word not in words_dict:
        words_dict[word] = 0
    words_dict[word] += 1

for k, v in words_dict.items():
    if v % 2 != 0:
        print(k, end=" ")
