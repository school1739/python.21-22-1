"""Напишите функцию, принимающую на вход длины двух катетов прямо-
угольного треугольника и возвращающую длину гипотенузы, рассчитан-
ную по теореме Пифагора. В главной программе должен осуществляться
запрос длин сторон у пользователя, вызов функции и вывод на экран
полученного результата."""
a = int(input("Катит 1:"))#Ввёл переменные
b = int(input("Катит 2:"))
с =(a * a + b * b) ** 0.5 #Теоремма Пифагора
print("Гипотенуза =",с)