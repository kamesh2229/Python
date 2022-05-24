#                   1
#         012345678901234
parrot = "Norwegian Blue"
#

print(parrot)

print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot)
print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

# Slicing

print(parrot[0:6])  # Includes 0 and excludes the 6th digit.
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])  # From oth charcter to 9th character

print(parrot[10:14])
print(parrot[10:])  # From 10th Character to last
print(parrot[:6])
print(parrot[6:])
print(parrot[:6] + parrot[6:])

print(parrot[:])

letters = "abcdefghijklmnopqrsuvwxyz"
print(letters[:]) # prints all letters
print(letters[0:5]) # prints abcde
print(letters[9:12]) # prints jkl
print(letters[22:]) # print xyz
print(letters[:11]) # print abcdefghijk

print(parrot[-4:-2]) # Bl
print(parrot[-4:12]) # Bl


# Using a step in Slice.. Slices at every character based on the number provided.
print(parrot[0:6:2]) # Nre
print(parrot[0:6:3]) # Nw

number = "9,223;344:057 798,899;734"
seperators = (number[1::4])
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])


days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])