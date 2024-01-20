import asyncio
import random











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



