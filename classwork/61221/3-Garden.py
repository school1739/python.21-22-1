# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
garden_set = set(garden)
meadow_set = set(meadow)
all_the_flowers = garden_set | meadow_set

# выведите на консоль все виды цветов
for flower in all_the_flowers:
    print(flower, end=" ")

# выведите на консоль те, которые растут и там и там
print()

# создаем лист цветов, которые растут и там и там
itamitam = garden_set & meadow_set
# печатаем каждый цветок по отдельности:
for flower in itamitam:
    print(flower, end=" ")

# выведите на консоль те, которые растут в саду, но не растут на лугу
print()

# создаем лист цветов, которые растут в саду, но не растут на лугу
tamnonetam = garden_set - meadow_set
# печатаем каждый цветок по отдельности:
for flower in tamnonetam:
    print(flower, end=" ")

# выведите на консоль те, которые растут на лугу, но не растут в саду
print()

# создаем лист цветов, которые растут на лугу, но не растут в саду
netamnotam = meadow_set - garden_set
# печатаем каждый цветок по отдельности:
for flower in netamnotam:
    print(flower, end=" ")

# Evaluation: OK