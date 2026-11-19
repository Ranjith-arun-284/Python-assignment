
order_amount = float(input("Enter the order amount (in Rs): "))
membership_input = input("Are you a member? (yes/no): ")

membership = membership_input.strip().lower()

is_amount_valid = order_amount >= 0 and order_amount <= 100000
is_membership_valid = membership == "yes" or membership == "no"

if not is_amount_valid:
    print("Eligibility status: Invalid order amount (must be between 0 and 1,00,000).")
elif not is_membership_valid:
    print("Eligibility status: Invalid membership input (please enter yes or no).")
else:
    if order_amount >= 5000:
        discount_percent = 15
    elif membership == "yes" and order_amount >= 2000:
        discount_percent = 10
    else:
        discount_percent = 0

    discount_amount = order_amount * discount_percent / 100
    final_amount = order_amount - discount_amount

    print("Original amount     : Rs", order_amount)
    print("Discount percentage :", discount_percent, "%")
    print("Discount amount     : Rs", discount_amount)
    print("Final payable amount: Rs", final_amount)

    if discount_percent > 0:
        print("Eligibility status: Eligible for a discount.")
    else:
        print("Eligibility status: Not eligible for a discount.")
