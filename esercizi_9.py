import random

# Generate a random number between 1 and 9
random_number = random.randint(1, 9)

while True:
    # Ask the user to guess the number
    guess = int(input("Guess the number between 1 and 9: "))

    # Check if the guess is too low, too high, or exactly right
    if guess < random_number:
        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it right!")
        break  # Exit the loop if the guess is correct
