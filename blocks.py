for i in range(1,13):
    print("No. {} squared is {} and cubed is {}".format(i, i ** 2, i ** 3))
    print("*" * 80)

name = input("Please enter your name: ")
age = int(input("How old are you {0}: ".format(name)))
print(age)

if age>=18:
    print("You are old enough to vote")
else:
    print("Please come back in {0} years".format(18-age))


if age<=18:
    print("Please come back in {0} years".format(18-age))
elif age == 900:
    print("Sorry you die in the return of jedi")
else:
    print("you are old enough to vote")
    print("please put an X in the box")
