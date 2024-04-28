def generate_fibonacci(count):
    fibonacci_series = [0, 1]  # Initialize Fibonacci series with the first two numbers

    # Generate Fibonacci numbers
    for i in range(2, count):
        next_number = fibonacci_series[-1] + fibonacci_series[-2]  # Calculate the next Fibonacci number
        fibonacci_series.append(next_number)  # Add the next Fibonacci number to the series

    return fibonacci_series

# Ask the user how many Fibonacci numbers to generate
count = int(input("How many Fibonacci numbers do you want to generate? "))

# Generate and print the Fibonacci numbers
fibonacci_numbers = generate_fibonacci(count)
print("Fibonacci numbers:", fibonacci_numbers)
