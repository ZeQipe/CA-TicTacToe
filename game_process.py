import move_logic
import os


def print_board(board: list) -> None:
    """
    Выводит на консоль игровое поле...
    :param board: type str
    :return: None
    """
    os.system('cls')
    for i in range(0, 9, 3):
        print("|".join(board[i:i + 3]))


def check_winner(board: list) -> bool:
    """
    проверка на победную комбинацию
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


async def bot_vs_bot(board) -> None:
    """
    Запускает матч 2 ботов, в случае, если на поле нет пустых мест - объявляет ничью.
    :param board:
    :return:
    """
    current_player = 'X'
    while ' ' in board:
        print_board(board)
        move = await move_logic.bot_move(board)
        if move == -1:
            return

        if move_logic.make_move(board, move, current_player):
            if check_winner(board):
                print_board(board)
                input(f"{current_player} Победил!\n Нажмите Enter что бы вернуться...")
                return

            current_player = switch_player(current_player)
    input('Ничья!\nНажмите Enter что бы вернуться')


async def player_vs_bot(board) -> None:
    """
    Запускает матч игрока против бота, в случае, если на поле нет пустых мест - объявляет ничью.
    :param board:
    :return:
    """
    current_player = 'X'

    while ' ' in board:
        print_board(board)

        if current_player == "X":
            print('Ваш ход! Выбирайте (r - для возврата в главное меню):')
            move = await move_logic.user_move()
            if move == -1:
                return
        else:
            move = await move_logic.bot_move(board)

        if move != -1 and move_logic.make_move(board, move, current_player):
            if check_winner(board):
                print_board(board)
                if current_player == "X":
                    input("Вы победили =)\nНажмите Enter что бы вернуться...")
                else:
                    input("Вы проиграли =(\nНажмите Enter что бы вернуться...")
                return

            current_player = switch_player(current_player)
    input("Ничья -_-\nНажмите Enter что бы вернуться...")


async def player_vs_player(board):
    current_player = 'X'

    while ' ' in board:
        print_board(board)

        if current_player == "X":
            print('Ход игрока Х')
            move = await move_logic.user_move()
        else:
            print('Ход игрока О')
            move = await move_logic.user_move()

        if move != -1 and move_logic.make_move(board, move, current_player):
            if check_winner(board):
                print_board(board)
                if current_player == "X":
                    input("Победил игрок 'Х'\nНажмите Enter что бы вернуться...")
                else:
                    input("Победил игрок 'О'\nНажмите Enter что бы вернуться...")
                return

            current_player = switch_player(current_player)
    input("Ничья :Ъ\nНажмите Enter что бы вернуться...")
