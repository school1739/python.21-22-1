a = int(input("Длинна стороны треугольника a: "))
b = int(input("Длинна стороны треугольника b: "))
c = int(input("Длинна стороны треугольника c: "))
if a > 0 and b > 0 and c > 0:
    if a==b==c:
        print("Треугольник равносторонний")
    elif a==b and a != c and b != c:
        print("Труегольник равнобедренный")
    elif (a==c) and a != b and c != b:
        print("Труегольник равнобедренный")
    elif c==b and c != a and b != a:
        print("Труегольник равнобедренный")
    else:
        print("Треугольник разносторонний")
else:
    print("error, число отрицательное или равно 0")

# Evaluation: OK. *длиНа (с 1 буквой Н)