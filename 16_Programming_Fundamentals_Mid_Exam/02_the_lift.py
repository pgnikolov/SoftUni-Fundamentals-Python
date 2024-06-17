# Write a program that finds a place for the tourist on a lift.
# Every wagon should have a maximum of 4 people on it.
# If a wagon is full, you should direct the people to the next one with space available.
# Input
#     • On the first line, you will receive how many people are waiting to get on the lift
#     • On the second line, you will receive the current state of the lift separated by a single space: " ".
# Output
# When there is no more available space left on the lift, or there are no more people in the queue,
# you should print on the console final state of the lift's wagons separated by " " and one of the following messages:
#     • If there are no more people and the lift has empty spots, you should print:
# "The lift has empty spots!
# {wagons separated by ' '}"
#     • If there are still people in the queue and no more available space, you should print:
# "There isn't enough space! {people} people in a queue!
# {wagons separated by ' '}"
#     • If lift is full and there are no more people in the queue, you should print only the wagons separated by " ".

waiting_people = int(input())

current_state_of_the_lift = [int(char) for char in input().split(" ")]

for i in range(len(current_state_of_the_lift)):
    while current_state_of_the_lift[i] < 4 and waiting_people > 0:
        current_state_of_the_lift[i] += 1
        waiting_people -= 1

if waiting_people == 0 and not all(wagon == 4 for wagon in current_state_of_the_lift):
    print("The lift has empty spots!")
elif waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!")

print(*current_state_of_the_lift, sep=" ")

