# Read two integer numbers and, after that, exchange their values.
# Print the variable values before and after the exchange.
# use a temporary variable to remember the old value of a then assign the value of b to a
# and then assign the value of the temporary variable to b.

a = int(input())
b = int(input())

c = a
a = b
b = c

print(f"Before:\na = {b}\nb = {a}\nAfter:\na = {a}\nb = {b}")
