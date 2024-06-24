import random


def get_user_choice():
    """Get the user's choice."""
    user_choice = input("Enter your choice: ").rstrip('\r\n')
    while user_choice not in ['1', '2', '3']:
        print("Invalid choice. Please enter 1, 2, or 3.")
        user_choice = input("Enter your choice: ").rstrip('\r\n')
    return ['rock', 'paper', 'scissors'][int(user_choice) - 1]


def get_computer_choice():
    """Get the computer's choice."""
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):
    """Determine the winner."""
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        return "Meat bags win!"
    else:
        return "Meat bags: 0 Computers: 1"


def play_game():
    """Play the game."""
    print(
        "1. Rock \n"
        "2. Paper \n"
        "3. Scissors \n"
    )
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}. {result}")


# Run the game
play_game()
