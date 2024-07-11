start_char = input()
end_char = input()
random_string = input()

print(sum([ord(char) for char in random_string if ord(start_char) < ord(char) < ord(end_char)]))
