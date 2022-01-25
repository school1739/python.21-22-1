"""Напишите функцию, которая будет принимать в качестве параметров
строку s, а также ширину окна в символах – w. Возвращать функция долж-
на новую строку, в которой в начале добавлено необходимое количество
пробелов, чтобы первоначальная строка оказалась размещена по центру
заданного окна. Новая строка должна формироваться по следующему
принципу:
-> если длина исходной строки s больше или равна ширине заданного
окна, возвращаем ее в неизменном виде;
-> в противном случае должна быть возвращена строка s с ведущими
пробелами в количестве (len(s) – w) // 2 штук.
В вашей основной программе должен осуществляться пример вывода
нескольких строк в окнах разной ширины."""


def centering(s, width):
    """
        Если строчка больше заданной ширины, вертаем взад
    """
    if width < len(s):
        return s
    """
        Считаем пробелы, которые будут использованы для 'centering' строки
    """
    spaces = (width - len(s)) // 2
    result = " " * spaces + s
    return result


# примеры вывода от балды
print(centering("Что-то:", 50))
print(centering("Где-то:", 2))
print(centering("Как-то:", 15))
print(centering("Nill Kiggers cause its good", 70))