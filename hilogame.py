number = 5
multiplier = 8
answer = 0

# add your loop after this comment
answer = number * multiplier

print(answer)


low = 1
high = 1000

print("Please give a number between {} {}".format(low, high))
input("Press Enter to Start")

guesses = 1
while True:
    print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should i guess higher or lower? "
                     "Enter h or l, or c if my guess was correct ".format(guess).casefold())
    if high_low == "h":
        # Guess Higher. The low end of the range becomes 1 greater than the guess
        low = guess + 1
    elif high_low == "l":
        # Guess Lower. The high end of the range becomes 1 lower than the guess
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses ".format(guesses))
        break
    else:
        print("please enter h,l or c")

    #guesses = guesses + 1
    guesses += 1


