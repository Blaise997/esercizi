a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for element in a:
    if element < 5:
        print(element)

# Create a new list containing elements less than 5
new_list = [element for element in a if element < 5]

# Print the new list
print(new_list)

# Asking the user for a number
number = int(input("Enter a number: "))

# Creating a new list containing elements smaller than the user-provided number
new_list = [element for element in a if element < number]

print(new_list)