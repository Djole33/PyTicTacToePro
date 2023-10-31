marker_positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

board = [' '] * 9


def display_board():
    updated_board = [None] * 9
    for i in range(9):
        if board[i] != ' ':
            updated_board[i] = board[i]
        else:
            updated_board[i] = marker_positions[i]

    print('---|---|---')
    print(f' {updated_board[6]} | {updated_board[7]} | {updated_board[8]} ')
    print('---|---|---')
    print(f' {updated_board[3]} | {updated_board[4]} | {updated_board[5]} ')
    print('---|---|---')
    print(f' {updated_board[0]} | {updated_board[1]} | {updated_board[2]} ')
    print('---|---|---')


def place_marker(marker, position):
    if board[position - 1] == ' ':
        board[position - 1] = marker
        return True
    else:
        print("Position already occupied. Try another position.")
        return False


def check_win(marker):
    return (board[6] == board[7] == board[8] == marker) or \
        (board[3] == board[4] == board[5] == marker) or \
        (board[0] == board[1] == board[2] == marker) or \
        (board[6] == board[3] == board[0] == marker) or \
        (board[7] == board[4] == board[1] == marker) or \
        (board[8] == board[5] == board[2] == marker) or \
        (board[6] == board[4] == board[2] == marker) or \
        (board[8] == board[4] == board[0] == marker)


def check_tie():
    return ' ' not in board


def play_game():
    while True:
        global board
        board = [' '] * 9
        marker = 'X'
        while True:
            display_board()
            while True:
                position = int(input(f"Player {marker}, choose your next position (1-9): "))
                if place_marker(marker, position):
                    break
            if check_win(marker):
                display_board()
                print(f"Player {marker} wins!")
                break
            if check_tie():
                display_board()
                print("It's a tie!")
                break
            marker = 'O' if marker == 'X' else 'X'
        replay = input("Do you want to play again? (yes/no): ")
        if replay.lower() != 'yes':
            break


play_game()