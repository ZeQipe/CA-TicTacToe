import asyncio
import random


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


async def bot_move(board: list) -> None:
    """
    Выбирает ячейку, на которую будет делать ход
    Так же имитирует ожидание перед ходом
    :param board: str
    :return:
    """
    await asyncio.sleep(1)
    return random.choice([i for i, x in enumerate(board) if x == " "])


async def user_move() -> int:
    """

    :return:
    """
    while True:
        try:
            move = input("Enter your move (1-9): ").lower().replace(' ', '')
            if move == 'r':
                return -1
            move = int(move) - 1
            if 0 <= move <= 8:
                return move
            else:
                print("Invalid move. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")