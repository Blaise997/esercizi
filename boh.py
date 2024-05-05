def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Usage example:
fib_gen = fibonacci()
for _ in range(10):  # Print the first 10 Fibonacci numbers
    print(next(fib_gen))

