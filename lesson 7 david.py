# Задачи 84, 95, 96, 114, 98

# Пользователь вводит курс доллара в рублях. Показать таблицу цен 1$, 2$, ...,
# 100$ в рублях, третьим столбцом добавить количество кг конфет, которые можно купить на данные суммы, если цена 1 кг
# конфет равна 20 руб. Пример: 1$ - 70 р - 3.5 кг и так далее (всего 100 строк).

def task84():
    user_input = int(input('Write dollar value in rub.:'))
    amount_of_dollars = 0
    NUMBER_OF_STRINGS = 99
    one_kilo_candy = 20
    while amount_of_dollars <= NUMBER_OF_STRINGS:
        amount_of_dollars += 1
        exchange_rates = amount_of_dollars * user_input
        amount_of_candy = exchange_rates / one_kilo_candy
        print(f'{amount_of_dollars}$ - {exchange_rates} RUB. - {amount_of_candy}kg')



# Даны a и n. Вычислите p=(a+1)2(a+2)2⋅…⋅(a+n)2

def task95():
    a_variable = int(input('Write a number: '))
    n_variable = int(input('Write n number: '))
    counter_of_n_variable = 0
