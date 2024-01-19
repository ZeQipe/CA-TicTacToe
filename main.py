import asyncio
import random
import os


def print_board(board):
    for i in range(0, 9, 3):
        print("|".join(board[i:i + 3]))


def make_move(board, position, current_player):
    if board[position] == " ":
        board[position] = current_player
        return True
    return False


def switch_player(current_player):
    return "O" if current_player == "X" else "X"


def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != " ":
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            return True
    if board[0] == board[4] == board[8] != " " or \
            board[2] == board[4] == board[6] != " ":
        return True
    return False


async def bot_move(board, current_player):
    await asyncio.sleep(1)  # Simulating bot's "thinking" time
    return random.choice([i for i, x in enumerate(board) if x == " "])


async def play_game():
    board = [" "] * 9
    current_player = "X"
    clear = lambda: os.system('cls')

    while True:
        clear()
        print_board(board)

        move = await bot_move(board, current_player)

        if make_move(board, move, current_player):
            if check_winner(board):
                clear()
                print_board(board)
                input(f"{current_player} wins!")
                break

            current_player = switch_player(current_player)


if __name__ == "__main__":
    asyncio.run(play_game())
