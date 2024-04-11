# you are going to receive the gifts you plan on buying on a single line, separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
#     • "OutOfStock {gift}"
#         ◦ Find the gifts with this name in your collection, if any, and change their values to "None".
#     • "Required {gift} {index}"
#         ◦ If the index is valid, replace the gift on the given index with the given gift.
#     • "JustInCase {gift}"
#         ◦ Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with the value "None",
# separated by a single space in the following format:
# "{gift1} {gift2} {gift3} … {giftn}"

gifts = input().split(" ")
commands = ['OutOfStock', 'Required', 'JustInCase', 'No Money']
not_finished = True

while not_finished:
    command = input()
    if command != "No Money":
        command_atr = command.split(" ")
        if command_atr[0] == 'OutOfStock':
            gifts = ["None" if item == command_atr[1] in gifts else item for item in gifts]
        elif command_atr[0] == "Required":
            index = int(command_atr[2])
            if (len(gifts) - 1) >= index:
                gifts[index] = command_atr[1]
            else:
                continue
        elif command_atr[0] == "JustInCase":
            gifts[-1] = command_atr[1]
    elif command == "No Money":
        not_finished = False

for word in gifts:
    if word == "None":
        gifts.remove("None")

gifts_str = " ".join(gifts)
print(gifts_str)
