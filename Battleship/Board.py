from Dot import Dot
from Ship import Ship
from exceptions import BoardShipsPlacement, BoardOutException, BoardRepetitionDotException

class Board:    #создаем доску, также добавляем список точек и кораблей
    def __init__(self, hid = False, size = 6):
        self.hid = hid
        self.size = size

        self.count = 0

        self.board = [["O"] * size for i in range(size)]

        self.busy = []  #создаем список использованных точек
        self.ships = [] #создаем список кораблей

    def __str__(self):  #выводим доску
        board_res = ""
        board_res += "    1   2   3   4   5   6  "
        for i, row_ in enumerate(self.board):
            board_res += f"\n{i + 1} | " + " | ".join(row_) + " |"

        if self.hid:
            board_res = board_res.replace("*", "O")
        return board_res

    def out(self, dot_):    #проверяем выход за пределы поля
        return not (0 <= dot_.x < self.size) or not (0 <= dot_.y < self.size)

    def contour(self, ship, verb = False):  #вывод контура корабля
        nier = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for dot_ in ship.dots:
            for dx, dy in nier:
                cur_ = Dot(dot_.x + dx, dot_.y + dy)
                if not (self.out(cur_)) and cur_ not in self.busy:
                    if verb:
                        self.board[cur_.x][cur_.y] = "."
                    self.busy.append(cur_)

    def add_ship(self, ship):   #добавляем корабли
        for dot_ in ship.dots:
            if self.out(dot_) or dot_ in self.busy: #проверяем на выход из поля и повторение
                raise BoardShipsPlacement()
        for dot_ in ship.dots:
            self.board[dot_.x][dot_.y] = "*"
            self.busy.append(dot_)

        self.ships.append(ship)
        self.contour(ship)

    def shot(self, dot_):   #производим выстрелы
        if self.out(dot_):  #проверяем на выход из поля
            raise BoardOutException()

        if dot_ in self.busy:   #проверяем на повторение
            raise BoardRepetitionDotException()

        self.busy.append(dot_)

        for ship in self.ships:
            if ship.shooten(dot_):
                ship.live_points -= 1
                self.board[dot_.x][dot_.y] = "X"
                if ship.live_points == 0:
                    self.count += 1
                    self.contour(ship, verb = True)
                    print("Корабль уничтожен, так держать!")
                    return False
                else:
                    print("Корабль ранен, не останавливайтесь!")
                    return True

        self.board[dot_.x][dot_.y] = "."
        print("Промах!")
        return False

    def begin(self):    #обнуляем список занятых точек перед началом игры
        self.busy = []
