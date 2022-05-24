shopping_list = ["milk", "spam", "pasta", "eggs", "rice", "bread"]

item_to_find = "spam"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
print("Item found at position {}".format(found_at))

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

print("Item found at position {}".format(found_at))

    