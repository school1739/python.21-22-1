a = input()
b = int(input())
power = 1#степень
ans = 0
for i in a[::-1]:#переворот
    ans +=int(i)*power#считаем
    power *= b#увеличение степени
print(ans)
#это вроде перевод из любой системы в 10, я больше не знаю как сделать



