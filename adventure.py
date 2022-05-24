available_exists = {"north", "south", "east", "west"}

chosen_exist = ""
while chosen_exist not in available_exists:
    chosen_exist = input("please choose a direction: ")
    if chosen_exist.casefold() == "quit":
        print("Game over ")
        break;

print("Aren't you glad that you got out of there")

for i in range(0, 100, 7):
    print(i)
    if i > 0 and (i % 11 == 0):
        print("The point reached")
        break;

for i in range(0,20):
    print(i)
    while i > 0 and (i % 3 == 0 and i % 5 == 0):
        print(i)

