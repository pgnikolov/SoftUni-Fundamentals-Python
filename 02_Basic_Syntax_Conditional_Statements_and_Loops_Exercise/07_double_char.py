# You will be given strings until you receive the command "End". For each string given, you should print a
# string in which each character (case-sensitive) is repeated twice. Note that if you receive the string
# "SoftUni", you should NOT print it!

not_end = True

while not_end:
    new_word = ""
    word = input()
    if word == "SoftUni":
        continue
    elif word == "End":
        not_end = False
        break
    else:
        for i in range(len(word)):
            new_word += 2 * word[i]
        print(new_word)
