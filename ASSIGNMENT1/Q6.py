def factorial(n):
    
    if n == 0:
        return 1
    else:
        fact = 1
        i = 1
        while i <= n:
            fact *= i
            i += 1
        return fact

# Example usage:
number = 5
print("Factorial of", number, "is", factorial(number))
