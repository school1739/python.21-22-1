a = int(input("Сколько <2 лет:"))
b = int(input("Сколько от 3 до 12:"))
c = int(input("Сколько взрослых:"))
d = int(input("Сколько >65:"))
A = a*0
B = b*150
C = c*450
D = d*250
Sum = A+B+C+D
i = 1000
if Sum < i:
    print(Sum, "Цена")
    print(i - Sum, "Сдача")
else:
    S = (Sum // i + 1) * i
    print(Sum, "Цена")
    print(S-Sum, "Сдача")