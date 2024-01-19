import asyncio
import random
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


def make_move(board: list, position: int, current_player: str) -> bool:
    """
    Делает ход, меняя пустое значение на доске на нужный символ игрока.
    Предварительно проверяет, пустая ли позиция для хода.
    :param board: str
    :param position: int
    :param current_player: str
    :return: Вернет True, если ход сделан, либо False, если ячейка не пуста.
    """
    if board[position] == " ":
        board[position] = current_player
        return True
    return False


def switch_player(current_player: str) -> str:
    """
    После успешного хода, меняет текущего пользователя.
    :param current_player: str
    :return: str ('X' or 'O').
    """
    return "O" if current_player == "X" else "X"


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


async def bot_move(board: list) -> None:
    """
    Выбирает ячейку, на которую будет делать ход
    Так же имитирует ожидание перед ходом
    :param board: str
    :return:
    """
    await asyncio.sleep(1)
    return random.choice([i for i, x in enumerate(board) if x == " "])


async def play_game() -> None:
    """
    Контролирует весь игровой процесс.
    :return:
    """
    board = [" "] * 9
    current_player = "X"

    while True:
        print_board(board)
        move = await bot_move(board)

        if make_move(board, move, current_player):
            if check_winner(board):
                print_board(board)
                input(f"{current_player} wins!")
                return

            current_player = switch_player(current_player)


#Run app and game
if __name__ == "__main__":
    asyncio.run(play_game())
