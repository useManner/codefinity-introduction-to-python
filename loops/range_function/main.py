# for day in range(7):
#     print(day)
# for day in range(25, 32):
#     print(day)
# for hour in range(1,13,3): # 1 : 代表开始值，13：代表停止值，3：代表每次的步数是几（递增）
#     print(hour)


# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for day in range(5):
    weekday = weekdays[day]
    promotion = daily_promotions[day]
    print(f"{weekday}:Promotion on {promotion}")