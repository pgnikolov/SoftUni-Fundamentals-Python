# Write a program that prints you a receipt for your new computer. You will receive the parts' prices (without tax)
# until you receive what type of customer this is - special or regular.
# Once you receive the type of customer you should print the receipt.
# The taxes are 20% of each part's price you receive.
# If the customer is special, he has a 10% discount on the total price with taxes.
# If a given price is not a positive number, you should print
# "Invalid price!" on the console and continue with the next price.
# If the total price is equal to zero, you should print "Invalid order!" on the console.
# Input
#     • You will receive numbers representing prices (without tax) until the command "special" or "regular":
# Output
#     • The receipt should be in the following format:
# "Congratulations you've just bought a new computer!
# Price without taxes: {total price without taxes}$
# Taxes: {total amount of taxes}$
# -----------
# Total price: {total price with taxes}$"
# Note: All prices should be displayed to the second digit after the decimal point!
# The discount is applied only on the total price. Discount is only applicable to the final price!

command = input()
total_no_tax = 0

while not (command == "special" or command == "regular"):
    price = float(command)

    if price < 0:
        print("Invalid price!")
        pass
    else:
        total_no_tax += price
    command = input()



if total_no_tax == 0:
    print("Invalid order!")
elif command == "special":
    final_price = total_no_tax * 1.20
    taxes = final_price - total_no_tax
    final_with_discount = final_price * 0.9
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_no_tax:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          "-----------\n"
          f"Total price: {final_with_discount:.2f}$")
else:
    final_price = total_no_tax * 1.20
    taxes = final_price - total_no_tax
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_no_tax:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          "-----------\n"
          f"Total price: {final_price:.2f}$")
