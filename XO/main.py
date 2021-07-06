# Код взял из вебинара, немного подредактировал под себя.
# Зациклил. Для выхода нужно ввести X. Игровое поле из решётки, вместо клетки.
# Разработка с нуля заняла бы у меня много времени в данное время. Лень было возиться. Не успел бы.


def greet():
    # Функция вывода приветствия
    print("-------------------")
    print("  Приветствуем вас ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")
    print(" Выход - введите X ")


def show():
    # функция выводит текущее игровое поле
    print()
    print("      0   1   2   ")  # выводим столбцы строк
    for i, row in enumerate(field):
        # с помощью цикла выводим построчно сначала номера строк, потом данные поля i ряда
        row_str = f"  {i}   {' | '.join(row)}   "
        print(row_str)
        if i < 2:  # рисуем решётки, последнюю горизонтальную линию не рисуем
            print("     -----------  ")
    print()


def ask():
    # функция запроса координат
    while True:
        a = input("  Ваш ход: ")  # запрос координат
        if a.lower() == "x":  # выход из игры, если введён символ X в любом регистре
            print("До встречи!")
            exit(0)

        cords = a.split()  # разбиение строки на значения, разделённые пробелом

        # проверка на ввод двух координат
        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords  # присвоим координаты переменным x и y

        # проверка на ввод не числовых значений
        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        # преобразование переменных в числовые значения
        x, y = int(x), int(y)

        # проверка выхода за пределы игрового поля
        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        # проверка занятой клетки
        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        # возврат координат из функции
        return x, y


def check_win():
    # функция проверяет совпадение из кортежа с выигрышными вариантами
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    # перебор выигрышных вариантов
    for cord in win_cord:
        symbols = []
        for c in cord:
            # добавление символа в список в соответствии с возможным вариантом выигрыша
            symbols.append(field[c[0]][c[1]])

        # если в списке все символы X, выводим о выигрыше крестиков и вернём из функции True
        if symbols == ["X", "X", "X"]:
            print("Выиграл крестик!!!")
            return True
        # если в списке все символы O, выводим о выигрыше ноликов и вернём из функции True
        if symbols == ["O", "O", "O"]:
            print("Выиграл нолик!!!")
            return True

    # иначе возврат False, если варианты выигрыша не совпали
    return False


def main():
    # основная функция с бесконечным циклом
    while True:

        greet()  # вывод приветствия

        # формирование игрового поля 3x3 в двумерный массив
        field_game = [[" "] * 3 for _ in range(3)]
        count = 0  # устанавливаем счётчик ходов на 0

        # игровой цикл
        while True:
            count += 1  # прибавляем счётчик ходов на 1 ход
            show()  # отобразить игровое поле со значками

            # вывод кому ходить, если чётный ход - ходят нолики, если нечётный - крестики
            if count % 2 == 1:
                print(" Ходит крестик!")
            else:
                print(" Ходит нолик!")

            # получение введённых координат
            x, y = ask()

            # сохранение значков в игровое поле, в зависимости от чётности счётчика хода
            if count % 2 == 1:
                field_game[x][y] = "X"
            else:
                field_game[x][y] = "O"

            # проверка на выигрыш, в случе выигрыша, выходим из игрового цикла
            if check_win():
                break

            # если сделано максимально возможное количество ходов, объявляем ничью и выходим их игрового цикла
            if count == 9:
                print(" Ничья!")
                break


# запуск главной функции
main()