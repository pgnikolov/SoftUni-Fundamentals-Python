# You will be given a sequence of strings, each on a new line until you receive the "stop" command.
# Every odd line on the console represents a resource (Gold, Silver, Copper, and so on) and every even - quantity.
# Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# "{resource} -> {quantity}"
# The quantities will be in the range [1 … 2 000 000 000].

command = input()

resources_dict = {}

while command != "stop":
    quantity = int(input())
    if command not in resources_dict:
        resources_dict[command] = 0
    resources_dict[command] += quantity
    command = input()

for k, v in resources_dict.items():
    print(f"{k} -> {v}")
