print('Введите группы из восьми бит:')
# Вводим биты пока не будет пустая строка
while (bits := input()) != '':
    # Проверяем ввод
    if len(bits) == 8 and all(c in ('0', '1') for c in bits):# размер бита
        # Выводим бит чётности
        parity_bit = bits.count('1') % 2
        print(parity_bit)
    else:
        # Неверный ввод
        print('Error')
        # parity(четность бита)
        # len(кол - во символов в строке)
        # ЗАПОМНИТЬ !!!