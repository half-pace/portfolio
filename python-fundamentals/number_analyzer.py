user = int(input("Enter a positive number: "))

even = [num for num in range(1, user) if num % 2 == 0]
odd = [num for num in range(1, user) if num % 2 != 0]
div_3 = [num for num in range(1, user) if num % 3 == 0]
sum_total = sum(range(1, user))
is_prime = False
if user <= 1:
    print("Not a prime number")