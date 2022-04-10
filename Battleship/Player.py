from random import randint

from exceptions import BoardException
from Dot import Dot

class Player:   #создаем игроков
    def __init__(self, your_board, enemy_board):
        self.your_board = your_board
        self.enemy_board = enemy_board

    def ask(self):
        pass

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy_board.shot(target)
                return repeat
            except BoardException as e:
                print(e)

class User(Player): #выстрел игрока
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:
                print(" Введите 2 координаты через пробел (от 1 до 6)! ")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Введите числа! ")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)

class AI(Player): #выстрел ИИ
    def ask(self):
        dot_ = Dot(randint(0, 5), randint(0, 5))
        print(f" Ход ИИ: {dot_.x + 1} {dot_.y + 1}")
        return dot_
