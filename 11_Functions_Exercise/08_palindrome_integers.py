# Write a function that receives a list of positive integers, separated by comma and space ", ".
# The function should check if each integer is a palindrome - True or False. Print the result.
def check_palindrome(word):
    if word == word[::-1]:
        return True
    return False


num_list = input().split(", ")
for number in num_list:
    print(check_palindrome(number))
