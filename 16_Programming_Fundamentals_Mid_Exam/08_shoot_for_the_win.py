# Write a program that helps you keep track of your shot targets. You will receive a sequence with integers,
# separated by a single space, representing targets and their value. Afterward, you will be receiving indices until
# the "End" command is given, and you need to print the targets and the count of shot targets.
# Every time you receive an index, you need to shoot the target on that index, if it is possible.
# Every time you shoot a target, its value becomes -1, and it is considered a shot. Along with that, you also need to:
#     • Reduce all the other targets, which have greater values than your current target, with its value.
#     • Increase all the other targets, which have less than or equal value to the shot target, with its value.
# Keep in mind that you can't shoot a target, which is already shot.
# You also can't increase or reduce a target, which is considered a shot.
# When you receive "End" command, print targets in their current state and count of shot targets in following format:
# "Shot targets: {count} -> {target1} {target2}… {targetn}"

targets = [int(char) for char in input().split()]
shoots = 0
command = input()

while command != "End":
    trg_ind = int(command)
    if trg_ind <= len(targets) - 1 and targets[trg_ind] != -1:
        value_to_use = targets[trg_ind]
        shoots += 1

        for i in range(len(targets)):
            if i == trg_ind:
                continue
            elif targets[i] > value_to_use:
                targets[i] -= value_to_use
            elif targets[i] <= value_to_use and targets[i] != -1:
                targets[i] += value_to_use

        targets[trg_ind] = -1
    else:
        pass

    command = input()

result = [str(char) for char in targets]

print(f'Shot targets: {shoots} -> {" ".join(result)}')

