def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

# get user input
original_price = float(input("Enter the original price of the item: $"))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate and print the final price
final_price = calculate_discount(original_price, discount_percentage)

if final_price != original_price:
    print(f"The final price after applying a {discount_percentage}% discount is: ${final_price:.2f}")
else:
    print("No discount applied. The original price remains: ${:.2f}".format(original_price))
