prices = [29.99, 45.50, 12.75, 38.20]
zhekou = [0.1,0.2,0.15,0.05]

for index in range(len(prices)):
    prices[index] = prices[index] * (1 - zhekou[index])
    print(f"Updated price for item {index}: ${prices[index]:.2f}")






# grocery_list = ["Apples", "Bananas", "Carrots", "Cucumbers"]
# for item in range(len(grocery_list)):
#     print("Index:", item)
#     print("Item" , grocery_list[item])
#     print("----")