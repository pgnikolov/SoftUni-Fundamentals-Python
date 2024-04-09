# Write a program to check if a number is prime. A prime number is a natural number greater than 1,
# not a product of two smaller natural numbers. the only ways of writing 5 as a product, 1 × 5 or 5 × 1, 5 itself.
# The input comes as an integer number.
# The output should be True if the number is prime and False otherwise.


number = int(input())

is_prime = True
for i in range(2, number):
    if number % i == 0:
        is_prime = False

if is_prime:
    print("True")
else:
    print("False")
