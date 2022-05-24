a = 12
b = 3

print(a + b)  # 15
print(a - b)  # 9
print(a * b)  # 36
print(a / b)  # 4.0
print(a // b)  # 4 Integer division rounded towards minus infinity
print(a % b)  # 0 modulo: the reminder after integer division

print()

for i in range(1, a // b):
    print(i)

print(a + b / 3 - 4 * 12)  # / and * has higger precedence over + and 1
print(a + (b / 3) - (4 * 12))
print((((a + b) / 3) - 4) * 12)

# Multiplication and Addition have equal precedence
# Addition and subtraction have equal precedence
# If in program if we have both available then the execution will be form left to right..
c = a + b
d = c / 3
e = d - 4
print(e * 12)
