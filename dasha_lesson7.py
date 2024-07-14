import math


def task1():
    # Даны две переменные, в которых хранятся числа. Поменять местами значения в них.
    first_number = int(input('Введите первое число '))
    second_number = int(input('Введите второе число '))
    print(f'Меняю местами {first_number} и {second_number} => {second_number} {first_number}')


def task2():
    # Дан список чисел. Определить, содержит ли список данное число ровно 3 раза.

    list = [1, 1, 2, 3, 4, 4, 4, 5]
    counter = 0
    repeatable_number = int
    result = bool

    for x in list:
        counter = list.count(x)
        repeatable_number = x
        if counter == 3:
            result = True
            break
        else:
            result = False
    if result:
        print(f'Повторяющееся три раза число в списке {list} = {repeatable_number}')
    else:
        print(f'В списке {list} нет повторяющихся чисел')


def task3():
    # Дан список чисел. Найти наименьшее четное число. Если такого нет, то вывести no.
    a = [1, 3, 5]
    even_list = [x for x in a if x % 2 == 0]
    min = int

    if len(even_list) == 0:
        print('no')
    else:
        for even_number in even_list:
            min = even_list[0]
            if even_number < min:
                min = even_number
        print(f'Минимальное число списка {a} = {min}')


def task4():
    # Дано число. Показать все числа, на которые оно делится.
    user_number = int(input('Введите целое число: '))
    divider = 1

    while True:
        for x in range(1, user_number + 1):
            if user_number == 0 or user_number < divider:
                break

            elif user_number % x == 0:
                print(divider, end=' ')
                break
        divider += 1
        # решу на следующий урок
        pass


# Задачи 84, 95, 96, 114, 98
def task84():
    # Пользователь вводит курс доллара в рублях. Показать таблицу цен 1$, 2$, ..., 100$ в рублях, третьим столбцом
    # добавить количество кг конфет, которые можно купить на данные суммы, если цена 1 кг конфет равна 20 руб.
    # Пример: 1$ - 70 р - 3.5 кг и так далее(всего 100 строк).
    # решу на следующий урок
    pass


def task95():
    # Даны a и n. Вычислите p = (a + 1)^2*(a + 2)^2*…*(a + n)^2
    a = 1
    n = 3
    p = 1
    for x in range(1, n + 1):
        p *= (a + x) ** 2
    print(p)


def task96():
    # Дано натуральное число n. Вычислите 1/cosx+1/cos(x^2)+...+1/cosx^n
    a = 1
    n = 3
    x = 1
    p = 0
    for y in range(1, n + 1):
        p += 1 / math.cos(x ** y)
    print(round(p, 3))


def task114():
    # Вывести 30 строк. Нечетные строки содержат натуральные числа от 1 до номера текущей строки включительно с шагом
    # 1, четные строки состоят из пяти единиц.
    for x in range(1, 31):
        if x % 2 == 0:
            print('1 ' * 5)
        else:
            line_numbers = list(range(1, x + 1))
            print(' '.join(str(y) for y in line_numbers))


def task98():
    # Начав тренировки, лыжник в первый день пробежал 10 км. Каждый следующий день он увеличивал пробег на 10% от
    # пробега предыдущего дня. Определите: а) пробег лыжника за второй, третий, ..., десятый день тренировок;
    # б) какой суммарный путь он пробежал за первые 7 дней тренировок. в) суммарный путь за n дней тренировок;
    # г) в какой день ему следует прекратить увеличивать пробег, если он не должен превышать 80 км?
    # решу на следующий урок
    pass


def task5():
    # Вывести в консоль таблицу квадратов
    for x in range(101):
        square = x ** 2
        if x % 10 == 0 and x != 0:
            print(square, '\n')
        else:
            print(square, end=' ')


def task6():
    # Проверьте, содержит ли данный список из n чисел, все целые числа от 1 до n.
    # решу на следующий урок
    pass


def task7():
    # Даны два списка. Вывести на экран числа первого списка, которых нет во втором.
    a = [1, 2, 7, 5]
    b = [5, 6, 7, 8]

    for x in a:
        not_repeatable = False
        for y in b:
            if y == x:
                not_repeatable = True
                break
        else:
            print(x, end=' ')
