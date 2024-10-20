import random

# Function to get the result of the game
def game_result(computer_choice, user_choice):
    if computer_choice == user_choice:
        return "It's a tie!"
    
    # Snake > Water, Water > Gun, Gun > Snake
    if (user_choice == 's' and computer_choice == 'w') or \
       (user_choice == 'w' and computer_choice == 'g') or \
       (user_choice == 'g' and computer_choice == 's'):
        return "You win!"
    else:
        return "You lose!"

# Main function to play the game
def play_game():
    choices = ['s', 'w', 'g']
    computer_choice = random.choice(choices)
    
    print("Welcome to Snake-Water-Gun Game!")
    print("Choose: Snake (s), Water (w), or Gun (g)")
    
    user_choice = input("Your choice: ").lower()
    
    if user_choice not in choices:
        print("Invalid input! Please choose 's', 'w', or 'g'.")
        return
    
    print(f"Computer chose: {computer_choice}")
    
    # Get the result of the game
    result = game_result(computer_choice, user_choice)
    print(result)

# Run the game
play_game()
