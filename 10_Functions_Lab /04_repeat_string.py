# Write a function that receives a string and a counter n. The function should return a new string –
# the result of repeating the old string n times. Print the result of the function. Try using lambda.

repeat_str = lambda word, num: string * num

string = input()
counter = int(input())
result = repeat_str(string, counter)
print(result)
