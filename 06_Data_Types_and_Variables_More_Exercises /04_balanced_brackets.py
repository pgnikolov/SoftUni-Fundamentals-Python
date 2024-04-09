# On the first line, you will receive n – the number of lines, which will follow.
# On the following n lines, you will receive one of the following:
#     • Opening bracket – "(",
#     • Closing bracket – ")" or
#     • Random string
# Your task is to find out if the brackets are balanced. after every opening bracket should follow a closing one
# Nested parentheses are not valid, and if, for example, two consecutive opening brackets exist,
# the expression should be marked as unbalanced.
# You should print "BALANCED" if the parentheses are balanced and "UNBALANCED" otherwise.

number_of_lines = int(input())
list_of_brackets = []
is_balanced = True

for _ in range(number_of_lines):
    string = input()
    if string == "(" or string == ")":
        list_of_brackets.append(string)

for index in range(len(list_of_brackets)):
    if index % 2 == 0 and not list_of_brackets[index] == "(":
        is_balanced = False
    elif not index % 2 == 0 and not list_of_brackets[index] == ")":
        is_balanced = False

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
