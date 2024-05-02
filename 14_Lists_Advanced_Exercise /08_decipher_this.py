# You are given a secret message you should decipher. To do that, you need to know that in each word:
#     • the second and the last letter are switched (e.g., Holle means Hello)
#     • the first letter is replaced by its character code (e.g., 72 means H)

secret_message_list = input().split()
decrypted_message_list = []

for word in secret_message_list:
    digits = [char for char in word if char.isnumeric()]
    code = int("".join(digits))
    first_letter = chr(code)
    word = [char for char in word if char not in digits]
    word[0], word[-1] = word[-1], word[0]
    final_word = "".join(list(first_letter) + word)
    decrypted_message_list.append(final_word)
print(*decrypted_message_list, sep=" ")
