def factorial(n):
    
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact


for number in range(11):
    print("Factorial of", number, "is", factorial(number))
