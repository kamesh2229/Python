# If i want to split the complete String into several lines then use
# "\n" before the word which has to be printed from new line.
split_string = "This String has been\nsplit\nover\nseveral lines"
print(split_string)

# If we want to add tab between words then use "\t"
tabbed_string = "1\t2\t3\t4"
print(tabbed_string)

# /can be used to escape the single and double quote characters
# If the string is inside a single quote then using a single quote should be escaped with in the string
# If the string is inside a double quote then using a double quote should be escaped with in the string.

print('The pet shop owner said "No, no, \'e \'s uh,...he\'s is resting".')
print("The pet shop owner said \"No, no, 'e's uh...he's resting")
print("""The pet shop owner said "No, no, 'e 's uh,... he's good".""")

# If using """ then it is not needed to have \n for splitting the string into new line.
another_string = """This String
has been
split over
several lines"""
print(another_string)

# Use backslash at the end of line to escape the new line so that all strings will print in single line.
dont_split_string = """This String \
has been \
split over \
several lines"""
print(dont_split_string)

print("C:\\Users\\eprkame\\photos")
print(r"C:\Users\eprkame\photos")