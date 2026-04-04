def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n: int) -> int:
    """Calculate the factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using recursion."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor of two numbers using Euclid's algorithm using recursion."""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome."""
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return s == s[::-1]  # Check if the string is equal to its reverse

def main():
    # Example usage of the functions
    print(is_prime(17))  # True
    print(factorial(5))  # 120
    print(fibonacci(10))  # 55
    print(gcd(48, 18))  # 6
    print(is_palindrome("A B A"))
    
if __name__ == "__main__":    main()