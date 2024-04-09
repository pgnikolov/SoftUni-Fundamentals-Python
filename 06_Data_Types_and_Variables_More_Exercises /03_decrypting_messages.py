# On the first line, you will receive a key (integer)
# On the second line, you will receive n – the number of lines, which will follow.
# On the next n lines – you will receive a lower and an uppercase letter per line.
# You should add the key to each of the characters and append them to a message.
# In the end, print the decrypted message.

key = int(input())
number_of_lines = int(input())
result = []

for _ in range(number_of_lines):
    char = input()
    result.append(chr(ord(char) + key))

print(''.join(result))

