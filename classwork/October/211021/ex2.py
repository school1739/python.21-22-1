import random

# создаем массивы цветов
red = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
dark = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}
green = {0, "00"}

# генерируем случайное число в диапазоне от 0 до 36 и 00)
random_number = random.choice([0, 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36, 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35, "00"])

# создаем условия итога, если выпала красная выемка
if random_number in red:
    if random_number % 2:
        if 0 < random_number < 19:
            print("Выпавший номер:", random_number)
            print("Выигравшая ставка:", random_number)
            print("Выигравшая ставка: красное")
            print("Выигравшая ставка: четное")
            print("Выигравшая ставка: от 1 до 18")

        else:
            print("Выпавший номер:", random_number)
            print("Выигравшая ставка:", random_number)
            print("Выигравшая ставка: красное")
            print("Выигравшая ставка: четное")
            print("Выигравшая ставка: от 19 до 36")
    else:
        if 0 < random_number < 19:
            print("Выпавший номер:", random_number)
            print("Выигравшая ставка:", random_number)
            print("Выигравшая ставка: красное")
            print("Выигравшая ставка: нечетное")
            print("Выигравшая ставка: от 1 до 18")

        else:
            print("Выпавший номер:", random_number)
            print("Выигравшая ставка:", random_number)
            print("Выигравшая ставка: красное")
            print("Выигравшая ставка: нечетное")
            print("Выигравшая ставка: от 19 до 36")

# создаем условия итога, если выпала черная выемка
elif random_number in dark:
    if random_number % 2:
        if 0 < random_number < 19:
            print("Выпавший номер:", random_number)
            print("Выигравшая ставка:", random_number)
            print("Выигравшая ставка: черное")
            print("Выигравшая ставка: четное")
            print("Выигравшая ставка: от 1 до 18")

        else:
            print("Выпавший номер:", random_number)
            print("Выигравшая ставка:", random_number)
            print("Выигравшая ставка: черное")
            print("Выигравшая ставка: четное")
            print("Выигравшая ставка: от 19 до 36")
    else:
        if 0 < random_number < 19:
            print("Выпавший номер:", random_number)
            print("Выигравшая ставка:", random_number)
            print("Выигравшая ставка: черное")
            print("Выигравшая ставка: нечетное")
            print("Выигравшая ставка: от 1 до 18")

        else:
            print("Выпавший номер:", random_number)
            print("Выигравшая ставка:", random_number)
            print("Выигравшая ставка: черное")
            print("Выигравшая ставка: нечетное")
            print("Выигравшая ставка: от 19 до 36")

# создаем условия итога для зеленых выемок
else:
    if random_number == 0:
        print("Выпавший номер: 0…\nВыигравшая ставка: 0")
    else:
        print("Выпавший номер: 00…\nВыигравшая ставка: 00")

# Evaluation: OK. Многовато ручных print'ов. Можно было бы вложить IF в IF, для чётности и цвета, записать результаты
# в отдельные переменные, а затем конкатенировать в выводе.