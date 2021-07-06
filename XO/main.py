# Код взял из вебинара, немного подредактировал под себя.
# Зациклил. Для выхода нужно ввести X. Игровое поле из решётки, вместо клетки.
# Разработка с нуля заняла бы у меня много времени в данное время. Лень было возиться. Не успел бы.

def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")
    print(" Выход - введите X ")

def show():
    print()
    print("      0   1   2   ")
    for i, row in enumerate(field):
        row_str = f"  {i}   {' | '.join(row)}   "
        print(row_str)
        if i<2: print("     -----------  ")
    print()


def ask():
    while True:
        a = input("  Ваш ход: ")
        if a.lower() == "x":
            print("До встречи!")
            exit(0)

        cords = a.split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл крестие!!!")
            return True
        if symbols == ["O", "O", "O"]:
            print("Выиграл нолик!!!")
            return True
    return False

field = [
    [" ", "X", " "],
    [" ", "X", " "],
    [" ", "X", " "]
]

def main():
    while True:

        greet()
        field = [[" "] * 3 for i in range(3)]
        count = 0
        while True:
            count += 1
            show()
            if count % 2 == 1:
                print(" Ходит крестик!")
            else:
                print(" Ходит нолик!")

            x, y = ask()

            if count % 2 == 1:
                field[x][y] = "X"
            else:
                field[x][y] = "O"

            if check_win():
                break

            if count == 9:
                print(" Ничья!")
                break

main()
