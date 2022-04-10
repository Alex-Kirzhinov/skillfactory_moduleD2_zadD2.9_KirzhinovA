class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return("Ваш сняряд вылетел за поле, попытайтесь снова!")

class BoardRepetitionDotException(BoardException):
    def __str__(self):
        return ("Вы повторяетесь, попытайтесь снова!")

class BoardShipsPlacement(BoardException):
    pass
