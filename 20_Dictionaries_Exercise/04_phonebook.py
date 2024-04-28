# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-".
# If you receive a name that already exists in the phonebook, update its number.
# After filling out the phonebook, you will receive a number – N.
# Your program should be able to perform a search of contact by name and print its details in the format:
# "{name} -> {number}". In case the contact isn't found, print: "Contact {name} does not exist."

command = input()

phonebook = {}

while "-" in command:
    person_info = command.split("-")
    phonebook[person_info[0]] = person_info[1]
    command = input()

for i in range(int(command)):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
