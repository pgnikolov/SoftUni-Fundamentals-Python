# You will be given two sequences of strings, separated by ", ". Print a new list containing only the strings
# from the first input line, which are substrings of any string in the second input line.

list1 = input().split(", ")
list2 = input().split(", ")

result_list = [subs for word in list2 for subs in list1 if subs in word]

print(sorted(set(result_list), key=list1.index))
