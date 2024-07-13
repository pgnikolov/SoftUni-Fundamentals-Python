activation_key = input()

while True:
    command = input()
    if command == 'Generate':
        break

    info = command.split('>>>')

    if info[0] == 'Contains':
        if info[1] in activation_key:
            print(f"{activation_key} contains {info[1]}")
        else:
            print("Substring not found!")
    elif info[0] == 'Flip':
        substring = activation_key[int(info[2]):int(info[3])]
        if info[1] == "Upper":
            activation_key = activation_key.replace(substring, substring.upper())
        elif info[1] == "Lower":
            activation_key = activation_key.replace(substring, substring.lower())
        print(activation_key)
    elif info[0] == 'Slice':
        substring = activation_key[int(info[1]):int(info[2])]
        activation_key = activation_key.replace(substring, "")
        print(activation_key)

print(f"Your activation key is: {activation_key}")
