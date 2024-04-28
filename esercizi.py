# Asking for user input
name = input("Give me your name: ")
age = int(input("Enter your age: "))

# Calculating the year when the user will turn 100
current_year = 2024  # Assuming the current year is 2024
year_turn_100 = current_year - age + 100

# Printing out the message
print("Hello, " + name + "! You will turn 100 years old in the year", year_turn_100)
