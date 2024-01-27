import os
import game_process
import asyncio


def play_game() -> None:
    """
    Подготовка к игре, стартовое меню. Главный жизненный цикл игры
    :return:
    """
    while True:
        os.system('cls')
        board = [" "] * 9
        print('Выберите режим игры (s - завершение работы):\n\t1 - bot vs bot\n\t2 - plaer vs bot'
              '\n\t3 - player vs player')
        type_game = input('>>').replace(' ', '').lower()
        match type_game:
            case '1':
                asyncio.run(game_process.bot_vs_bot(board))

            case '2':
                asyncio.run(game_process.player_vs_bot(board))

            case '3':
                asyncio.run(game_process.player_vs_player(board))

            case 's':
                return
