# Write a function that receives three integer numbers and returns the smallest. Print the result on the console.
# Use an appropriate name for the function.

def min_num(num1, num2, num3):
    smallest = min([num1, num2, num3])
    return smallest


a = int(input())
b = int(input())
c = int(input())
print(min_num(a, b, c))
