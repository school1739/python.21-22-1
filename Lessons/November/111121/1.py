sum = 0
k = int(input())
i = 0                #Проверяем первое число
if k == 0:
    print("Первое число не ноль")
else:                #Высчитываем среднее арифметическое
    while k != 0:
        sum += k
        k = int(input())
        i+=1
print(sum/(i))
