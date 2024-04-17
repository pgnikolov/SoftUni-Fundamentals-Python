# On the first line, you will receive words separated by a single space. On the second line,
# you will receive a palindrome. First, you should print a list containing all the found palindromes in the sequence.
# Then, you should print the number of occurrences of the given palindrome in
# the format: "Found palindrome {number} times".

words = input()
palindrome = input()

list_words = words.split(" ")
result_1 = [char for char in list_words if char == char[::-1]]
print(result_1)
print(f"Found palindrome {list_words.count(palindrome)} times")
