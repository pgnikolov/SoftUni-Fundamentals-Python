def insert_space(msg, place):
    msg = msg[:place] + " " + msg[place:]
    return msg


def reverse_string(msg, substring):
    if substring in msg:
        msg = msg.replace(substring, substring[::-1], 1)
        return msg


def change_all(msg, substring, replacement):
    if substring in msg:
        msg = msg.replace(substring, replacement)
        return msg


concealed_message = input()

while True:
    command = input()
    if command == 'Reveal':
        break

    info = command.split(':|:')
    if info[0] == 'InsertSpace':
        concealed_message = insert_space(concealed_message, int(info[1]))
        print(concealed_message)
    elif info[0] == 'Reverse':
        if info[1] in concealed_message:
            concealed_message = reverse_string(concealed_message, info[1])
            print(concealed_message)
        else:
            print('error')
    elif info[0] == 'ChangeAll':
        concealed_message = change_all(concealed_message, info[1], info[2])
        print(concealed_message)

print(f'You have a new text message: {concealed_message}')
