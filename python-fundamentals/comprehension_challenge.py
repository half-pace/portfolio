# comprehension_challenge.py


# 1. Pythagorean triples
triples = [
    (a, b, c)
    for a in range(1, 31)
    for b in range(a, 31)
    for c in range(b, 31)
    if a*a + b*b == c*c
]

print("1. Pythagorean Triples:")
print(triples)


# 2. 10x10 multiplication table
table = [
    [i*j for j in range(1, 11)]
    for i in range(1, 11)
]

print("\n2. Multiplication Table:")
print(table)


# 3. Extract words
sentence = "Hello Zack went to Delhi for Python Programming"

words = [
    word
    for word in sentence.split()
    if len(word) > 3 and word[0].isupper()
]

print("\n3. Capitalized Words:")
print(words)


# 4. Caesar cipher (+3)
text = "Hello World!"

cipher = "".join([
    chr((ord(ch)-65+3)%26 + 65) if ch.isupper()
    else chr((ord(ch)-97+3)%26 + 97) if ch.islower()
    else ch
    for ch in text
])

print("\n4. Caesar Cipher:")
print(cipher)


# 5. Even sum pairs
nums = [1, 2, 3, 4, 5, 6]

pairs = [
    (i, j)
    for i in range(len(nums))
    for j in range(i+1, len(nums))
    if (nums[i] + nums[j]) % 2 == 0
]

print("\n5. Even Sum Pairs:")
print(pairs)