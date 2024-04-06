# # Given a string, calculate how many times the words "Sand", "Water", "Fish", and "Sun" appear (case-insensitive).

words = ["Sand", "Water", "Fish", "Sun"]
# Convert input string to lowercase for case-insensitive matching
string_input = input().lower()

counter = 0

# Iterate over each word in the words list
for word in words:
    # Count the occurrences of the current word in the input string
    count = string_input.count(word.lower())
    counter += count

print(counter)
