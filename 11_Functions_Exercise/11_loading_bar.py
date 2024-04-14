# You receive single integer number between 0 and 100 (inclusive) divisible by 10 without remainder (0, 10, 20, 30...).
# Your task is to create a function that returns a loading bar depending on the number you have received in the input.
# Print the result on the console. For more clarification, see the examples below.

def loading_bar(num):
    num_dev_ten = num // 10
    loading_process = ['.'] * 10
    for index in range(num_dev_ten):
        loading_process[index] = "%"
    if num_dev_ten == 10:
        print('100% Complete!')
        print(f'[{"".join(loading_process)}]')
    else:
        print(f'{num}% [{"".join(loading_process)}]')
        print('Still loading...')


number = int(input())
loading_bar(number)
