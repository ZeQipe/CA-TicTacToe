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


async def bot_move(board: list) -> int:
    """
    Возвращае индекс ячейки, на которую будет делать ход
    Так же имитирует ожидание перед ходом
    :param board: str
    :return: int
    """
    await asyncio.sleep(1)
    try:
        return random.choice([i for i, x in enumerate(board) if x == " "])
    except IndexError:
        return -1


async def user_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8:
                return move
            else:
                print("Invalid move. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")