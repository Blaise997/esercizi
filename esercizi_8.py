print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:
    print("Player 1, enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    choice1 = int(input("Enter your choice :"))

    # looping until user enter invalid input
    while choice1 > 3 or choice1 < 1:
        choice1 = int(input('Enter a valid choice please (1-3):'))

    print("\nPlayer 2, enter your choice: \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    choice2 = int(input("Enter your choice: "))
    while choice2 > 3 or choice2 < 1:
        choice2 = int(input('Please enter a valid choice (1-3):'))


    if choice1 == 1:
        choice_name1 = 'Rock'
    elif choice1 == 2:
        choice_name1 = 'Paper'
    else:
        choice_name1 = 'Scissors'

    if choice2 == 1:
        choice_name2 = 'Rock'
    elif choice2 == 2:
        choice_name2 = 'Paper'
    else:
        choice_name2 = 'Scissors'

    print("Player 1 chose:", choice_name1)
    print("Player 2 chose:", choice_name2)

    if choice1 == choice2:
        print("It's a tie!")
    elif (choice1 == 1 and choice2 == 3) or (choice1 == 2 and choice2 == 1) or (choice1 == 3 and choice2 == 2):
        print("Player 1 wins")
    else:
        print("Player 2 wins")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        break