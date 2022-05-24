answer = 5

print("please guess a number between 1 and 10: ")
guess = int(input())

# if guess != answer:
#     if guess < answer:
#         print("please guess higher")
#     else:
#         print("please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("You have guess it right")
#     else:
#         print("sorry you have not guessed correctly")
# else:
#     print("you got it first time")

if guess == answer:
    print("you got it right")
elif guess < answer:
    print("please guess higher")



# if guess < answer:
#     print("please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you did it")
#     else:
#         print("sorry you didn't guess correctly")
# elif guess > answer:
#     print("please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("well done you did it")
#     else:
#         print("sorry you didn't guess correctly")
# else:
#     print("you got it first time")