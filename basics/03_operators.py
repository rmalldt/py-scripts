# ------------------ Operators
a = 6
b = 3
print(a + b)  # 9
print(a - b)  # 3
print(a * b)  # 18
print(a / b)  # 2.0
print(a // b)  # 2 integer division, rounded to floor
print(a % b)  # 0 module, the remainder after integer division
print(a**b)  # 216

# ------------------ Operator Precedence
# Numerical Precedence follows BEMA order.
# - B: Brackets
# - E: Exponents
# - M: Multiplication / Division
# - A: Addition / Subtraction
print(a + b / 3 - 4 * 2)  # -1
print(a + (b / 3) - (4 * 2))  # -1
print((((a + b) / 3) - 4) * 2)  # -2
