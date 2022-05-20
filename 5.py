coord = input("Введите координаты клетки: ")
if (int(coord[1]) % 2) != 0:
    if coord[0] == 'a' or coord[0] == 'c' or coord[0] == 'e' or coord[0] == 'g':
        print("Клетка чёрная")
    else:
        print("Клетка белая")
else:
    if coord[0] == 'a' or coord[0] == 'c' or coord[0] == 'e' or coord[0] == 'g':
        print("Клетка белая")
    else:
        print("Клетка чёрна")