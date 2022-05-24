shopping_list = ["milk", "pasta", "spam", "bread", "rice"]

for item in shopping_list:
    if item != "spam": ## (Spam not included)
        print("Buy " + item)


for items in shopping_list:
    if items == "spam":
        continue
    print(" Buy " + items)