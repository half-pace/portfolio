print("Type Detective")

# 1) Bool is a subclass of int
print("isinstance(True, int))  # True", isinstance(True, int))
print("type(True)", type(True))
print()

# 2) True behaves like 1 and False behaves like 0
print("True + True =", True + True)
print("True: ", True)
print("False + False =", False + False)
print("False: ", False)

# 3) Float precision issues with solution: round()
print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.1 + 0.2 =", round(0.1 + 0.2, 2))

# 4) Int caching with is
a = 100
b = 100
print("a is b:", a is b)

x = 1000
y = 1000
print("x is y:", x is y)

# 5) None is a singleton
n1 = None
n2 = None
print("n1 is n2:", n1 is n2)
print(type(None))

# 6) Everything is an object
print("type(42):", type(42))
print("type(3.14):", type(3.14))
print("type('Hello'):", type('Hello'))

# 7)boolean arithmetic with integers
print("True * 5 =", True * 5)
print("False * 5 =", False * 5)