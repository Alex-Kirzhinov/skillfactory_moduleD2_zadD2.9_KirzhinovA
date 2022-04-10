from random import randint

from Board import Board
from Ship import Ship
from Dot import Dot
from exceptions import BoardShipsPlacement
from Player import Player, User, AI

class Game:
    def __init__(self, size = 6):
        self.size = size
        board_player = self.random_board()
        board_ai = self.random_board()
        board_ai.hid = True

        self.player_ = User(board_player, board_ai)
        self.ai_ = AI(board_ai, board_player)


    def try_board(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        your_board = Board(size = self.size)
        attempts_ = 0
        for l in lens:
            while True:
                attempts_ += 1
                if attempts_ > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))
                try:
                    your_board.add_ship(ship)
                    break
                except BoardShipsPlacement:
                    pass
        your_board.begin()
        return your_board

    def random_board(self):
        your_board = None
        while your_board is None:
            your_board = self.try_board()
        return your_board

    def greet(self):
        print("Добро пожаловать в игру")
        print("***** МОРСКОЙ БОЙ *****")
        print("_______________________")
        print(" Формат  ввода: х  и у ")
        print("  х  -   номер строки ")
        print("  у  -   номер столбца")

    def loop(self):
        num_ = 0
        while True:
            print("-" * 20)
            print("Доска игрока")
            print(self.player_.your_board)
            print("-" * 20)
            print("Доска ИИ")
            print(self.ai_.your_board)
            if num_ % 2 == 0:
                print("-" * 20)
                print("Ход игрока")
                repeat = self.player_.move()
            else:
                print("-" * 20)
                print("Ход ИИ")
                repeat = self.ai_.move()
            if repeat:
                num_ -= 1

            if self.ai_.your_board.count == 7:
                print("-" * 20)
                print("Игрок выиграл. Поздравляем!")
                break
            if self.player_.your_board.count == 7:
                print("-" * 20)
                print("ИИ выиграл. Не отчаивайтесь!")
                break
            num_ += 1

    def start(self):
        self.greet()
        self.loop()

g = Game()
g.start()