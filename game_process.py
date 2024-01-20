import asyncio
import plaer_move
import os

def print_board(board: list) -> None:
    """
    Выводит на консоль игровое поле...
    :param board: type str
    :return: None
    """
    clear = lambda: os.system('cls')
    clear()
    for i in range(0, 9, 3):
        print("|".join(board[i:i + 3]))


def check_winner(board: list) -> bool:
    """
    Проверяет на то, что один из игроков уже победил.
    :param board: str
    :return: Вернет True, если есть победная комбинация. Иначе вернёт False.
    """
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


def switch_player(current_player: str) -> str:
    """
    После успешного хода, меняет текущего пользователя.
    :param current_player: str
    :return: str ('X' or 'O').
    """
    return "O" if current_player == "X" else "X"


async def bot_vs_bot(board):
    current_player = 'X'
    while True:
        print_board(board)
        move = await plaer_move.bot_move(board)

        if plaer_move.make_move(board, move, current_player):
            if check_winner(board):
                print_board(board)
                print(f"{current_player} wins!")
                return

            current_player = switch_player(current_player)


async def plaer_vs_bot(board):
    print('Кем хотите играть? X -- O')
    current_player = 'X'

    while True:
        print_board(board)

        if current_player == "X":
            move = await plaer_move.user_move()
        else:
            move = await plaer_move.bot_move(board)

        if move != -1 and plaer_move.make_move(board, move, current_player):
            if check_winner(board):
                print_board(board)
                if current_player == "X":
                    print("You win!")
                else:
                    print("Bot wins!")
                return

            current_player = switch_player(current_player)