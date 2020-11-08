
def display_board(board):
    i = board
    print('\n' * 20)
    print(i[7] + '|' + i[8] + '|' + i[9])
    print('-----')
    print(i[4] + '|' + i[5] + '|' + i[6])
    print('-----')
    print(i[1] + '|' + i[2] + '|' + i[3])


def player_input():
    choices = ['X', 'O']
    choice = ''
    while choice.upper() not in choices:

        choice = input('Player 1, would you like to play as X or O? ')
        if choice not in choices:
            print('\n' * 100)
            print('Invalid Response.')
    return choice.upper()


def place_marker(board, marker, position):
    board = board[:]
    board[position] = marker
    return board


def win_check(board, mark):
    return (board[1] == board[2] == board[3] == mark or #row 1
           board[4] == board[5] == board[6] == mark or #row 2
           board[7] == board[8] == board[9] == mark or #row 3
           board[1] == board[4] == board[7] == mark or #column 1
           board[2] == board[5] == board[8] == mark or #column 2
           board[3] == board[6] == board[9] == mark or #column 3
           board[1] == board[5] == board[9] == mark or #diag1
           board[3] == board[5] == board[7] == mark) #diag 2


import random

def choose_first():
    return random.randint(1, 2)


def space_check(board, position):
    return board[position] not in ['X', 'O',]


def full_board_check(board):
    for marker in board[1:]:
        if marker in ['X', 'O']:
            pass
        else:
            return False
    return True


def player_choice(board):
    choice = 0
    choices = [i for i in range(1, 10)]
    while choice not in choices:
        try:
            choice = int(input('Which position will you take next? (1-9) on the numpad.'))
            space = space_check(board, choice)
            if choice == 0:
                display_board(board)
                print('Invalid response.')
            elif space:
                break
            else:
                display_board(board)
                print('Sorry that position is taken!')
                choice = 0
        except ValueError:
            display_board(board)
            print('Invalid response.')
    return int(choice)


def replay():
    choice = ''
    choices = ['Y','N']
    while choice not in choices:
        choice = input('Would you like to play again? (Y or N) ')
        if choice.upper() not in choices:
            print('\n'*100)
            print('Invalid Response.')
        else:
            return choice.upper() == 'Y'


def take_turn(board, marker, turn):
    display_board(board)
    print(f"player {turn}'s turn.")
    position = player_choice(board)
    return place_marker(board, marker, position)


def game_on():
    print('\n' * 100)
    print('Welcome to Tic Tac Toe!')

    p1 = player_input()
    p2 = ('X' if p1 == 'O' else 'O')
    turn = choose_first()

    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    win = False
    full = False
    print('\n' * 100)
    print(f'Player 1 will play as {p1} and player 2 will play as {p2}.')
    print('Randomizing who makes the first move...')
    print(f'Player {turn} will go first.')
    input('Ready to play? Enter to continue. ')



    while not win and not full:
        if turn == 1:
            board = take_turn(board, p1, turn)
            turn = 2
            win = win_check(board, p1)
            full = full_board_check(board)

        elif turn == 2:
            board = take_turn(board, p2, turn)
            turn = 1
            win = win_check(board, p2)
            full = full_board_check(board)

    if win_check(board, p1):
        display_board(board)
        print(f'Congratulations player 1 you win!')
    elif win_check(board, p2):
        display_board(board)
        print(f'Congratulations player 2 you win!')
    elif full_board_check(board):
        display_board(board)
        print(f'Oh no! the game is a draw!')

    ask = replay()
    if ask:
        game_on()
    else:
        print('\n' * 100)
        print('Thanks for playing!')
        print('Bye!')


game_on()

