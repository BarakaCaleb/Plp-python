# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. 
# The function should take the original price (price) and the discount percentage (discount_percent) as parameters. 
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.


def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price
    

original_price = int(input("Enter the original price of the item:"))

discount_percentage = int(input("Enter the discount percentage:"))

print("The final price after the discount is:", calculate_discount(original_price, discount_percentage))

