db = int(input("Введите уровень шума "))
if 39 < db < 131:
    if db == 40:
        print("Тихая комната")
    elif 40 < db < 70:
        print("Между тихой комнатой и будильником")
    elif db == 70:
        print("Будильник")
    elif 70 < db < 106:
        print("Между будильником и газонокосилкой")
    elif db == 106:
        print("Газонокосилка")
    elif 106 < db < 130:
        print("Между газонокосилкой и отбойным молотком")
    elif db == 130:
        print("Отбойный молоток")
else:
    print("Ошибка")
    print("Внимательно прочитайте условие и введите значение не меньше 40 db и не больше 130db")