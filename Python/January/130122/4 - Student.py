# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Январь: # для каждого месяца!
#       Расходы: ХХХ.ХХ рублей.
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

# Месяцы учебного года
months = [
    'Сентябрь', 'Октябрь', 'Ноябрь',
    'Декабрь', 'Январь', 'Февраль',
    'Март', 'Апрель', 'Май',
    'Июнь'
]

result = 0
for month in months:
    result += expenses - educational_grant
    print(f'{month}:\n\tРасходы: {expenses:.2f} рублей.')
    expenses *= 1.03

print(f'Студенту надо попросить {result:.2f} рублей')
