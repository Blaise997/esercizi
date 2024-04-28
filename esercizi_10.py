import random

# Generate two random lists of different lengths
a = random.sample(range(1, 100), random.randint(5, 15))
b = random.sample(range(1, 100), random.randint(5, 15))

# Initialize an empty list to store common elements
common_elements = []

# Iterate over elements in list 'a'
for element in a:
    # Check if the element is also present in list 'b' and not already in common_elements
    if element in b and element not in common_elements:
        common_elements.append(element)

print("List a:", a)
print("List b:", b)
print("Common elements:", common_elements)

