board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def display(board):
    print('\n'*100)
    print('  |   | ')
    print(board[1]+' | '+board[2]+' | '+board[3])
    print('  |   | ')
    print("----------")
    print('  |   | ')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('  |   | ')
    print("----------")
    print('  |   | ')
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('  |   | ')


def player_input():
    marker = ''
    player1 = ''
    computer = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Please select a marker 'x' or 'o': ").upper()
        if (marker != 'X') or (marker != 'O'):
            print('\n'*100)
        if marker == 'X':
            print(f"You are '{marker}' '")
            print("Computer is 'O'")
            player1, computer = 'X', 'O'
        elif marker == 'O':
            print(f"You are '{marker}' '")
            print("Computer is 'X'")
            player1, computer = 'O', 'X'
    return player1, computer

def display_position_board(): #to show user where to place a marker
    print("Please select a position to place your marker")
    print('  |   | ')
    print(f"{1} | {2} | {3}")
    print('  |   | ')
    print("----------")
    print('  |   | ')
    print(f"{4} | {5} | {6}")
    print('  |   | ')
    print("----------")
    print('  |   | ')
    print(f"{7} | {8} | {9}")
    print('  |   | ')

def position_chioce():
    chioce = ''
    while chioce not in range(1,10):
        chioce = int(input("Select a position to place your marker(1-9): "))
        if chioce not in range(1,10):
            print('\n'*100)
    return chioce


def empty_space(position, board):
    return board[position] == ' '

def win_check(board,mark): #check if we have a winner
    return (board[1] == mark and board[2] == mark and board[3] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[7] == mark and board[8] == mark and board[9] == mark) or (board[1] == mark and board[4] == mark and board[7] == mark) or (board[2] == mark and board[5] == mark and board[8] == mark) or (board[3] == mark and board[6] == mark and board[9] == mark) or (board[1] == mark and board[5] == mark and board[9] == mark) or (board[3] == mark and board[5] == mark and board[7] == mark)

def full_board_check(board):
    for i in range(1,10):
        if board[i] == ' ':
            return False
    return True


def placing_input(board, position, marker):  # to place a marker on the selected position
    board[position] = marker


def question():
    return input("Do you want to go another round(y/n): ")

import random

def computer():
    return random.randint(1,9)

def whose_turn():
    r = random.randint(1,2)
    if r == 1:
        return "player1"
    else:
        return "computer"


print("Welcome to my Tic Tac Toe Game")

play = True

while play:
    answer = ' '

    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    player1_marker, computer_marker = player_input()

    display_position_board()

    turn = whose_turn()

    game_on = True

    while game_on:

        if turn == "player1":
            position = position_chioce()
            if empty_space(position, board) == True:
                placing_input(board, position, player1_marker)
                display(board)
                turn = "computer"

                if win_check(board, player1_marker):
                    display(board)
                    print("Congratulations you have won")
                    answer = input("Do you want to go another round(y/n):")
                    if answer == 'n':
                        game_on = False
                        play = False
                    else:
                        game_on = False
                        play = True


                else:
                    if full_board_check(board):
                        display(board)
                        print("The game is a draw")
                        answer = input("Do you want to go another round(y/n):")
                        if answer == 'n':
                            game_on = False
                            play = False
                        else:
                            game_on = False
                            play = True
                    else:
                        turn = "computer"

            elif empty_space(position, board) == False:
                print('\n'*100)
                display(board)
                print('Please select a valid position')
                turn = "player1"
                continue


        else:
            if turn == "computer":
                position = computer()
                if empty_space(position, board) == True:
                    placing_input(board, position, computer_marker)
                    display(board)
                    turn = "player1"

                    if win_check(board, computer_marker):
                        display(board)
                        print("Sorry you loose")
                        answer = input("Do you want to go another round(y/n):")
                        if answer == 'n':
                            game_on = False
                            play = False
                        else:
                            game_on = False
                            play = True

                    elif full_board_check(board):
                        display(board)
                        print("We have a draw")
                        answer = input("Do you want to go another round(y/n):")
                        if answer == 'n':
                            game_on = False
                            play = False
                        else:
                            game_on = False
                            play = True
                    turn = "player1"

print("Thanks for playing")











