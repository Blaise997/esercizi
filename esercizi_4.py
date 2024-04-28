# Ask the user for a number
number = int(input("Enter a number: "))

# Initialize a list to store the divisors
divisors = []

# Iterate from 1 to the number and check for divisibility
for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

# Print the list of divisors
print("The divisors of", number, "are:", divisors)