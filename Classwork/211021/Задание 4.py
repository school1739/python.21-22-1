day = int(input("Введите ДЕНЬ своего рождения: "))
month = input("Введите МЕСЯЦ своего рождения (в родительном падеже, с маленькой буквы!): ")
year = int(input("Введите ГОД своего рождения: "))
if (22 <= day <= 31 and month == "декабря") or (1 <= day <= 19 and month == "января"):
    print("По гороскопу вы Козерог")

elif (20 <= day <= 31 and month == "января") or (1 <= day <= 18 and month == "февраля"):
    print("По гороскопу вы Водолей")

elif (19 <= day <= 29 and month == "февраля") or (1 <= day <= 20 and month == "марта"):
    print("По гороскопу вы Рыбы")

elif (21 <= day <= 31 and month == "марта") or (1 <= day <= 19 and month == "апреля"):
    print("По гороскопу вы Овен")

elif (20 <= day <= 30 and month == "апреля") or (1 <= day <= 20 and month == "мая"):
    print("По гороскопу вы Телец")

elif (21 <= day <= 31 and month == "мая") or (1 <= day <= 20 and month == "июня"):
    print("По гороскопу вы Близнецы")

elif (21 <= day <= 30 and month == "июня") or (1 <= day <= 22 and month == "июля"):
    print("По гороскопу вы Рак")

elif (23 <= day <= 31 and month == "июля") or (1 <= day <= 22 and month == "августа"):
    print("По гороскопу вы Лев")

elif (23 <= day <= 31 and month == "августа") or (1 <= day <= 22 and month == "сентября"):
    print("По гороскопу вы Дева")

elif (23 <= day <= 30 and month == "сентября") or (1 <= day <= 22 and month == "октября"):
    print("По гороскопу вы Весы")

elif (23 <= day <= 31 and month == "октября") or (1 <= day <= 21 and month == "ноября"):
    print("По гороскопу вы Скорпион")

elif (22 <= day <= 30 and month == "ноября") or (1 <= day <= 21 and month == "декабря"):
    print("По гороскопу вы Стрелец")
else:
    print("Вы не могли родиться в такой день!")

"Как сделать определение по китайскому гороскопу я понятия не имею :("