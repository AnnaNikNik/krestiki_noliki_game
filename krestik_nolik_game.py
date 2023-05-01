def greet():
    print("  Добро пожаловать ")
    print("      в игру       ")
    print("  крестики-нолики  ")
    print("...................")
    print("     ввод: x y     ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")

#ПОЛЕ

def show():
    print()
    print('   | 0 | 1 | 2 | ')
    print('  ______________')
    for i, row in enumerate(field):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print('  ______________')
    print()

#ВВОД

def ask():
    while True:
        cords = input('       Ваш ход:').split()

        if len(cords) != 2:
            print('   Введите 2 координаты! ')
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print('  Только числа! ')
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2 :
            print(' Мимо! ')
            continue

        if field[x][y] != ' ':
            print(' Занято!')
            continue

        return x, y

#ПОБЕДНАЯ КОМБИНАЦИЯ

def check_win():
    win_card = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for card in win_card:
        symbols = []
        for c in card:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print('Выиграл X!')
            return True
        if symbols == ["0", "0", "0"]:
            print('Выиграл 0!')
            return True
    return False

###

greet()
field = [[" "] * 3 for i in range(3) ]

#ИГРА

num = 0
while True:
    num += 1
    show()
    if num % 2 == 1:
        print('Ходит крестик')
    else:
        print('Ходит нолик')

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if num == 9:
        print('Ничья')
        break

