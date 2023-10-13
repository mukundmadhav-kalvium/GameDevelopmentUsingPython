import random

# Define Snakes and Ladders
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Function to roll a dice
def roll_dice():
    return random.randint(1, 6)

# Function to move the player
def move_player(player, steps):
    new_position = player + steps
    if new_position in snakes:
        print(f"Oops! You landed on a snake. Going back to position {snakes[new_position]}.")
        return snakes[new_position]
    elif new_position in ladders:
        print(f"Yay! You found a ladder. Climbing to position {ladders[new_position]}.")
        return ladders[new_position]
    # elif new_position>100:
    #     break
    else:
        return new_position

# Main game loop
def play_game():
    player1_position = 0
    player2_position = 0
    current_player = 1

    while True:
        if current_player == 1:
            input("Player 1, press Enter to roll the dice...")
            steps = roll_dice()
            print(f"Player 1 rolled a {steps}.")
            player1_position = move_player(player1_position, steps)
            print(f"Player 1 is now at position {player1_position}.\n") 
            if player1_position == 100:
                print("Player 1 wins!")
                break
            if player1_position == player2_position:
                player2_position = 0
                print("Player 1 is in the same position as Player 2.")
                print(f"Player 2 is now at position {player2_position}.\n")
        else:
            input("Player 2, press Enter to roll the dice...")
            steps = roll_dice()
            print(f"Player 2 rolled a {steps}.")
            player2_position = move_player(player2_position, steps)
            print(f"Player 2 is now at position {player2_position}.\n")
            if player2_position == 100:
                print("Player 2 wins!")
                break
            if player2_position == player1_position:
                player1_position = 0
                print("Player 2 is in the same position as Player 1.")
                print(f"Player 1 is now at position {player1_position}.\n")

        current_player = 3 - current_player  # Switch players (1 to 2 and 2 to 1)

# Start the game
print("Welcome to Snake and Ladder!")
play_game()
