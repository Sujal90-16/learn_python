# Application of Recursion
# Fibonacci series
# f0 = 0
# f1 = 1
# f2 = f1 + f0
# f3 = f2 + f1
# fn = f(n-1) + f(n-2)

def fibonacci(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return (fibonacci(n-1)) + (fibonacci(n-2))
print(fibonacci(8))
