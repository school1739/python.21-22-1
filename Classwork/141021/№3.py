print("Введите скольо вы  сувениров и безделушек.")
_suvenir= int(input())
_bezdel= int(input())
print("Вес вышей покупки составляет:" + " " +str(round(75*_suvenir + 112*_bezdel,0)) + " " + "грамм")

# Evaluation: OK. Если запрос на ввод состоит из одного предложения, пользователь чаще всего решит, что вводить числа
# можно прямо через пробел. Так что лучше "введите сувениры" и "введите безделушки" упаковывать прямо в input(),
# либо использовать метод split: https://dev.to/mohit355/3-5-split-method-in-python-2e19