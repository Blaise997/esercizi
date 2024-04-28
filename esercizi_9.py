import random

# Generate a random number between 1 and 9
random_number = random.randint(1, 9)

# Initialize the number of guesses
guesses = 0

while True:
    # Ask the user to guess the number or exit
    guess_input = input("Guess the number between 1 and 9, or type 'exit' to quit: ")

    # Check if the user wants to exit
    if guess_input.lower() == 'exit':
        print("Exiting the game. Thanks for playing!")
        break

    # Convert the guess to an integer
    try:
        guess = int(guess_input)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 9, or type 'exit' to quit.")
        continue

    # Increment the number of guesses
    guesses += 1

    # Check if the guess is too low, too high, or exactly right
    if guess < random_number:
        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it right in {guesses} guesses!")
        break

