user = int(input("Enter a positive number: "))

even = [num for num in range(1, user) if num % 2 == 0]
odd = [num for num in range(1, user) if num % 2 != 0]
div_3 = [num for num in range(1, user) if num % 3 == 0]
sum_total = sum(range(1, user))

if user <= 1:
    print("Not a prime number")
else:
    is_prime = True
    for i in range(2, int(user**0.5) + 1):
        if user % i == 0:
            is_prime = False
            break
    print(f"{user} is a prime number" if is_prime == True else f"{user} is not a prime number")
    
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")
print(f"Numbers divisible by 3: {div_3}")
print(f"Sum of numbers from 1 to {user} is: {sum_total}")