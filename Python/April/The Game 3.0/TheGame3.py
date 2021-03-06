"""Перепишите The Game 2.0 с использованием библиотеки rich.
Использование классов обязательно. Количество раундов: >=1000.

В процессе игры отображается прогресс-бар, вывод игрового процесса на консоль не происходит.
По окончанию игры выводится таблица с результатами каждого раунда (см. ниже), ниже таблицы -- имя победителя.
То же самое записывается в файл game_log.txt с использованием export_text().

Пример таблицы:

                             The Game 3.0 Progress
┏━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━┓
┃ Round ┃ P1 Move ┃ P2 Move ┃ P1 Cheat ┃ P2 Cheat ┃ P1 Sco… ┃ P2 Score ┃ Winn… ┃
┡━━━━━━━╇━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━┩
│  666  │   123   │   321   │    ✅    │    ❌    │   34    │    12    │ Dick  │
└───────┴─────────┴─────────┴──────────┴──────────┴─────────┴──────────┴───────┘

"""