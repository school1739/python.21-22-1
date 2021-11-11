##
# Находим стоимость билетов
#
cost = 0
# Вводим возраст пока не будет пустая строка
while (age := input()) != '':
    age = int(age)
    # Прибавляем к общей сумме стоимость билета в зависимости от возраста
    if age > 65:
        cost += 250
    elif age > 12:
        cost += 450
    elif age > 2:
        cost += 150
# Выводим общую цену и сдачу с ближайшей тысячи рублей
print(f'Общая цена: {cost}')
print(f'Сдача с ближайшей тысячи рублей: {1000 - cost % 1000 if cost % 1000 != 0 else 0}', end='')