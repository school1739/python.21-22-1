a = int(input("Чему равна сумма первоначального депозита?"))
b = a * 0.04 + a
c = b * 0.04 + b
d = c * 0.04 + c
print("В конце первого года:", "%.2f" % b, "рублей")
print("В конце второго года:", "%.2f" % c, "рублей")
print("В конце третьего года:", "%.2f" % d, "рублей")