from random import randint
from typing import List, Tuple, Dict
from collections import defaultdict


def case1() -> None:
    print("""Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество 
           элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
           Каждое число вводится с новой строки.""", end='\n\n')

    first_number: int = int(input("Введите первый элемент арифметической прогрессии: "))
    difference: int = int(input("Введите разность между элементами: "))
    number_of_elements: int = int(input("Введите кол-во элементов: "))

    list_number_progression: List[int] = [first_number + (i - 1) * difference for i in range(1, number_of_elements + 1)]

    print(f"\nАрифметическая прогрессия начиная с числа {first_number} с шагом {difference} в колличестве"
          f" {number_of_elements} элементов = {list_number_progression}")


def case2() -> None:
    print("""Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
          (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно.""")

    min_number: int = int(input("Введите минимальное значение диапазона поиска: "))
    max_number: int = int(input("Введите максимальное значение диапазона поиска: "))
    number_of_elements: int = int(input("Введите кол-во элементов в списке: "))

    list_number: list = [randint(min_number - 500, max_number + 500) for _ in range(number_of_elements)]

    print(list_number)
    print(f"Ответ: {[i for i in range(len(list_number)) if min_number < list_number[i] < max_number]}")


def case3():
    # Инициализация игрового поля
    board: List[str] = [' ' for _ in range(9)]

    # Функция для вывода игрового поля
    def print_board(board: List[str]) -> None:
        print()
        print(f' {board[0]} | {board[1]} | {board[2]} ')
        print('---+---+---')
        print(f' {board[3]} | {board[4]} | {board[5]} ')
        print('---+---+---')
        print(f' {board[6]} | {board[7]} | {board[8]} ')
        print()

    # Функция для проверки окончания игры
    def is_game_over(board: List[str]) -> bool:
        # Проверяем строки, столбцы и диагонали на наличие выигрыша
        for i in range(0, 9, 3):
            if board[i] == board[i + 1] == board[i + 2] != ' ':
                return True
        for i in range(3):
            if board[i] == board[i + 3] == board[i + 6] != ' ':
                return True
        if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
            return True
        # Проверяем, остались ли пустые клетки, если нет, то ничья
        if ' ' not in board:
            return True
        return False

    # Функция для хода бота
    def bot_move(board: List[str]) -> int:
        # Бот пытается занять клетку рядом со своей
        for i in range(9):
            if board[i] == 'O':
                for j in [1, -1, 3, -3]:
                    if i + j in range(9) and board[i + j] == ' ':
                        return i + j
        # Если это невозможно, бот занимает случайную пустую клетку
        while True:
            move = randint(0, 8)
            if board[move] == ' ':
                return move

    # Начинаем игровой цикл
    while True:
        # Ход игрока
        move: int = int(input("Ваш ход. Введите число от 1 до 9: ")) - 1
        if board[move] != ' ':
            print("Недопустимый ход. Попробуйте еще раз.")
            continue
        board[move] = 'X'
        print_board(board)
        if is_game_over(board):
            print("Игра окончена. Вы выиграли!")
            break

        # Ход бота
        move = bot_move(board)
        board[move] = 'O'
        print("Ход бота.")
        print_board(board)
        if is_game_over(board):
            print("Игра окончена. Бот выиграл!")
            break


def case4():
    def calculation_scores(matches: List[Tuple[str, int, str, int]]) -> Dict[str, List[int]]:
        teams = defaultdict(lambda: [0, 0, 0, 0, 0])

        for match in matches:
            team1, score1, team2, score2 = match
            teams[team1][0] += 1
            teams[team2][0] += 1

            if score1 > score2:
                teams[team1][1] += 1
                teams[team1][4] += 3
                teams[team2][3] += 1
            elif score1 < score2:
                teams[team2][1] += 1
                teams[team2][4] += 3
                teams[team1][3] += 1
            else:
                teams[team1][2] += 1
                teams[team1][4] += 1
                teams[team2][2] += 1
                teams[team2][4] += 1
        return teams

    number_matches: int = int(input("Введите количество матчей: "))
    matches: List[Tuple[str, int, str, int]] = []
    for _ in range(number_matches):
        match = input("Введите результаты матча в формате 'Команда1;Голы1;Команда2;Голы2: '")
        team1, score1, team2, score2 = match.split(';')
        matches.append((team1, int(score1), team2, int(score2)))

    teams: Dict[str, List[int]] = calculation_scores(matches)

    for team, stats in teams.items():
        print(f"{team}: {stats[0]} игр, {stats[1]} побед, {stats[2]} ничьих, {stats[3]} поражений, {stats[4]} очков")


def default():
    print("\nВы выбрали неизвестный случай")


switch_case = {
    1: case1,
    2: case2,
    3: case3,
    4: case4,
}

user_input = int(input("""1: Заполнение массива элементами арифметической прогрессии.
2: Определение индексов элементов массива (списка).
3: Крестики - нолики.
4: Football.
Выберите номер задачи для запуска кода: """))

print("-" * 50)
switch_case.get(user_input, default)()
