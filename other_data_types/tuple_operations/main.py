# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]

shelf1_update_tuple = tuple(shelf1_update)
shelf1_concat = shelf1 + shelf1_update_tuple
celery_count = shelf1_concat.count("celery")
celery_index = shelf1_concat.index("celery")
print("Updated Shelf #1:",shelf1_concat)
print("Number of Celery:",celery_count)
print("Celery Index:",celery_index)






# 示例应用
#  假设你有一些列表，其中存储了过去三个月内所有打折商品的信息。你需要讲这些列表转换为元祖，连接这些元祖
#  然后确定每个商品在过去三个内搭着的次数。此外，你还需要确定每个商品首次出现的位置。
janSales_list = ["apples","oranges","apples"]
febSales_list = ["bananas","oranges","bananas"]
marSales_list = ["apples","bananas","apples"]

quarterlySales = janSales_list + febSales_list + marSales_list;
apples_sale_count = quarterlySales.count("apples");
# print("Apples have been on sale:", apples_sale_count,"times.");

first_apple_sale_index = quarterlySales.index("apples");
# print("The first sale of apples this quarter was at index:",first_apple_sale_index)