print("Hello world!")

#multiple assignments
a, b, c = 1, 2, 3
print(a, b, c)
#swap
x, y = 1, 2
x, y = y, x
print(x, y)
print(id(x), id(y))

#string indexing
name = "Alice"
print(name[0])  # A
print(name[1])  # l
print(name[-1])  # e

#string slicing
print(name[0: 3])
print(name[1: 4])
print(name[::2])
print(name[::-1]) #reverses the string

#string concatenation
print("Hello" + " " + name)
#string length
print(len(name))
#string repetition
print("ha" * 3)
#to check if a substring is in a string
print("li" in name)  # True
#print multiple values
print("Name: ", "Arjun", "Age:", 20)
#separator parameter
print("20", "2", "2026", sep="-")
#end parameter to avoid new line
print("Hello", end=" ")
print("World!")

