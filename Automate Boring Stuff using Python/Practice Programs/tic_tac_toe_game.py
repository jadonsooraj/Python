# Tic Tac Toe Game
# This is a simple command-line Tic Tac Toe game for two players.

def check_win(board, player):
    win_combos = [
        ['TL', 'TM', 'TR'],
        ['ML', 'MM', 'MR'],
        ['BL', 'BM', 'BR'],
        ['TL', 'ML', 'BL'],
        ['TM', 'MM', 'BM'],
        ['TR', 'MR', 'BR'],
        ['TL', 'MM', 'BR'],
        ['TR', 'MM', 'BL']
    ]
    for combo in win_combos:
        if all(board[pos] == player for pos in combo):
            return True
    return False

def main():
    positions = ['TL', 'TM', 'TR', 'ML', 'MM', 'MR', 'BL', 'BM', 'BR']
    board = {pos: ' ' for pos in positions}
    current_player = 'X'
    moves = 0

    while True:
        board_print = lambda: print(
            f"{board['TL']} | {board['TM']} | {board['TR']}\n"
            "---------\n"
            f"{board['ML']} | {board['MM']} | {board['MR']}\n"
            "---------\n"
            f"{board['BL']} | {board['BM']} | {board['BR']}\n"
        )
        print("Current Board:")
        board_print()
        move = input(f"Player {current_player}, enter position (e.g., TL, MM): ").strip().upper()
        if move not in positions or board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[move] = current_player
        moves += 1
        if check_win(board, current_player):
            print("Current Board:")
            board_print()
            print(f"Player {current_player} wins!")
            break
        if moves == 9:
            print("Current Board:")
            board_print()
            print("It's a tie!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()