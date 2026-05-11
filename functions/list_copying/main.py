# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

def apply_discount(prices):
    prices_copy = prices.copy()
    for price in range(len(prices_copy)):
        if prices_copy[price] > 2.00:
            prices_copy[price] = prices_copy[price] * 0.9
    return prices_copy
            

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)
print("Updated product prices:",updated_prices)
# def add_strawberry(original_list):
#     list_copy = original_list.copy()
#     list_copy.append("Strawberry")
#     return list_copy
# fruits = ["Apple","Banana","Cherry"]
# new_fruits = add_strawberry(fruits)
# print("Original list:" ,fruits)
# print("Modified list",new_fruits)