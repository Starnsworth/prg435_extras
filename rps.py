#    Paper/rock/scissors in Python
import random
moves = ["rock", "paper", "scissor"]
winning_moves = {"rock" : "scissor", "paper" : "rock", "scissor" : "paper"}


def get_winner(player1move, player2move):
    if player2move == winning_moves[player1move]:
        return 1
    elif player1move == winning_moves[player2move]:
        return 2


def get_player_move():
    valid_move = False
    while not valid_move:
        print("Player Move Select")
        playerchoice = input("Select rock, paper, or scissor? ")
        if playerchoice == "rock":
            return moves[0]
        elif playerchoice == "paper":
            return moves[1]
        elif playerchoice == "scissor":
            return moves[2]
        else:
            print("Invalid Input")


def get_comp_move():
    print("Computer Move Select")
    compmove = random.choice(moves)
    print(compmove)
    return compmove

while True:
    match get_winner(get_player_move(), get_comp_move()):
        case 1:
            print("Player Wins!")
        case 2:
            print("Computer Wins!")
        case _:
            print("Draw!")



