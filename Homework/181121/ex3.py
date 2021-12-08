import random

# Максимальное значение в ряду
max_num = 0
# Количество смен максимального значения
updates = 0

# Повторяем 100 раз
for _ in range(100):
    # Берём случайное число от 1 до 100 и выводим его
    rand = random.randint(1, 100)
    print(f'> {rand}', end='')
    # Если случайное значение больше максимального
    if rand > max_num:
        # Меняем максимальное значение, увеличиваем количество изменений
        max_num = rand
        updates += 1
        # Помечаем обновление максимума
        print(' <== Обновление')
    else:
        # Иначе просто заканчиваем строку
        print()

# Выводим
print(f'Максимальное значение в ряду: {max_num}')
print(f'Количество смен максимального значения: {updates}')
