"""Интернет-магазин предоставляет услугу экспресс-доставки для части
своих товаров по цене $10,95 за первый товар в заказе и $2,95 – за все
последующие. Напишите функцию, принимающую в качестве единствен-
ного параметра количество товаров в заказе и возвращающую общую
сумму доставки. В основной программе должны производиться запрос
количества позиций в заказе у пользователя, и отображаться на экране
сумма доставки (сумму перевести в рубли по курсу $1 = 75₽."""

def delivery(number_product): # Ввод функции
    payment = 10.95 * 70 + 2.95 * (number_product - 1) * 70
    return payment

x = round(delivery(number_product=int(input("number product:"))), 2)# Вызов функции

print("payment:",x) #Цена

# OK