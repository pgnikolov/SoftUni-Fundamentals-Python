# Let us take the string "skipTest_String044160" as an example.
# Take every digit from the string and transfer it somewhere. After this operation,
# you should have two lists of items - a numbers list and a non-numbers list:
#     • Numbers' list: [0, 4, 4, 1, 6, 0]
#     • Non-numbers: [s, k, i, p, T, e, s, t, _, S, t, r, i, n, g]
# After that, take every digit in the numbers list and split it up into a take list and a skip list.
# In the take list, you should keep all digits at an even index.
# In the skip list, you should keep all digits at an odd index.
#     • Numbers' list: [0, 4, 4, 1, 6, 0]
#     • Take list: [0, 4, 6]
#     • Skip list: [4, 1, 0]
# Afterward, iterate over both lists:
#     • First, take m characters from the non-numbers list and store it in a result string
#     • Then, skip n characters from the non-numbers list
# Note that the skipped characters are summed up as they go. The process would look like this:
#     1. Current string: "skipTest_String". Take 0 characters and skip 4 characters:
#     • Taken string: ""
#     • Skipped string: "skip"
#     2. The remaining string looks like this: "Test_String". Take 4 characters and skip 1 character:
#         ◦ Taken string: "Test"
#         ◦ Skipped string: "_"
#     3. The string looks like this: "String". Take 6 characters and skip 0 characters:
#         ◦ Taken string: "String"
#         ◦ Skipped string: ""
#     4. The final string is "TestString".
# After that, print the final string on the console.

hidden_msg = [char for char in input()]

num_list = [int(char) for char in hidden_msg if char.isdigit()]

non_num = [char for char in hidden_msg if not char.isdigit()]

take_list = [num_list[i] for i in range(len(num_list)) if i % 2 == 0]
skip_list = [num_list[i] for i in range(len(num_list)) if i % 2 != 0]

final_msg = []
for index in range(len(take_list)):
    for i in range(take_list[index]):
        if len(non_num) > 0:
            final_msg.append(non_num[0])
            non_num.pop(0)
    if non_num:
        for j in range(skip_list[index]):
            non_num.pop(0)

print("".join(final_msg))
