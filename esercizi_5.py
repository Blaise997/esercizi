import random

# Generate two random lists
a = random.sample(range(1, 100), 10)  # Generate a random list of 10 unique numbers between 1 and 100
b = random.sample(range(1, 100), 10)  # Generate another random list of 10 unique numbers between 1 and 100

# Define the intersection function
intersection = lambda a, b: [value for value in a if value in b]

# Print the result of the intersection function
print(intersection(a, b))

print([value for value in random.sample(range(1, 100), 10) if value in random.sample(range(1, 100), 10)])