budget = int(input())

not_end = True
total_price = 0

while not_end:
    command = input()
    if command != "End":
        price = int(command)
        total_price += price
        if total_price > budget:
            print("You went in overdraft!")
            break
    else:
        not_end = False
        print('You bought everything needed.')

