age = 24
print("My age is " + str(age) + " Years")

print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
    .format(31, "Jan", "Mar", "May", "July", "Aug", "OCT", "DEC"))

print("Jan: {0}, Feb: {1}, Mar: {2}, Apr: {2}, May: {1}"
      .format(28,30,31))

print()

print("""Jan: {2}
Feb: {1}
Mar: {0}
Apr: {0}
""".format(28,30,31))
