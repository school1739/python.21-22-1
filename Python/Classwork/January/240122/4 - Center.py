# Пишем функцию
def f(s, w):
    # Сравнение длинны строки и ширины окна
    if len(s) >= w:
        return s
    else:
        # Костыль
        costyl = len(s)
        costyl = int(costyl)
        n = ((w - (costyl)) // 2)
        s = (" " * n) + s
        return s


# Если длинна строки больше ширины окна
print(f("ааакакжеяусталёпарасете", 8))
# Если длинна строки меньше ширины окна
print(f("амогус", 10))
# Если длинна строки равна ширине окна
print(f("сугома", 6))
