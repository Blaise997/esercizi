# Asking for user input
num = int(input("Give me one number: "))

# Checking if the number is even or odd
if num % 2 == 1:
    print("The number is odd")
else:
    print("The number is even")
# Checking if the number is a multiple of 4
if num % 4 == 0:
    print("The number is a multiple of 4")

# Asking for user input
num = int(input("Enter the number to check: "))
check = int(input("Enter the number to divide by: "))

# Checking if the second number divides evenly into the first number
if num % check == 0:
    print(check, "divides evenly into", num)
else:
    print(check, "does not divide evenly into", num)
