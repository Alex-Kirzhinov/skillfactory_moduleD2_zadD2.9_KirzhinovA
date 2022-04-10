from Dot import Dot

class Ship:
    def __init__(self, dot_front, len_, ship_orientation):
        self.dot_front = dot_front
        self.len_ = len_
        self.ship_orientation = ship_orientation
        self.live_points = len_

    @property           #класс, сам бы не догадался
    def dots(self):     #функция расттавления точек корабля
        ship_dots = []
        for i in range(self.len_):      #сначала нос корабля, затем остальное в зависимости от ориентации
            cur_x = self.dot_front.x
            cur_y = self.dot_front.y

            if self.ship_orientation == 0:
                cur_x += i
            elif self.ship_orientation == 1:
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots

    def shooten(self, shot):    #проверяем попадание в точку
        return shot in self.dots
