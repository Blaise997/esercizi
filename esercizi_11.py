# Ask the user for a number
number = int(input("Enter a number: "))

# Initialize a list to store the divisors
divisors = []

# Iterate from 1 to the number and check for divisibility
for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

# Check if the number is prime
if len(divisors) == 2:  # Prime numbers have only 2 divisors: 1 and the number itself
    print("Your number is prime")
else:
    print("Your number is not prime")
