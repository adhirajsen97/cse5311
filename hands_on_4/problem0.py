def fib(n):
    print(n)
    if n < 0:
        raise ValueError("Input must be non-negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)  

    
response = fib(5)
print(response)