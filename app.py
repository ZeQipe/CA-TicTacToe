import game_process
import asyncio


def play_game() -> None:
    """
    Контролирует весь игровой процесс.
    :return:
    """
    while True:
        board = [" "] * 9
        print('Выберите режим игры:\n\t1 - bot vs bot\n\t2 - plaer vs bot')
        type_game = input('>>').replace(' ', '').lower()
        match type_game:
            case '1':
                asyncio.run(game_process.bot_vs_bot(board))
            case '2':
                asyncio.run(game_process.plaer_vs_bot(board))

