import random
snakes = {22: 6, 45: 30, 96: 64}
ladders = {7: 24, 21: 77, 42: 90, 40: 60}
WINNING_POSITION = 100

def roll_dice():
    return random.randint(1, 6)

def move_player(position):
    dice = roll_dice()
    print("Rolled a {}".format(dice))
    position += dice

    if position > WINNING_POSITION:
        position -= dice
        print("Can't move! Needs exact roll to win.")
    elif position in snakes:
        print("Oh no! Bitten by a snake at {}. Go down to {}.".format(position, snakes[position]))
        position = snakes[position]
    elif position in ladders:
        print("Yay! Climbed a ladder from {} to {}.".format(position, ladders[position]))
        position = ladders[position]
    else:
        print("Moved to {}".format(position))
    return position

def play_game():
    num_players = int(input("Enter number of players: "))
    player_positions = [0] * num_players
    winner = None
    turn = 0

    while winner is None:
        print("\nPlayer {}'s turn (Position: {})".format(turn + 1, player_positions[turn]))
        input("Press Enter to roll the dice...")
        new_position = move_player(player_positions[turn])
        player_positions[turn] = new_position

        if new_position == WINNING_POSITION:
            winner = turn + 1
            print("\nPlayer {} wins the game!".format(winner))
            break

        turn = (turn + 1) % num_players

if __name__ == "__main__":
    play_game()
