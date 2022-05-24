print("Today is a good day to learn python")
print('Python is fun')
print("Python's Strings are easy to use")
print('we can even include "quotes" in Strings')
print("Hello" + " world")
greeting = "Hello"
name = "Kamesh"
# We can pass the argument using the function "input" from a user.
PassArgs = input("Please enter your name")

# If we want to add a space we can add that too
# To add space between words we have to use [' '].

print(greeting + ' ' + name)
print(greeting + ' ' + PassArgs)
age = 37
print(age)

print(type(greeting))
print(type(age))

age_in_words = "2 years"
print(age)
print(type(age))
print(name + f" is {age} years old" )

pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")
