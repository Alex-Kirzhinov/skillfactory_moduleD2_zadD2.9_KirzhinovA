# Заглавие и основные правила
print('*' * 20, '" Игра Крестики-нолики" ', '*' * 20)
print('-' * 61)
print('Побеждает тот у кого выстроилась строка, столбец или диагональ из "Х" или "0"')
print('-' * 61)

# Создаем игровое поле:
game_field = [[' -', ' -', ' -'] for i in range(3)]

# Вывод игрового поля:
def show_game_field():
    print(f"   0  1  2")
    for i in range(3):
        print(f"{i} {game_field[i][0]} {game_field[i][1]} {game_field[i][2]}")

# Ввод Х или 0
def take_input(player_token):
   valid = False
   while not valid:
       row_ = input('Введите номер строки (0, 1 или 2) для ' + player_token+': ')
       column_ = input('Введите номер столбца (0, 1 или 2) для ' + player_token+': ')
       try:
           if int(row_) in range(0, 3) and int(column_) in range(0, 3):
               row_ = int(row_)
               column_ = int(column_)
               if (str(game_field[row_][column_]) not in " X O"):
                   game_field[row_][column_] = player_token
                   valid = True
               else:
                   print("Эта клетка уже занята! Попробуйте снова!")
           else:
               print("Номер строки или столбца не входит в диапазон (0, 1, 2), попробуйте снова!")
       except:
           print("Номер строки или столбца не входит в диапазон (0, 1, 2), попробуйте снова!")


# Проверка выигрыша
def check_win(game_field):
    win_coord = (([0, 0], [0, 1], [0, 2]), ([1, 0], [1, 1], [1, 2]), ([2, 0], [2, 1], [2, 2]),
                 ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 1], [2, 1]), ([0, 2], [1, 2], [2, 2]),
                 ([0, 0], [1, 1], [2, 2]), ([0, 2], [1, 1], [2, 0]))
    for each in win_coord:
        if game_field[each[0][0]][each[0][1]] == game_field[each[1][0]][each[1][1]] == \
                game_field[each[2][0]][each[2][1]] and game_field[each[0][0]][each[0][1]] != " -":
            return game_field[each[0][0]][each[0][1]]
    return False

#Основное поле
def main(game_field):
    counter = 0
    win = False
    while not win:
        show_game_field()
        if counter % 2 == 0:
            take_input(" X")
        else:
            take_input(" O")
        counter += 1
        if counter > 4:
            tmp = check_win(game_field)
            if tmp:
                print(tmp, "выиграл! Поздравляем Вас!")
                win = True
                break
        if counter == 9:
            print("У нас ничья!")
            break
    show_game_field()
main(game_field)

input("Нажмите Enter для выхода!")

