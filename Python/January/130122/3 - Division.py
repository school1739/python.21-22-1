# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

# задаем значения
a, b = 179, 37
result = -1
remains = 0

# цикл целочисленного деления любых целых чисел (положительных и отрицательных)
if b != 0:
    while remains <= abs(a):
        remains += abs(b)
        result += 1
    print("Целочисленное деление", a, "на", b, "дает", result)
else:
    print("ты дурак, на ноль делить нельзя ващета")

# OK