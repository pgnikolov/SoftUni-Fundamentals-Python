# You will be given two strings. Transform the first string into the second one, letter by letter,
# starting from the first one. After each interaction, print the resulting string only if it is unique.
# Note: the strings will have the same length.

string1 = input()
string2 = input()


seen = {string1}
result = string1

for i in range(len(string1)):
    new_string = result[:i] + string2[i] + result[i+1:]
    if new_string not in seen:
        print(new_string)
        seen.add(new_string)
        result = new_string


