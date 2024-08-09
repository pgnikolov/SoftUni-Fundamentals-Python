# You will be given a number. Print the largest number that can be formed from the digits of the given number.
number = int(input())

if number < 0:
    print("Largest number cannot be formed from negative numbers.")
else:
    digits = list(str(number))

    for i in range(len(digits) - 1):
        for j in range(i + 1, len(digits)):
            if digits[i] < digits[j]:
                digits[i], digits[j] = digits[j], digits[i]

    largest_number_str = "".join(digits)
    largest_number = int(largest_number_str)

    print(largest_number)
