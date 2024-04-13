# Write a function that receives two characters and returns a single string with all the characters in between them
# (according to the ASCII code), separated by a single space. Print the result on the console.

def ascii_finder(first, second):
    chars = " ".join([chr(i) for i in range(ord(first) + 1, ord(second))])
    return chars


sym1 = input()
sym2 = input()

print(ascii_finder(sym1, sym2))
