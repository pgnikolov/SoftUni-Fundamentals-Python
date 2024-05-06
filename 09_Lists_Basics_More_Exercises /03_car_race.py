# # You will receive a sequence of numbers. Each number represents the time the car needs to
# # pass through that step (the index). There will be two cars. The first one starts from the left side,
# # and the other one starts from the right side. The middle index of the sequence is the finish line.
# Calculate the total time each racer needs to reach the finish line and print the winner with his total time
# (the racer with less time). If you have a zero in the list, you should reduce the racer's
# time that reached it by 20% (from his current time).
# The number of elements in the sequence will always be odd.
# Print the result in the following format "The winner is {left/right} with total time: {total_time}".
# The time should be formatted to the first decimal point.

nums = [int(char) for char in input().split(" ")]

midle_point_index = int((len(nums) - 1) / 2)

left = nums[:midle_point_index]
right = nums[midle_point_index + 1:][::-1]


def car_time(car: list):
    time = 0
    for lap in car:
        if lap == 0:
            time *= 0.80
        else:
            time += lap
    return time


left_time = car_time(left)
right_time = car_time(right)

if left_time <= right_time:
    print(f'The winner is left with total time: {left_time:.1f}')
else:
    print(f'The winner is right with total time: {right_time:.1f}')
