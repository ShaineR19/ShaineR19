# Shaine Ransford
# 3/21/2025
# Fibonacci

def fib(n):
    a,b = 0, 1
    while a < n:
        print(f"{a},")
        a, b = b, a+b

fib(1000)

print(fib(0))